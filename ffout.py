

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

############## NEW LISTS for calculated amounts ############

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0 

############## TUPLES OF CONSTANT ############
#             C       S      J     M 
# indexs      0       1      2     3
PAY_RATE = ( 16.50, 15.75, 15.75, 19.50 )


#          FED   STATE  SS    MED   RET
#index      0     1     2      3    4
DEB_RATE = (.12, .03, .062, .0145, .04 ) 




############## DEF MAIN PRORGAM ##############

def main():
    perform_calc()
    create_output_file()




def perform_calc():
    global total_gross, total_net

    for i in range(num_emps):

        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]


        ############ CALC DEDUCTIONS 
        fed = pay * DEB_RATE[0]
        state = pay * DEB_RATE[1]
        social = pay * DEB_RATE[2]
        medi_care = pay * DEB_RATE[3]
        retire = pay * DEB_RATE[4]

        
        net = pay - fed - state - social - medi_care - retire
        

        #add totals
        total_gross += pay
        total_net += net 

        #add amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(social)
        medicare.append(medi_care)
        ret401k.append(retire)
        net_pay.append(net)



def create_output_file():
    currency = '8,.2f'
    line = '\n-------------------------------------------------'
    tab = '\t'
   


    ################# Output file ###############
    out_file = 'payroll.txt'
    f = open(out_file, 'w')
    f.write(line)
    f.write('\n************** FRESH FOODS MARKET ***************')
    f.write('\n************** WEEKLY PAYROLL REPORT ************')
    f.write(line)
    f.write('\n' + tab + str(datetime.datetime.now()))
    f.write(line)
    titles1 = '\nEmp Name' + tab + '    ' + 'Code' + tab + tab + 'Gross' + tab + tab 
    titles2 = 'Fed Inc Tax' + tab  + tab + 'State Inc Tax' + tab + tab + "Soc Sec" + tab+ tab + "Medicare" + tab + tab + '401k' + tab + tab + "Net"
    alltitles = (titles1 + titles2)
    f.write(alltitles)
    ############# CREATE THE MISSING CODE TO F.WRITE OUT EMPLOYEE DATA, ONE LINE AT A TIME #####################

    for i in range (num_emps):
        data1 = '\n' + emp[i] + '     ' + job[i] + tab + tab + '      ' + format(gross_pay[i], currency)  + tab  + tab + format(fed_tax[i], currency) + tab + tab
        data2 = format(state_tax[i], currency) + tab + '      ' + format(soc_sec[i], currency) + tab + '      ' + format(medicare[i], currency) + tab + tab
        data3 = data3 = "     " + format(ret401k[i], currency) + tab + '    ' + format(net_pay[i], currency)
        f.write(data1 + data2 + data3)
    f.write(line)    
    f.write('\n************** Total Gross: $' + format(total_gross, currency))
    f.write('\n************** Total  Net : $' + format(total_net, currency))
    f.write(line)
    
    f.close()
    print("Open " + out_file + " to view your report")
    


            
            
main()  
