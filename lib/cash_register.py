#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self._total = 0
        self._items = []
        self.last_transaction_amount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._discount = value
        else:
            raise ValueError("Discount must be a non-negative number.")

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._total = value
        else:
            raise ValueError("Total must be a non-negative number.")

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = value
        else:
            raise ValueError("Items must be a list.")

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(
                f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0


pass
