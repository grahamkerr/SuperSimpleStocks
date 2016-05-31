""" 
NAME: supersimplestocks_examples.py

AUTHOR: Graham Kerr

PURPOSE: To show examples of using the classes 
         from supersimplestocks to make some trades, 
         and perform calculations based on a set 
         of stocks.

INPUTS:  None, the stock data is hardcoded at the 
         start of the code

OUTPUTS: Prints to screen (on terminal)

DATE WRITTEN: 31st May 2016
     MOD HISTORY:

NOTES: This is really just meant to show some of
       the functionality of supersimplestocks.py, 
       so I run through a series of actions using
       the classes and methods.

       This version is all hardcoded with no user 
       input or GUI. I manually made some trades with
       a time value set to > 15 mins to help
       simulate computing the volume weighted stock
       price using using only trades from a certain 
       time window. 

"""
#Import some modules
from time import time
from supersimplestocks import Stock, Trade, Portfolio

if __name__ == '__main__':

    # Set up the stocks:
    tea = Stock("TEA", "Common", 0.0, 100.00)
    pop = Stock("POP", "Common", 8.0, 100.00)   
    ale = Stock("ALE", "Common", 23.0, 60.00)
    gin = Stock("GIN", "Preferred", 8.0, 100.00, 2.00)
    joe = Stock("JOE", "Common", 13.0, 250.00)

    # Show the stocks in the market, illustrating their
    # print format
    print tea, pop, ale, gin, joe

    # For a common type stock, perform some calculations:
    #    * dividend yield, price = 40p
    #    * p/e ratio, price = 40p
    #    * make a trade, buying 70 shares of pop, at 40p
    #       per share, with a timestamp indicating when the 
    #       trade occurred
    #    * Print the trade to show what we have done
    print "    Dividend yield = %s" % (pop.div_yield(40.00))
    print "    P/E ratio = %s" % (pop.pe_ratio(40.00))
    pop_tr1 = pop.trade_stock(40.0, 70, 'b')
    print pop_tr1

    # Now, lets add this trade to a new Portfolio, where
    # we pass an empty list since it is a new set of trades
    tradeport = Portfolio("GrahamKerr",[pop_tr1])
    print tradeport

    # Before showing the calculations that can be perfomed on 
    # a portfolio of trades, lets create some new trades and 
    # add them to the Portfolio using the .add_trade() method
    pop_tr2 = pop.trade_stock(44.0, 20, 'b')
    pop_tr3 = pop.trade_stock(30.0, 54, 'b')
    pop_tr4 = pop.trade_stock(50.0, 100,'s')
    pop_tr5 = pop.trade_stock(49.0, 70, 's')
    tea_tr1 = tea.trade_stock(20.0, 20, 'b')
    tea_tr2 = tea.trade_stock(20.0, 20, 's')
    gin_tr1 = gin.trade_stock(43.0, 20, 'b')
    gin_tr2 = gin.trade_stock(26.0, 56, 's')
    gin_tr3 = gin.trade_stock(43.0, 34, 'b')

    trades = [pop_tr2, pop_tr3, pop_tr4, pop_tr5,
              tea_tr1, tea_tr2, gin_tr1, gin_tr2, gin_tr3]

    # for item in trades:
    [tradeport.add_trade(item) for item in trades]

    # The portfolio is now bigger...
    print "\n ... Number of trades in %s's Portfolio: %s" % (
    	              tradeport.tradername, tradeport.num_tr())
    # ... made up of X number of different stocks...
    print "\n ... Number of types of stock in %s's Portfolio: %s" % (
    	              tradeport.tradername, tradeport.num_stocks())
    # ... of stock type:
    print "\n ... Types of stock in %s's Portfolio: %s" % (
    	              tradeport.tradername, tradeport.stock_types())

    # We can choose one of these stocks and compute the 
    # volume weighted stock price.
    # If we choose the 'pop' stock, and want to search over 
    # the previous 15 minutes then this is:
    vwsp_pop = tradeport.volweightsp('pop',15.00) 
    print "\n ... The volume weighted stock price of POP over the" \
           "past 15 mins is: %.3fp" % (vwsp_pop)
 
    # If we want to instead compute the GBCE all share 
    # index in the previous 15 mins:
    gbce_index = tradeport.gbce_calc(15.00)
    print "\n ... The GBCE All Share Index over the past 15 mins is:" \
          "%.3fp" % (gbce_index)


    # We can find out the earliest trade in the portfolio 
    # via the .earliest_tr() method.
    # First, lets make some trades, and manually change their
    # timestamp to be time() - (20*60), that is 20 mins before
    # the current time. 
    # These are then added to our portfolio, then find the 
    # earliest entry. 

    pop_tr6 = pop.trade_stock(49.0, 34,'b')
    pop_tr7 = pop.trade_stock(182.0, 73, 'b')
    tea_tr3 = tea.trade_stock(45.0, 29, 'b')
    tea_tr4 = tea.trade_stock(27.0, 80, 's')
    gin_tr4 = gin.trade_stock(69.0, 40, 'b')
    ale_tr1 = ale.trade_stock(9.0, 30, 's')
    ale_tr2 = ale.trade_stock(19.0, 33, 'b')
    
    pop_tr6.timestamp = time() - (20.0*60.0)
    pop_tr7.timestamp = time() - (20.0*60.0)
    tea_tr3.timestamp = time() - (20.0*60.0)
    tea_tr4.timestamp = time() - (20.0*60.0)
    gin_tr4.timestamp = time() - (20.0*60.0)
    ale_tr1.timestamp = time() - (20.0*60.0)
    ale_tr2.timestamp = time() - (20.0*60.0)

    trades2 = [pop_tr6, pop_tr7, ale_tr1, ale_tr2,
              tea_tr3, tea_tr4, gin_tr4]

    [tradeport.add_trade(item) for item in trades2]

    earliest = tradeport.earliest_tr()

    # If we try to compute the vwsp for a stock not in our 
    # portfolio the code will exit and tell us
    vwsp_joe = tradeport.volweightsp('joe',15.00) 

    # If we search over a time period where there are no trades
    # of a particular stock we are told
    vwsp_ale= tradeport.volweightsp('ale',15.00) 


    # Trying to compute gbce or vwsp on an empty portfolio:
    tradeport_empty = Portfolio("LazyTrader",[])
    # The vwsp calc error is handled by the error 
    # mentioned above:
    vwsp_pop2 = tradeport_empty.volweightsp("pop", 15.00)
    # In the case of gbce:
    gbce_index2 = tradeport_empty.gbce_calc(15.00)



    # The following show some examples of what happens if you 
    # enter incorrect values as input:
    div_yield_errtest = pop.div_yield(-40.00)
    pe_ratio_errtest  = pop.pe_ratio(0.00)
    pop_tr_errtest = pop.trade_stock(-40.0, 0, 'c')



