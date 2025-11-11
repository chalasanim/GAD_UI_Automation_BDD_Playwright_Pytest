import pytest,csv
import logging,inspect
from typing import Optional

logger = logging.getLogger(__name__)

# usage of ispect meodule to get more details about functions
sig = inspect.signature(func)
print(func) # gets more details about function 

class GlobalVariables:
    Email: Optional[str] = ""    


def read_user_data_from_csv(file_path):
    with open(file_path,newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader :
        
            try:
            
              if all(field in row for field in ['first_name','last_name','email','password','dob','profile_image']):
                   return(
                       row['first_name'],
                       row['last_name'],
                       row['email'],
                       row['password'],
                       row['dob'],
                       row['profile_image']
                   )
            except ValueError as e:
                # logger.warning r logger.debug also can be included
                raise ValueError("Csv file must contain 'first_name','last_name','email','password','dob','profile_image' columns")

        
#read csv

first_name,last_name,email,password,dob,profile_image = read_user_data_from_csv('./data/user_data.csv')

            
#get python version
import sys
print (sys.version)

#get hostname
from socket import gethostname

print (gethostname())

#Get Hostname
import socket
print (socket.gethostname())




 