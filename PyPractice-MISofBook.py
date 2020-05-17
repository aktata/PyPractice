import os
import prettytable as pt

all_books_list = [
    ['Python编程:从入门到实践', 62.8, '人民邮电出版社', 99.9],
    ['Python zen', 62.8, "O'Reilly", 99.9],
    ['笨办法学Python3', 46.1, '人民邮电出版社', 98.9],
    ['Python核心编程（第3版）', 98, '人民邮电出版社', 99.2],
    ['Python编程快速上手：让繁琐工作自动化', 68.3, '人民邮电出版社', 99.1],
    ['了不起的JavaScript工程师：从前端到全端高级进阶', 78.2, '电子工业出版社', 97.9],
    ['移动Web前端高效开发实战：HTML5 + CSS3 + JavaScript', 64.8, '电子工业出版社', 98.3],
    ['JavaScript程序设计基础与范例教程（第2版）', 46.5, '电子工业出版社', 99.4],
    ['JavaScript权威指南（第6版）', 109.8, '机械工业出版社', 99.9],
    ['区块链项目开发指南', 48.7, '机械工业出版社', 99.4],
    ['区块链安全技术指南', 56.9, '机械工业出版社', 99.3]
]

menu = pt.PrettyTable()
menu.field_names = ['选项']
menu.add_row(['1.浏览图书'])
menu.add_row(['2.增加图书'])
menu.add_row(['3.删除图书'])
menu.add_row(['4.修改图书'])
menu.add_row(['5.查询图书'])
menu.add_row(['6.按价格排序'])
menu.add_row(['7.按好评排序'])
menu.add_row(['8.退出'])


def print_books(book_list):
    books = pt.PrettyTable()
    books.field_names = ['书名', '价格', '出版社', '好评度']
    for book in book_list:
        books.add_row(book)
    print(books)


def show():
    print_books(all_books_list)


def add():
    try:
        name = input('请输入您要添加的书名：')
        price = float(input('请输入本书的价格：'))
        press = input('请输入本书的出版社：')
        star = float(input('请输入本书的好评度：'))
    except:
        print('输入错误')
    else:
        all_books_list.append([name, price, press, star])


def delete():
    try:
        name = input('请输入您要删除的书名：')
    except:
        print('输入错误')
    else:
        for book in all_books_list:
            if book[0].find(name) != -1:
                all_books_list.remove(book)


def modify():
    try:
        name = input('请输入您要修改的书名：')
    except:
        print('输入错误')
    else:
        for book in all_books_list:
            if book[0].find(name) != -1:
                try:
                    name = input('请输入修改后的书名：')
                    price = float(input('请输入修改后本书的价格：'))
                    press = input('请输入修改后本书的出版社：')
                    star = float(input('请输入修改后本书的好评度：'))
                except:
                    print('输入错误')
                else:
                    book[0] = name
                    book[1] = price
                    book[2] = press
                    book[3] = star


def search():
    searched_list = []
    keyword = input('请输入要查找的书名：')
    for book in all_books_list:
        if book[0].find(keyword) != -1:
            searched_list.append(book)

    if not searched_list:
        print('没有这本书')
    else:
        print_books(searched_list)


def price():
    reverse = bool(input('输入是否降序（True/False）：'))
    all_books_list_temp = all_books_list[:]
    all_books_list_temp.sort(key=lambda x: x[1], reverse=reverse)
    print_books(all_books_list_temp)


def star():
    reverse = bool(input('输入是否降序（True/False）：'))
    all_books_list_temp = all_books_list[:]
    all_books_list_temp.sort(key=lambda x: x[3], reverse=reverse)
    print_books(all_books_list_temp)


options = {
    1: show,
    2: add,
    3: delete,
    4: modify,
    5: search,
    6: price,
    7: star
}


def main():
    while True:
        print(menu)
        try:
            option = int(input('请输入您的选项：'))
        except ValueError:
            print('输入类型错误')
        else:
            if 1 <= option <= 7:
                options[option]()
            elif option == 8:
                break
            else:
                print('输入数字错误')
        os.system('pause')


if __name__ == '__main__':
    main()
