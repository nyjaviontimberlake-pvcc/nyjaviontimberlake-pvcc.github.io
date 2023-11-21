




import datetime

################# define global variables #####################

PP_TAX = .042
TAX_RELIEF = .33
#NON_TR = 0 

################# create list #####################

vehicle = ["2019 Volvo " ,
           "2018 Toyota" ,
           "2022 Kia   " ,
           "2020 Ford  " ,
           "2023 Honda " ,
           "2019 Lexus " ,]


vehicle_val = [13000, 10200, 17000, 21000, 28000, 16700]


pptr_elg = [ "Y", "Y", "N", "Y", "N", "Y", ]


owner_name = ["Brand, Debra       ",
              "Smith, Carter      ",
              "Johnson, Bradley   ",
              "Garcia, Jennifer   ",
              "Henderson, Leticia ",
              "White, Danielle    " ,]

ppt_owed = []

num_vehicles = len(vehicle)

tax_due = 0
total = 0



################# define program #####################

def main():
    perform_calculations()
    display_results()


def perform_calculations():
    global total

    for i in range(num_vehicles):
        
        tax_due = (vehicle_val[i] * PP_TAX / 2)

        if pptr_elg[i].upper() == "Y":
            tax_due = tax_due * (1-TAX_RELIEF)


        ppt_owed.append(tax_due)
                   
        total += tax_due

        





def display_results():
    moneyf  = '8,.2f'
    line = ('----------------------------------------------------------------------------------------')
    tab = '\t'
    
    print (line)
    print ('********************* PERSONAL PROPERTY TAX REPORT *********************')
    print ('                        Charlottesville, Virginia ')
    print ('\n\t\tRUN DATE/TIME: ' + str(datetime.datetime.now()))

    
    print ('\nName' + tab + tab + tab + " " + 'VEHICLE' + tab + tab + "  " + 'VALUE'  + tab + tab + 'RELIEF' + tab + tab + 'TAX DUE')
    print (line)

    for i in range(num_vehicles):
        dataline1 = owner_name[i] + tab + vehicle[i] + tab + tab + '$' + format(vehicle_val[i], moneyf) + tab
        dataline2 = "  " + pptr_elg[i] + tab + '      ' + '$' + format(ppt_owed[i], moneyf) 
        print(dataline1 + dataline2) 

    print(line)
    print('************************************************************ TOTAL TAX DUE:    $' + format(total,moneyf))



main()
