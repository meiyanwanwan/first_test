import allure


class  TestLogin:
    @allure.step(title="这是一个步骤")
    def test_01(self):
        print("haha")
        allure.attach('描述2', '哈哈')
        assert 1

    @allure.step(title="这是一个步骤")
    def test_02(self):
        print("sb")
        allure.attach('描述2','这是一个描述')
        assert 0