# 测试用例
import pytest
from appiumPO_test.page.app import App
import yaml


def get_data():
    with open("../data/data.yaml", encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        addnumber = data["add"]
        return addnumber


class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,phone", get_data())
    def test_add_contact(self, name, phone):
        # name = "jeff"
        # phone = "13288888888"
        toast = self.main.click_addresslist().add_member().addconect_manual(). \
            edit_name(name).edit_phone(phone).click_save().get_toast()

        assert toast == "添加成功"
