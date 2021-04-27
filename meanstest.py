# David Cabrera
# CS 021
# Final project

# This program performs a two tailed t test for comparing the means of two data sets when the population
# standard deviation is unknown. The data is collected by asking the user to enter it.

import statistics
import math

def main():

    # Collect data from user and make each value its own separate item in the list
    x_values = input("Enter the integer values for the x group: ")
    x_values = x_values.split()


    y_values = input("Enter the integer values for the y group: ")
    y_values = y_values.split()

    # Pass the integer lists into the main function and input validation
    try:
        x_values_int = x_vals_str_to_int(x_values)
    except ValueError:
        print('You cannot have letters or punctuation in your x values. They must all be integers.')
        x_values = input("Enter the integer values for the x group: ")
        x_values = x_values.split()
        
    try:
        y_values_int = y_vals_str_to_int(y_values)
    except ValueError:
        print('You cannot have letters or punctuation in your y values. They must all be integers.')   
        y_values = input("Enter the integer values for the y group: ")
        y_values = y_values.split()

    # Print null and alternative hypotheses
    print('Null hypothesis: The means of groups x and y are the same.')
    print('Alternative hypothesis: The means of groups x and y are not the same.')

    # Print means of x group and y group
    try:
        x_mean = calculate_x_mean(x_values_int)
        print('Mean of group x: ', format(x_mean, ',.2f'))
    except UnboundLocalError:
        print('You cannot have letters or punctuation in your x values. They must all be integers.')

    try:
        y_mean = calculate_y_mean(y_values_int)
        print('Mean of group y: ', format(y_mean, '.2f'))
    except UnboundLocalError:
        print('You cannot have letters or punctuation in your y values. They must all be integers.')
    

    # Calculate the difference of the means of both groups and take the absolute value of it.
    means_diff = x_mean - y_mean
    means_diff = abs(means_diff)
        
    print('Difference of means: ', format(means_diff, ',.2f'))

    # Pass degrees of freedom to main function and print them
    degrees_of_freedom = calculate_df(x_values_int, y_values_int)
    print('Degrees of freedom: ', degrees_of_freedom)

    # Use statistics module to calculate variances of x and y groups so the standard error and test statistic
    # can be calculated.
    x_var = statistics.variance(x_values_int)
    y_var = statistics.variance(y_values_int)

    # Pass test statistic into main function and print it
    test_statistic = calculate_test_statistic(x_values_int, y_values_int, x_mean, y_mean, x_var, y_var, means_diff)
    print('Test statistic: ', format(test_statistic, '.4f'))

    # Ask user to enter critical value from t distribution table
    critical_value = float(input('Enter the critical value from the t distribution table, using degrees of freedom and significance level (usually 0.05): '))

    # Print possible results of the test using if else statements
    if critical_value < test_statistic:
        print('Reject the null hypothesis. There is evidence of a difference between the two means.')
    else:
        print('Fail to reject the null hypothesis. The means are the same.')

# This function takes each item in the list of data for the x group and converts it from a string to an integer
# and returns the new list
def x_vals_str_to_int(x_values):

    i = 0
    for item in x_values:
        x_values[i] = int(x_values[i])
        i += 1
    return x_values

# This function does the same as the one above, but for the y group
def y_vals_str_to_int(y_values):

    i = 0
    for item in y_values:
        y_values[i] = int(y_values[i])
        i += 1
    return y_values

# This function uses a loop to calculate the mean of the data in the x group, then returns the value
def calculate_x_mean(x_values_int):

    x_values_sum = 0
    for item in x_values_int:
        x_values_sum += item

    x_values_mean = x_values_sum / len(x_values_int)
    return x_values_mean

# This function calculates the mean of the data in the y group and returns it
def calculate_y_mean(y_values_int):
    y_values_sum = 0
    for item in y_values_int:
        y_values_sum += item

    y_values_mean = y_values_sum / len(y_values_int)
    return y_values_mean

# This function calculates and returns the degrees of freedom used for the test. Degrees of freedom are the
# smaller sample size minus 1
def calculate_df(x_values_int, y_values_int):
    if len(x_values_int) < len(y_values_int):
        df =  len(x_values_int) - 1
    elif len(x_values_int) > len(y_values_int):
        df = len(y_values_int) - 1
    elif len(x_values_int) == len(y_values_int):
        df = len(x_values_int) - 1

    return df

# This function calculates the standard error and test statistic for the t test. The test statistic is returned.
def calculate_test_statistic(x_values_int, y_values_int, x_mean, y_mean, x_var, y_var, means_diff):
    n_x = len(x_values_int)
    n_y = len(y_values_int)

    se = math.sqrt((x_var/n_x)+(y_var/n_y))

    test_statistic = means_diff / se
    return test_statistic

# Call main
main()
