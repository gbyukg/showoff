<!SLIDE>
# request
`requests` 是一个非常简单高效的 HTTP 库, 通过它, 我们可以方便的创建任意类型的 HTTP 请求.

## 安装 requests
`requests` 并不属于 Python 的内置库, 因此在使用之前, 必须先要安装:  
`pip install requests`

安装好之后, 就可以在代码中通过 `import` 引入 `requests` 库了:  
`import requests`

# HTTP 请求方法

4 种最常用的 HTTP 请求方法

- `GET` 向 HTTP server 发送查询请求
- `HEAD` 类似于 `GET`, 但仅仅返回 HTTP 响应状态 和 HTTP头信息
- `POST` 向 HTTP server 发送数据
- `DELETE` 向 HTTP 发送 delete 请求通知服务器我们想要删除数据

# 发送请求
## GET 请求
通过 `requests` 提供的 `get()` 方法发送一个 GET 请求, 该方法至少接收一个 URL 作为参数. 同时该方法返回一个 `reuests.response` 对象, 该对象保存了所有获取到的 HTTP 响应信息, 同时也保存了所有的请求信息.

    @@@ python
    import requests
    r = requests.get('https://api.github.com')

通过 `response` 对象的 `text` 获取 HTTP 响应信息中的 `body` 部分.

    @@@ python
    print(r.text)

### GET 传递数据
GET 请求传递数据有2中方式:

**通过常规的方式, 将所有参数放到 URL 中传递给 HTTP 服务器**

    @@@ python
    r = requests.get('http://httpbin.org/get?name=user1')

**通过 get 方法中的 `params` 参数, 将要传递的数据以字典的方式发送出去**

    @@@ python
    data = {'name': 'user1'}
    r = requests.get('http://httpbin.org/get', params=data)

## 发送 POST 请求
`requests` 中的 `post()` 方法用体发送一个 POST 请求, 当使用 `post()` 方法时, 除了传递一个 URL 外, 还需要将要发送的数据通过 `data` 参数传递给它

    @@@ python
    r = requests.post('http://httpbin.org/post', data = {'name':'user1'})

传递 JSON

    @@@ python
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    r = requests.post(url, json=payload)

## 其他请求

    @@@ python
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')

# 自定义头信息
当我们发送一个请求后, requests 会自动为我们定义一些默认的请求头信息, 可以通过返回的 response 对象中的 `request.headers` 来获取发送的请求头信息

`get()` 方法的 `headers` 参数能够让我们自定义要传递的 HTTP 头信息.

    @@@ python
    headers = {'user-agent': 'Custom Request HEADERS'}
    r = requests.get('http://httpbin.org/get', headers=headers)
    r.requests.headers

    #  获取响应头信息
    r.headers

# 请求状态
向一个 HTTP server 发送请求时, 并不是每次都会成功, HTTP 通过状态码来反应请求的状态. 比如最常见的 200 表示成功, 404 表示自愿未找到, 500 表示 server 端出错.

response 对象的 `status_code` 属性记录了 HTTP 状态码, `r.reason` 记录了状态码对应的简短描述, 比如 `OK` 表示状态码为200, 请求成功;

requests 库提供了一个自定义对象 `requests.codes`, 里面记录了所有 HTTP 状态码, 比如 `requests.codes.ok` 对应的状态码为 `200`, 通常可以用它与 `status_code` 比较来判断请求是否成功:

    @@@ python
    r.status_code == requests.codes.ok

# `raise_for_status()` 方法
当一个 HTTP 请求发生错误时, 即状态码不为 `200`, 可以通过 `raise_for_status()` 方法抛出一个异常, 这个方法将会自动根据 HTTP 状态码生成相应的异常消息.

    @@@ python
    r = requests.get('http://httpbin.org/get/404')
    r.raise_for_status()

.callout.info 如果一个状态码为 `200` 的 request 对象调用 `raise_for_status()` 方法, 不会发生任何事.

# cookies
    @@@ python
    r = requests.get('http://httpbin.org/cookies', cookies={'cookies_are':'working'})
    print(r.text)

# request 对象
## 属性

- `status_code`: HTTP 响应状态码
- `reason`: 状态码的简短描述
- `headers`: HTTP 响应的头信息
- `url`: 发送请求的 URL 地址
- `_content`: HTTP 响应的 body, 以二进制格式保存(换行符不会被转换)
- `encoding`: 编码格式
- `request`: request 对象, 保存了所有的 HTTP 请求信息

## 方法
- `content`: 以二进制的格式返回 HTTP 请求头中的
- `text`: 以 `encoding` 中指定的编码格式对 `content` 进行编码后, 以文本方式返回回来.
- `json`: 如果返回的结果是 json 字符串, 则直接将 JSON 格式的字符串转换成 Python 中的对象, 如果结果不是正确的 JSON 格式的字符串, 则会抛出异常.
- `ok`: 当 `status_code` 小于 400 时, 该值为 `True`. 注意: 该值为 `True` 并不代表 HTTP 状态码就是 200.

# requests 异常
所有异常信息全部定义在 `requests.exceptions` 中, 比较常见的异常信息有:

- `HTTPError`: 如果获取到了错误的 HTTP 响应, 则抛出该异常.
- `ConnectionError`: 通常在网络出现错误时抛出该异常.
- `Timeout`: 等待响应时间时遇到超时时抛出该异常.
- `TooManyRedirects`: 重定向次数超出最大限制时抛出该异常.

<!SLIDE transition=turnUp>
# requests 示例

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import os
    import sys
    import requests
    import json

    class Issues():
        def __init__(self, url, token, timeout=10):
            self.url = url
            self.timeout = timeout
            self.headers = {
                'user-agent': 'zzlzhang',
                'Content-Type': 'application/json',
                'Authorization': "token {0:s}".format(token),
            }

        def _request(self, *args, **kvargs):
            '''
            发送请求
            '''

            #  如果传递了名为 json 的参数, 则使用 requests 的 post 方法,
            #  json 的值应该为一个字典, 表示要 post 的数据
            #  否则调用 get 方法
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
        api.create_issue(issue_data)

        for issue in api.get_issues:
            print('{title}: {body}'.format(**issue))
    except (requests.HTTPError, requests.Timeout) as e:
        sys.exit(e)
    except Exception as e:
        sys.exit(e)

<!SLIDE transition=turnUp>
# requests 高级应用
# `session` 对象
HTTP 属于无状态连接, 每次连接都是单独的, 相互独立的, 互相之间不能共享信息. 但是有些时候我们希望服务器端能记住我们的连接, 典型的例子就是用户登录, 当用户登录一个 web 系统后, 之后的每次请求, 服务器端都应该知道这是一个已经登录的用户, 并且能够分辨出具体是哪个用户, 既然 HTTP 是无状态连接, 它不能将我们的信息告诉服务器端, 这时就出现了 cookies 和 session, 来帮助我们达到这个目的.

requests 模提供了 `session` 对象, 我们可以向该对象中添加一些需要持久化的数据, 或者是 cookies, 这样当我们通过 `session` 对象向同一 URL 发送的所有 HTTP 请求都将共享这些数据.

创建 session 对象

    @@@ python
    s = requests.session()

request 中的所有请求方法, session 对象中都有同样的方法.

    @@@ python
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')

也可以提前为 session 对象预设一些属性, 这样通过这个 session 对象发送的请求都会包含这些信息

    @@@ python
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})

    # both 'x-test' and 'x-test2' are sent
    s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

    # 此时 x-text2 头信息将不会被传递
    # 只有通过 session 对象设定的属性才会被所有请求共享
    s.get('http://httpbin.org/headers')

# `stream` 参数

默认情况下, 当发送一个请求时, 接收到的请求中的 body 部分将全部被下载下来, 如果 body 部分很大(下载文件), 一次性将这些内容全部出去出来, 将会占用大量的内存空间.

此时我们可以将 `stream` 参数设置为 `True`, 当我们再次发送请求后, 返回给我们的仅仅是响应头信息, 真正的内容此时并没有返回给我们, 并且这个连接一直保持打开状态, 这样可以让我们持续地从这个连接中读取真正的内容.

    @@@ python
    r = requests.get("https://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz", stream=True)
    r.headers['content-length']

我们可以通过 headers 中的 `content-length` 属性来获取整个 body 中的长度.

当我们使用这种方式打开一个连接后, 就可以依次下载并读取 body 中的内容了, 有两个函数可以达到这个目的:

  - `Response.iter_content(chunk_size=1, decode_unicode=False)`: 返回一个迭代器, 每次从 body 中读取 `chunk_size` 个字节, 如果 `decode_unicode` 指定为 `True`, 则在读取内容时不进行解码
  - `Response.iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)`: 返回一个迭代器, 每次读取 body 中的一行内容, 或是 `chunk_size` 个字节(当行长度超过这个长度时).

当我们以这种方式打开一个连接后, 连接会始终保持打开状态, 除非 body 中的内容被全部读取完毕以后, 或者是显示地调用 `Response.close()` 方法来关闭连接.

完整示例

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import requests

    r = requests.get("https://pypi.python.org/packages/source/F/Flask/Flask-0.10.1.tar.gz", stream=True)

    with open('Flash.tar.gz', 'wb+') as f:
        for data in r.iter_content(2048, decode_unicode=False):
            print("Length: {:d}".format(len(data)))
            f.write(data)

    r.close()

# hook
requests 实现了 hook 机制, 通过它我们可以对请求回来的响应信息做一些二次操作, 或者是监听某个特定信号.

## 注册 hoook
hook 是通过 `hooks` 参数注册的, 该参数接收一个字典, 字典的格式为

    @@@ python
    hooks = {hook_name: callback_function}

其中 `hook_name` 是我们要注册的 hook 名字, 当前可用的 hook 有 `response`, 每当请求返回时, `response` hook 将会被调用.  
`callback_function` 指向了一个函数, 当 hook 机制触发后, 该函数将被调用, 并且返回的 `response` 将作为第一个参数传递给它.

示例:

    @@@ python
    def print_url(r, *args, **kwargs):
        print(r.url)

    requests.get('http://httpbin.org', hooks=dict(response=print_url))