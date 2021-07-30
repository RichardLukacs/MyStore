
class GeneralConsoleView:
    @staticmethod
    def main_menu():
        print('1 Products')
        print('2 Clients')
        print('x Exit')
        option = input('Select Option: ')
        return option

    @staticmethod
    def display_wrong_option():
        print('No such option')
