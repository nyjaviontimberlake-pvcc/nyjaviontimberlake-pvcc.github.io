#Name: NyJavion Timberlake
#Program Purpose: Property Tax for car 

# Property Tax rate: 4.20%
# Tax relief 33%


import datetime

################# define global variables #####################

vehicle_valv = 0
PP_TAX = .042
TAX_RELIEF = .33
semi_tax = 0 



def main():

    vehicle_tax = True

    while vehicle_tax:
        get_user_data()
        perform_calculations()
        display_result()

        askAgain = input("n\Would you like to add another for vehicle?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            vehicle_tax = False
            print ("Thank you for paying your taxes.")


def get_user_data():
    global vehicle_valv, tax_relief
    
    vehicle_valv = int(input("What is the assessed value of your vehicle? :"))
    tax_relief = int(input("Are you eligible for tax relief?\n1 for Yes\n2 for No\nInput:  "))
    
    if tax_relief == 1 or tax_relief == 2:
        print("Relief amount will be shown on bill.")
 
        
    

def perform_calculations():
    global relief_amt, full_amt, total, semi_tax

        
    full_amt = vehicle_valv * PP_TAX / 2
    
    if tax_relief == 1:
        semi_tax = full_amt * TAX_RELIEF / 2
    else:
        semi_tax
        
    total = full_amt - semi_tax
    


def display_result():
    moneyformat  = '8,.2f'
    line = ('------------------------------------------')
    print (line)
    print ('****Personal Property Tax for Vehicle****')
    print (line)
    print ('Assessed Value      $ '+ format(vehicle_valv, moneyformat))
    print ('Full Amount Owed    $ '+ format(full_amt, moneyformat))
    print ('Relief Amount       $ '+ format(semi_tax, moneyformat))
    print ('Total Amount Due    $ '+ format(total, moneyformat))
    print (line)
    print (str(datetime.datetime.now()))
    
    
    
    
main()
    
                       
                       

