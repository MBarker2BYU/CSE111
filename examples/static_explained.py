from os import system, name

class Coding:
    
    PRESS_KEY = "Enter"

    def __init__(self, text):
        
        self.m_text = text

    def run(self):

        self.clear_screen()

        print(F"Coding {self.m_text}")

        self.press_space_continue()
        

    #I can only use inside this class. Notice the 'self' as a parameter.
    def clear_screen(self):

        system("cls" if name == "nt" else "clear")
    
    #I can only use this in this class
    def press_space_continue(self):
        
        print("")

        input(F"Press {self.PRESS_KEY} to continue...")

        print("")

    
class Coding2:
    
    PRESS_ENTER = "Enter"

    def __init__(self, text):
        
        self.m_text = text

    def run(self):

        Coding2.clear_screen()

        print(F"Coding2 {self.m_text}")

        #Here we call this with static members of this class.
        Coding2.press_space_continue(self.PRESS_ENTER)

    #I can use this anywhere by coding Coding2.clear_scree(). Notice the 'self' parameter is no longer there.
    @staticmethod
    def clear_screen():

        system("cls" if name == "nt" else "clear")

    #I can use this anywhere by coding Coding2.clear_scree(). Notice the 'self' parameter is no longer there and we pass in the press_key.
    @staticmethod
    def press_space_continue(press_key):
        
        print("")

        input(F"Press {press_key} to continue...")

        print("")


class Coding3:
    
    def __init__(self, text):
        
        self.m_text = text

    def run(self):

        #I call existing code. This allows for better support. Only one point of failure.
        Coding2.clear_screen()

        print(F"Coding3 {self.m_text}")

        #Notice I use all external items here. 
        Coding2.press_space_continue(Coding2.PRESS_ENTER)


if __name__=="__main__":

    Coding('Internal methods only').run()
    Coding2('Static methods only').run()
    Coding3('I use extenal static methods and values.').run()