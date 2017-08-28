# 属性装饰器

在 Employee 类的构造方法中, 我们通过手动拼接的方式拼接出每个员工的邮箱地址, 但是问题是, 当我们修改了员工的first name 或是 last name 后, 员工的邮箱地址不会发生相应的变化, 除非是在我们修改了员工名字后在手动修改邮箱地址.

我们可以为 Employee 类创建一个方法, 专门用来获取用户邮箱的, 这个方法中每次都会获取员工的名字来拼接邮箱地址, 这样即使员工的姓名发生了变化, 我们也能正确获取到员工的邮箱了.

    @@@ python
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    # 移除掉构造函数中的 email 属性
    # 这样我们就可以直接通过调用 email() 方法来获取员工的邮箱地址了
    print(mgr_1.email())

虽然现在我们可以正确获取到用户的邮箱地址了, 但是我们需要通过追加括号的方式调用 email 方法, 来获取用户的email信息. 怎么样才能向访问一个属性那样直接访问emai地址呢?  
答案就是通过 property decorator.  
定义一个 property decorator 非常简单, 在方法上加上 @property 即可, 这样我们就可以忽略 emai 后面的括号, 而像访问属性那样访问这个方法了.

用同样的方式修改 fullname() 方法, 就像类中已经有了 fullname 属性那样, 可以直接访问全名了.

# setter decorator
现在我们又有新的需求了, 既然 fullname 是通过 first name 和 last name 拼接而成的, 那么我们希望可以通过像给 first 属性那样给一个员工赋值一个全名, 我们的类会根据给定的这个全名拆分成 first name 和 last name, 并分别赋给实例的 first 和 last 属性.

例如: 我们希望通过语句 `mgr_1.fullname = 'John Smith'` 来给 emp_1 员工赋值一个全名, 并且更新他的 fist name 和 last name.  
如果此时我们直接执行这段代码, Python 会提示我们一个错误: `can't set attribute.`  
这是因为当前的 Employee 中已近存在了一个名为 `fullname` 的方法, 当我们再次尝试设置一个同名的属性时, Python 就会提示我们无法设置这个属性.  
为了实现这个功能, 我们必须使用 Python 中的 setter decorator. setter decorator 同样是作用在类中的方法上的. 当我们将某个方法设置成了 setter decorator 后, 就可以像为属性赋值那样通过赋值语句调用这个方法了. setter decorator 除了自动接收 `self` 参数以外, 还会额外接收一个参数, 这个参数就是我们调用赋值语句时等号右边的值.

创建一个 setter decorator 的格式为: `@方法名.setter`

    @@@ python
    # 这个例子中, 我们希望像直接给 fullname 赋值那样来使用
    # 所以创建一个 fullname 的 setter decorator
    @fullname.setter
    # 接着创建一个同名的 fullname 方法
    # 这个方法会接收一个参数, 我们这里使用 name
    # 而它的值就是来自于我们调用
    # mgr_1.fullname = 'John Smith 时指定的值
    def fullname(self, name):
        # 首先使用空格拆分 fullname
        # 并将拆分的结果分别赋值给 first 变量和 last 变量
        first, last = name.split(' ')
        # 当获取到 first name 和 last name后
        # 就可以更新实例中的这两个属性了
        self.first = first
        self.last = last

    # 这是我们就可以像给类属性赋值那样调用 fullname 这个方法了
    mgr_1.fullname = 'John Smith'
    # 打印出 first name 和 last name
    # 查看结果
    print(mgr_1.first)
    print(mgr_1.last)
    # 这是我们再次尝试获取 email 地址, 也能够正确获取到了
    print(mgr_1.email)

# deleter decoratory

继续使用这个例子, 现在我们希望能够像删除属性那样删除 Employee 中的 fullname, 与此同时, first name 和 last name 属性也应当同时置空.

    @@@ python
    # 设置一个 deleter decoratory
    @ fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
    # 删除 fullname 属性
    del mgr_1.fullname
