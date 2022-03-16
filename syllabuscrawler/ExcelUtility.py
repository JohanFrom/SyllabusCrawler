import xlsxwriter
from termcolor import colored
import string
from pathlib import Path

class ExcelUtility:
    def excel_write(result, keywords, links):
        try:
            download_path = str(Path.home() / 'Downloads')
            file_name = 'search_result.xlsx'
            workbook = xlsxwriter.Workbook(f'{download_path}\{file_name}')
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', 'Länkar ↓ Nyckelord →') 
            worksheet.set_column('A:D', 50)
            
            for i, link in enumerate(links):
                worksheet.write('A' + str(i+2), links[i])
                
            for i, keyword in enumerate(keywords):
                if len(keyword) == 0:
                    worksheet.write(string.ascii_uppercase[i+1] + str(1), 'Inget nyckelord')
                else:  
                    worksheet.write(string.ascii_uppercase[i+1] + str(1), keywords[i].capitalize())
                    
            for r in result:
                for i, x in enumerate(r, start=0):
                    worksheet.set_row(i+1, 30) 
                    worksheet.write('B' + str(i+2), r[i])
            
            workbook.close()
      
        except Exception as e:
            print("")
            print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
            print(e)
            print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
            print("")
        