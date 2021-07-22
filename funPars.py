import openpyxl


def get_data_xls():
    book = openpyxl.open('out.xlsx', read_only=True)
    sheet = book.active

    data = []

    for row in range(300, 311):
        data.append({'oktmo': sheet[row][1].value,
                     'name': sheet[row][2].value,
                     'all': sheet[row][3].value,
                     'count_member':sheet[row][4].value,
                     'r_otv': sheet[row][5].value,
                     'd_r_all': sheet[row][7].value,
                     'publish_n': sheet[row][8].value,
                     'no_publish_n': sheet[row][9].value,
                     'p_r_o': sheet[row][10].value
                   })
        data.append(sheet[4][0].value)

    return data

def get_data_xls2():
    book = openpyxl.open('out.xlsx', read_only=True)
    sheet = book.active
    data = []

    for row in range(299, 300):
        data.append({'oktmo': sheet[row][0].value,
                     'name': sheet[row][2].value,
                     'all': sheet[row][3].value,
                     'count_member': sheet[row][4].value,
                     'r_otv': sheet[row][5].value,
                     'd_r_all': sheet[row][7].value,
                     'publish_n': sheet[row][8].value,
                     'no_publish_n': sheet[row][9].value,
                     'p_r_o': sheet[row][10].value
                     })
    return data

print(get_data_xls2())