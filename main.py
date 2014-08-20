import IPython
import json 
import CryptsyPythonAPI.Cryptsy as Cryptsy
import JSON.Markets as Markets

PRIVATE_KEY = '9bd15515d2c34f582eddd4975d03bb73f50761d7ef628a2d0f6f66551dcd642bd7dc30747400185f'
PUBLIC_KEY = '2f2ef8959a68c1912fe51b6cbee0fc973798854b'
MKRT = 'LTC/BTC'

if __name__ == '__main__':

	C = Cryptsy.Cryptsy(PUBLIC_KEY,PRIVATE_KEY)
	M = Markets.Markets(MKRT)

	m_dict = C.getMarkets()
	m_id = M.get_market(m_dict)

	IPython.embed()