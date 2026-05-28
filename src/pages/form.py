class NavegationFormUex:
    """
    Navega no formulário de pesquisa UEx
    """
    def __init__(self, driver, by, key, wait, ec):
        self.driver = driver
        self.by = by
        self.keys = key
        self.wait = wait
        self.ec = ec
    

    def element_drop_down_situation(self):
        list_situacao = self.wait(self.driver, 12).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '//*[@id="cbAptaPagamento"]')
            )
        )
        
        
        list_situacao.send_keys(self.keys.ARROW_DOWN)
        list_situacao.send_keys(self.keys.ARROW_DOWN)
        list_situacao.send_keys(self.keys.TAB)

    
    def element_radio_cnpj_option(self):
        radio_cnpj = self.driver.find_element(
            self.by.XPATH, '//*[@id="ext-comp-1113"]'
        )
        radio_cnpj.click()

    
    def element_input_cnpj_code(self, cnpj_code: str):
        cnpj = self.wait(self.driver, 10).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '//*[@id="txCnpj"]')
            )
        )
        
        cnpj.send_keys(self.keys.CONTROL, 'a')
        cnpj.send_keys(cnpj_code)


    def element_button_search(self):
        btn_pesquisar = self.wait(self.driver, 10).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '//*[@id="ext-gen183"]')
                )
            )
        btn_pesquisar.click()