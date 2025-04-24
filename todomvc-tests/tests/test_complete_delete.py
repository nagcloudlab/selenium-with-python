
from pages.todo_page import TodoPage
from utils.base_test import BaseTest
import time


def test_complete_and_delete_todo(browser):
    page = TodoPage(browser)
    page.load()
    page.add_todo("Delete me")
    time.sleep(5)
    page.complete_todo("Delete me")
    time.sleep(5)
    page.delete_todo("Delete me")

    assert "Delete me" not in page.get_todo_texts()


class TestTodoFeature(BaseTest):
    def test_add_item(self, browser):
        self.log("Starting Add Todo Test")
        ...