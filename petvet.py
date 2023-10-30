#Name: NyJavion
#Prog Purpose: This program finds the costs of pet vaccines & medications for dogs and cats
#NOTE: Pet medication prescribed by licensed veterinarias are not subject to sales tax in virginia

#Pet care meds pricing
#-------------------------------------------------------

#Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAPP $35.00
#   3. Influenza $48.00
#   4. Leptospirosis $21.00
#   5. Lyme Disease $41.00
#   6. Rabies $25.00
#   7. Full vaccine Package (includes all vaccines): 15% discount

# Canine Heartworm Preventative Chews (prices per chew; one chew per month)
#   Small dogs, Up to 25 lbs: $9.99
#   Medium-sized, 26 to 50 lbs: $11.99
#   Large dogs: 51 to 100 lbs: $13.99

import datetime

##################### define global variables #####################
#define dog prices

PR_BORD = 30
PR_DAPP = 35
PR_FLUZ = 48
PR_LEPTO = 21
PR_LYMD = 41
PR_RABI = 25
PR_ALL = 0

#define cat prices
PR_LEUK = 35
PR_RHINO = 30
PR_CAT_RABI = 25
PR_CAT_ALL = 0

#CAT CHEWS
PR_CAT_CHEWS = 8

#SALE TAX
SALES_TAX = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

#define global variables
pr_vax = 0 
pet_vax = 0
pr_chews = 0
num_chews = 0


##################### define program functions #####################
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\Would you like to process another pet (Y/N)?")
        if askAgain.upper() == "N":
            more = False
            print ('Thank you for trusting PET CARE MEDS with your pet vaccines and medication.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or a cat (C)? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))



    

##################### DOG functions #####################

    
def get_dog_data():
    global  pet_vax, num_chews, dog_menu
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella: $30.00 \n\t2.DAPP: $35.00 \n\t3.Influenza: $48.00 \n\t4.Leptospirosis: $21.00"
    dog2 = "\n\t5.Lyme Disease: $41.00 \n\t6.Rabies: $25.00 \n\t7.Full Vaccine Package: Includes all vaccines with a 15% discount \n\t8.NONE"
    dog_menu = dog1 + dog2 
    pet_vax = int(input(dog_menu + "\n** Enter Vaccine Number: "))
    



    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N?) ")
    if heart_yesno.upper()=="Y":
        num_chews = int(input("How many heart worm chews would you like to order?"))



def perform_dog_calculations():
    global vax_cost, chews_cost, total, pr_chews

    ######## vaccines
    if pet_vax == 1:
        vax_cost = PR_BORD

    elif pet_vax == 2:
        vax_cost = PR_DAPP

    elif pet_vax == 3:
        vax_cost = PR_FLUZ

    elif pet_vax == 4:
        vax_cost = PR_LEPTO

    elif pet_vax == 5:
        vax_cost = PR_LYMD

    elif pet_vax == 6:
        vax_cost = PR_RABI

    elif pet_vax == 7:
         PR_ALL = PR_BORD + PR_DAPP + PR_FLUZ + PR_LEPTO + PR_LYMD + PR_RABI
         vax_cost = .85 * PR_ALL

    else:
        vax_cost = 0.00
        
            
        
       


    ######### HEART WORMS CHEWS
    if num_chews != 0 :
        if pet_weight <= 25:
            pr_chews = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight <= 50:
            pr_chews = num_chews * PR_CHEWS_MED

        else:
            pr_chews = num_chews * PR_CHEWS_LARGE


    ##### FIND TOTAL
    total = vax_cost + pr_chews
   
    



def display_dog_results():
    moneyformat = '8,.2f'
    line = ('-----------------------------------------')
    print(line) 
    print('********** Pet Care Meds  **********')
    print('********** Vaccine Prices **********')
    print(line)
    print('Dog Vaccines     Total  $' + format( vax_cost, moneyformat ))
    print('Heart Worm Chews Total  $' + format( pr_chews, moneyformat ))
    print(line)
    print('Sales Tax           $' + format( SALES_TAX, moneyformat))
    print('Total               $' + format( total, moneyformat ))
    print(str(datetime.datetime.now()))
    









##################### CAT functions ########################
def get_cat_data():
    global  pet_vax, num_chews, cat_menu, pr_chews
    cat1 = "\n** Cat Vaccines: \n\t1.Feline Leukemia: $35.00 \n\t2.Feline Viral Rhinotracheitis: $30.00 \n\t3.Rabies (One Year): $25.00 \n\t4.Full Vaccine Package: Includes all vaccines with a 10% discount"
    cat_menu = cat1
    pet_vax = int(input(cat_menu + "\n** Enter Vaccine Number: "))
    



    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " for only $8.00 (Y/N?) ")
    if heart_yesno.upper()=="Y":
        pr_chews = PR_CAT_CHEWS
        



def perform_cat_calculations():
    global vax_cost, chews_cost, total, pr_chews

    ######## vaccines
    if pet_vax == 1:
        vax_cost = PR_LEUK
        
    elif pet_vax == 2:
        vax_cost = PR_RHINO

    elif pet_vax == 3:
        vax_cost = PR_CAT_RABI

    else:
         PR_ALL = PR_LEUK + PR_RHINO + PR_CAT_RABI
         vax_cost = .90 * PR_ALL




   

    ##### FIND TOTAL
    total = vax_cost + pr_chews
   
    



def display_cat_results():
    moneyformat = '8,.2f'
    line = ('-----------------------------------------')
    print(line) 
    print('********** Pet Care Meds  **********')
    print('********** Vaccine Prices **********')
    print(line)
    print('Cat Vaccines     Total  $' + format( vax_cost, moneyformat ))
    print('Heart Worm Chews Total  $' + format( PR_CAT_CHEWS, moneyformat ))
    print(line)
    print('Sales Tax           $' + format( SALES_TAX, moneyformat))
    print('Total               $' + format( total, moneyformat ))
    print(str(datetime.datetime.now()))
    

##################### Call on main program ########################

main()










    
    
    

