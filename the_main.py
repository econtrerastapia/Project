from gui import *


def main():
    '''
    Gets the application started by creating the Gui window
    '''
    window = Tk()
    window.title('Final Project')
    window.geometry('400x500')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
