import pandas as pd
import Customer

""" Program reads data from excel sheet, puts them in a txt file then compares them with a new file containing all known
customers in the database. if a customers name does not appear in the database it will be kept in the array the array
is then written to a txt file. this helps speed up the data entry process by hours and allows for customers to not be
missed.

results of the program showed that there were old customers that were never entered due to human error.

program will be updated to showcase some analysis of the data

author - Rafael Rubenstein 
"""

# reads customer data from a txt file and returns and array with customer objects
def read_Customer_data(file_name):
    arr = []
    with open(file_name, 'r') as cust:
        line = cust.readline()
        while line != "":
            customer = line.rstrip('\n').split(',')
            if len(customer) == 2:
                customer = Customer.Customer(customer[0], customer[1])
                arr.append(customer)
            else:
                customer = Customer.Customer(customer[0])
                arr.append(customer)
            line = cust.readline()
        return arr


# writes cutomer data from excel to a txt file in the same format as the new customers txt file
def write_customer_data_from_excel(file_name):
    with open(file_name, "w") as ex:
        for i in range(len(df)):
            firstName = str(df.iloc[i, 0]).rstrip()
            lastName = str(df.iloc[i, 1])
            ex.write(lastName + ", " + firstName + "\n")


# writes the customers that were not found in the excel sheet allowing for faster data entry
def write_customer_notIn(file_name, array):
    with open(file_name, "w") as notin:
        for i in range(len(array)):
            firstName = array[i].get_first_name()
            lastName = array[i].get_last_name()
            if firstName is None:
                notin.write(lastName + "\n")
            else:
                notin.write(lastName + "," + firstName + "\n")


"""O(n^2) time for now. compares the customers in excel to all customers in database. if customer name is in excel it 
pops it from the array """


def compare_excel_new(excel_arr, newcustomer_arr):
    for index_ex in range(len(excel_arr)):
        for index in range(len(newcustomer_arr)-1):
            if new_customers[index].equals(excel_customers[index_ex]):
                new_customers.pop(index)


# reads excel to pandas df, renames columns, and drops columns with no names in it
df = pd.read_excel("ABSOLUTE CUSTOMERS LIST.xlsx")
df.rename(columns={"FIRST NAME": "first name", "LAST NAME ": "last name"}, inplace=True)
df.dropna(subset=["first name"], inplace=True)

# reads the new customers into an array
new_customers = read_Customer_data("customers.txt")
# reads the excel customers into an array
excel_customers = read_Customer_data("customerinexcel.txt")

# compare excel customers to new and removes customers found in excel
compare_excel_new(excel_customers, new_customers)

# add menu driven program so program can be used by all
