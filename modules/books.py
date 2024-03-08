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
            'name' : input("Write the book's name (ENTER to exit): : "),
            'author/s' : [],
            'ISBN' : '',
            'publisher' : '',
            'publication year' : '',
            'genre/cat' : '',
            'stock' : '',
            'state' : '',
            'historial' : {}
        }
        if book['name'] == '':
            return
        
        
        add_author = True
        while add_author: #starts loop to add as many authors as you want
            scr.clean()
            book['author/s'].append(input("Write the book's author's name "))
            while True: #starts loop to exit or not the add authors
                scr.clean()
                yes_or_not = input('Do you want to add other author for this book? y(yes) - n(not): ').upper()
                if yes_or_not == 'Y':
                    break
                elif yes_or_not == 'N':
                    add_author = False
                    break
                
                
                
        while True: #Loop to validate the isbn is correct
            try: 
                scr.clean()
                isbn = int(input("Write the book's isbn: "))
                book['ISBN'] = isbn
                break           
            except ValueError: #If the written value is not correct
                print('Write a correct value for the isbn: ' )
                scr.pause()
        book['publisher'] = input("Write the book's publisher's name: ")
        
        
        while True: #Loop to validate a correct publication year
            try:
                scr.clean()
                book['publication year'] = int(input("Write the book's publication year: "))
                break
            except ValueError:
                print('Write a correct value for a publication year') 
                scr.pause()       
        
        
        book['genre/cat'] = input("Write the book's genre: ")
        
        
        while True:
            try:
                scr.clean()
                book['stock'] = int(input("Write the current book's stock: "))
                break
            except ValueError:
                print("Write a correct value for the book's stock")
                scr.pause()            