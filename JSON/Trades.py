import IPython
import json 
import numpy as np


class Trades: 
		
	def get_data(self,t_dict):

		if(t_dict.get('success') == '1'): 
			t_list = t_dict.get('return')
		else: 
			return 0; 

		Data = np.zeros((len(t_list),3))

		for i in range(0,len(t_list)):
			
			Data[i,0] = float(t_list[i].get('quantity'))
			Data[i,1] = float(t_list[i].get('tradeprice'))
			if (t_list[i].get('initiate_ordertype') == 'Buy'):
				Data[i,2] = float(t_list[i].get('total'))
			else: 
				Data[i,2] = -float(t_list[i].get('total'))

		return Data

	def EMA(self,data):
		alpha = 0.1
		length = np.max(data.shape)
		
		for i in range(1,length):
			data[i] = alpha*data[i]+(1-alpha)*data[i-1]

		return data