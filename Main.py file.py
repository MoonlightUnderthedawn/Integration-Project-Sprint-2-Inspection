#Nathaniel Lee Powell
#A clcualtor that slpit up your profit from some taxes to see what you have left in total
print("Hello this is a clcualtor that helps you see how much money you have after taxes in the USA.")
print(" ")
#allow to read and understand what step you are in the clcualor when the progarm is running

print("Some warning to know before the use of the clcualtor")
print("This caulator is simple you need to put all the tax and income for it to work.")
#A warning sp the peron knpw tha they will need to put all the info in here
print("You will only need to put in numbers. don't added any commas(,) or anything else then numbers.")
#Another warning so people only put numbers to not cause a error
print("Last warning is you need to put a number unless tell to not too.")
#If they not put a number in the floatinput then it cause a error so teiing before hand left it to not happen


def  Calculate_Total_income_tax(num1,num2,num3):
    Total_income_tax = num1 + num2 + num3
    return Total_income_tax
    # Not added in one yet so it aded to make a total numeric operators

def  Calculate_FICA_Tax(num1,num2,num3):
    FICA_Tax = num1 + num2 + num3
    return FICA_Tax
    #them addeding up for the total FICA tax number numeric operators


def  Calculate_Total_Tax(num1,num2,num3):
    Total_Tax = num1 + num2 + num3
    return Total_Tax
    #Need to add all to make it easy to put divde the income numeric operators
def  Calculate_The_percentage_of_Total_Tax(num1):
    The_percentage_of_Total_Tax = num1 / 100
    return The_percentage_of_Total_Tax
    #there is not in the % yet so must change that by divding numeric operators
def  Calculate_Money_that_is_left(num1,num2):
    Money_that_is_left = num1 * num2
    return Money_that_is_left
    #The part where the tax is remove from income by timesing numeric operators
def  Calculate_Amount_of_tax_take(num1,num2):
    Amount_of_tax_take = num1 - num2
    return Amount_of_tax_take

keep_going = 0
while keep_going <= 0:
    keep_going_part2 = False
    while not keep_going_part2 == True:

        print(" ")
        Year_income = float(input("Frist put up your income you make in a year " + "$" ))
        #With no income vaule then it will not work and use a string operator of + to added the dollar sign to the number
        print(" ")
        
        print("Now put the income tax that you have. If you don't have it just press enter")
        print(" ")
        #There are Three income tax
        Federal_income_tax = float(input("Your federal income tax rate: "))
        #It Can change so left it to the person to put it and allows it to be use for years
        State_income_tax = float(input("Your state income tax rate: "))
        #There are 50 states that have a different tax rate
        Local_income_tax = float(input("Your local income tax rate: "))
        #Some citys have there own tax rate
        Total_income_tax = Calculate_Total_income_tax(Federal_income_tax,State_income_tax,Local_income_tax)

        print(" ")
        print("Put your FICA Tax numbers into here")
        #FICA Tax is the total of social security and medicare
        Social_Security_tax = float(input("Put your Social Security tax number: "))
        #may change have them added it
        Medicare_Tax = float(input("Put your medicare Tax number: "))
        #may change hhave them added it
        Additional_medicare_tax = float(input("Add the additional medicare tax if you have one: "))
        #If your income is very high you need to pay more medicar tax and feels easy to put it this way
        FICA_Tax = Calculate_FICA_Tax(Medicare_Tax,Social_Security_tax,Additional_medicare_tax)
        
        print(" ")
        print("if you have a property then put a number if not just put a 0.")
        #Some people ave a property while others rent(will add a rent part next time)
        Property_Tax = float(input("The property tax that you have: " ))
        #The tax may be different or change so have them put it
        print(" ")
        
        print("Bellow this will show the vaules you input.")
        print("Press enter if the info is correct to what you put.")
        print(" ")
        print("Your year income")
        print(Year_income)
        print("Your total income tax")
        print(Total_income_tax)
        print("Your FICA tax")
        print(FICA_Tax)
        print("Your Property tax")
        print(Property_Tax)
        Enter_is_corrct = input("If correct then type 'Yes' or if you want to stop the progarm type 'Stop' or type anything else to restart to the beging.")
        #Allow them to see what they put and restart it if is there anything worng
        print(" ")
        if Enter_is_corrct == 'Yes':
            keep_going_part2 = True
            print("Now starting to calculate")
        elif Enter_is_corrct == 'Stop':
            keep_going_part2 = True
            keep_going += 1
        else:
            print("restarting to the beging")
            
    if keep_going <= 0:
        for x in range (10, -1, -1):   
            print(x)



        
        Total_Tax = Calculate_Total_Tax(Total_income_tax,FICA_Tax,Property_Tax)
        
        The_percentage_of_Total_Tax = Calculate_The_percentage_of_Total_Tax(Total_Tax) 
        
        Money_that_is_left = Calculate_Money_that_is_left(The_percentage_of_Total_Tax,Year_income)
        
        Amount_of_tax_take = Calculate_Amount_of_tax_take(Year_income,Money_that_is_left)
        
        print("This is the money left")
        print(Money_that_is_left)
        print("This is he amount the tax take")
        print(Amount_of_tax_take)
        print("This is the amount of tax you have in percentage")
        print(Total_Tax)
        #Fully lay it out the info
        
        print(" ")
        print("Thank you for using this calutor for some tax's.")
        keep_going_part3 = True
        while keep_going_part3 == True:
            To_restart = input("If you want to restart the calutor then say 'Yes' if not say 'No'")
            if To_restart == 'Yes' or To_restart == 'No':
                keep_going_part3 = False
            elif To_restart != 'Yes' and To_restart != 'No':
                print("worng input try again")
        if To_restart == 'Yes':
            print("Restarting")
        else:
            keep_going += 1

print("Progarm stoping")
        
                    
    


















                        
