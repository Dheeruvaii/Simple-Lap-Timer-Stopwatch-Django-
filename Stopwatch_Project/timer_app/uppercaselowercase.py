str1 = 'stechies.com'
print(str1.upper())

# Initialize a string with uppercase & lowercase characters 
str1 = 'StecHIes.com'
print(str1.lower())




str1 = 'STECHIES'
str2 = 'SteChies'

# Compare string without using upper() function
if(str1 == str2):
    print(str1,'and ',str2,' are same')
else:
    print(str1,'and ',str2,' are not same')
    
# Compare string with upper() function
if(str1.upper() == str2.upper()):
    print(str1,'and ',str2,' are same')
else:
    print(str1,'and ',str2,' are not same')