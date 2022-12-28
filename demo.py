class ClassDemo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Class constructor")

    def class_sample_method(self):
        print("sample class method")

classObj = ClassDemo(2,3)
classObj.class_sample_method()
