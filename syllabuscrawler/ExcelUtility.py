import xlsxwriter
from termcolor import colored
import string

class ExcelUtility:
    def excel_write(result, keywords, links):
        for r in result:
            for x in r:
                try:
                    workbook = xlsxwriter.Workbook('search_result.xlsx')
                    worksheet = workbook.add_worksheet()
                    worksheet.write('A1', 'Länkar ↓ Nyckelord →')
                    for i, keyword in enumerate(keywords):
                        if len(keyword) == 0:
                            worksheet.write(string.ascii_uppercase[i+1] + str(1), 'Inget nyckelord')
                            worksheet.write('C' + str(i+2), r[i])
                            
                        else:
                            worksheet.write('A' + str(i+2), links[i])
                            worksheet.write(string.ascii_uppercase[i+1] + str(1), keywords[i])
                            worksheet.write('C' + str(i+2), r[i])
                    
                    workbook.close()
                except Exception as e:
                    print("")
                    print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
                    print(e)
                    print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
                    print("")
