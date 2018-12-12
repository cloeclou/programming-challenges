#Author: Claudia (@cloeclou)
def days_in_month(mon):
    # (str) -> int
    # Returns the number of days of a given month in a non-leap year 
    # Prerequisite: capitalize the month and spell it properly
    #
    #>>> days_in_month('January')
    #31
    #>>> days_in_month('September')
    #30
    months =['January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December']
    num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dictionary = dict(zip(months, num_days))
    return dictionary[num]
