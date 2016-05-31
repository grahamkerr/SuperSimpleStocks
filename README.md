# SuperSimpleStocks

<b>SuperSimpleStocks is a code that models a very simple trading market. 

1) supersimplestocks.py contains three classes: Stock, Trade and Portfolio. Using these allows you to set up a collection of stocks with certain attributes, make trades on those stocks, and include those trades within your portfolio.

Stocks: This class is set up with the stock name, type, last dividend, par value, Fixed Dividend.

            tea = Stock("tea", "common", 0.0, 100) 
... in this case fixed dividend = None

You can then compute the dividend yield by,

            divyield = tea.div_yield(40.00) 
... where the input, 40.00, is the price.

You can also compute the P/E ratio by,

            pe_ratio = tea.pe_ratio(40.00) 
... where again, 40.00 is the price

You can make a trade using the method .trade_stock(PRICE, QUANTITY, BUY or SELL)

            teatrade = tea.trade_stock(44.0, 2.0, 'b').
... this then makes an object called teatrade using the Trade class

Trades: This class holds a trade. It takes the stock name, price, quantity, buy or sell indicator, and the cuurent time as a timestamp.

        trade = Trade("tea", 44.0, 2.0, 'b', time()) 
The timestamp is in seconds, but the class is printed with time in a readable format (YYYY/MM/DD, HH:MM:SS). Multiple trades can be added to a portfolio object
        
Portfolio: This class holds one or more trades in a list, along with the trader's name.
           
e.g for a list of trades = [trade1, trade2, trade3]

                tradeportfolio = Portfolio("GrahamKerr",trades)
A number of methods using all of the trades can then be performed such as -

Computing the volume weighted share price for a particular stock over a set time range,

                vwsp_tea = tradeportfolio.volweightsp('tea', 15) 
... for 15 in units of minutes. 

Computig the GBCE share index over a time range,

                gbce = tradeportfolio.gbce_comp(15) 
... again, for 15 in units of minutes
            
You can open an empty portfolio by inputting an empty list,

                tradeportfolio = Portfolio("GrahamKerr,[])
                
In both cases (an initially empty portfolio, or one that is created with some pre-existing trades), trades can be added by,

                tradeportfolio.add_trade(trade) 
... for a single trade or

                [tradeportfolio.add_trade(item) for item in trades] 
... for multiple trades held in a list called trades.
             

2) supersimplestocks_examples.py contains a few examples of using the classes and their methods. 
No user input is required until the very end, where the code looks at what happens if you enter an invalid input (for example, a negative price).
        

