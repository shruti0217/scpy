'''
Exercise - Processing CSV files using a dictionary of lists

We defined the functions read_csv and write_csv above to convert a CSV file into a list of dictionaries and vice versa. In this exercise, you'll transform the CSV data into a dictionary of lists instead, with one list for each column in the file.

For example, consider the following CSV file:

amount,duration,rate,down_payment
828400,120,0.11,100000
4633400,240,0.06,
42900,90,0.08,8900
983000,16,0.14,
15230,48,0.07,4300

We'll convert it into the following dictionary of lists:

{
  amount: [828400, 4633400, 42900, 983000, 15230],
  duration: []120, 240, 90, 16, 48],
  rate: [0.11, 0.06, 0.08, 0.14, 0.07],
  down_payment: [100000, 0, 8900, 0, 4300]
}

Complete the following tasks using the empty cells below:

    Download three CSV files to the folder data2 using the URLs listed in the code cell below, and verify the downloaded files.
    Define a function read_csv_columnar that reads a CSV file and returns a dictionary of lists in the format shown above.
    Define a function compute_emis that adds another key emi into the dictionary with a list of EMIs computed for each row of data.
    Define a function write_csv_columnar that writes the data from the dictionary of lists into a correctly formatted CSV file.
    Process all three downloaded files and write the results by creating new files in the directory data2.

Define helper functions wherever required.
'''
#2

def read_csv_columnar(path):
  with open(path, mode = 'r') as file_r:
    file_content = file_r.readlines()       #readlines will return an list of lines like this ['1,234,345\n','323,435,54'] 
    
    return file_content

#3    

def dic_con(file_content):
  dic = {}
  
  #creating a dictionary of given format :
  for i in conv_to_lis(file_content[0]):    #as first line in csv contains metadata
    dic[i] = []
  
  #filing the data :

  for i in file_content[1:]:                            #traverse through file content, i will have value of line 
    for val,key in zip(conv_to_lis(i),dic.keys()):  # val = [amount,dur,rate,downpay] and key = amount,dur,rate,downpay
      dic[key].append(0.0) if val == '' else dic[key].append(float(val)) # check if this throws error

  return dic

#4 
#4.1

import math

#copied from the given notebook
def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi

#4.2 
def new_dic(dic):
  dic['emi'] = []
  leng = len(dic['amount'])  #coz how else ????
  emi = 0
  for i in range(0,leng):
    emi = loan_emi(dic['amount'][i],dic['duration'][i],dic['rate'][i],dic['down_payment'][i])  
    dic['emi'].append(emi)
    
#5

def write_csv_columnar(path,dic):
  with open(path, mode = 'w') as file:
    file.write(f"amount,duration,rate,down_payment,emi\n")
    
    for i in range(0,len(dic['amount'])):
      file.write(f"{dic['amount'][i]},{dic['duration'][i]},{dic['rate'][i]},{dic['down_payment'][i]},{dic['emi'][i]}\n")
    
    

#function to convert file line into a list

def conv_to_lis(line):
  return line.strip().split(',')


import urllib.request

if __name__ == '__main__':
  #1. Download files 
  '''  
  url1 = ""
  url2 = ""
  url3 = ""

  urllib.request.urlretrieve(url,./file_1.txt)    #
  urllib.request.urlretrieve(url2,./file_2.txt)
  urllib.request.urlretrieve(url3,./file_3.txt)
  '''
  
  #2.Read files 
'''  
  file1_con = read_csv_columnar(./file_1)
  file2_con = read_csv_columnar(./file_2)
'''

file3_con = read_csv_columnar(r'data_sc.py/working_with_files/os_file_handle/loans.txt')

  #3. Convert Data to given format
'''  
  dic_1 = dic_con(file1_con)
  dic_2 = dic_con(file2_con)

'''  
dic_3 = dic_con(file3_con)



  #4. Compute and update data
    #4.1 compute emi 
    #4.2 fill emi
  
new_dic(dic_3)
print(dic_3)
  #5. Write the processed data in the result file in CSV format 
write_csv_columnar(r"data_sc.py/working_with_files/os_file_handle/new_loans.txt",dic_3)