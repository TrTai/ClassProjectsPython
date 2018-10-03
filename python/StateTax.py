#Tax Calculation
#Treye Chaney
#9/19/2016 release
#calculating total payment after adding set tax for state and county
>>> purchase = float(input('Total payment for purchase? '))
>>> StateTax = 0.05
>>> CountyTax = 0.025
>>> Total = (purchase*StateTax*CountyTax)+purchase
>>> print ('Amount of purchase\t',format(purchase, '.2f'))
>>> print ('State tax\t', format(StateTax, '.2f'))
>>> print ('County tax\t', format(CountyTax, '.2f'))
>>> print ('County tax\t', format(CountyTax, '.3f'))
>>> print ('Total of sale\t', format(Total, '.2f'))
>>> 
