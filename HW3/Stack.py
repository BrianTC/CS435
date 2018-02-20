import ctypes

class Stack:
	def __init__(self):
		self._data = None
		self._capacity = 0
		self._used = 0

	def empty(self):
		return self._used == 0

	def clear(self):
		self._used = 0

	def push(self, e):
		self._resize(self._used + 1)
		self._data[self._used] = e
		self._used += 1

	def pop(self):
		self._used -= 1
		return self._data[self._used]

	def top(self):
		return self._data[self._used - 1]

	def _resize(self, newCapacity):
		if self._capacity < newCapacity:
			newCapacity = max(newCapacity, self._capacity * 2)
			newData = (newCapacity * ctypes.py_object)()
			for i in range(self._used):
				newData[i] = self._data[i]
			self._data = newData
			self._capacity = newCapacity

