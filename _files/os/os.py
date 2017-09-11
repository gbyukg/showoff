import os

os.getcwd()

# 也可以使用相对路径
# os.chdir('../')
os.chdir('Users/gbyukg/Desktop')

os.listdir()

os.mkdir('tmp')
os.chdir('tmp')
os.getcwd()

# 报错, 因为上层目录不存在
os.mkdir('tmp1/tmp2/tmp3')
# 可以使用 makedirs 来迭代创建目录
os.makedirs('tmp1/tmp2/tmp3')
# 报错, 提示目录不为空
os.rmdir('tmp1')
os.removedirs('tmp1/tmp2/tmp3')

# 创建文件
with open('test.txt', 'w') as f: pass
# 重命名
os.rename('test.txt', 'demo.txt')
os.listdir()

os.stat('demo.txt')
# 获取文件大小
os.stat('demo.txt').st_size
os.stat('demo.txt').st_mtime

for dirpath, dirname, filename in os.walk('.'):
    print('Current Path:', dirpath)
    print('Directories:', dirname)
    print('Files:', filename)

# 环境变量
os.environ
os.environ['HOME']
os.environ['MODULE'] = 'os'

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
os.makedirs(file_path)

os.path.basename('/Users/gbyukg/Desktop/os/demo.txt') # demo.txt
os.path.dirname('/Users/gbyukg/Desktop/os/demo.txt') # /Users/gbyukg/Desktop/os
os.path.split('/Users/gbyukg/Desktop/os/demo.txt') # ('/Users/gbyukg/Desktop/os', 'demo.txt')
os.path.exists('/Users/gbyukg/Desktop/os/demo.txt') # True

os.path.isdir('/Users/gbyukg/Desktop/os/demo.txt')
os.path.isfile('/Users/gbyukg/Desktop/os/demo.txt')
os.path.splitext('/Users/gbyukg/Desktop/os/demo.txt')
dir(os.path)
