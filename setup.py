import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-hbounding-box',
    version='0.0.13',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QGraphicsView with bounding box. User can move vertical border of the box horizontally.',
    url='https://github.com/yjg30737/pyqt-hbounding-box.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8'
    ]
)