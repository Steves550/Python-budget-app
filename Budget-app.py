
# Prompt the user for their total monthly net income and for the total amount in bills they pay each month. Store each value in two separate variables.
total_income = float(input("Enter your total monthly net income.\n"))
total_bills = float(input("What is the total amount per month that you pay for bills? (car payment, mortgage, utilities etc)\n"))

# Subtract total income by total monthly bills and store in a variable. Display a message showing the user how much income they have for the month after paying all bills.
available_income = total_income - total_bills
print("After paying all of your monthly bills you have", available_income, "leftover for the month.\n")

# Prompt the user for their dining, entertainment, and clothes expenses for the month and store each value into three seperate variabels.
dining_expense = float(input("Through out the month how much do you usually spend on going out to eat?\n"))
entertainment_expense = float(input("How much do you spend a month on entertainment? (movies, games, streaming services ect) \n"))
clothes_expense = float(input("How much do you typically spend on clothes each month?\n"))
total_expenses = dining_expense + entertainment_expense + clothes_expense

# Create a function that includes if and elif statements that use the max() function to look for the highest number value entered between the three expense variables.
# Display a message for each possibility of max between the three expense variables. Show the user what their maximum expense is by name.
def highest_expense():
    if max(dining_expense, entertainment_expense, clothes_expense) == dining_expense:
        return "Your highest expense each month is on dining"
    elif max(dining_expense, entertainment_expense, clothes_expense) == entertainment_expense:
        return "Your highest expense each month is for entertainment"
    elif max(dining_expense, entertainment_expense, clothes_expense) == clothes_expense:
        return "Your highest expense each month is for clothes"
         
# Create a function that includes if and elif statements that use the min() function to look for the lowest number value entered between the three expense variables.
# Display a message for each possibility of min between the three expense variables. Show the user what their minimum expense is by name.
def lowest_expense():
    if min(dining_expense, entertainment_expense, clothes_expense) == dining_expense:
        return "your lowest expense each month is on dining."
    elif min(dining_expense, entertainment_expense, clothes_expense) == entertainment_expense:
        return "your lowest expense each month is for entertainment."
    elif min(dining_expense, entertainment_expense, clothes_expense) == clothes_expense:
        return "your lowest expense each month is for clothes."

# store each result from the highest and lowest expense functions into two seperate variables.
most_expensive = highest_expense()
least_expensive = lowest_expense()

# Subtract the value from total net income by the totals for bills and expenses and store in a variable.
free_income = total_income - total_bills - total_expenses

# Display a message telling the user what their maximum and minimum expenses are. show them how much free money they have after all bills and expenses are taken into account.
print(most_expensive, "and" , least_expensive, "After all of your bills and expenses are paid for you have", free_income, "left over from your monthly income of", total_income)
