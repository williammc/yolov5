#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='yolov5',
      version='4.0.1',
      description='Yolov5 for object detection.',
      url='git@github.com:williammc/yolov5.git',
      author='ultralytics',
      author_email='',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE',
    )
