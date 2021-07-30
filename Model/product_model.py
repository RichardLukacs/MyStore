from Domain.product import Product
from os.path import exists


class ProductFileModel:
    def __init__(self, filename):
        self.__filename = filename
        self.__all_products = []
        self.read_products()

    def get_all_products(self):
        return self.__all_products

    def create_product(self, product_id, category, name, producer, price, stock):
        product = Product(
            product_id=product_id,
            category=category,
            name=name,
            price=price,
            producer=producer,
            stock=stock,
        )

        self.__all_products.append(product)
        self.__save_to_file()

    def read_products(self):
        """
        
        :return: 
        """
        if not exists(self.__filename):
            return

        with open(self.__filename, 'r') as my_file:
            for line in my_file:
                line = line.split('|')
                product = Product(
                    product_id=int(line[0]),
                    category=line[1],
                    name=line[2],
                    producer=line[3],
                    price=float(line[4]),
                    stock=int(line[5])
                )
                self.__all_products.append(product)

    def __save_to_file(self):
        """
        
        :return: 
        """
        with open(self.__filename, 'w') as my_file:
            for product in self.__all_products:
                line = ''
                line += str(product.product_id) + '|' + product.category + '|' + product.name + '|' + \
                        product.producer + '|' + str(product.price) + '|' + str(product.stock) + '\n'
                my_file.write(line)

    def update_product(self, product_id, category, name, producer, price, stock):
        """
        
        :param product_id: 
        :param category: 
        :param name: 
        :param producer: 
        :param price: 
        :param stock: 
        :return: 
        """
        for index, product in enumerate(self.__all_products):
            if product.product_id == product_id:
                if name:
                    self.__all_products[index].name = name
                if category:
                    self.__all_products[index].category = category
                if producer:
                    self.__all_products[index].producer = producer
                if price:
                    self.__all_products[index].price = price
                if stock:
                    self.__all_products[index].stock = stock
                break
        self.__save_to_file()

    def delete_product(self, product_id):
        for index, product in enumerate(self.__all_products):
            if product.product_id == product_id:
                del self.__all_products[index]

        self.__save_to_file()

    def find_by_id(self, product_id):
        for product in self.__all_products:
            if product.product_id == product_id:
                return product
        return None
