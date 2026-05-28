from services.extraction_history_service import ExtractionHistory


class NavegationListUex:
    def __init__(self, driver, by, wait, ec):
        self.driver = driver
        self.by = by
        self.wait = wait
        self.ec = ec


    def element_list_operation(self):
        list_operation = self.wait(self.driver, 10).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]')
                )
            )

        return list_operation
    

    def element_table_of_datas(self):
        get_table_list_history = self.wait(self.driver, 12).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '/html/body/div[23]/div[2]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]')
            )
        )

        return get_table_list_history
    

    def element_title(self):
        get_identification = self.wait(self.driver, 10).until(
             self.ec.visibility_of_element_located(
                  (self.by.XPATH, '/html/body/div[23]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div')
                )
        )

        return get_identification


    
    def element_list(self):
        name_history = self.wait(self.driver, 10).until(
            self.ec.visibility_of_element_located(
                (self.by.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr/td[4]/div')
                )
            )
        
        
        
        self.list_operation = self.element_list_operation()

        numbers_lines = len(self.list_operation.find_elements(self.by.TAG_NAME, 'tr'))

        for i in range(numbers_lines):
            operation_detail_history = self.wait(self.driver, 10).until(
                self.ec.visibility_of_element_located(
                    (self.by.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div')
                    )
                )

            lines = operation_detail_history.find_elements(self.by.TAG_NAME, 'tr')

            line = lines[i]

            column = line.find_elements(self.by.TAG_NAME, 'td')

            if column:
                try:
                    btn_operation = column[12].find_element(self.by.TAG_NAME, 'a')
                    btn_operation.click()

                    title = self.element_title()
                    table = self.element_table_of_datas()

                    self.record = ExtractionHistory(title, table, name_history)
                    self.record.record()

                    btn_close_window_history = self.wait(self.driver, 10).until(
                         self.ec.visibility_of_element_located(
                              (self.by.XPATH, '/html/body/div[23]/div[2]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/em/button')
                              )
                        )
                    btn_close_window_history.click()

                except:
                    self.driver.execute_script("arguments[0].click();", btn_operation)
                
                finally:
                    print('Dados salvo com sucesso.')
