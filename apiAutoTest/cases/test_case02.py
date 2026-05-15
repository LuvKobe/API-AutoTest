class Test:
    def setup_method(self):
        print("Setup: Before each test")

    def test01(self):
        print("test01方法")

    def test02(self):
        print("test02方法")

    def teardown_method(self):
        print("Teardown: After each test")
