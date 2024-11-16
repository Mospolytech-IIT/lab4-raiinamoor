'''Product class definition'''

class Product:
    '''Represents one type of product'''
    __id: int
    __name: str

    def __init__(self, _id: int, name: str) -> None:
        self.id = _id
        self.name = name
        # self.__quantity = quantity

    @property
    def id(self) -> int:
        '''Product ID'''
        return self.__id

    # 5
    @id.setter
    def id(self, value: int):
        if value < 0:
            raise ValueError

        self.__id = value


    @property
    def name(self) -> str:
        '''Product name'''
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "" or value is None:
            raise ValueError

        self.__name = value
