import os
import csv
import numpy as np
import pandas as pd

# Path to collect data from the Resources folder
Emp_data= "employee_data.csv"
Emp_data_df=pd.read_csv(Emp_data)

# varibles Emp ID,Name,DOB,SSN,State
name=Emp_data_df

#The `Name` column should be split into separate `First Name` and `Last Name` columns.x
new = name["Name"].str.split(" ", n = 1, expand = True) 
name["First Name"]= new[0] 
name["Last Name"]= new[1]  
name.drop(columns =["Name"], inplace = True) 

#The `DOB` data should be re-written into `MM/DD/YYYY` format.
