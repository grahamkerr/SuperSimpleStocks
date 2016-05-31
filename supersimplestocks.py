""" 
NAME:   supersimplestocks.py

AUTHOR: Graham Kerr

PURPOSE:  Defines three classes
           1) Stock -- Defines the attributes and methods
                       of the Stock class. 
           2) Trade -- Defines the attributes and methods 
                        of the Trade class. If a trade is 
                        made of a stock then this class
                        defines how to make the resulting 
                        object
           3) Portfolio -- Defines the attributes and methods
                           of the Portfolio class. This is a 
                           collection of trades of any stock.             

DATE WRITTEN: 31st May 2016
     MOD. HISTORY: 

NOTES:   ** This code defines three classes. These can be imported
         and used by a user to create a Portfolio of Trades 
         given some stocks. There are some restrictions on 
         allowed inputs, with the expected inputs for creating 
         a new object, or using a method described below within 
         each class/method. 

         ** For the most part the code already finds where invalid 
         values are entered and asks the user to re-input a 
         correct value (or alternatively to exit the method). Only
         a basic implementation.
         
"""

# Imported modules
from time import gmtime, strftime, time


# Define the classes: Stock, Trade and Portfolio

class Stock(object):
    """ 
    The Stock class decsribes the attributes and methods
    associated with the Stocks. 
   
    Attributes: 
       sym      = The stock abbreviation (type = string)
       typ      = The type of stock (common or preferred, type = string)
       lastdiv  = The last dividend of the stock (type = float)
       fixeddiv = If applicable, the fixed dividend (type = float)
    	          Applies in the case of preferred stock.
       parval   = The stock par val (type = float)

    Methods:
       __repr__    = To format the printing of the class details
       div_yield   = Computes the dividend yield
       pe_ratio    = Computes the P/E pe_ratio
       trade_stock = Will trade some stock, buying or selling

    """
  
    def __init__(self, sym, typ, lastdiv, parval, fixeddiv=None):
    	""" Initialise the class """
        self.sym = sym.upper()  # Set to upper case
        self.typ = typ.lower()  # Set to lower case
        self.lastdiv = float(lastdiv) # Makes sure this is a float
        self.fixeddiv = fixeddiv 
        self.parval = float(parval) # Makes sure this is a float

        #Express the fixed div as a decimal not a percentage
        if self.fixeddiv != None:
            self.fixeddiv/=100.00

        # Some variables to use in this class when asking for 
        # user input in the event of an inappropriate input 
        self.PRICE_ERR = "\n!! You have entered a zero or negative price."\
                    "Either end the query, 'X', or enter a new price 'P'?: "
        self.QUANT_ERR = "\n!! You have entered a zero or negative quantity."\
                    "Either end the trade, 'X', or enter a new quantity 'Q'?: "
        self.BORS_ERR = "\n!! You have not entered 'B','b','S' or 's'. Either end"\
                   "the trade, 'X', or re-enter 'B' (buy) or 'S' (sell)?: "
    
    def __repr__(self):
    	""" Format how the class should be printed to screen """
    	return "\n\nThe %s stock has the following details: \
    	\n  Symbol: %s\n  Type: %s\n  Last dividend: %s\n"\
        "  Fixed dividend: %s\n  Par Val: %s" \
    	% (self.sym, self.sym, self.typ, self.lastdiv, 
           self.fixeddiv, self.parval)

    def div_yield(self, price):
    	""" 
    	NAME: .div_yield(price)

    	PURPOSE: Computes the dividend yield, given 'price'. 
    	         For 'common' type stock this is:-
    	               last dividend / price
    	         For 'preferred' type stock this is:-
    	               (fixed dividend * par value) / price
    	
    	INPUTS: price =  Price should be number > 0. 

    	OUTPUTS: div_yield = The dividend yield in same units as price

    	NOTES: The code will check the price and query the user to 
    	       ascertain whether to quit or enter a new price if 
    	       price is input < 0.

    	"""
        # Tell the user what is happening
    	print "\n>>> Computing Dividend Yield Ratio for %s at price"\
              "= %sp <<<" % (self.sym, price)

    	#Checks to see if price is a float. If not it converts to a float
    	if type(price) != float:
    		price = float(price)
    
    	# Checks to see if a negative or zero value has been given.
    	# The user can either fix the price, or exit the method.
        while price <=0:
            price_neg = raw_input(self.PRICE_ERR)
            price_neg = price_neg.upper()
            if price_neg == 'X':
                print "... Cancelling query"
                return
            elif price_neg == 'P':
                price = float(raw_input(
                        "... Please enter the actual price now: "))
            
        # Compute the div yield depening on stock type
        if self.typ == 'common':
        	return self.lastdiv / price 
        elif self.typ == 'preferred':
        	return (self.fixeddiv * self.parval) / price
        else:
            print "!! Invalid stock type entered. Please correct."
            print " ... should be either 'common' or 'preferred'"
            return 

    def pe_ratio(self, price):
    	""" 
    	NAME: .pe_ratio(price)

    	PURPOSE: Computes the P/E ratio, given 'price'.
    	         This is the value:- price/dividend 
    	
    	INPUTS: price =  Price should be number > 0. 

    	OUTPUTS: pe_ratio -- The P/E ratio 

    	NOTES: The code will check the price and query the user to 
    	       ascertain whether to quit or enter a new price if 
    	       price is input < 0.

    	"""     
        # Tell the user what is happening       
    	print "\n>>> Computing P/E Ratio <<<"

    	#Checks to see if price is a float. If not it converts to a float
    	if type(price) != float:
    		price = float(price)
    
    	# Checks to see if a negative or zero value has been given.
    	# The user can either fix the price, or exit the method.
        while price <=0:
            price_neg = raw_input(self.PRICE_ERR)
            price_neg = price_neg.upper()
            if price_neg == 'X':
                print "... Cancelling query"
                return
            elif price_neg == 'P':
                price = float(raw_input(\
                        "... Please enter the actual price now: "))

        # If the dividend is currently zero then the p/e ratio is 
        # set to 0 to avoid div by zero
        if self.lastdiv == 0:
        	return 0
        else:
        	return price/self.lastdiv

    def trade_stock(self, price, quant, bors):
        """ 
        NAME: .trade_stock(price,quant,bors)

        PURPOSE:  To perform a trade of this stock 

        INPUTS:  price     = The price at which to trade (> 0, float)
                 quant     = The quantity of stock to trade (> 0, int)
                 tradetime = The timestamp of the trade (set in code)
                 bors      = A string indicating if it was 'Buy' or 'Sell'

        OUTPUTS: A trade object

        NOTES: The code will check the price & quant inputs, and query 
               the user to ascertain whether to quit or enter a new value if 
    	       either is input < 0.

        """
        # Tell the user what is happening
    	print "\n>>> Beginning trade of %s <<<" % (self.sym)

        # Checks to see if a negative or zero value has been given.
        # The user can either fix the price, or end the trade.
        while price <=0:
            price_neg = raw_input(self.PRICE_ERR)
            price_neg = price_neg.upper()
            if price_neg == 'X':
                print "... Cancelling query"
                return
            elif price_neg == 'P':
                price = float(raw_input(
                        "... Please enter the actual price now: ")) 
        if type(price) != float:
        	price = float(price)  
        
        # Checks to see if a negative or zero value has been given.
        # The user can either fix the quantity, or end the trade.
        while quant <= 0:
            quant_neg = raw_input(self.QUANT_ERR)
            quant_neg = quant_neg.upper()
            if quant_neg == 'X':
                print "... Cancelling trade"
                return
            elif quant_neg == 'Q':
                quant = float(raw_input(
                        " ... Please enter the actual quantity now: "))  
        if type(quant) != float:
        	quant = float(quant)

        # The indicator must be a string that is 'B' or 'S'
        # Converts to upper case so user can enter either
        # b, B, s or S
        if type(bors) != str:
    		bors = str(bors)
    	bors = bors.upper()
    	while (bors != 'B') and (bors != 'S'):
            bors_val = raw_input(self.BORS_ERR)
            bors_val = bors_val.upper()
            if bors_val == 'X':
                print "... Cancelling trade"
                return
            elif (bors_val == 'B') or (bors_val == 'S'):
            	bors = bors_val
            
        #Assign the timestamp to the current time in seconds
        timestamp = time()
        
        #Prints the trade, with the timestamp in a readable format
        # of YYYY/MM/DD, HH:MM:SS
        print "    %s  -- %s %s of %s at %sp" % (
                    strftime("%Y-%m-%d, %H:%M:%S", 
        	        gmtime(timestamp)), bors, quant, self.sym, price
                    )

        #Returns the trade as an object of the Trade class
        return Trade(self.sym, price, quant, bors, timestamp)


class Trade(object):
    """ 
    The Trade class decsribes the attributes and methods
    associated with the trades. 
   
    Attributes: 
       stock     = The stock involved in the trade (abbr symbol) 
                   (type = string)
       tr_price  = The price of stock in the trade (type = float)
       tr_quant  = The quantity of the stock traded (type = float)
       bors      = A string indicating if the stock was bought or 
                   sold (type = string)
       timestamp = The time of the trade in seconds (type = float)

    Methods are:
       __repr__  = To format the printing of the class details
       show_time = To show the timestamp in a readable format
      
    """
    
    def __init__(self, stock, tr_price, tr_quant, bors, timestamp):
    	""" Initialise the class """
        self.stock = stock.upper() #Capitalise if not already
        self.tr_price = tr_price
        self.tr_quant = tr_quant
        self.bors = bors
        self.timestamp = timestamp

    def __repr__(self):
    	""" Format the printing of the class """
    	#Convert to a readable time
    	str1 = strftime("%Y-%m-%d, %H:%M:%S", gmtime(self.timestamp))
    	#Expand out the abbreviation
    	if self.bors == 'B':
    		str2 = "Bought"
    	else:
    		str2 = "Sold"
        #Print the Trade
        return "\n%s  -- %s %s of %s at %sp" % (
                        str1, str2, self.tr_quant, 
        	            self.stock, self.tr_price
                        )
       
    def show_time(self):
    	"""
    	NAME: show_time()
    	
    	PURPOSE: To display and return the timestamp in a 
                 readable format
        
        INPUTS: None (self)

        OUTPUTS: Prints to screen and returns a string

    	"""
        print "\n>>> Trade timestamp is: %s" % (
                           strftime("%Y-%m-%d, %H:%M:%S", 
                           gmtime(self.timestamp))
                           )
        return strftime("%Y-%m-%d, %H:%M:%S", gmtime(self.timestamp))


class Portfolio(object):
    """ 
    The Portfolio class describes the attributes and methods 
	associated with a trader's portfolio. Effectively, this
	holds a set of trades. 

	Attributes: 
	    tradername  = The trader's name (type = string)
        tradelist   = The trades previously completed, if
                	  these are to be added to this 
                	  portfolio. This should have an empty
                	  set entered if a new portfolio. 
                	  (type = list)      
	Methods:
	    __repr__    = To format the printing of portfolio
	    add_trade   = To add a trade into the portfolio 
	    volweightsp = The volume weighted stock price
	    asi_calc    = The All Share Index
	    earliest_tr = Print the time of the earlist trade 
	    num_tr      = The number of trades in the portfolio
	    num_stocks  = The number of different stocks
	    stock_types = The stock types in the portfolio

    """

    def __init__(self, tradername, tradelist):
        """ Initialise the portfolio object """
    	self.tradername = tradername
        self.tradelist = tradelist
        
    def __repr__(self):
    	""" Format the printing of the portfolio object"""
    	print "\n\n%s's Portfolio:" % self.tradername 
        return "".join(repr(item) for item in self.tradelist)

    def add_trade(self,trade):
    	"""
    	NAME: .add_trade(trade)

    	PURPOSE: To add a trade into the tradelist

    	INPUTS:  A trade object

    	OUTPUTS: The updated tradelist

    	"""
    	#Tell the user what is happening
    	print "\n... Updating %s's Portfolio " % (self.tradername)
    	
        #Append the trade object to the list
        return self.tradelist.append(trade)

    def volweightsp(self, stock_search, trange):
    	"""
    	NAME: volweightsp(stock_search, trange)

    	PURPOSE: To compute the volume weighted stock 
    	         price for a given stock type over 
    	         the time trange provided. This is computed as
    	         sum( price*quantity ) / sum( quantity )

    	INPUTS:  stock  = The abbreviation of the stock 
    	                  name (type = string)
    	         trange = The time range over which to 
    	                  compute the vol weighted price
    	                  in minutes (type = float)
        
        OUTPUTS: The vol. weighted stock price. 
                
        NOTES:   If the stock is either not present in the 
                 portfolio, or hasn't been traded in the allotted
                 time range then 0 (zero) is returned and the 
                 trader is informed that the search criteria
                 was not met.

        """
        #Tell the user what is happening
        print "\n>>> Computing the Volume Weighted Stock Price <<<"

        if type(stock_search) != str:
            stock_search = str(stock_search)

        # Check if the stock if present, and if it is not exit 
        # this retuning 0 (zero). It is present then extract the
        # trades that match the search criteria into a new list
        stock_pres = len([trades for trades in self.tradelist if
                         trades.stock == stock_search.upper()]) >=1
        stock_inrange = len([trades for trades in self.tradelist if
        	             (trades.stock == stock_search.upper() and
                         (time() - trades.timestamp) <= (trange*60.))
                         ]) >=1
        if stock_pres == False:
            print "\n >>> The stock you are searching for (%s) is not"\
                  " in %s's portfolio." % (
                        stock_search.upper(), self.tradername)
            return 0
        elif stock_inrange == False:
            print "\n >>> The stock (%s) has not been traded by %s within"\
                  "the time range of %s mins." % (
                        stock_search.upper(), self.tradername, trange)
            return 0
        else:
            valid_trades = [trades for trades in self.tradelist if \
                            (trades.stock == stock_search.upper()) and \
                            ((time() - trades.timestamp) <= (trange*60.))]     
            # Sum the value of price * quantity for the trades within 
            # the valid trades, and also sum just the quanity so that 
            #the weighted sum can then be computed
            price_quant_sum = sum(trades.tr_price*trades.tr_quant 
                                   for trades in valid_trades) 
            quant_sum = sum(trades.tr_quant 
                                   for trades in valid_trades)
            return price_quant_sum/quant_sum

    def asi_calc(self,trange):
        """
        NAME: gbce_calc()

        PURPOSE: Computes the All Share Index (ASI) using the 
                 geometric mean of the stock prices

        INPUTS:  trange = The time in minutes over which to 
                          compute the ASI

        OUTPUTS: The ASI

        NOTES: In the event of an empty tradelist the 
               method exits, returning zero, with a message
               informing the user that the tradelist is empty.

        """   
        #Tell the user what is happening
        print "\n>>> Computing All Share Index (ASI) using %s's" \
               "Portfolio <<<" % (self.tradername)

        #First check if the tradelist is empty
        if len(self.tradelist) == 0:
            print "\n ...%s's portfolio is empty, can't compute "\
                  "all share index\n" % (self.tradername)
            return 0

        #Initially set the price product to an initial value of 1
        price_product = 1
        
        
        # This line finds the unique occurrences of a stock name, so 
        # that we can then compute the volume weighted stock price 
        # for each stock within the portfolio
        stock_names = list(set([self.tradelist[i].stock 
                                for i in range(len(self.tradelist))]))
        num_stocks = len(stock_names)
        
        # Loop through each type of stock, compute the volume weighed 
        # stock price and update the price_product variable
        for name in stock_names:
            price_product*=self.volweightsp(name,trange)
          
        if price_product == 1:
            print " >>> No trades in given time range..."
            return 0  
        #The geometric mean is then:
        else:
        	return price_product**(1/float(num_stocks))

    def earliest_tr(self):
    	""" 
    	NAME: earliest_tr()

    	PURPOSE: Prints the earliest trade to the screen, 
    	         both the readable time and the time 
    	         in seconds
        
        INPUTS:  None (self)

        OUTPUTS: A print statement and the time of the
                 earliest trade is returned, in seconds
                 from the current time
    	"""
    	#Grab the timestaps, in seconds, of each trade
    	trade_times = [time()-self.tradelist[i].timestamp 
                           for i in range(len(self.tradelist))]
        print "\n>>> The earliest trade was %ss ago:" % (max(trade_times))
        print (self.tradelist[trade_times.index(max(trade_times))])
        return max(trade_times)
            
    def num_tr(self):
    	""" 
    	NAME: num_tr()

    	PURPOSE: Returns the number of trades in the portfolio

        INPUTS: none (self)

        OUTPUTS: The number of trades

    	"""
        return len(self.tradelist)

    def num_stocks(self):
    	""" 
    	NAME: num_stocks()

    	PURPOSE: Returns the number of stock types in the portfolio

        INPUTS: none (self)

        OUTPUTS: The number of unique stock types

    	"""
        return len(set([self.tradelist[i].stock 
                         for i in range(len(self.tradelist))]))

    def stock_types(self):
    	""" 
    	NAME: stock_types()

    	PURPOSE: Returns a list of stock types in the portfolio

        INPUTS: none (self)

        OUTPUTS: A list containing the names of the types of
                 stock within the portfolio

    	"""
        return list(set([self.tradelist[i].stock 
                          for i in range(len(self.tradelist))]))



