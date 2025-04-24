

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TodoPage(BasePage):
    
    URL = "https://todomvc.com/examples/javascript-es6/dist/"
   
    INPUT_BOX = (By.CLASS_NAME, "new-todo")
    TODO_ITEMS = (By.CSS_SELECTOR, ".todo-list li")

    def load(self):
        self.driver.get(self.URL)

    def add_todo(self, text):
        self.type(*self.INPUT_BOX, text + "\n")

    def get_todo_texts(self):
        return self.get_texts(*self.TODO_ITEMS)

