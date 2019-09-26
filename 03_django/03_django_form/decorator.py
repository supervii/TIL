def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('HAHAHAHA')
    return wrapper




@hello
def bye():
    print('byebye')

bye()