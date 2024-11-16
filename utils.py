import uuid
from classes.exceptions import EmptyStorageError, ProductExistsError, ProductNotFoundError
from classes.product import Product
from classes.storage import Storage


# 2
def create_storage(storage_id: int, *args):
    '''Create an instance of Storage'''
    args = list(args)
    storage: Storage
    try:
        storage = Storage(storage_id, args)
    except Exception:
        storage = Storage(1, args)
    finally:
        print("Storage created successfully")

    return storage


# 3
def create_product_with_uuid(name: str) -> Product:
    '''Create an instance of product with uuid4'''
    uuid_int = uuid.uuid4().int
    product: Product
    try:
        product = Product(uuid_int, name)
    except Exception:
        product = Product(uuid_int, f"product{uuid_int}")

    return product


# 4
def add_products_to_storage(storage: Storage, *products):
    '''Add all products in a list to storage'''
    for product in products:
        try:
            storage.add_product(product)
        except ProductExistsError as e:
            print(f"ProductExistsError: {e}")
            continue
        except ValueError as e:
            print(f"ValueError: {e}")
            continue
        except Exception as e:
            print(f"Exception: {e}")
            continue


# 7
def remove_products_from_storage(storage: Storage, *product_ids):
    '''Remove all products in a list from storage'''
    for product_id in product_ids:
        try:
            storage.remove_product(product_id)
        except ProductNotFoundError as e:
            print(f"ProductNotFoundError: {e}")
            continue
        except ValueError as e:
            print(f"ValueError: {e}")
            continue
        except Exception as e:
            print(f"Exception: {e}")
            continue


def get_products(storage: Storage):
    '''Gets products from storage'''
    result: list
    try:
        result = storage.products
    except EmptyStorageError as e:
        print(f"EmptyStorageError: {e}")
        return
    except ValueError as e:
        print(f"ValueError: {e}")
        return
    except Exception as e:
        print(f"Exception: {e}")
        return

    return result
