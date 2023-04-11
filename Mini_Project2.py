#Mini project

'''
A county collects property taxes on the assessment value of property, which is 60 percent of
the property's actual value. For example, if an acre of land is valued at $10,000, its assessment
value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
actual value of a piece of property and displays the assessment value and property tax.
'''
'''
New task!
Make an actual list of properties(def made will have it read from a file) and see if you can make it look like a real list(going to attemp) and output a graph of price
compare the prices(def create) of each property and tell the user whats the best property based on the price
*Have to have a loop , write it too a file*
'''
#Project part 2

#this will allow me to create 
import pandas as pd
from tabulate import tabulate

#Final Var for tax
FINAL_TAX= .72

def properties():
#this will read from the properties file
    try:
        propDF= pd.read_csv('properties.csv')
        propDF['Price']= propDF['Price'].str.replace('[$|,]', '', regex=True)
        propDF['Price']=pd.to_numeric(propDF['Price'])
        return propDF
        
        '''
        while True:
            with open('properties.csv', 'r') as f1:
                read_properties= f1.read()
            return read_properties'''
        
    except FileNotFoundError:
        print("Properties file not found. Please make sure it exists")


propDF= properties()
print(propDF)
#read it from the file(done)

'''
def calculateTax(contents):
#this will calculate the tax for each property
    
    #split the data into lines 
    contents= properties()
    
    #split int line
    lines= contents.split('\n')
    #loop to find the line that has the price of the property
    
    for line in lines:
        #take the price from the string
        price_str= line.split(':')[-1].strip()
        #remove the price from the line
        price_str= price_str.replace(',','')
        #convert the price to a number
        prince = float(price_str)

    
    pass

def prop_assessment():
    pass

def compareTax():
#this will compare the taxes of the properties

#this will need a loop to compare the prices of the properties
    pass

'''



    




'''

#Final Var for tax
FINAL_TAX= .72

#property assessment function
#takes in parameters from the users inputs
def prop_assessment(value, percent):
    
    #calculation for the assessment value
    assessVal= float(value * percent)

    #Calculates the price per acre
    price_per_acre= float(assessVal / 100)

    #Prop tax calculation
    prop_tax= float(price_per_acre * FINAL_TAX)

    #retuns the values after they are calulated
    return assessVal, prop_tax




#main funtions
def main():
    landVal= int(input('Input the value of the property: '))
    
    percentage= float(input('Enter percatage of property actual value: '))

    assessVal , prop_tax= prop_assessment(landVal, percentage)

    print(f'The value of the property is ${landVal:.2f} \nThe property tax is ${prop_tax:.2f}  \nThe assessment value is ${assessVal:.2f}' )

main()

'''




