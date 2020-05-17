import os
import prettytable as pt

menu = pt.PrettyTable()
menu.field_names = ['选项']
menu.add_row(['1.浏览图书'])
menu.add_row(['2.增加图书'])
menu.add_row(['3.删除图书'])
menu.add_row(['4.修改图书'])
menu.add_row(['5.查询图书'])
menu.add_row(['6.按价格排序'])
menu.add_row(['7.按好评排序'])
menu.add_row(['8.保存退出'])

menu_modify = pt.PrettyTable()
menu_modify.field_names = ['修改选项']
menu_modify.add_row(['1.修改书名'])
menu_modify.add_row(['2.修改价格'])
menu_modify.add_row(['3.修改出版社'])
menu_modify.add_row(['4.修改好评度'])


def save():
    book_data = open('data/book_data.txt', 'a')
    book_data.seek(0)
    book_data.truncate()
    for book in all_books_list:
        for data in book:
            book_data.write(str(data))
            book_data.write(' ')
        book_data.write('\n')
    book_data.close()


def load():
    try:
        book_data = open('data/book_data.txt', 'r')
    except IOError:
        error = []
        return error
    content = book_data.readlines()
    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]
        content[i] = content[i].split()
    for book in content:
        book[1] = float(book[1])
        book[3] = float(book[3])
    book_data.close()
    return content


all_books_list = []
all_books_list = load()


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
        print('添加成功')


def delete():
    try:
        name = input('请输入您要删除的书名：')
    except:
        print('输入错误')
    else:
        for book in all_books_list:
            if book[0].find(name) != -1:
                all_books_list.remove(book)
                print('删除成功')


def modify():
    try:
        name = input('请输入您要修改的书名：')
    except:
        print('没有找到该书')
    else:
        for book in all_books_list:
            if book[0].find(name) != -1:
                print(menu_modify)
                try:
                    option = int(input('请输入您的选项：'))
                except ValueError:
                    print('输入类型错误')
                else:
                    if option == 1:
                        name = input('请输入修改后的书名：')
                        book[0] = name
                        print('修改成功')
                        break
                    elif option == 2:
                        price = float(input('请输入修改后本书的价格：'))
                        book[1] = price
                        print('修改成功')
                        break
                    elif option == 3:
                        press = input('请输入修改后本书的出版社：')
                        book[2] = press
                        print('修改成功')
                        break
                    elif option == 4:
                        star = float(input('请输入修改后本书的好评度：'))
                        book[3] = star
                        print('修改成功')
                        break
                    else:
                        print('输入数字错误')



def search():
    searched_list = []
    keyword = input('请输入要查找的关键词：')
    for book in all_books_list:
        if book[0].find(keyword) != -1:
            searched_list.append(book)

    if not searched_list:
        print('没有这本书')
    else:
        print_books(searched_list)


def book_sort(key):
    reverse = bool(int(input('输入是否降序（1/0）：')))
    all_books_list_temp = all_books_list[:]
    all_books_list_temp.sort(key=lambda x: x[key], reverse=reverse)
    print_books(all_books_list_temp)


def price():
    book_sort(1)


def star():
    book_sort(3)


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
                save()
                break
            else:
                print('输入数字错误')
        os.system('pause')


if __name__ == '__main__':
    main()
