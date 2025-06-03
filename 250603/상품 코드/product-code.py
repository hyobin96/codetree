class Product:
    def __init__(self, name, code):
        self.n = name
        self.c = code

name, code = input().split()

product1 = Product('codetree', 50)
product2 = Product(name, code)

print(f'product {product1.c} is {product1.n}')
print(f'product {product2.c} is {product2.n}')