class ClientConsoleView:
    @staticmethod
    def display_one_client(client):
        """
        Display one client in the console
        :param client: Client
        """
        if client:
            print(client)
        else:
            print('No such client')

    @staticmethod
    def display_all_clients(clients):
        """
        Display all clients in the console
        :param clients: List(Client)
        """
        for client in clients:
            print(client)

    @staticmethod
    def get_client_cnp():
        """
        Read a client cnp from the console
        :return: cnp: str
        """
        return input('Please provide a client cnp')

    @staticmethod
    def get_client_fields():
        """
        Read all client fields from the console: cnp, last_name, first_name, age_group, email
        :return:  cnp:str, last_name:str, first_name:str, email:str
        """
        cnp = input('Please provide the client cnp: ')  # TODO Validate cnp
        last_name = input('Please provide the client last name: ')
        first_name = input('Please provide the client first name: ')
        email = input('Please provide the client email: ')  # TODO Validate email

        return cnp, last_name, first_name, email

    @staticmethod
    def display_delete_message():
        """
        Display delete message to console
        """
        print('You are about to delete a client')

    @staticmethod
    def display_update_message():
        """
        Display update message to console
        """
        print('You are about to update a client, leave the fields you want the same empty')

    @staticmethod
    def client_menu():
        """
        Display client menu to console
        :return: Selected option from the menu
        """
        print('1 Add')
        print('2 Update')
        print('3 Remove')
        print('4 Display One')
        print('5 Display All')
        print('x Exit')
        option = input('Select Option: ')
        return option

    @staticmethod
    def display_fields_not_empty():
        """
        Display message that fields cannot be empty
        """
        print('Fields cannot be empty')

    @staticmethod
    def display_duplicate(field):
        print(f'Field {field} is duplicated')
