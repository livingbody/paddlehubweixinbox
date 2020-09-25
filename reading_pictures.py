# coding:utf-8
# author: Livingbody
# date: 2020.05.06

from flask import Flask, render_template, request, jsonify, Response
from werkzeug.utils import secure_filename
import os
import requests
import paddlehub as hub
import cv2
import time
from flask import Blueprint, render_template
import requests
import json
import cv2
import base64
from flask import json

index_reading_pictures = Blueprint("reading_pictures", __name__)
# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'bmp', 'jpeg'])
# 当前文件所在路径
basepath = os.path.dirname(__file__)


def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tostring()).decode('utf8')


def allowed_file(filename):
    filename = filename.lower()
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 上传并抠图
@index_reading_pictures.route('/reading_pictures', methods=['POST', 'GET'])  # 添加路由
def upload():
    print(request)
    if request.method == 'POST':
        try:
            f = request.files['file']
            print(f.filename)
            if not (f and allowed_file(f.filename)):
                # return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
                return render_template('404.html')
            sourcefile = os.path.join('static/images/source', secure_filename(f.filename))
            print('sourcefile: %s' % sourcefile)
            upload_path = os.path.join(basepath, sourcefile)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
            f.save(upload_path)
            print(upload_path)
            print('upload_path: %s' % upload_path)
            results = reading_pictures(sourcefile)
            headers = {"Content-type": "application/json", "charset": "gbk"}
            # results: [{'Poetrys': '山隈山坳山，海滨岭颠海。中有无底渊，千古不可改。'}]
            # return Response(json.dumps(results), content_type='application/json')
            return jsonify(results)
        except Exception:
            return render_template('404.html')
    return render_template('index.html')


# 干活
# def reading_pictures(upload_path):
#     write_poem = hub.Module(name="reading_pictures_writing_poems")
#     print('upload_path %s' % upload_path)
#     print(time.time())
#     print(50 * '*')
#     results = write_poem.WritingPoem(images=[cv2.imread(upload_path)], use_gpu=False)
#     print(50 * '*')
#     print(results)
#     print(time.time())
#     return results
# 干活
def reading_pictures(upload_path):
    print('upload_path: %s' % upload_path)
    # 指定图片分割方法为deeplabv3p_xception65_humanseg并发送post请求
    data = {'images': [cv2_to_base64(cv2.imread(upload_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://localhost:8866/predict/reading_pictures_writing_poems"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    print('request: %s' % r)
    t = time.time()
    results = r.json()["results"]
    print('results: %s' % results)
    return results
