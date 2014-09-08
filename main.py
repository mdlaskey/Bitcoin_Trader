import IPython
import json 
import CryptsyPythonAPI.Cryptsy as Cryptsy
import JSON.Markets as Markets
import JSON.Trades as Trades
import Learner.QLearner as QLearner
import Wallet
import visuals 
import numpy
import cPickle as pickle
import time

PRIVATE_KEY = '9bd15515d2c34f582eddd4975d03bb73f50761d7ef628a2d0f6f66551dcd642bd7dc30747400185f'
PUBLIC_KEY = '2f2ef8959a68c1912fe51b6cbee0fc973798854b'
MKRT = 'LTC/BTC'

if __name__ == '__main__':

	C = Cryptsy.Cryptsy(PUBLIC_KEY,PRIVATE_KEY)
	M = Markets.Markets(MKRT)
	T = Trades.Trades()
	V = visuals.Visuals()
	Q = QLearner.QLearner()
	W = Wallet.Wallet()
	


	States = []
	Trade_Data = []
	i = 0
	while( i < 2):

		m_dict = C.getMarkets()
		m_id,price = M.get_market(m_dict)
		m_trades = C.marketTrades(m_id)

		trade_data = T.get_data(m_trades)
		price_EMA = T.EMA(trade_data[:,1])

		wallet = W.get_wallet()

		state = Q.get_state(price_EMA,price,wallet,0)
		States.append(state)
		Trade_Data.append(trade_data)
		print i
		#V.plot_trades(trade_data)
		i = i+1
		time.sleep(10)

	file_dump = [States,Trade_Data]
	raw_data = open("raw_data.p","wb")
	pickle.dump(file_dump,raw_data)
	raw_data.close()
