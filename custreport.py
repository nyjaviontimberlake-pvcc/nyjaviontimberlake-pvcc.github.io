


cust = []


def main():
    read_in_cust_file()
    display_cust_list()
    
def read_in_cust_file():
    cust_data = open("data3.csv" , "r")
    cust_in = cust_data.readlines()
    cust_data.close()

    #split the data into fields
    for i in cust_in:
        cust.append(i.split(','))

def display_cust_list():
    total = 0
    fcurrency = '8,.2f'
    line = '----------------------------------------'

    print(line)
    print('****Customer Sales Report****')

    for i in range(len(cust)):
        amt_owed = float(cust[i][2]) * 1.10
        total += amt_owed
        print(cust[i][1] + '    \t' + cust[i][0] + '   \t' + format(amt_owed, fcurrency))

    print(line)
    print('******** Total Amount: \t$' + format(total, fcurrency))


main()
    
