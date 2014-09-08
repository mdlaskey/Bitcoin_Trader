import IPython 
import numpy as np

class Wallet:

	def __init__(self):
		self.BTC = 1
		self.LTC = 10
		self.value = 0

	def update_wallet(self,action,quantity_btc,quantity_ltc):
		#ACTION 0: SELL LTC
		#ACTION 1: BUY LTC
		if action == 0:
			self.LTC = self.LTC - quantity_ltc
			self.BTC = self.BTC + quantity_btc
		else: 
			self.LTC = self.LTC + quantity_ltc
			self.BTC = self.BTC - quantity_btc

	def caculate_reward(self,price):

		new_value = self.LTC/price
		Reward = new_value - self.value

		self.value = new_value
		return Reward

	def get_wallet(self):

		wallet = np.zeros((2,1))
		wallet[0,0] = self.LTC
		wallet[1,0] = self.BTC

		return wallet


