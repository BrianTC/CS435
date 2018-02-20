#!/usr/bin/python3
class Product:
	def __init__(self,productCode,description):
		self.upc=productCode
		self.desc=description
		self.price=0
	def setPrice(self,dollarAmmount):
		self.price=dollarAmmount
	def getPrice(self):
		return self.price
	def getProductCode(self):
		return self.upc
	def outOfStock(self):
		return True if self.price==0  else False
	def printInformation(self):
		print("Code:        "+self.upc)
		print("Description: "+self.desc)
		print("Price:       "+str(self.price))
		
