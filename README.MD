# 0.环境
## 0.0 flask相关包安装
>paddlepaddle 以及paddlehub均最新版<br>
>flask_bootstrap flask-blueprint插件

```shell script
pip install flask_bootstrap
pip install flask-blueprint
```
## 0.1 paddlehub模块安装
```python
hub install stylepro_artistic
hub install reading_pictures_writing_poems
```

# 1.命令行运行
```shell script
hub run reading_pictures_writing_poems --input_image "scenery.jpg"
hub run stylepro_artistic --选项 选项值
```

# 2. 程序中运行
```python
import paddlehub as hub
import cv2

readingPicturesWritingPoems = hub.Module(name="reading_pictures_writing_poems")
readingPicturesWritingPoems.WritingPoem(image = "scenery.jpg", use_gpu=True)


stylepro_artistic = hub.Module(name="stylepro_artistic")
result = stylepro_artistic.style_transfer(
    images=[{
        'content': cv2.imread('/PATH/TO/CONTENT_IMAGE'),
        'styles': [cv2.imread('/PATH/TO/STYLE_IMAGE')]
    }])

```

# 3.hub中运行

```shell script
hub run reading_pictures_writing_poems --input_image "scenery.jpg"
hub serving start --config cpuconfig.json
hub serving start --modules reading_pictures_writing_poems
hub serving start --modules stylepro_artistic
```
# 3.存在问题
>不支持serving <br>
>单独程序中运行可以<br>
>合并到flask程序中就一直卡死<br>
```shell script
C:\Users\Administrator\Anaconda3\envs\paddle\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\plugins\python-ce\helpers\pydev\pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 1469 --file C:/Users/Administrator/PycharmProjects/reading_pictures_writing_poems/app.py
pydev debugger: process 9572 is connecting

Connected to pydev debugger (build 193.7288.30)
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
2020-09-12 14:10:26,972-INFO:  * Restarting with stat
pydev debugger: process 4048 is connecting

2020-09-12 14:10:31,180-WARNING:  * Debugger is active!
2020-09-12 14:10:31,184-INFO:  * Debugger PIN: 162-828-337
2020-09-12 14:10:43,076-INFO:  * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
<Request 'http://localhost/reading_pictures' [GET]>
2020-09-12 14:10:45,343-INFO: 127.0.0.1 - - [12/Sep/2020 14:10:45] "GET /reading_pictures HTTP/1.1" 200 -
2020-09-12 14:10:45,523-INFO: 127.0.0.1 - - [12/Sep/2020 14:10:45] "GET /PV?peerid=0&uri=http://thunderqtypv.union.xunlei.com&src=localhost HTTP/1.1" 404 -
<Request 'http://localhost/reading_pictures' [POST]>
scenery.jpg
sourcefile: static/images/source\scenery.jpg
C:\Users\Administrator\PycharmProjects\reading_pictures_writing_poems\static/images/source\scenery.jpg
upload_path: C:\Users\Administrator\PycharmProjects\reading_pictures_writing_poems\static/images/source\scenery.jpg
[2020-09-12 14:10:50,589] [    INFO] - Installing reading_pictures_writing_poems module
[2020-09-12 14:10:51,254] [    INFO] - Module reading_pictures_writing_poems already installed in C:\Users\Administrator\.paddlehub\modules\reading_pictures_writing_poems
[2020-09-12 14:10:51,255] [    INFO] - Installing xception71_imagenet module
[2020-09-12 14:10:51,297] [    INFO] - Module xception71_imagenet already installed in C:\Users\Administrator\.paddlehub\modules\xception71_imagenet
[2020-09-12 14:10:52,396] [    INFO] - Installing ernie_gen_couplet module
[2020-09-12 14:10:52,441] [    INFO] - Module ernie_gen_couplet already installed in C:\Users\Administrator\.paddlehub\modules\ernie_gen_couplet
[2020-09-12 14:11:02,039] [    INFO] - Installing ernie_gen_poetry module
[2020-09-12 14:11:02,391] [    INFO] - Module ernie_gen_poetry already installed in C:\Users\Administrator\.paddlehub\modules\ernie_gen_poetry
upload_path static/images/source\scenery.jpg
1599891070.123725
[2020-09-12 14:11:10,366] [    INFO] - 638 pretrained paramaters loaded by PaddleHub

```
