import numpy
import matplotlib.pyplot as plt
import IPython 

class Visuals: 

	def plot_trades(self,Data):

		plt.figure(1)
		plt.clf()
		plt.cla()
	   	
	   	plt.autoscale(True,'x',True)
	    
		plt.subplot(3,1,1)
		plt.ylabel('Quantity')
		plt.plot(Data[:,0],'b-')

		plt.subplot(3,1,2)
		plt.ylabel('Price')
		plt.plot(Data[:,1],'b-')

		plt.subplot(3,1,3)
		plt.ylabel('Value')
		plt.plot(Data[:,2],'b-')
	   
		plt.show(block=False)
    	plt.pause(.05)