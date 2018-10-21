


class test_dict(object):
    def __init__(self, a):
        self.a = a

    def run(self, b):
        self.b = b

if __name__=='__main__':
    t = test_dict('aa')
    t.run('bb')
    print t.__dict__

    print type(t.__dict__)
