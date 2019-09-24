#This program gets the projected total sales.
#9-12-19
#CTI-110 P2T1 - Sales Prediction
#Tyler Anderson

total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit.
print('The profit is $', format(profit, ',.2f'))
