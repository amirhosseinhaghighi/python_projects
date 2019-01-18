
from datetime import datetime





current_month = datetime.now().strftime('%m') # 02 //This is 0 padded

# current_month_text = datetime.now().strftime('%h') # Feb
# current_month_text = datetime.now().strftime('%B') # February
# current_day = datetime.now().strftime('%d')   # 23 //This is also padded
# current_day_text = datetime.now().strftime('%a')  # Fri
# current_day_full_text = datetime.now().strftime('%A')  # Friday

# current_weekday_day_of_today = datetime.now().strftime('%w') #5  Where 0 is Sunday and 6 is Saturday.

current_year_full = datetime.now().strftime('%Y')  # 2018
# current_year_short = datetime.now().strftime('%y')  # 18 without century

# current_second= datetime.now().strftime('%S') #53
# current_minute = datetime.now().strftime('%M') #38 
# current_hour = datetime.now().strftime('%H') #16 like 4pm
# current_hour = datetime.now().strftime('%I') # 04 pm

# current_hour_am_pm = datetime.now().strftime('%p') # 4 pm

# current_microseconds = datetime.now().strftime('%f') # 623596 Rarely we need.

# current_timzone = datetime.now().strftime('%Z') # UTC, EST, CST etc. (empty string if the object is naive).




currentdate = current_year_full + current_month

password = input("Please Enter Your Username:\n>>").upper()
password = "["+ password + currentdate + "@123" + "]"

print(password)