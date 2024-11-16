'''Storage class definition'''

from classes.exceptions import EmptyStorageError, ProductExistsError, ProductNotFoundError
from classes.product import Product


class Storage:
    '''Stores and accesses product instances'''
    __id: int
    __products: list

    def __init__(self, _id: int, products: list) -> None:
        self.id = _id
        self.products = products


    @property
    def id(self) -> int:
        '''Product ID'''
        return self.__id

    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError

        self.__id = value


    @property
    def products(self) -> list:
        '''List of products in storage'''
        if len(self.__products) == 0:
            raise EmptyStorageError(self.id)

        return list(self.__products)

    @products.setter
    def products(self, value: list):
        self.__products = value


    def find_product_by_id(self, product_id) -> Product | None:
        '''Find a product by ID'''
        products_with_same_id = [p for p in self.__products if p.id == product_id]
        product = products_with_same_id[0] if len(products_with_same_id) > 0 else None

        return product


    def add_product(self, product: Product):
        '''Add a product to the list'''
        search_result = self.find_product_by_id(product.id)
        if search_result is not None:
            raise ProductExistsError(product.id)

        self.__products.append(product)


    def remove_product(self, product_id: int):
        '''Remove a product from the list'''
        search_result = self.find_product_by_id(product_id)
        if search_result is None:
            raise ProductNotFoundError(product_id)

        self.__products.remove(search_result)
