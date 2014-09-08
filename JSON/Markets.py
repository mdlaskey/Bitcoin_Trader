import IPython
import json 
import numpy as np



class Markets: 
	def __init__(self,market):
		self.m_key = market 

	def get_market(self,m_dict):

		if(m_dict.get('success') == '1'): 
			m_list = m_dict.get('return')
		else: 
			return 0; 

		price = np.zeros((2,1))
		for i in range(0,len(m_list)):
			
			if(self.m_key == m_list[i].get('label')):

				price[0,0] = float(m_list[i].get('low_trade'))
				price[1,0] = float(m_list[i].get('high_trade'))


				return m_list[i].get('marketid'),price

