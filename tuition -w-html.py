#Name: Jay 
#PR



import datetime

#Define Tuition & Fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAP_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#Define Global Variables
inout = 1 # 1 means in-state, 2 meanas out of state
numcredits = 0
scholarshipamt = 0


###create output file 
outfile = 'tuition.html'


#################### Define Main Program ####################

def main():

    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        yesno = input("\nWould you like to calculate tuition and fees for another student? (Y/N?): ")
        if yesno == "n" or yesno == "N":
            more = False
            print('\n** Thank you for enrolling to PVCC! Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()
            
        


def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition <br /></title>\n')
    f.write('<style> td{text-align: right} ; h2{text-align: center} ; </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(pvcc.png) ; color: #ffffff;">\n')
    


def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for In-State; Enter a 2 for Out-of-State: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount recieved: "))



def perform_calculations():
    global tuition_cost, tuition_total, cap_fee, instuition_fee, activity_fee, total, balance
    if inout == 1 :
        tuition_cost = RATE_TUITION_IN
        cap_fee = 0

    else:
        tuition_cost = RATE_TUITION_OUT
        cap_fee = RATE_CAP_FEE * numcredits


    tuition_total = tuition_cost * numcredits
    instuition_fee = RATE_INSTITUTION_FEE * numcredits
    activity_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition_total + cap_fee + instuition_fee + activity_fee
    balance = total - scholarshipamt 


def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #0C589f ;font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 2>\n')
    f.write('<h2> PVCC Tuition</h2></td></tr>')
    f.write('<tr><td colspan = 2>\n')
    f.write('*** Tuition for Semester ***\n')
    
    f.write(tr + 'Tuition' + endtd + format(tuition_total,currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + format(cap_fee,currency) + endtr)
    f.write(tr + 'Institution Fee ' + endtd +  format(instuition_fee,currency)  + endtr)
    f.write(tr + 'Activity Fee ' + endtd +  format(activity_fee,currency)  + endtr)


    f.write(tr + 'Total ' + endtd + format(total,currency)  + endtr)     
    f.write(tr + 'Scholarship ' + endtd + format(scholarshipamt,currency) + endtr)
    f.write(tr + 'Total Balance' + endtd + format(balance,currency) + endtr)
    
    f.write('<tr><td colspan= "2">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table>')



main()

