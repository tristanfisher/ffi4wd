from ctypes import cdll

path = 'libffi_ctypes.so'
lib = cdll.LoadLibrary(path)

class HelloWorld(object):
    def __init__(self):
        self.obj = lib.HelloWorld_new()

    def example_world(self):
        lib.HelloWorld_example_world(self.obj)

t = HelloWorld()
t.example_world()
