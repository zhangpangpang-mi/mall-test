import openpyxl


def read_excel(path):

    workbook = openpyxl.load_workbook(path)

    sheet = workbook.active


    rows = list(sheet.values)


    # 第一行作为字段名
    headers = rows[0]


    data = []


    for row in rows[1:]:

        item = {}

        for i in range(len(headers)):

            item[headers[i]] = row[i]


        data.append(item)


    return data
