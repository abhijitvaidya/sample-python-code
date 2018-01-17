
'''
	Minimal blockschain implementation in python.
'''
import time
from hashlib import sha256 as sha256

class SimpleBlockChain():
	def __init__(self):
		self.__blocks = []

	def add_first_block(self, data):
		self.push_block(data, '')

	def add_block(self, data):
		prev_hash = self.__blocks[-1]
		self.push_block(data, prev_hash)

	def __is_valid_block(self, hash):
		if hash.startswith('0000'):
			return True
		return False
		
	def push_block(self, data, prev_hash):
		var = 0
		t = int(time.time())
		block_data = '{0}-{1}-{2}-{3}'.format(data, t, prev_hash, var)
		blockhash = sha256(block_data).hexdigest()
		while(not self.__is_valid_block(blockhash)):
			var += 1
			block_data = '{0}-{1}-{2}-{3}'.format(data, t, prev_hash, var)
			blockhash = sha256(block_data).hexdigest()
		self.__blocks.append(blockhash)

	def print_all_blocks(self):
		print[i for i in self.__blocks]


b = SimpleBlockChain()
b.add_first_block('Hello World')
b.add_block('Second block')
b.add_block('adding Third blockk')
b.add_block('Last block in the chain')
b.print_all_blocks()
