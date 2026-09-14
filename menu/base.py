class Menu:
    def __init__(self, title, option_list: list['Option']):
        self.title = title
        self.option_list = option_list

    def get_title(self) -> str:
        return self.title

    def get_option_list(self) -> list:
        return self.option_list


class Option:
    def __init__(self, title: str, next_menu: Menu | None, func):
        self.title = title
        self.next_menu = next_menu
        self.function = func

    def get_title(self) -> str:
        return self.title

    def get_next_menu(self) -> Menu | None:
        return self.next_menu

    def execute(self):
        return self.function()
    
        


    
    

    

    