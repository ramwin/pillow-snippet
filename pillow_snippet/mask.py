#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-21 10:59:50


from PIL import Image

"""
create a mask from an image
"""


class Mask(object):

    def __init__(self, image):
        self.image = image
        self.image_grey = image.convert(mode="L")
        self.size = image.size

    def create_transparent_image(self):
        image = Image.new("RGBA", self.size, "#00000000")
        return image

    def get_exclude_white_image(self, tolerance=1):
        threshold = 255 - tolerance
        image = self.create_transparent_image()

        def exclude_white(x):
            if x > threshold:
                return 0
            return 255

        mask = Image.eval(self.image_grey, exclude_white)
        image.paste(self.image, (0,0), mask)
        return image
