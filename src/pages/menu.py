class NavegationMenu:
    """Navega no menu principal\n
       consulta situação > consulta situação uex 
    """
    def __init__(self, driver, by, wait, ec):
        self.driver = driver
        self.by = by
        self.wait = wait
        self.ec = ec
    

    def element_button_search(self):
        btn_consulta = self.wait(self.driver, 10).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '//*[@id="ext-gen20"]')
                )
        )
        
        btn_consulta.click()

    
    def element_button_search_situation_uex(self):
        btn_consulta_situacao_uex = self.driver.find_element(
            self.by.XPATH, '//*[@id="ext-gen39"]/div/table/tbody/tr/td[2]/div'
        )
        btn_consulta_situacao_uex.click()