from setuptools import find_packages, setup
import pathlib
import os


setup(
    name = "py_fuctions",
    version = "0.4",
    author = "Rama Chaitanya Karanam",
    author_email = "ramachaitanya0@gmail.com",
    description = 'Collection of Handy python functions used daily in data science work',
    # long_description = readme,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/ramachaitanya0/my_py_functions",

    classifiers = [ 
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ] ,
    

    license='MIT',
    packages = find_packages()
    # install_requires = [ 'pandas','numpy','sklearn>=0.22.1']
)

