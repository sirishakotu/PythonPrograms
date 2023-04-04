'''
1 day = 24 hours
1 day = 24 * 60 =  1440 minutes
One year = 365 * 24 = 8760 hours
One year = 365 * 1440 = 525600 minutes
1 hour = 3600 seconds
8760 * 3600 = 31536000
Convert age into seconds,hours,minutes

'''
age = float(input("Enter your age:"))
age_seconds = age * 31536000
print("Your age is:",str(age))
print("Your age in seconds:",str(age_seconds))
age_hours = age * 8760
age_minutes = age * 525600
print("Your age in hours:",str(age_hours))
print("Your age in minutes:",str(age_minutes))