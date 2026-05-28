class NavegationLogin:
    """Navega na tela de login\n
       Insere username > Insere password > clica no botão
    """
    
    def __init__(self, driver, by, wait, ec):
        self.driver = driver
        self.by = by
        self.wait = wait
        self.ec = ec


    def element_input_user(self, user: str):
        user_loggin = self.wait(self.driver, 25).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '//*[@id="j_username"]')
                )
        )
        user_loggin.send_keys(user)


    def element_input_password(self, password: str):
        password_loggin = self.driver.find_element(
            self.by.XPATH, '//*[@id="login"]/form/fieldset/label[2]/input'
        )
        password_loggin.send_keys(password)


    def element_button_login(self):
        btn_login = self.driver.find_element(
            self.by.XPATH, '//*[@id="login"]/form/fieldset/input'
        )
        btn_login.click()