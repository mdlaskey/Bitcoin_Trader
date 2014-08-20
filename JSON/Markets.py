import IPython
import json 



class Markets: 
	def __init__(self,market):
		self.m_key = market 

	def get_market(self,m_dict):

		if(m_dict.get('success') == '1'): 
			m_list = m_dict.get('return')
		else: 
			return 0; 


		for i in range(0,len(m_list)):
			
			if(self.m_key == m_list[i].get('label')):

				return m_list[i].get('marketid')

