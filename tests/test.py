#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-20 17:51:50


from pillow_snippet import convert

from PIL import Image


image = Image.open('example.jpg')

image = image.resize((200, 200))
circle_image = convert.circle_image(image)
circle_image.save("test_result/circle_image.png")
