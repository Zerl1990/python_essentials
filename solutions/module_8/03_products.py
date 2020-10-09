class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.cost == other.cost
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.cost > other.cost
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Product):
            return self.cost >= other.cost
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.cost < other.cost
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Product):
            return self.cost <= other.cost
        else:
            return False

    def __str__(self):
        return f'Product {self.name}: {self.cost}'


class Products:
    def __init__(self, *args):
        self.__products = list(args)

    def add(self, product):
        self.__products.append(product)

    def sort(self):
        self.__products.sort()

    def __str__(self):
        return '\n'.join(str(prod) for prod in self.__products)

    def __len__(self):
        return len(self.__products)


products = Products()
products.add(Product('Product A', 8))
products.add(Product('Product A', 23))
products.add(Product('Product B', 34))
products.add(Product('Product C', 14))
products.add(Product('Product D', 2))
products.add(Product('Product E', 67))
products.add(Product('Product F', 3))
products.add(Product('Product F', 5))

print(f'Total products: {len(products)}')
print(products)
products.sort()
print('*' * 80)
print(products)
