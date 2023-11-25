class Calculator:
    def calculateDiscount(self, purchase_amount, discount_percentage):
        discount = purchase_amount - (purchase_amount * discount_percentage / 100)
        return discount

