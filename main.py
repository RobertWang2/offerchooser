# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 11:39
# @Author  : XiaoMa（小马）
# @qq      : 1530253396（任何问题欢迎联系）
# @File    : main.py
import kivy
kivy.require('1.0.6')  # 用你当前的kivy版本替换
from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    MyApp().run()