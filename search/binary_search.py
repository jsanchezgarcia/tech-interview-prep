import unittest
import random
import copy

def binary_search(alist, item):
	# alist is a sorted list
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) / 2
		if alist[midpoint] == item:
			found = True
		else:
			if alist[midpoint] > item:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

def recursive_binary_search(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if alist[midpoint] > item:
				return recursive_binary_search(alist[:midpoint], item)
			else:
				return recursive_binary_search(alist[midpoint+1:], item)

class Test(unittest.TestCase):
	n = 100
	alist = sorted([int(random.random()*100) for i in xrange(n)])
	item = int(random.random()*100)

	def test_binary_search(self):
		self.assertEquals(binary_search(self.alist, self.item), self.item in self.alist)

	def test_recursive_binary_search(self):
		self.assertEquals(recursive_binary_search(self.alist, self.item), self.item in self.alist)

if __name__ == '__main__':
	unittest.main()