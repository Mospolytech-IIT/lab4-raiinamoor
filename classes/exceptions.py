'''Custom exception definitions'''

class ProductExistsError(ValueError):
    '''Product already exists'''
    def __init__(self, product_id) -> None:
        self.__product_id = product_id


    def __str__(self) -> str:
        return f"Product with ID {self.__product_id} already exists"


class ProductNotFoundError(ValueError):
    '''Product was not found'''
    def __init__(self, product_id) -> None:
        self.__product_id = product_id


    def __str__(self) -> str:
        return f"Product with ID {self.__product_id} does not exist"


class EmptyStorageError(ValueError):
    '''Storage is empty'''
    def __init__(self, storage_id) -> None:
        self.__storage_id = storage_id


    def __str__(self) -> str:
        return f"Storage with ID {self.__storage_id} is empty"
