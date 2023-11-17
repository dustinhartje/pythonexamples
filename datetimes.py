from datetime import datetime as dt

# Get a datetime object representing now
now = dt.now()
print(f"now = {now}")
print(type(now))

# ...as a string
now_as_str = dt.now().strftime('%m/%d/%Y %H:%M:%S')
print(f"now_as_str = {now_as_str}")
print(type(now_as_str))

# Get a datetime object from a string
some_day_time = dt.strptime('12/21/1962 01:42:57', '%m/%d/%Y %H:%M:%S')
print(f"some_day_time = {some_day_time}")
print(type(some_day_time))

# get a Date only object from a datetime
some_day = some_day_time.date()
print(f"some_day = {some_day}")
print(type(some_day))
some_time = some_day_time.time()
print(f"some_time = {some_time}")
print(type(some_time))



# need some datetime delta stuff here
