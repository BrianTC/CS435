#!/usr/bin/python3
from product import Product
supermarket=[
	Product("001","1 Head of Lettuce"),
	Product("002","1 Lbs of Tomatoes"),
	Product("003","16oz Loaf of Bread")
	]
supermarket[0].setPrice(1.49)
supermarket[1].setPrice(1.99)

def checkout(supermarket,cart):
	cartTotal=0
	for cartItem in cart:
		noSuchItem=True
		for stockItem in supermarket:
			if stockItem.getProductCode()==cartItem:
				noSuchItem=False
				stockItem.printInformation()
				if(stockItem.outOfStock()):
					print("Item "+stockItem.getProductCode+" is out of stock")
				else:
					cartTotal+=stockItem.getPrice()
		if(noSuchItem):
			print("Item "+cartItem+" not found.")
		print()
	print("Cart Total: $"+str(cartTotal))
cart=["007","001"]

checkout(supermarket,cart)
