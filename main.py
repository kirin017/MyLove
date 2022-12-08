#!/usr/bin/env python
# -*- coding:utf-8 -*-

import turtle
import time

def hart_arc():

    for i in range(200):

        turtle.right(1)

        turtle.forward(2)

def move_pen_position(x, y):

    turtle.hideturtle () # Bàn chải ẩn (đầu tiên)

    turtle.up () # <

    turtle.goto(x, y) # Bàn chải di động đến tọa độ bắt đầu được chỉ định (trung tâm của cửa sổ là 0,0)

    turtle.down () # <<

    turtle.showturtle () # Hiển thị bàn chải

# Khởi tạo

turtle.setup(width=800, height=500) # Kích thước (Canvas)

turtle.color('red', 'pink') # màu

turtle.pensize(3) # Độ dày của bàn chải

turtle.speed(1) # tốc độ vẽ

# Khởi tạo Brush bắt đầu tọa độ

move_pen_position(x=0,y=-180) # Vị trí bàn chải di động

turtle.left(140) # Xoay 140 độ sang trái




turtle.begin_fill () # Vị trí điền nền nhãn

# # Đường thẳng (phía dưới bên trái)
turtle.forward(224) # Di chuyển bút hoạt hình về phía trước, 224

# Vòng cung

hart_arc () # <<
turtle.left(120) # Điều chỉnh quan điểm của bàn chải
hart_arc () # arc bên phải

# # (Dưới bên phải)

turtle.forward(224)

turtle.end_fill () # Label Nền điền vào vị trí kết thúc

# Nhấp vào cửa sổ để đóng chương trình

window = turtle.Screen()

window.exitonclick()
