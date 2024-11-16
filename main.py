'''Main module'''
import utils

# 9
def main() -> None:
    '''The main function that calls all the other functions'''
    storage = utils.create_storage(-1)
    print(f"The id of this storage should be 1: {storage.id}")

    product_1 = utils.create_product_with_uuid("Washing machine")
    product_2 = utils.create_product_with_uuid("Vacuum cleaner")
    product_3 = utils.create_product_with_uuid("")

    print("Next line should be a ProductExistsError, "
          + "because the function call adds the same item twice:")
    utils.add_products_to_storage(
        storage,
        product_1,
        product_2,
        product_3,
        product_3)

    print("Next line should be a ProductNotFoundError, "
          + "because the function call removes the same item twice")
    utils.remove_products_from_storage(
        storage,
        product_1.id,
        product_2.id,
        product_3.id,
        product_3.id)

    print("Next line should be an EmptyStorageError, because all the items were previously removed")
    products = utils.get_products(storage)
    print(f"This should print 'None': {products}")


if __name__ == "__main__":
    main()
