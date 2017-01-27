class CartListItem:
    """Used for cart items list"""

    def __init__(self, item=None):
        if item == None:
            self.total = 0
        else:
            self.id = item.id
            self.item_id = item.item.id
            self.item_name = item.item.name
            self.price = item.item.price
            self.quantity = item.quantity
            self.total = item.item.price * item.quantity
