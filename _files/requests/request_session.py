#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json

class Issues():
    def __init__(self, url, token, timeout=10):
        self.session = requests.session()
        self.session.headers.update({
            'user-agent': 'zzlzhang',
            'Content-Type': 'application/json',
            'Authorization': "token {0:s}".format(token),
        })
        self.url = url
        self.timeout = timeout
        #  self. headers = {
        #  }

    def _request(self, *args, **kvargs):
        '''
        发送请求
        '''

        def print_url(r, *args, **kwargs):
            print(r.request.__dict__)
            for i in args:
                print(i)
            for key, val in kwargs.items():
                print('{}->{}'.format(key, val))

        #  如果传递了名为 json 的参数, 则使用 requests 的 post 方法,
        #  json 的值应该为一个字典, 表示要 post 的数据
        #  否则调用 get 方法
        req_method = (self.session.get, self.session.post)[False if kvargs.get('json', None) is None else True]
        h = lambda r, *args, **kvargs: print(r.url)

        r = req_method(self.url,
            timeout=self.timeout,
            hooks=dict(response=lambda r, *args, **kvargs: print(r.url)),
            *args,
            **kvargs)
        print('after request')

        if r.status_code != requests.codes.ok:
            r.raise_for_status()
        return r

    def create_issue(self, issue_data):
        '''创建 issue'''
        return self._request(json=issue_data)

    @property
    def get_issues(self):
        '''获取所有 issue'''

        #  直接返回 json 格式
        return self._request().json()

api_url = 'https://api.github.com'
issue_url = '{}/repos/{}/{}/issues'.format(api_url, 'gbyukg', 'auto-install')
#  从环境变量中获取 Github token
token = os.environ.get('token', None)

api = Issues(issue_url, token)
try:
    issue_data = {
        'title': 'issue 4',
        'body': 'This is a issue 4',
    }
    # api.create_issue(issue_data)

    for issue in api.get_issues:
        print('{title}: {body}'.format(**issue))
except (requests.HTTPError, requests.Timeout) as e:
    sys.exit(e)
except Exception as e:
    sys.exit(e)
