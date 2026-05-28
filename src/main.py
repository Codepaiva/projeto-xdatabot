from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings.config import Settings

from pages.login import NavegationLogin
from pages.menu import NavegationMenu
from pages.form import NavegationFormUex
from pages.data_list import NavegationListUex




class XdataBot:
  def __init__(self):
    pass
  
  def user_input_cnpj(self):
    cnpj = input('Insira o CNPJ: ')
  
    if not cnpj:
      print('Insira um CNPJ válido, por favor.')
      
    return cnpj
    
  def run_bot(self, cnpj):
    self.settings = Settings()  # type: ignore
    

    self.driver_chrome = webdriver.Chrome()
    self.driver_chrome.get(self.settings.URL)

    self.login = NavegationLogin(self.driver_chrome, By, WebDriverWait, EC)
    self.menu = NavegationMenu(self.driver_chrome, By, WebDriverWait, EC)
    self.form_uex = NavegationFormUex(self.driver_chrome, By, Keys, WebDriverWait, EC)
    self.list_uex = NavegationListUex(self.driver_chrome, By, WebDriverWait, EC)

    # steps of process:
    # step login:
    self.login.element_input_user(self.settings.USER_NAME)
    self.login.element_input_password(self.settings.USER_PASSWORD)
    self.login.element_button_login()

    # step menu:
    self.menu.element_button_search()
    self.menu.element_button_search_situation()

    # step form:
    self.form_uex.element_drop_down_situation()
    self.form_uex.element_radio_cnpj_option()
    self.form_uex.element_input_cnpj_code(cnpj)
    self.form_uex.element_button_search()

    # step list operation:
    self.list_uex.element_list()
    


if __name__ == '__main__':
  bot = XdataBot()
  cnpj = bot.user_input_cnpj()
  
  bot.run_bot(cnpj)