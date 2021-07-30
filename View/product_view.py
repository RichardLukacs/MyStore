from utils import CATEGORY_LIST, read_float


class ProductConsoleView:
    @staticmethod
    def display_one_product(product):
        """
        Display one product in the console
        :param product: Product
        """
        if product:
            print(product)
        else:
            print('No such product')

    @staticmethod
    def display_all_products(products):
        """
        Display all products in the console
        :param products: List(Product)
        """
        for product in products:
            print(product)

    @staticmethod
    def get_product_id():
        """
        Read a product_id from the console
        :return: product_id: int
        """
        return int(input('Please provide a product_id'))

    @staticmethod
    def get_product_fields(category_empty):
        """
        Read all product fields from the console: product_id, category, name, price, producer, stock
        :return:  product_id:int, category:str, name:str, price:float, producer:str, stock:int
        """
        product_id = ''
        while type(product_id) is str:
            try:
                product_id = int(input('Please provide the product_id: '))
            except TypeError:
                print('The product id must be a number')

        name = input('Please provide the product name: ')
        producer = input('Please provide the product producer: ')
        category = ''
        while category not in CATEGORY_LIST:
            category = input(f'Please provide a category from the following: {CATEGORY_LIST}').lower()
            if category_empty and category == '':
                break

        price = input('Please provide the product price: ')
        if price:
            price = float(price)
        stock = input('Please provide the product stock: ')
        if stock:
            stock = int(stock)
        return product_id, category, name, price, producer, stock

    @staticmethod
    def display_delete_message():
        """
        Display delete message to console
        """
        print('You are about to delete a product')

    @staticmethod
    def display_update_message():
        """
        Display update message to console
        """
        print('You are about to update a product, leave the fields you want the same empty')

    @staticmethod
    def product_menu():
        """
        Display product menu to console
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
