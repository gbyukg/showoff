#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json

class Issues():
    def __init__(self, url, token):
        self.url = url
        self.timeout = 10
        self. headers = {
            'user-agent': 'zzlzhang',
            'Content-Type': 'application/json',
            'Authorization': "token {0:s}".format(token),
        }

    def _request(self, *args, **kvargs):
        method = 'get' if kvargs.get('json', None) is None else 'post'

        req_method = (requests.get, requests.post)[False if kvargs.get('json', None) is None else True]

        r = req_method(self.url,
            headers=self.headers,
            timeout=self.timeout,
            *args,
            **kvargs)


        if r.status_code != requests.codes.ok:
            r.raise_for_status()
        return r

    def create_issue(self, issue_data):
        '''创建 issue'''
        return self._request(json=issue_data)

    @property
    def get_issues(self):
        '''获取 issue'''

        #  Github API 返回 JSON 格式字符串
        #  直接将返回 JSON 数据转换成字典
        return self._request().json()

api_url = 'https://api.github.com'
issue_url = '{}/repos/{}/{}/issues'.format(api_url, 'gbyukg', 'auto-install')
token = os.environ.get('token', None)

api = Issues(issue_url, token)
try:
    issue_data = {
        'title': 'issue 4',
        'body': 'This is a issue 4',
    }
    #  api.create_issue(issue_data)

    for issue in api.get_issues:
        print('{title}: {body}'.format(**issue))
except (requests.HTTPError, requests.Timeout) as e:
    sys.exit(e)
except Exception as e:
    sys.exit(e)
