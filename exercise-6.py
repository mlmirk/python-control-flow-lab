# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
winter=('jan','feb','mar')
spring=('apr','may','jun')
summer=('jul','aug','sep')
fall=('oct','nov','dec')

user_input_month = input("Enter a month in a three letter abbreviation[jan,feb,mar] ").lower()
user_input_day = int(input("enter a day in the month "))
day=user_input_day
if user_input_month in winter:
  if user_input_month == 'mar' and user_input_day>19:
    print(f'{user_input_month} {user_input_day} is in spring ')
  else:
    print(f'{user_input_month} {user_input_day} is in winter ')
elif user_input_month in spring:
  if user_input_month == 'jun' and user_input_day>20:
    print(f'{user_input_month} {user_input_day} is in summer ')
  else:
    print(f'{user_input_month} {user_input_day} is in spring ')
elif user_input_month in summer:
  if user_input_month == 'sep' and user_input_day>21:
    print(f'{user_input_month} {user_input_day} is in fall ')
  else:
    print(f'{user_input_month} {user_input_day} is in summer ')
elif user_input_month in fall:
  if user_input_month == 'dec' and user_input_day>20:
    print(f'{user_input_month} {user_input_day} is in winter ')
  else:
    print(f'{user_input_month} {user_input_day} is in fall ')
else:
  print(f'I dont think {user_input_month} and {user_input_day} followed the correct format')
