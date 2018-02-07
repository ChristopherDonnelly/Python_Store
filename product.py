class Product(object):
    def __init__(self, id, price, name, weight, brand, status="for sale"):
        self.id = id
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

        print '~~~ Created new product {} ~~~'.format(name)
        self.display_info()
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax_amount):
        taxed = ((tax_amount / 100) * self.price) + self.price
        returnAmount = ''
        if self.status != 'defective':
            returnAmount = self.name+' - Price with Sales Tax: $' + str(round(taxed, 2)) + '\n'
        else:
            returnAmount = self.name+' - This product is defective and cannot be sold\n'

        return returnAmount
    def add_discount(self, discount_amount):
        self.price -= ((discount_amount / 100) * self.price)

        return self
    def return_item(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in box' or reason == 'like new':
            self.status = 'for sale'
        elif reason == 'used' or reason == 'opened':
            self.status = 'used'
            self.add_discount(20.0)

        print '~~~ Returned {} as {} ~~~'.format(self.name,  reason)

        self.display_info()
        return self
    def display_info(self):
        print 'Prod ID:', self.id, '\nName:', self.name, '\nBrand:', self.brand, '\nPrice: ${0:.2f}'.format(self.price, 2), '\nStatus:', self.status, '\nWeight:', self.weight
        return self

if(__name__ == "__main__"):
    gobstopper = Product(1, 1000000.00, 'Everlasting Gobstopper', 0.5, 'Willy Wonka', 'not for sale')
    triple_cream = Product(2, 1.00, 'Triple Cream Cup', 0.75, 'Willy Wonka')
    squanch = Product(3, 2.00, 'Squelchy Snorter', 1.0, 'Willy Wonka')
    sizzler = Product(4, 2.50, "Slugworth's Sizzler", 0.25, 'Willy Wonka')

    print squanch.add_tax(8.25)
    squanch.return_item('used')
    print squanch.add_tax(8.25)
    squanch.return_item('defective')
    print squanch.add_tax(8.25)
else:
    print '~~~ Imported {} ~~~\n'.format(__name__)