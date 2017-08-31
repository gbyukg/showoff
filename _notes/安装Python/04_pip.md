# pip
@@@ bash
    pip -h
    pip install -h

    pip search requests
    pip search requests | grep -i '^requests '

    pip install requests

    pip list

    pip show requests
    pip show -v/--verbose requests

    # pip uninstall requests
    pip uninstall -y requests

    pip install requests==2.0.0
    # 安装大于版本号大于 2.0.0 的版本
    pip install requests>=2.0.0

    # 查看有更新的版本
    pip list -o

    pip install -U requests

# requirement file
    @@@ bash
    pip freeze
    pip freeze > requirement.txt
    pip install -r requirement.txt
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
