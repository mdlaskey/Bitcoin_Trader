import IPython 
import numpy as np


TRADE_NUM = 100
MAX_PRICE_NUM = 2
WALLET_NUM = 2
NUM_ACTIONS = 2

STATE_SIZE = TRADE_NUM+MAX_PRICE_NUM+WALLET_NUM+1



class QLearner: 

	def __init__(self):
		self.state = np.zeros((STATE_SIZE,1))
		self.weights =  np.zeros((STATE_SIZE,1))+1
		self.gamma = 0.9
		self.rho = 0.2
		
	def get_state(self,trade_data,max_price,wallet,action):
		
		for i in range(0,TRADE_NUM):		
			self.state[i] = trade_data[i]

		for i in range(0,MAX_PRICE_NUM):
			self.state[TRADE_NUM+i,0] = max_price[i,0]
		
		for i in range(0,WALLET_NUM):
			self.state[TRADE_NUM+MAX_PRICE_NUM+i,0] = wallet[i,0]

		self.state[STATE_SIZE-1,0] = action
		return self.state

	def update_weigths(self,state_t,state_tp1,reward):

		value_t = reward+self.gamma*np.dot(state_tp1,self.weights)
		Q_t = np.dot(state_t,self.weights)

		self.weights = self.weights + self.rho*(value_t - Q_t)*state_t

	def take_action(self,state_t):

		max_val = 0
		for i in range(0,NUM_ACTIONS):
			state_t[end,0] = i;
			val = np.dot(self.weights,state_t) 
			if(val > max_val):
				action = i
				max_val = val

		return action