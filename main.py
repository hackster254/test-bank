import csv

from sqlalchemy import null

outfile = open('edited.csv', 'w')

with open("Input Text.txt", 'r') as infile:
    reader = csv.reader(infile, delimiter=":",)
    #print(reader)


    for row in reader:
        #print(row[2])
        list2 = row[2]
        #use row[2] as check
        
  
        if(row[0]=='TRANSFER'): #means its a transfer
            # ken = []
            # row = ken
            # print(ken[1:3])
            primary2 = row[1]
            secondary2= row[2]
            amount2= row[3]
            line ="{},{},{},{}\n".format('TRANSFER',row[1],row[2],row[3])
            outfile.write(line) 


            # print(list2 + 'mylist')
            # if(type(list2 == str)):
            #     for ele in list2:
            #         amount2 = ele
            #         print(row[2])
            #         print('transfer')
            #         line = "{},{},{},{}\n".format('hello','world','please',ele)
        elif(type((row[2]) == int)): #means its a withdraw or deposit
            #print(row[0])
            amount= row[2]
            transaction = row[0]
            secondary=" "
            primary = row[1]
            line ="{},{},{},{}\n".format(transaction,primary,secondary,amount)
            # outfile.write()
            outfile.write(line)   
            



        # if row[0] == 'Deposit' or 'Withdraw':
        #     transaction = row[0]
        #     primary = row[1]
        #     secondary = ''
        #     amount = row[2]
        #     line ="{},{},{},{}\n".format(transaction,primary,secondary,amount)
        #     outfile.write(line) 
        
        # elif row[0] == 'Transfer':
        #     transaction2 = row[0]
        #     primary2 = row[1]
        #     secondary2 = row[3]
        #     amount2 = row[4]
        #     line2 ="{},{},{},{}\n".format(transaction2,primary2,secondary2, amount2)
        #     outfile.write(line2) 
    outfile.close()

        

def read_input_file():
    with open(r'edited.csv')as f:
        reader = csv.DictReader(f)

        return reader

