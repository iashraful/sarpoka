import os

from setuptools import find_packages, setup

__author__ = 'Ashraful'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sarpoka',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Sarpoka is a rapidly development Python micro framework designed for serverless applications',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://ashraful.dev',
    author='Mohammad Ashraful Islam',
    author_email='ashrafulrobin3@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'WebOb>=1.8.2'
    ]
)
