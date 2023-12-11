######## Name: NyJavion Timberlake
######## Program Purpose: Web page for hotel resort

import datetime

#       S-TAX  OCC-TAX
#         0      1
TAXES = (0.065, 0.1125)


#       SR    DR   SU 
#        0     1    2
RATES = (195, 250, 350) 


## HTML File
outfile = 'hotelsalesrep.html'


guest = []

def main():
    readin_custfile()
    perform_calc()
    open_outfile()
    create_outfile()
    

def readin_custfile():
    guest_data = open('emerald.csv', 'r')
    guest_in = guest_data.readlines()
    guest_data.close()

    ## Spliting data & insert into list called 'guest'
    for i in guest_in:
        guest.append(i.split(','))


    
def perform_calc():
    global grand_total, subtotal, sales_tax, occupancy, total
    grand_total = 0
    
    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])
                        

        if room_type == "SR":
            subtotal = num_nights * RATES[0]
            #print(subtotal)

        elif room_type == "DR":
            subtotal = num_nights * RATES[1] 

        else:
            subtotal = num_nights * RATES[2] 
            
        sales_tax = subtotal * TAXES[0]
        occupancy = subtotal * TAXES[1]
        total = subtotal + sales_tax + occupancy
        grand_total += total

        

        guest[i].append(subtotal)
        guest[i].append(sales_tax)
        guest[i].append(occupancy)
        guest[i].append(total)

     
def open_outfile():
    global f
    
    
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort <br /></title>\n')
    f.write('<style> td{text-align: center} ; h2{text-align: center} ; </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(hotel3.png) ; color: #2A411f ;">\n')
    

    
def create_outfile():
    global f 
    
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    tab = '\t'
    th = '<th>'
    endth = '</th>'

    f.write('\n<table border="8" ; style ="background-color: #DEC87D ;font-family: arial; margin: auto;">\n')
    f.write('<tr><td colspan = 8>\n <h2><br> Emerald Beach Hotel & Resort Guest Report <h2></td></tr>')
    f.write('<tr><td colspan = 8><h3><br> Guest Sales Report </h3> ' + str(day_time) + endtr )
    #f.write('<tr><td colspan = 8><h3> Guest Sales Report </h3> </td></tr>')
    #f.write('<tr><td colspan = 8> Date/Time: ' + str(day_time) + endtr)
    

    f.write(tr) 
    table1 = (' Last Name </td>'  + '<td> First Name </td>'  + '<td> Room Type </td>' + '<td> Num Nights </td>' )
    table2 = ('<td> Subtotal </td>'  + '<td> Sales Tax </td>'  + '<td> Occupancy Tax </td>'  + '<td> Total </td>')
    alltables = (table1 + table2)
    f.write(alltables)
    f.write(endtr) 
    
    for i in range(len(guest)):

        
        f.write(tr) 
        data1 = guest[i][0] + endtd + guest[i][1] + endtd + guest[i][2] + endtd + guest[i][3] + endtd + format(guest[i][4], currency) + endtd
        data2 = format(guest[i][5], currency) + endtd + format(guest[i][6], currency) + endtd + format(guest[i][7], currency) + endtr
        alldata = data1 + data2
        f.write(alldata)
        

              

    f.write('<tr><td colspan = 7> Grand Total: </td><td>' + format(grand_total, currency) + endtr)
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()
    print('\n** Sales Report for Resort! Open this file to see your report: ' + outfile)



    
        
        
        #f.write(tr)
        #f.write(tr + 'Last' + endtd + cust[i][0] + endtr)
        #f.write(tr + 'First' + endtd +  cust[i][1] + endtr)
        #f.write(tr + 'Num Nights' + endtd + cust[i][3] + endtr)
        #f.write(tr + 'Subtotal' + endtd + format(subtotal, currency) + endtr)
        #f.write(tr + 'Sales Tax' + endtd + format(sales_tax, currency) + endtr)
        #f.write(tr + 'Occ. Tax' + endtd + format(occ_tax, currency) + endtr)
        #f.write(tr + 'Total' + endtd + format(total, currency) + endtr)
        #f.write(endtd + endtr)
    

            
    
   

        
   

main() 
