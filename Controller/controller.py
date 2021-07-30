from typing import Union

from Model.client_model import ClientFileModel, ClientSQLModel
from Model.product_model import ProductFileModel
from View.client_view import ClientConsoleView
from View.general_view import GeneralConsoleView
from View.product_view import ProductConsoleView


class Controller:
    def __init__(self, client_model: Union[ClientFileModel, ClientSQLModel], product_model: ProductFileModel, client_view: ClientConsoleView,
                 product_view: ProductConsoleView, general_view: GeneralConsoleView):
        self.client_model = client_model
        self.product_model = product_model
        self.client_view = client_view
        self.product_view = product_view
        self.general_view = general_view

    def add_product(self):
        """
        Get product fields from view and create a product in the model
        """
        product_id, category, name, price, producer, stock = self.product_view.get_product_fields(category_empty=False)
        # Repeat read if fields are empty
        while not product_id or not category or not name or not price or not producer or not stock:
            self.product_view.display_fields_not_empty()
            product_id, category, name, price, producer, stock = self.product_view.get_product_fields(category_empty=False)
        self.product_model.create_product(product_id, category, name, producer, price, stock)

    def delete_product(self):
        """
        Display delete message, get product_id and delete product from model based on product_id
        """
        self.product_view.display_delete_message()
        product_id = self.product_view.get_product_id()
        self.product_model.delete_product(product_id)

    def update_product(self):
        """
        Display update message, get product fields and update product from model based on product fields
        """
        self.product_view.display_update_message()
        product_id, category, name, price, producer, stock = self.product_view.get_product_fields(category_empty=True)
        self.product_model.update_product(product_id, category, name, producer, price, stock)

    def display_all_products(self):
        """
        Get all products from model. Display all products in view
        """
        products = self.product_model.get_all_products()
        self.product_view.display_all_products(products)

    def display_one_product(self):
        """
        Get product_id from view. Get product from model by product_id. Display product in view
        """
        product_id = self.product_view.get_product_id()
        product = self.product_model.find_by_id(product_id)
        self.product_view.display_one_product(product)

    def start(self):
        """
        Start controller menu. Display main menu options and call the correct submenu
        """
        while True:
            option = self.general_view.main_menu()
            if option == '1':
                self.product_menu()
            elif option == '2':
                self.client_menu()
            elif option == 'x':
                return
            else:
                self.general_view.display_wrong_option()

    def product_menu(self):
        """
        Display the product menu and call specific operations
        """
        while True:
            option = self.product_view.product_menu()
            if option == '1':
                self.add_product()
            elif option == '2':
                self.update_product()
            elif option == '3':
                self.delete_product()
            elif option == '4':
                self.display_one_product()
            elif option == '5':
                self.display_all_products()
            elif option == 'x':
                return
            else:
                self.general_view.display_wrong_option()

    def client_menu(self):
        """
        Display the client menu and call specific operations
        """
        while True:
            option = self.client_view.client_menu()
            if option == '1':
                self.add_client()
            elif option == '2':
                self.update_client()
            elif option == '3':
                self.delete_client()
            elif option == '4':
                self.display_one_client()
            elif option == '5':
                self.display_all_clients()
            elif option == 'x':
                return
            else:
                self.general_view.display_wrong_option()

    def add_client(self):
        """
        Get client fields from view and create a client in the model
        """
        cnp, last_name, first_name, email = self.client_view.get_client_fields()
        # Repeat read if fields are empty
        while not cnp or not last_name or not first_name or not email:
            self.client_view.display_fields_not_empty()
            cnp, last_name, first_name, email = self.client_view.get_client_fields()
        if self.client_model.id_exists(cnp):
            self.client_view.display_duplicate('cnp')
        else:
            self.client_model.create_client(cnp, last_name, first_name, email)

    def delete_client(self):
        """
        Display delete message, get client cnp and delete client from model based on client cnp[
        """
        self.client_view.display_delete_message()
        cnp = self.client_view.get_client_cnp()
        self.client_model.delete_client(cnp)

    def update_client(self):
        """
        Display update message, get client fields and update client from model based on client fields
        """
        self.client_view.display_update_message()
        cnp, last_name, first_name, email = self.client_view.get_client_fields()
        self.client_model.update_client(cnp, last_name, first_name, email)

    def display_all_clients(self):
        """
        Get all clients from model. Display all clients in view
        """
        clients = self.client_model.get_all_clients()
        self.client_view.display_all_clients(clients)

    def display_one_client(self):
        """
        Get cnp from view. Get client from model by cnp. Display client in view
        """
        cnp = self.client_view.get_client_cnp()
        client = self.client_model.find_by_id(cnp)
        self.client_view.display_one_client(client)
