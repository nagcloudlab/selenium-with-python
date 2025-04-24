

import pytest
from pages.todo_page import TodoPage
from utils.assert_helpers import assert_text_in_list

@pytest.mark.smoke
def test_edit_todo(browser):
    page = TodoPage(browser)
    page.load()
    page.add_todo("Initial Task")

    page.edit_todo("Initial Task", "Updated Task")
    texts = page.get_todo_texts()
    assert_text_in_list("Updated Task", texts)

