import xlsxwriter
from termcolor import colored
import string
from pathlib import Path
import openpyxl

class ExcelUtility:
    def excel_write(result, keywords, links):
        try:
            c1 = 1;
            c2 = 1;
            c3 = 1;
            download_path = str(Path.home() / 'Downloads')
            file_name = 'search_result.xlsx'
            workbook = xlsxwriter.Workbook(f'{download_path}\{file_name}')
            wb = openpyxl.load_workbook(f'{download_path}\{file_name}')
            sheet_checker = wb.active
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
                    
            keyword1 = sheet_checker['B1'].value
            keyword2 = sheet_checker['C1'].value
            keyword3 = sheet_checker['D1'].value
                    
            for r in result:
                for i, x in enumerate(r, start=0):
                    worksheet.set_row(i+1, 30) 
                    if keyword1 in r[i]:
                        c1 += 1
                        worksheet.write('B' + str(c1), r[i])
                    elif keyword2 in x:
                        c2 += 1
                        worksheet.write('C' + str(c2), r[i])
                    elif keyword3 in x:
                        c3 += 1
                        worksheet.write('D' + str(c3), r[i])
                    #worksheet.write('B' + str(i+2), r[i])
            
            workbook.close() # Writing in to excel
            wb.close() # Sheet checkern
      
        except Exception as e:
            print("")
            print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
            print(e)
            print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
            print("")
        
