class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        result_list = []
        for product in self.products:
            if product[0] == first_letter:
                result_list.append(product)

        return result_list

    def __repr__(self):
        self.products.sort()
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(self.products)

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)   

