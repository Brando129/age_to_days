# Create a function that takes the age in years and returns the age in days.

def years_to_days(years):
    days = years * 365
    return f"{years} years is {days} days "

print(years_to_days(2))