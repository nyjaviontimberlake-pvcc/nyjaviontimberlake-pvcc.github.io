#Name: NyJavion Timberlake
#Program Purpose: This program finds the cost of movie tickets
# Price for one ticket: $10.99
# Price for one bucket of popcorn: $12.99
# Price for one drink: $4.99
# Sales tax rate: 5.5%

import datetime

################# define global variables #####################
# define tax rate and prices

SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 12.99
PR_DRINK = 4.99

# define global variables
num_tickets = 0
num_popcorn = 0
num_drinks = 0
popcorn_cost = 0
tickets_cost = 0
drink_cost = 0
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
    global num_tickets, num_popcorn, num_drinks, num_popcorn
    num_tickets = int(input("Number of the movie tickets: "))
    num_popcorn = int(input("Number buckets of popcorn: "))
    num_drinks = int(input("Number cups of drinks: "))


def perform_calculations():
    global subtotal, sales_tax, total, popcorn_cost, tickets_cost, drink_cost
    tickets_cost = num_tickets * PR_TICKET
    popcorn_cost = num_popcorn * PR_POPCORN
    drink_cost = num_drinks * PR_DRINK
    subtotal = tickets_cost + popcorn_cost + drink_cost 
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_result():
    moneyformat  = '8,.2f'
    line = ('-------------------------------')
    print (line)
    print ('****CINEMA HOUSE MOVIES****')
    print ('Your neighboorhood movie house')
    print (line)
    print ('Tickets   $ ' + format(tickets_cost, moneyformat))
    print ('Popcorn   $ ' + format(popcorn_cost, moneyformat))
    print ('Drinks    $ ' + format(drink_cost, moneyformat))
    print (line)
    print ('Subtotal   $ ' + format(subtotal, moneyformat))
    print ('Sales Tax  $ ' + format(sales_tax, moneyformat))
    print ('Total      $ ' + format(total, moneyformat))
    print (line)
    print (str(datetime.datetime.now()))

################# call on main program to excute #####################
main()

