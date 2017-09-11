其实在 Python 中有很多 HTTP 库, 比如内置的就有 urllib2, 和后来的 urllib3, 但是 requests 库非常方便, 一般用 urllib 库需要很多代码才能实现的功能, 用 requests 库几行代码就可以搞定.  
其实 requests 库就是对 urllib 库的二次封装

## GET

    @@@ python
    r = requests.get('http://httpbin.org/get')
    type(r)
    # 或 r?
    r.text # 获取HTTP响应信息的 body 部分
    print(r.text)

## 传递数据
    @@@ python
    # 通过 URL 传递数据给 HTTP server
    r = requests.get('http://httpbin.org/get?name=user1')
    print(r.text)

    # 我们还可以将要传递的数据从 URL 中分离出来
    # 以字典的形式使用 get 方法的 params 参数传递
    r = requests.get('http://httpbin.org/get', params={'name': 'user1'})

## POST
    @@@ python
    r = requests.post('http://httpbin.org/post', data = {'name':'user1'})

    # 有些时候, 我们需要向一个请求发送 JSON 格式的数据
    # 比如几乎所有的 github api
    # 我们可以直接把将要传递的字典通过 json 参数传递给 post 方法
    # requests 会自动将传递给它的字典转换成 json 格式
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    r = requests.post(url, json=payload)

## 自定义头信息
当我们发送一个请求后, requests 会自动为我们定义一些默认的请求头信息

`get()` 方法的 `headers` 参数能够让我们自定义要传递的 HTTP 头信息.

    @@@ python
    headers = {'user-agent': 'Custom Request HEADERS'}
    r = requests.get('http://httpbin.org/get', headers=headers)

## 请求状态
向一个 HTTP server 发送请求时, 并不是每次都会成功, HTTP 通过状态码来反应请求的状态. 比如最常见的 200 表示成功, 404 表示自愿未找到, 500 表示 server 段出错.

    @@@ python
    # 来获取 HTTP 状态码
    r.status_code
    # 同时 r.reason 记录的状态码的简短说明
    r.reason

## requests.codes
Python 提供了一个内置对象 requests.codes, 里面记录了所有状态码信息, 比如

    @@@ python
    # 比如 表示成功
    requests.codes.ok
    # 404
    requests.codes.not_found

    dir(requests.codes)

    # 判断一个请求是否成功
    r.status_code == requests.codes.ok

## 抛出异常
当 HTTP 请求发生错误时, 即状态码不是 200, 我们可以使用 Response 对象的 `raise_for_status()` 方法来抛出一个异常, 这个方法将会自动根据 HTTP 状态码生成相应的异常消息.

向一个状态码为 200 的 Response 对象调用 `raise_for_status()` 方法没有任何效果

    @@@ python
    r = requests.get('http://httpbin.org/get/404')
    r.status_code
    r.reason
    r.raise_for_status()

## cookies
    @@@ python
    r = requests.get('http://httpbin.org/cookies', cookies={'cookies_are':'working'})
    print(r.text)

## Response 对象
    @@@ python
    # 获取所有属性信息
    r.__dict__
    # 已经介绍过了 status_code 和 reason

    r.headers
    r.url
    # 以二进制格式反回 HTTP body 中的内容
    # 这就说明里面的换行符不会被转义
    r._content
    print(r._content)
    # 获取HTTP响应头信息
    r.headers
    # 也可以获取指定头信息
    r.headers['Content-Type']
    # 因为是字典, 所以还可以使用 get
    r.headers.get('Content-Type')

    # 方法
    # 一直只是用的 text 方法
    r.text
    # 注意它并不是属性
    r.text?
    # 可以看到它其实是一个使用了 property 装饰器的方法

    # 同样的方法还有
    r.content
    # 以二进制的格式返回
    # 而 text 方法会根据 `encoding` 对 content 内容转以后
    # 以文本的格式返回回来

# session
HTTP 属于无状态连接, 就是每次连接都是相互独立的, 但是有些时候我们希望服务器端能记住我们的连接, 典型的例子就是用户登录, 当用户登录一个web系统后, 之后的每次请求, 服务器端都应该知道这是一个已经登录的用户, 并且能够分辨出到底是它哪个用户, 既然 HTTP 是无状态的连接, 它不能将我们的信息告诉服务器端, 这时就出现了 cookies 和 session, 来达到这个目的.



---

首先需要安装 Requests 模块: `pip install -U requests`

    @@@ python
    import requests

    # 我们知道, HTTP提供了4个基本的请求方法
    # GET(查)，POST(改)，PUT(增)，DELETE(删)
    # HEAD

    # 先看一下最简单的 gt 请求
    # 通过调用 requests 的 get 方法
    # 就可以发送一个 get 请求了
    # 至少接收一个 URL 地址作为参数
    requests.get('http://httpbin.org/')

    # 当执行这段代码时
    # requests 就像这个 URL 地址发送了一个 get 请求
    # 我们知道, 向一个 HTTP 发送请求后
    # HTTP server 处理完请求后, 还会返回给我们一个响应, 叫 Response
    # 无论是用什么语言, 还是什么浏览器, 都是这个流程
    # 所以当请求发送完毕, 会继续等待响应
    # 直到获取响应后
    # get 方法才会返回
    # 并且将返回的信息封装到一个对象中
    # 通过这个返回的对象, 我们可以获取到所有我们需要的信息
    # 所以为了捕获返回回来的信息,
    # 我们需要使用一个变量来接收这个返回的对象
    r = requests.get('http://httpbin.org/get')

这里为了方便查看返回的对象, 我们继续使用 iPython, 在 iPyhton 中执行这段代码

    @@@ python
    import requests
    r = requests.get('https://api.github.com')

    r? # Response 类
    # 既然是类, 我们就能看到这个类里有哪些属性
    r.__dict__

    # HTTP 响应码
    r.status_code
    # 请求地址
    r.url
    # 请求头
    r.headers
    # 请求的 body(内容)
    r._content

    # 但是我们通常不会这样获取 response 的内容
    # 可以通过 content 来获取
    r.content
    # 它返回的是一个 raw 字符串(原始字符串)
    print(r.content)
    # content 其实是 Response 类中的一个方法
    r.content?
    # 使用了 property 装饰器
    # 使它看起来像个属性

    # 还有一个跟 content 方法类似的方法 text
    r.text
    # 它返回的其实是使用 r.encoding 解码后的 content 字符串
    print(r.text)

## 向请求发送数据


## 自定义头信息
    @@@ python
    payload = {'some': 'data'}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)




## 判断请求是否成功
每个 HTTP 响应头中都包含了一个状态码, 比如 200 最常见的状态码, 表示请求跟响应都成功了, 我们可以通过 返回的 response 对象中的 `status_codes` 属性来获取这个状态码.

    @@@ python
    r.status_code

requests 为我们提供了一个内置的 LookupDict 对象 requests.codes, 里面保存了所有的状态码, 通过和它比较可以很方便的判断出响应是否成功

    @@@ python
    r.status_code == requests.codes.ok
    # 返回 True 表示执行成功
    # 有时也会用 r.reason == 'OK' 来判断一个请求是否成功

    # 查看所有定义的状态码
    requests.codes.__dict__

    # 在看一个例子
    bad_r = requests.get('http://httpbin.org/404')
    bad_r.status_code
    # 同时 r.reason 保存了对应的错误信息
    
    # 当 return code 不是 200, 说明有错误产生,
    # 此时我们可以使用 requests 的 raise_for_status() 方法
    # 来抛出一个异常
    # 这个方法会自动根据当前的返回码来抛出相应的错误信息
    bad_r.raise_for_status()
    # 如果尝试使用一个返回值是 200 的对象调用这个方法
    # 则什么也不会做
    r.raise_for_status()