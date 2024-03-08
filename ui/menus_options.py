import modules.screen as scr


#Creates main menu
def main_menu_options():
    scr.clean()
    #Draws the menu's title
    title = """ 
        +++++++++++++++++++++++++++++
        + LIBRARY MANAGEMENT SYSTEM +
        +++++++++++++++++++++++++++++
    """
    print(title)
    print('')
    print('Enter the number correspondig to the action you want to do')
    print('')
    op = input('1. Add book\n2. See books list\n3. Search book\n4. Lend a book\n5. Return a book\n6. See borrowed books list\n7. Exit\n')
    return op #Returns the option the user want to go in