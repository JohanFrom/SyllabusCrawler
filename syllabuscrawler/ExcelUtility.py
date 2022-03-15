import xlsxwriter
from termcolor import colored
import string

class ExcelUtility:
    def excel_write(result, keywords, links):
        for r in result:
            for i in r:
                try:
                    workbook = xlsxwriter.Workbook('search_result.xlsx')
                    worksheet = workbook.add_worksheet()
                    worksheet.set_column(
                        0,
                        4,
                        20
                    )
                    worksheet.write('A1', 'Länkar ↓ Nyckelord →')
                    for i, keyword in enumerate(keywords):
                        if len(keyword) == 0:
                            worksheet.write('A' + str(i+2), links[i])
                            #worksheet.write('A' + str(1+2), "Inget nyckelord")
                            worksheet.write(string.ascii_uppercase[i+1] + str(1), 'Inget nyckelord')
                            worksheet.write('C' + str(i+2), r[i])
                            #worksheet.write(string.ascii_uppercase[i+1] + str(1), links[i])
                        else:
                            worksheet.write('A' + str(i+2), links[i])
                            worksheet.write(string.ascii_uppercase[i+1] + str(1), keywords[i])
                            worksheet.write('C' + str(i+2), r[i])
                            #worksheet.write(string.ascii_uppercase[i+1] + str(1), links[i])
                            #worksheet.write(string.ascii_uppercase[i] + str(1+i), r[0])

                    workbook.close()
                except Exception as e:
                    print("")
                    print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
                    print(e)
                    print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
                    print("")
