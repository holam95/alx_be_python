from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_datetime)


display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)


calculate_future_date()

