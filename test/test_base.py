# coding: utf-8

import os
import sys

#can not be removed ,since 'asposeThreeDcloud' need
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)

from aspose3dcloud.rest import ApiException
from aspose3dcloud.apis.three_d_cloud_api import ThreeDCloudApi
from aspose3dcloud.api_client import ApiClient

grantType = "client_credentials"
clientId = "****your AppID****"
clientSecret = "****your AppKey****"
threeDCloudApi=None

def GetThreeDCloudApi():
    global threeDCloudApi
    if threeDCloudApi is None:
        threeDCloudApi=ThreeDCloudApi(grantType,clientId,clientSecret)

    return threeDCloudApi

 

