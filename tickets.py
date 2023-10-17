#Name: NyJavion Timberlake
#Program Purpose: This program finds the cost of movie tickets
# Price for one ticket: $10.99
# Sales tax rate: 5.5%

import datetime

################# define global variables #####################
# define tax rate and prices

SALES_TAX_RATE = .55
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0 

################# define program funtions #####################
def main():

    more_tickets = True
    
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_result()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_tickets = False
            print ("Thank you for order. Enjoy your movie!")
            
        
    
def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of the movie tickets: "))


def perform_calculations():
    global subtoal , sales_tax , total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_result():
    print ('-----------------------------')
    print ('****CINEMA HOUSE MOVIES****')
    print ('Your neighboorhood movie house')
    print ('-----------------------------')
    print ('Tickets    $ ' + format(subtotal, '1,.2f'))
    print ('Sales Tax  $ ' + format(sales_tax, '1,.2f'))
    print ('Total      $ ' + format(total, '1,.2f'))
    print ('-----------------------------')
    print (str(datetime.datetime.now()))

################# call on main program to excute #####################
main()
get_user_data()
perform_calculations()
display_result()
