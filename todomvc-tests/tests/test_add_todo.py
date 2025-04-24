

import pytest
from pages.todo_page import TodoPage
from utils.json_loader import load_test_data

@pytest.mark.parametrize("item", load_test_data("todos.json"))
def test_add_todo_item(browser, item):
    page = TodoPage(browser)
    page.load()
    page.add_todo(item["task"])
    assert item["task"] in page.get_todo_texts()

