print("imported my_module...")
print('the value of name in my_module is: {}'.format(__name__))

__all__ = ['find_index', 'test']

test = 'Test String'

def pr():
    print('_pr')

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
