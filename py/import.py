import pymysql
import xlrd
import xlwt


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='602511dtywyy', db='pyimport', charset='utf8')
    return conn


def insert(cur, sql, args):
    cur.execute(sql, args)


def read_xlsx_to_mysql(filename):
    excel = xlrd.open_workbook(filename)  # 打开xlsx文件,返回一个对象
    sheet0 = excel.sheet_by_index(0)  # 获取第1个sheet表格
    sheet1 = excel.sheet_by_index(1)  # 获取第2个sheet表格
    sheet2 = excel.sheet_by_index(2)  # 获取第3个sheet表格
    sheet3 = excel.sheet_by_index(3)  # 获取第4个sheet表格
    sheet4 = excel.sheet_by_index(4)  # 获取第5个sheet表格
    sheet5 = excel.sheet_by_index(5)  # 获取第6个sheet表格
    sheet6 = excel.sheet_by_index(6)  # 获取第7个sheet表格
    sheet7 = excel.sheet_by_index(7)  # 获取第8个sheet表格
    sheet8 = excel.sheet_by_index(8)  # 获取第9个sheet表格
    sheet9 = excel.sheet_by_index(9)  # 获取第10个sheet表格
    conn = get_conn()
    cur = conn.cursor()
    sql7 = 'insert into games values(%s,%s,%s)'
    print(sheet7.nrows)
    for row in range(sheet7.nrows):
        print(row)
        args = sheet7.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql7, args=args)

    sql0 = 'insert into caijing values(%s,%s,%s)'
    print(sheet0.nrows)
    for row in range(sheet0.nrows):
        print(row)
        args = sheet0.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql0, args=args)

    sql1 = 'insert into fangchan values(%s,%s,%s)'
    print(sheet1.nrows)
    for row in range(sheet1.nrows):
        print(row)
        args = sheet1.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql1, args=args)

    sql2 = 'insert into jiaoyu values(%s,%s,%s)'
    print(sheet2.nrows)
    for row in range(sheet2.nrows):
        print(row)
        args = sheet2.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql2, args=args)

    sql3 = 'insert into keji values(%s,%s,%s)'
    print(sheet3.nrows)
    for row in range(sheet3.nrows):
        print(row)
        args = sheet3.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql3, args=args)

    sql4 = 'insert into junshi values(%s,%s,%s)'
    print(sheet4.nrows)
    for row in range(sheet4.nrows):
        print(row)
        args = sheet4.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql4, args=args)

    sql5 = 'insert into qiche values(%s,%s,%s)'
    print(sheet5.nrows)
    for row in range(sheet5.nrows):
        print(row)
        args = sheet5.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql5, args=args)

    sql6 = 'insert into tiyu values(%s,%s,%s)'
    print(sheet6.nrows)
    for row in range(sheet6.nrows):
        print(row)
        args = sheet6.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql6, args=args)

    sql8 = 'insert into yule values(%s,%s,%s)'
    print(sheet8.nrows)
    for row in range(sheet8.nrows):
        print(row)
        args = sheet8.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql8, args=args)

    sql9 = 'insert into qita values(%s,%s,%s)'
    print(sheet9.nrows)
    for row in range(sheet9.nrows):
        print(row)
        args = sheet9.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql9, args=args)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    read_xlsx_to_mysql('1617241934831197.xlsx')
