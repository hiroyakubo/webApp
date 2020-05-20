import glob
import os

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Image
from .form import ImageForms
from .ssd_tensorflow.inference import inference


media = "media"
DETECTION_INPUT_DIR = os.path.join(media, "images/detection")
DETECTION_RESULT_DIR = os.path.join(media, "images/detection_result")

def get_value(name):
    """
    Image.objectsの値を取得するための関数.

    Args:
        name: str

    Returns:
        list
    """
    return Image.objects.all().values_list(name, flat=True)

def get_result_url(urls):
    """
    推論結果画像の保存場所を取得するための関数.

    Args:
        urls: list

    Returns:
        list
    """
    url_lists = []
    for url in urls:
        url_list = url.split("/")
        url_list[-2] = "detection_result"
        url_lists.append(os.path.join(media, "/".join(url_list)))
    
    return url_lists
    
class Top_view(View):
    """
    トップページのビューを作成するクラス.
    """
    def get(self, request, *args, **kwargs):
        # トップページに表示する画像のパスを取得
        image_names = get_value("title")
        output_image = get_result_url(get_value("picture"))
        
        # html側で使いやすいように[{}]の形にしておく
        inputs = [{"image" : os.path.join(media, i), "name": n, "id": d} for i, n, d in zip(get_value("picture"), image_names, get_value("id"))]
        outputs = [{"image": i, "name": n} for i, n in zip(output_image, image_names)]
        context = {
            "form": ImageForms(), 
            "input_image": inputs, 
            "output_image": outputs, 
            }
        return render(request, "detection/index.html", context)

    def post(self, request, *args, **kwargs):
        """
        推論用画像のアップデートと推論の実施.
        """
        form = ImageForms(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "detection/index.html", {"form": form})

        img = form.save(commit=False)
        img.save()

        # inference関数でSSDの推論が実施される.
        ids = get_value("id")
        inference(Image.objects.get(id=max(ids)).title)
        
        return redirect(reverse("index"))

index = Top_view.as_view()

class Delete_all(View):
    """
    アップロードした画像および推論を実施した全ての画像を削除するクラス.
    """
    def get(self, request, *args, **kwargs):
        # アップロードされた画像および推論画像へのパスを取得.
        input_images = glob.glob(os.path.join(DETECTION_INPUT_DIR, "*"))
        result_images = glob.glob(os.path.join(DETECTION_RESULT_DIR, "*"))

        # 画像の削除.
        for i, r in zip(input_images, result_images):
            os.remove(i)
            os.remove(r)
        
        image = Image.objects.all()
        image.delete()
        
        return redirect(reverse("index"))

delete_all = Delete_all.as_view()

class Delete_part(View):
    """
    個々の画像を削除するクラス.
    """
    def get(self, request, delete_id, *args, **kwargs):
        # 削除ボタンが押された画像を削除する.
        image = Image.objects.get(id=delete_id)
        os.remove(os.path.join(media, image.picture_path))
        os.remove(get_result_url(get_value("picture"))[0])
        image.delete()

        return redirect(reverse("index"))

delete_part = Delete_part.as_view()