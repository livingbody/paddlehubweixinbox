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
import numpy as np
from flask import Blueprint, render_template
import requests
import json
import cv2
import base64
from flask import json

index_stylepro_artistic = Blueprint("stylepro_artistic", __name__)
# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'bmp', 'jpeg'])
# 当前文件所在路径
basepath = os.path.dirname(__file__)


def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tostring()).decode('utf8')


def base64_to_cv2(b64str):
    data = base64.b64decode(b64str.encode('utf8'))
    data = np.fromstring(data, np.uint8)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return data


def allowed_file(filename):
    filename = filename.lower()
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@index_stylepro_artistic.route('/stylepro_artistic', methods=['POST', 'GET'])  # 添加路由
def upload():
    print(request)
    if request.method == 'POST':
        try:
            f = request.files['file']
            print(f.filename)
            print(request.form.get('mystyle'))
            mystyle = request.form.get('mystyle')
            if not (f and allowed_file(f.filename)):
                # return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
                return render_template('404.html')
            sourcefile = os.path.join('static/images/source', secure_filename(f.filename))
            print('sourcefile: %s' % sourcefile)
            upload_path = os.path.join(basepath, sourcefile)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
            f.save(upload_path)
            results = change_pictures(sourcefile, mystyle)
            headers = {"Content-type": "application/json", "charset": "gbk"}
            return jsonify(results)
        except Exception:
            return render_template('404.html')
    return render_template('style.html')


def change_pictures(upload_path, style):
    style = 'static/images/style/' + str(style) + '.jpg'
    data = {'images': [
        {
            'content': cv2_to_base64(cv2.imread(upload_path)),
            'styles': [cv2_to_base64(cv2.imread(style))],
            # 'use_gpu': False,
            # 'visualization': True,
            # 'output_dir': 'static/images/stylepro_artistic'
        }
    ]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/stylepro_artistic"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    print('*'*50)
    print('stylepro_artistic OK...........')
    # print(base64_to_cv2(r.json()["results"][0]['data']))
    # save_path = r.json()["results"][0]['save_path']

    t = time.time()
    filename = str(t) + '.jpg'
    mypath = os.path.join(basepath, 'static/images/stylepro_artistic', filename)
    cv2.imwrite(mypath, base64_to_cv2(r.json()["results"][0]['data']))
    filepath = {'save_path': os.path.join('static/images/stylepro_artistic', filename)}
    print('filepath: %s' % filepath)
    return filepath

# def change_pictures(upload_path, style):
#     style = 'static/images/style/' + str(style) + '.jpg'
#     print("style: %s" % style)
#     stylepro_artistic = hub.Module(name="stylepro_artistic")
#     print('conttent: %s' % upload_path)
#     result = stylepro_artistic.style_transfer(
#         images=[{
#             'content': cv2.imread(upload_path),
#             'styles': [cv2.imread(style)],
#         }], output_dir='static/images/stylepro_artistic', visualization=True, use_gpu=False)
#     print('result: ')
#     print(result)
#     filepath = result[0]["save_path"]
#     print('filepath: %s' % filepath)
#     filepath = {'save_path': filepath}
#     return filepath
