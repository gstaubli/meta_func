from setuptools import setup

setup(
    name='meta_func',
    version='0.1.3',
    author='Garren Staubli',
    author_email='gstaubli@gmail.com',
    packages=['meta_func'],
    url='http://www.github.com/gstaubli/meta_func',
    description='Python decorator function to track metadata on function calls',
    long_description=open('README.md').read(),
    install_requires=[
        "decorator"
    ]
)