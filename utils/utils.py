# !/usr/bin/python3
# -*- coding:utf-8 -*-

import base64,hmac
import json
import time,datetime

import requests

class Util:
    def encode(self,key,iso_time,method,uri,data=None):
        if method.upper() == "POST":
            data = str(data).replace("\'","\"")
            message = f"{iso_time}{method}{uri}{data}"
        elif method.upper() == "GET":
            message = f"{iso_time}{method}{uri}"
        else:
            raise Exception("ERROR METHOD")
        print(f"encode_message:{message}")
        message = message.encode('utf-8')
        key = key.encode('utf-8')
        sign = base64.b64encode(hmac.new(key=key, msg=message, digestmod='sha256').digest()).decode('utf-8')
        return sign

    def get_iso_time(self):
        ticks = time.time()
        localdate = datetime.datetime.utcfromtimestamp(ticks)
        iso_time = localdate.isoformat()
        print(iso_time)
        sub = iso_time.rfind(".")
        iso_time_change = iso_time[:sub]+"Z"
        iso_time_change = iso_time[:23]+"Z"
        return iso_time_change

    def get_uri(self,uri, data, method='POST'):
        if method == 'GET' and data != {}:
            append_str = '?'
            append_count = 1
            for i in data:
                if append_count > 1:
                    append_str = append_str + '&'
                append_str = f"{append_str}{i}={data[i]}"
                append_count += 1
            uri = uri + append_str
        print(f"request url:{uri}")
        return uri

    def send_request(self,method,url,headers,data):
        print(f"method:{method},url:{url}")
        print(f"headers:{headers}")
        print(f"data:{data}")
        resp = ''
        if method.upper() == 'POST':
            data = json.dumps(data)
            resp = requests.post(
                url=url,
                headers=headers,
                data=data
            )
        elif method.upper() == 'GET':
            resp = requests.get(
                url=url,
                headers=headers
            )
        print(resp)
        return resp.json()


if __name__ == '__main__':
    res = Util().get_iso_time()
    print(res)
    # ticks = time.time()
    # print(ticks)
    # localdate = datetime.datetime.utcfromtimestamp(ticks)
    # print(localdate)
    # iso_time = localdate.isoformat()
    # print(iso_time)
    # sub = iso_time.rfind(".")
    # print(sub)
    # iso_time_change = iso_time[:sub] + "Z"
    # print(iso_time_change)