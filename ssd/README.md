# README

## 推論方法
詳細な紹介はblogに記載<br>
→blogはこちら

### 推論方法
1. ckptファイルを解凍する<br>
    ```bash
    $ webApp/ssd/detection/ssd_tensorflow/checkpoints unzip ssd_300_vgg.zip
    ```
    
2. 必要なパッケージのインストール
    - pipenvを使用する場合
        ```bash
        $ webApp/ssd pipenv sync --dev
        ```
    - requirements.txtからインストールする場合
        ```bash
        $ webApp/ssd pip install -r requirements.txt
        ```

3. 開発用サーバーを立ち上げる
    ```bash
    $ webApp/ssd python3 manage.py runserver
    ```

4. 推論したい画像を選択し、推論ボタンを押す