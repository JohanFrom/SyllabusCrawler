import xlsxwriter

class ExcelUtility:
    def excel_write():
        workbook = xlsxwriter.Workbook('search_result.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Keyword1')
        worksheet.write('B1', 'Keyword2')
        worksheet.write('C1', 'Keyword3')

        workbook.close()
