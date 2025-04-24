

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TodoPage(BasePage):
    
    URL = "https://todomvc.com/examples/javascript-es6/dist/"
   
    INPUT_BOX = (By.CLASS_NAME, "new-todo")
    TODO_ITEMS = (By.CSS_SELECTOR, ".todo-list li")

    def load(self):
        self.driver.get(self.URL)

    def add_todo(self, text):
        self.type(*self.INPUT_BOX, text + "\n")

    
    # Add to TodoPage
    def edit_todo(self, old_text, new_text):
        items = self.get_elements(*self.TODO_ITEMS)
        for item in items:
            if item.text == old_text:
                ActionChains(self.driver).double_click(item).perform()
                wait=WebDriverWait(self.driver, 10)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.editing")))
                self.driver.execute_script("""
                    const editInput = document.querySelector('li.editing input.edit');
                    editInput.value = arguments[0];
                """, new_text)
                edit_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.editing input.edit")))
                edit_input.send_keys(Keys.RETURN)  # Press Enter to save the changes
                break
    
    def complete_todo(self, text):
        items = self.get_elements(*self.TODO_ITEMS)
        for item in items:
            if item.text == text:
                checkbox = item.find_element(By.CSS_SELECTOR, "input.toggle")
                checkbox.click()
                break

    def delete_todo(self, text):
        items = self.get_elements(*self.TODO_ITEMS)
        for item in items:
            if item.text == text:
                self.driver.execute_script("arguments[0].scrollIntoView()", item)
                ActionChains(self.driver).move_to_element(item).perform()
                destroy = item.find_element(By.CSS_SELECTOR, "button.destroy")
                self.driver.execute_script("arguments[0].click();", destroy)
                break

    def get_todo_texts(self):
        return self.get_texts(*self.TODO_ITEMS)

