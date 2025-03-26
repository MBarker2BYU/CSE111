import curses

class MenuItem:
    def __init__(self):
        pass

class Menu:
    def __init__(self, callback):

        self._callback = callback
        self._exit = False

        self._window = curses.initscr
        self._window.keypad(True)

        curses.cbreak()
        curses.noecho()

    def show(self):
        
        

        while(True):
        
            if self._exit:
                break
            
            


def callback(menu_item):
    print("Callback")


def main():
    
    menu = Menu(callback)
    
    menu.click()


if __name__ == "__main__":
    main()