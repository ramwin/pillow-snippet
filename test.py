#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-20 17:51:50


from pillow_snippet import convert
from pillow_snippet.mask import Mask
import tempfile

from PIL import Image


origin_image = Image.open('colorful_example.png')
origin_image2 = Image.open("colorful_image.png")

image = origin_image.resize((200, 200))
circle_image = convert.circle_image(image)
circle_image.save("test_result/circle_image.png")

mask = Mask(origin_image)
exclude_white_image = mask.get_exclude_white_image(tolerance=8)
exclude_white_image.save("test_result/exclude_white_image.png")
change_to_red_image = mask.convert_to_single_color("#ff0000ff")
change_to_red_image.save("test_result/change_to_red_image.png")

mask2 = Mask(origin_image2)
change_to_green_image = mask2.convert_to_single_color("#00ff00ff", mode="L")
change_to_green_image.save("test_result/change_to_green_image_L.png")
change_to_green_image = mask2.convert_to_single_color("#00ff00ff", mode="opacity")
change_to_green_image.save("test_result/change_to_green_image_opacity.png")

# save the data to a temporaryfile
f = tempfile.TemporaryFile(suffix="png")
change_to_red_image.save(f, format="png")
f.seek(0)
with open("test_result/tempfile.png", "wb") as target:
    target.write(f.read())
