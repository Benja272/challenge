from dateutil import rrule

class Portfolio:
    def __init__(self):
        self.stocks = []
    
    def addStock(self, stock):
        self.stocks.append(stock)   
        
    def Profit(self, date1, date2):
        initialPrice = 0
        finalPrice = 0
        for stock in self.stocks:
            initialPrice += self.Price(date1)
            finalPrice += self.Price(date2)
        profit = (finalPrice - initialPrice)/initialPrice
        #calculate date difference in months
        months = rrule.rrule(rrule.MONTHLY, dtstart=date1, until=date2).count() 
        annualizedReturn = ((1 + profit) ** (1/months)) - 1
        return annualizedReturn



