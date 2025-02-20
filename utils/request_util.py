# -*- coding:utf-8 -*-
"""
# Author: Rocky Zhao
# Time: 2024/7/29 11:10
"""
from utils.utils import Util
class BaseMethod(object):
    def __init__(self, api_key, secret_key, passphrase, host, uri, method='GET'):
        self.api_key = api_key
        self.serect_key = secret_key
        self.passphrase = passphrase

        self.host = host
        self.uri = uri
        self.method = method
        self.iso_time = Util().get_iso_time()
        print(f"iso_time:{self.iso_time}")

        self.headers = {
            'OK-ACCESS-KEY': self.api_key,
            'OK-ACCESS-SIGN': "",
            'OK-ACCESS-TIMESTAMP': self.iso_time,
            'OK-ACCESS-PASSPHRASE': self.passphrase,
        }

    def request_app(self,data):
        uri_append = Util().get_uri(uri=self.uri, data=data, method=self.method)
        print(f"uri:{uri_append}")
        sign = Util().encode(key=self.serect_key, iso_time=self.iso_time, method=self.method, data=data, uri=uri_append)
        self.headers['OK-ACCESS-SIGN'] = sign
        url = self.host + uri_append
        resp = Util().send_request(self.method, url, self.headers, data)
        print(f"resp:{resp}")
        return resp