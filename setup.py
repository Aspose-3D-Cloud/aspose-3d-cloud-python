# coding: utf-8

"""
    Aspose.3D Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "aspose3dcloud"
VERSION = "20.5"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "asposestoragecloud"]

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.3D.Cloud for Python",
    author="asposecloud",
    author_email="aspose.cloud@aspose.com",
    url="https://github.com/aspose-3d-cloud/aspose-3d-cloud-python",
    keywords=["aspose", "3D", "cloud"],
    install_requires=REQUIRES,
    packages=['aspose3dcloud', 'aspose3dcloud.apis', 'aspose3dcloud.models'],
    include_package_data=True,
    long_description="Aspose.3D Cloud SDK for Python allows you to use Aspose.3D APIs in your Python applications",
    classifiers=[
        'Programming Language :: Python :: 3.7.4',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
