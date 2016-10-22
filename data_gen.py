#Program that generates randomised sample data to standard output
#To be redirected in the command line to a csv file

import random

#Treat fields as objects with field name and random data output
class gender():
    name="Gender"
    def getData():
        return random.choice(['Male', 'Female'])

class age():
    name="Age"
    def getData():
        return str(random.randint(10, 85))

class height():
    name="Height"
    def getData():
        return "{0:.2f}".format(random.uniform(1.5, 2.0))

#Start of program
#Determine number of records
num_records=10

#Add the fields into list in required order
fields=[]
fields.append(gender)
fields.append(age)
fields.append(height)

#Output header
print(', '.join(map((lambda x:x.name), fields)))

#loop through the required number of records
for i in range(num_records):
    #generate data, join with comma and output
    print(', '.join(map((lambda x:x.getData()), fields))) 
