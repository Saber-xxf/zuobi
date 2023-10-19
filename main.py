# This is a sample Python script.
# -*- coding: utf-8 -*-
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

from gevent import pywsgi
import init
import json
import keyboard
import screen
import time as t
import numpy as np
import upload_oss as al
import database
import asyncio
from gpt import Gpt
from model import OcrHandle
from flask import Flask, render_template, jsonify, request
import cv2
import threading

from flask_cors import CORS
app = Flask(__name__)
import log
id=""
key=""
ed=""
name=""
my_index=0;
bu_name=""
res=""
gpt=[]
log=""
def on_key_press(event):
    global my_index;
    if event.event_type == keyboard.KEY_DOWN and event.name == 'e' and keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'):
        screenshot = screen.capture_screen_at_mouse()
        name = str(my_index)+"-"+str(int(t.time()))
        path=str(name)+".png"
        my_index=my_index+1;
        screenshot.save(path)
        #禁用gpt
        # trans(path)
        al.Oss().upload(path,id,key,ed,bu_name)

def listen_for_keyboard_event():
    global my_index, id, key, ed, bu_name
    while True:
        if keyboard.is_pressed('ctrl+alt+e'):
            screenshot = screen.capture_screen_at_mouse()
            name = str(my_index) + "-" + str(int(t.time()))
            path = str(name) + ".png"
            my_index = my_index + 1
            screenshot.save(path)
            # 禁用gpt
            # trans(path)
            try:
                al.Oss().upload(path, id, key, ed, bu_name)
            except:
                pass

def trans(path):
    global res
    img = cv2.imread(path)
    r = OcrHandle().text_predict(img, 960)
    res = np.array(r)
    res = res[:, [1]]
    res[0] = "该题为算法题，请提供java代码"
    # print(res)

def task1():
    global my_index, id, key, ed, bu_name,gpt,log
    try:
        Gpt().init()
        my_index = 0
        json_data = init.read_json_file("conf.json")
        gpt = json_data["gpt"]
        mykey = json_data["key"]
        username = json_data["username"]
        id = json_data["conf"]["KeyId"]
        key = json_data["conf"]["KeySecret"]
        ed = json_data["conf"]["endpoint"]
        bu_name = json_data["conf"]["bucket_name"]
    except:
        pass;
    if mykey=='ahu_111_xxf':
        print("开始了")
        keyboard.on_press(on_key_press)
        keyboard.wait('esc')  # 等待按下ESC键退出监听
# 过滤数据的函数
def filter_data(item):
    # 使用正则表达式去掉开头的数字编码和符号
    filtered_item = re.sub(r'^\d+\s*[-、]\s*', '', item)
    # 使用正则表达式去掉结尾的中括号和数字编码
    return re.sub(r'\[\d+\]$', '', filtered_item)

@app.route('/')
def hello_world():
    global res,log
    if type(res) is not str:
        python_list = res.tolist()
        # 将Python列表转换为JSON
        json_data = json.dumps(python_list)
        filtered_data = [filter_data(item[0]) for item in python_list]
        return render_template("index.html",data=filtered_data)

    return log

@app.route('/send-data', methods=['POST'])
def send():
    try:
        # 解析前端发送的JSON数据
        data = request.get_json()
        # 在这里执行您的数据处理逻辑
        answer = Gpt().ask_question(data)
        # print(answer)
        # 构造响应数据
        response_data = answer
        # 返回处理后的结果，并设置字符编码为UTF-8
        return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=UTF-8'}
    except Exception as e:
        return jsonify({"error": str(e)})

def task2():
    app.run(host='0.0.0.0', port=8888)
    # server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    # server.serve_forever()

if __name__ == '__main__':
    task1()
    #禁用gpt
    # task2()


