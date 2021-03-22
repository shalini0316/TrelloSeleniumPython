import openpyxl


class HomePageData:

    test_HomePage_data = [{"Email":"shalini"}, {"Email":"Anshika"}]

    @staticmethod
    def getTestData(testCaseName):
        Dict = {}
        list=[]
        book = openpyxl.load_workbook("C:\\Users\\BLACKPEARL COMPUTERS\\PycharmProjects\\pythonProject\\PythonSelFramework\\tests\\testsuite.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):  # to get rows
            if sheet.cell(row=i, column=1).value == testCaseName:

                for j in range(2, sheet.max_column + 1):  # to get columns
                    # Dict["lastname"]="shetty
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
                list.append(Dict)
        return list

