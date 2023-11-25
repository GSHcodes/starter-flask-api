from datetime import datetime
from forex_python.converter import CurrencyRates
currency = CurrencyRates()
# currency coverting code.
def convert_currency(source_currency, amount_source, to_currency):
    converted = currency.convert(source_currency, to_currency, amount_source)
    return round(converted, 2)
#age calculating code
def calculate_age(dob_str):
    # Convert DOB string to a datetime object
    dob = datetime.strptime(dob_str, '%Y-%m-%d')

    # Get the current date
    current_date = datetime.now()

    # Handling future dates
    if dob > current_date:
        return "Invalid date of birth (DOB is in the future)"

    # Calculate the difference between current date and DOB
    years_difference = current_date.year - dob.year
    months_difference = current_date.month - dob.month
    days_difference = current_date.day - dob.day

    # Adjust for negative months or days
    if months_difference < 0 or (months_difference == 0 and days_difference < 0):
        years_difference -= 1
        months_difference = 12 + months_difference

        # Adjust for negative days
        if days_difference < 0:
            months_difference -= 1
            # Calculate the days in the month for the DOB
            days_in_dob_month = (dob.replace(year=current_date.year, month=dob.month + 1, day=1) - dob).days
            days_difference = days_in_dob_month + days_difference
    if(years_difference==0):
        if(months_difference==0):
            return f"Your age is {days_difference} days"
        else:
            return f"Your age is:  {months_difference} month/s, and {days_difference} days"
    else:
        if (months_difference == 0):
            return f"Your age is: {years_difference} years, {days_difference} days"
        else:
            return   f"Your age is: {years_difference} years,{months_difference} months, and {days_difference} days"
