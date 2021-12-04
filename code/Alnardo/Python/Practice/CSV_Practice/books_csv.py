#Practicing CSV

#I'm using this file to try and create a cleaner CSV code than my lab
#books.csv is used for the latest book in a series, so I know where I left off and if I have read it or not


relative_path = 'github/class_tardigrade/code/Alnardo/Python/Practice/CSV_Practice/'

with open('books.csv', 'r') as f:
    book_information = f.read()

book_info = book_information.split('\n')
# print(book_information)

csv_headers = book_info[0].split(', ')
# print(csv_headers)
list_of_books = []
# print(book_info[0].split(', '))

for information in book_info:
    information = information.split(', ')
    # print(information)
    if information == csv_headers:
        continue
    else:
        main_book_dict = {}
        book_title = {}
        book_author = {}
        book_series = {}
        for i, info in enumerate(information):
            if i == 0:
                book_title[csv_headers[i]] = info
            if i == 1:
                book_author[csv_headers[i]] = info
            if i == 2:
                book_series[csv_headers[i]] = info

            main_book_dict.update(book_title)
            main_book_dict.update(book_author)
            main_book_dict.update(book_series)
        list_of_books.append(main_book_dict)

# print(book_information)
# print(list_of_books)
#List_of_books now contains all of the books separated by title, author, series


# Search function in work
        # search_criteria = input('What would you like to search? (title/author/series): ').lower()
        # specific_search = input('What would you like to look up?: ')
        # for book in list_of_books:
        #     # print(book) #As is, it gives each dictionary set of books
        #     if specific_search in book[search_criteria]:
        #         print(f"Books by {book['author']} are {book['title']}.")
        #     else:
        #         continue

# Update function in work


# Delete function DENIED

def donate():
    #This function will be used to add(Create) a new book in the list
    donated_book = []
    donated_book_info = {'title' : '', 'author' : '', 'series' : ''}
    title = input('Please enter the title: ')
    author = input('Please enter the author: ')
    series = input('Please enter the series, if none put "novel": ')
    donated_book_info['title'] = title
    donated_book_info['author'] = author
    donated_book_info['series'] = series
    donated_book.append(donated_book_info)
    return donated_book

    # print('Thank you so much for your donation!')

def search():
    #This function will be used to Retrieve information
    view_all = input('Would you like to view the entire list? (yes/no): ')
    if view_all == 'yes':
        print(book_information)
    else:
        pass
    user_sort = input('Please enter a title, author, or series: ')
    for book in list_of_books:
        if user_sort in book['author']:
            print(f"{book['author']} wrote {book['title']}, part of the '{book['series']}' series.")
        if user_sort in book['title']:
            print(f"{book['title']}, by {book['author']}.")
        if user_sort in book['series']:
            print(f"{book['title']}, by {book['author']}.")
        else:
            pass


search()




def update():
    #This function will be used to Update information about the book, such as a misspelled title or a new book in the series
    print('Thank you for updating this!')

def burn():
    #This function will be used if the author completely goes off the rails and the series is no longer good
    print('Function denied, YOU HEATHEN.')



# question = input('Would you like to enter my library? (yes/no): ').lower()
# if question == 'yes':
#     print('Welcome to my personal library! I hope you enjoy your stay.')
# else:
#     print("Hmph, you probably dog-ear the pages anyway...")

# while question == 'yes':
#     user_choice = input('Would you like to donate a book? (yes/no): ')
#     if user_choice == 'yes':
#         new_book = donate()
#         list_of_books += new_book
#         print('Thank you for the donation!!!')
#         user_choice = input('Would you like to donate another? (yes/no): ')
#         # print(list_of_books)
#     question = input('Would you like to continue?: ')
    





#     question = input('Are you staying?: ')

# print('I hope you enjoyed your time here.')