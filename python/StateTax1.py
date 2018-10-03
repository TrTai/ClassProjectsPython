#Tax Calculation
#Treye Chaney
#9/30/2016 release
#calculating total payment after adding set tax for state and county
#Ask for input from user for amount of purchase
purchase = float(input('Input amount of purchase'))
#multiplying purchase amount by State Tax to find amount paid in State Taxes and assigning to variable "StateTax"
StateTax = 0.05*purchase
#multiplying purchase amount by County Tax to find amount paid in County Taxes and assigning to variable "CountyTax"
CountyTax = 0.025*purchase
#adding the purchase, amount found in State and County Tax to come a total amount paid in the transaction and assigning it to variable "total"
Total = (purchase+StateTax+CountyTax)
#printing inputted amount alongside results for each calculation in an organized format.
print ('Amount of purchase',format(purchase, '27,.2f'))
print ('State tax', format(StateTax, '36,.2f'))
print ('County tax', format(CountyTax, '35,.2f'))
print ('Total of sale\t\t', format(Total, '21,.2f'))
