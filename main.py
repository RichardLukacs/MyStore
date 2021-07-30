from Controller.controller import Controller
from Model.client_model import ClientFileModel, ClientSQLModel
from Model.product_model import ProductFileModel
from View.client_view import ClientConsoleView
from View.general_view import GeneralConsoleView
from View.product_view import ProductConsoleView


def main():
    product_model = ProductFileModel('Data/products.csv')
    product_view = ProductConsoleView()

    # client_model = ClientFileModel('Data/clients.csv')
    client_model = ClientSQLModel()
    client_view = ClientConsoleView()

    general_view = GeneralConsoleView()

    controller = Controller(
        product_view=product_view,
        product_model=product_model,
        client_model=client_model,
        client_view=client_view,
        general_view=general_view
    )

    controller.start()


if __name__ == '__main__':
    main()
