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

# Importing needed libraries
import pandas as pd

# Final Var for tax
FINAL_TAX = 0.72


def properties():
    # This will read from the properties file
    try:
        propDF = pd.read_csv('properties.csv')

        # Convert Price column to string
        propDF['Price'] = propDF['Price'].astype(str)

        # Remove special chars
        propDF['Price'] = propDF['Price'].str.replace('[$|,]', '', regex=True)

        # Converts the price column to all numeric values
        propDF['Price'] = pd.to_numeric(propDF['Price'])

        return propDF

    except FileNotFoundError as err:
        print('404: ', err)

    except EOFError:
        print("End of file reached!")


def calculateAssesVal(propDF):

    assesVal = propDF['Price'] * 0.6

    return assesVal


def propTax(assesVal):

    calc = assesVal / 100

    prop_tax = FINAL_TAX * calc

    return prop_tax


def updateFile():
    propDF = properties()

    propDF['Assessment Value'] = calculateAssesVal(propDF)

    propDF['Property Tax'] = propTax(propDF['Assessment Value'])

    propDF.to_csv('properties.csv', index=False)


def main():
    # Update properties file
    updateFile()

    # Read properties file
    df = pd.read_csv('properties.csv')

    # Get the number of rows in the dataframe
    num_rows = df.shape[0]

    # Loop through each row in the dataframe
    for i in range(num_rows):
        # Get the row
        row = df.loc[i]
        
        # Get the property name, assessment value, and property tax
        prop = row['Municipality']
        aVal = row['Assessment Value']
        tx = row['Property Tax']

        # Create message
        message = f'{prop} has an assessment value of ${aVal:,.2f} and a property tax of ${tx:.2f}'
        
        # Create list to hold messages
        prop_List = []
        
        # Append message to list
        prop_List.append(message)
        
        # Print the list of messages
        print(prop_List)


# Call the main function
main()
    


#code that I didn't use 
'''
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




