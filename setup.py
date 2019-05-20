#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-20 17:42:16

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pillow-snippet",
    version="0.0.1",
    author="Xiang Wang",
    author_email="ramwin@qq.com",
    description="some useful snippet for image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramwin/pillow_snippet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
