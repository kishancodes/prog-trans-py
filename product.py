class Product:
# Constructor
 def __init__(self, name, price, discountPercent):
  self._name = name
  self.__price = price
  self.__discountPercent = discountPercent
# Getter for discountPercentage
 def getDiscountAmount(self):
  return self.__discountPercent
# Calculate price with discount
 def getDiscountPrice(self):
  return self.__price - self.__price *
 self.__discountPercent / 100
# Display description
 def printDescription(self):
  print('Product: ' + str(self._name) + '. Discount: ' +
  str(self.getDiscountAmount()) +'%. Final price: $' +
  str(self.getDiscountPrice()))
class Book(Product):
# Constructor
 def __init__(self, name, price, discountPercent, author):
  super().__init__(name, price, discountPercent)
  self.__author = author
# Display description
 def printDescription(self):
  print('Product: ' + str(self._name) + '. Author: ' +
  str(self.__author)+ '. Discount: ' +
  str(self.getDiscountAmount()) + '%. Final price: $' +
  str(self.getDiscountPrice()))
class Movie(Product):
# Constructor
 def __init__(self, name, price, discountPercent, year):
  super().__init__(name, price, discountPercent)
  self.__year = year
# Display description
 def printDescription(self):
  print('Product: ' + str(self._name) + '. Year: ' +
  str(self.__year) + '. Discount: '+ str(self.getDiscountAmount())+ '%. Final price: $' + str(self.getDiscountPrice()))

#input data with their description
#Initialize two books and two movies
book1 = Book('The Day My Bum Went Psycho', 25, 15, 'Andy Griffiths')
movie1 = Movie('The Man from U.N.C.L.E.', 20, 50, '2015')
book2 = Book('Rainbow Six', 120, 25, 'Tom Clancy')
movie2 = Movie('Django Unchained', 40, 0, '2012')

#input data with their description
#Initialize two books and two movies
book1 = Book('The Day My Bum Went Psycho', 25, 15, 'Andy Griffiths')
movie1 = Movie('The Man from U.N.C.L.E.', 20, 50, '2015')
book2 = Book('Rainbow Six', 120, 25, 'Tom Clancy')
movie2 = Movie('Django Unchained', 40, 0, '2012')

# Add them all to the prodiuct list
product_list = []
product_list.append(book1)
product_list.append(movie1)
product_list.append(book2)
product_list.append(movie2)
 # Iterate the product list and display description
 for product in product_list:
   product.printDescription()
#input close
