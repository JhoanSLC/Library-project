import ui.menus_options as menu
import modules.books as book
def main_menu():
    isapprunning = True
    while isapprunning:
        op = menu.main_menu_options()
        #Add book
        if op == '1':
          book.add_book()
        #See books list
        if op == '2':
          pass
        #Search book
        if (op == '3'):
          pass
        #Lend a book
        if (op == '4'):
          pass
        #Return a book
        if (op == '5'):
          pass
        #See borrowed books
        if (op == '6'):
          pass
        #Exit
        if (op == '7'):
           isapprunning = False