import pandas as pd

# Example set and list
roll_no = [1, 2, 3, 4]
names = ['A', 'B', 'F', 'Z']
dob = ['2004-04-08', '2001-04-025', '2005-02-03', '2007-01-29']
yos = [1, 3, 2, 4]

mapping = {} # CREATING AN EMPTY DICTIONARY TO STORE THE MAPPED ELEMENTS

# ITERATING THROUGH ALL ELEMENTS IN ALL LISTS TO MAP THE DATA
for i in range(len(roll_no)): 
    mapping[roll_no[i]] = {'Names': names[i], 'DOB': dob[i], 'YOS': yos[i]}    

# MAPPED DATA IS GETTING STORED IN THE DICTIONARY 
s = pd.DataFrame.from_dict(mapping, orient='index')

# DISPLAYING THE DATA AND AFTER SORTING 
s = s.sort_index(ascending=False) 
print(s)
s = s.sort_values(by='Names')
print(s)
s = s.sort_values(by='DOB')
print(s)
s = s.sort_values(by='YOS')
print(s)


