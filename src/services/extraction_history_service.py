from bs4 import BeautifulSoup

from .export_excel_service import ExcelService


class ExtractionHistory:
    def __init__(self, title, table, name_file):
        self.title = title
        self.table = table
        self.name = name_file
    
    
    def parser_title(self):
        html_title = self.title.get_attribute('outerHTML')

        soup = BeautifulSoup(html_title, 'html.parser')

        titulo_history = soup.find_all('h2')
        
        return titulo_history
        

    def parser_history(self):
        html_table = self.table.get_attribute('outerHTML')

        soup = BeautifulSoup(html_table, 'html.parser')

        lines = soup.find_all('tr')

        self.data_history = []

        for line in lines:
            columns = line.find_all('td')

            if columns:
                row = [column.get_text(strip=True) for column in columns]
                self.data_history.append(row)
    
        return self.data_history
    

    def record(self):
        title = self.parser_title()
        history = self.parser_history()
        
        self.file = ExcelService()
        self.file.file_xlsx(title, history, self.name)
        