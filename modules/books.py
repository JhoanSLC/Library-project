import modules.jsonfiles as file
import modules.screen as scr

#Function to add a book to json file
def add_book():
    isaddbook = True
    while isaddbook: #Starts add book loop
        scr.clean()
        file.check_json('books.json')
        books_data = file.read_json('books.json') #Save json fil data in a python dict
        book = {
            'name' : input("Write the book's name: "),
            'author/s' : [],
            'ISBN' : '',
            'publisher' : '',
            'publication year' : '',
            'genre/cat' : '',
            'stock' : '',
            'state' : '',
            'historial' : {}
        }
        add_author = True
        while add_author: #starts loop to add as many authors as you want
            scr.clean()
            book['author/s'].append(input("Write the book's author's name: "))
            while True:
                scr.clean()
                yes_or_not = input('Do you want to add other author for this book? y(yes) - n(not): ').upper()
                if yes_or_not == 'Y':
                    break
                elif yes_or_not == 'N':
                    add_author = False
                    break
                