#Nathaniel Lee Powell
#A calculator that split up your profit from some taxes to see what you have left in total.
print("Hello this is a clcualtor that helps you see how much money you have after taxes in the USA.")
print(" ")
#Allow to read and understand what step you are in the calculator when the progarm is running.

print("Some warning to know before the use of the calculator.")
print("This calculator is simple you need to put all the tax and income for it to work.")
#A warning sp the peron knpw tha they will need to put all the info in here.
print("You will only need to put in numbers. Don't added any commas(,) or anything else then numbers.")
#Another warning so people only put numbers to not cause a error.
print("Last warning is you need to put a number unless it tell you not too.")
#If they not put a number in the floatinput then it cause a error so teiing before hand left it to not happen.
#Also let them know there will be times they will put numbers.

#Next up here will define these calculation for each one and letts me keep doing them if I had to.
#While not needing to retype it all(Put it here to understand what is happening after this).
def Calculate_Total_income_tax(num1,num2,num3):
    Total_income_tax = num1 + num2 + num3
    return Total_income_tax
    #Not added in one yet so it aded to make a total numeric operators.

def Calculate_FICA_Tax(num1,num2,num3):
    FICA_Tax = num1 + num2 + num3
    return FICA_Tax
    #them addeding up for the total FICA tax number numeric operators.

def Calculate_Total_Tax(num1,num2,num3):
    Total_Tax = num1 + num2 + num3
    return Total_Tax
    #Need to add all to make it easy to put divde the income numeric operators.
    #Separate these so I can understand which one do what later on easier while they still do the dame thing.

def  Calculate_The_percentage_of_Total_Tax(num1):
    The_percentage_of_Total_Tax = num1 / 100
    return The_percentage_of_Total_Tax
    #There is not in the % yet so must change that by divding numeric operators.

def Calculate_Money_that_is_left(num1,num2):
    Money_that_is_left = num1 * num2
    return Money_that_is_left
    #The part where the tax is remove from income by timesing numeric operators.

def Calculate_Amount_of_tax_take(num1,num2):
    Amount_of_tax_take = num1 - num2
    return Amount_of_tax_take
    #Show you how much the tax had taken from you income.

def Calculate_How_many_Thousand(num1):
    How_many_thousand = num1 // 1000
    return How_many_thousand
    #Return how many thousands are in the money left over.

def Calculate_How_many_Hundred(num1):
    How_many_Hundred = num1 // 100
    return How_many_Hundred
    #Return how many hundreds are in the money left over.

def Calculate_How_many_Ten(num1):
    How_many_Ten = num1 // 10
    return How_many_Ten
    #Return how many tens are in the money left over.

def Calculate_Divide_Twelve_Months(num1):
    Divde_Twelve_Months = num1 /12
    return Divde_Twelve_Months
    #Divide the money left by 12 to see the money each months may make or not after tax.

def Calculate_Twelve_Months(num1):
    Twelve_Months = num1 % 12
    return Twelve_Months
    #Lets you see the what is left after the 12 months divide much easier(No idea where else to put this).

def Calculate_Double_The_Money(num1,num2):
    multiplier = 2 ** num2
    Double_The_Money  = num1 * multiplier
    return Double_The_Money
    #Let you see what is the double the money if it double every year(No idea for this one else well just put in fun facts).

keep_going = 0
while keep_going <= 0:
#Frist loop keep the inpputing and the calcualteing in one.
#Allowing the progarm to rerun more then one time after it is done.
    keep_going_part2 = False
    while not keep_going_part2 == True:
    #Only keep the inputs in one loop as the sevond loop inside the frist.
        print(" ")
        Year_income = int(input("Frist put up your income you make in a year. " + "$" ))
        #With no income vaule then it will not work and use a string operator of + to added the dollar sign to the number.
        print(" ")
        
        print("Now put the income tax that you have. If you don't have it just press enter")
        print(" ")
        #There are Three income tax.
        Federal_income_tax = float(input("Your federal income tax rate: "))
        #It Can change so left it to the person to put it and allows it to be use for years.
        State_income_tax = float(input("Your state income tax rate: "))
        #There are 50 states that have a different tax rate.
        Local_income_tax = float(input("Your local income tax rate: "))
        #Some citys have there own tax rate.
        Total_income_tax = Calculate_Total_income_tax(Federal_income_tax,State_income_tax,Local_income_tax)

        print(" ")
        print("Put your FICA Tax numbers into here.")
        #FICA Tax is the total of social security and medicare.
        Social_Security_tax = float(input("Put your Social Security tax number: "))
        #May change have them added it.
        Medicare_Tax = float(input("Put your medicare Tax number: "))
        #May change hhave them added it.
        Additional_medicare_tax = float(input("Add the additional medicare tax if you have one: "))
        #If your income is very high you need to pay more medicar tax and feels easy to put it this way.
        FICA_Tax = Calculate_FICA_Tax(Medicare_Tax,Social_Security_tax,Additional_medicare_tax)
        
        print(" ")
        print("if you have a property then put a number if not just put a 0.")
        #Some people ave a property while others rent(will add a rent part next time).
        Property_Tax = float(input("The property tax that you have: " ))
        #The tax may be different or change so have them put it.
        print(" ")
        print("=" * 50)
        #These makes it easier to see the infi from the other stuff.
        print("Bellow this will show the vaules you input.")
        print("Press enter if the info is correct to what you put.")
        print("=" * 50)
        print(" ")
        print("=" * 50)
        print("Your year income:", end=" ")
        print("$", Year_income, sep="")
        print(" ")
        #Put these here to allow the person to read the info mch better.
        print("Your total income tax:", end=" ")
        print(Total_income_tax, "%", sep="")
        print(" ")
        print("Your FICA tax:", end="")
        print(FICA_Tax, "%", sep="")
        print(" ")
        print("Your Property tax:", end=" ")
        print(Property_Tax, "%", sep="")
        #Add them to one line while still adding % or $ to them/ To the other one are the same as well.
        print("=" * 50)
        print(" ")
        #Will fix the 0.000000 problem next time.
        print("If correct then type 'Yes' or if you want to stop the progarm type 'Stop'.")
        print("Or type anything else to restart to the beginning.")
        Enter_is_corrct = input("Type,'Yes', 'Stop', anything else: ")
        #Allow them to see what they put and restart it if is there anything worng. Also had to make it two print due to how longthe text is.
        print(" ")
        if Enter_is_corrct == 'Yes':
            keep_going_part2 = True
            print("Now starting to calculate will take a few seconds to do.")
        elif Enter_is_corrct == 'Stop':
            keep_going_part2 = True
            keep_going += 1
        else:
            print("Restarting to the beginnging.")
        #Lets you continue to the calculating, to stoping the progarm if you need to or restaring to the start of the progarm.
    if keep_going <= 0:
    #Allows the progarm to end here and not stop when 1 is added.
        for x in range (10, -1, -1):   
            print(x)
        #Make a space between the two loops and lets the person know It is calculating the numbers.

        Total_Tax = Calculate_Total_Tax(Total_income_tax,FICA_Tax,Property_Tax)
        
        The_percentage_of_Total_Tax = Calculate_The_percentage_of_Total_Tax(Total_Tax) 
        
        Money_that_is_left = Calculate_Money_that_is_left(The_percentage_of_Total_Tax,Year_income)
        
        Amount_of_tax_take = Calculate_Amount_of_tax_take(Year_income,Money_that_is_left)
        #Grab The def from the start and then use the numbers the person input to calculate the info.
        print(" ")
        print("=" * 50)
        print("This is the money left:", end=" ")
        print("$", Money_that_is_left, sep="")
        print(" ")
        print("This is he amount the tax take:", end=" ")
        print("$", Amount_of_tax_take, sep="")
        print(" ")
        print("This is the amount of tax you have in percentage:", end=" ")
        print(Total_Tax, "%", sep=" ")
        #Fully lay it out the info that was calculte.
        print("=" * 50)
        print(" ")
        print("Thank you for using this calculator for some tax's.")
        print("Due you want some more info about your money?")
        Fun_facts = input("Then type a 'Yes':")
        if Fun_facts == 'Yes':
        #Allows the person to get fun facts and if not they can restart or end progarm.
            How_many_years = float(input("The amount of years to doble your money:"))

            How_many_Thousand = Calculate_How_many_Thousand(Money_that_is_left)

            How_many_Hundred = Calculate_How_many_Hundred(Money_that_is_left)
            
            How_many_Ten = Calculate_How_many_Ten(Money_that_is_left)

            Divide_Twelve_Months = Calculate_Divide_Twelve_Months(Money_that_is_left)

            Twelve_Months = Calculate_Twelve_Months(Money_that_is_left)
            
            Double_The_Money = Calculate_Double_The_Money(Money_that_is_left,How_many_years)
            #Grab the def and make them calculate the numbers for the info.

            print(" ")
            print("=" * 50)
            print("How many Thousand in total for the money left:", end=" ")
            print(How_many_Thousand)
            print(" ")
            print("How many Hundreds in total for the money left:", end=" ")
            print(How_many_Hundred)
            print(" ")
            print("How many tens in total for the money left:", end=" ")
            print(How_many_Ten)
            print(" ")
            print("The money divide by 12 for the months:", end=" ")
            print("$", Divide_Twelve_Months, sep="")
            print(" ")
            print("The money left after the 12 month evenly:", end=" ")
            print("$", Twelve_Months, sep="")
            print(" ")
            print("The double of the money by how many years", end=" ")
            print("$", Double_The_Money, sep="")
            print("=" * 50)
            print(" ")
            #Just more info they want to know lay out in order.
            #May be helpful or not.
        
        keep_going_part3 = True
        while keep_going_part3 == True:
            To_restart = input("Then if you want to restart the calutor then say 'Yes' if not say 'No': ")
            if To_restart == 'Yes' or To_restart == 'No':
                keep_going_part3 = False
            elif To_restart != 'Yes' and To_restart != 'No':
                print("worng input try again")
                #This loop will make sure they put a Yes or No and notting else.
        if To_restart == 'Yes':
            print("Restarting.")
        else:
            keep_going += 1
        #Allowing for the progarm to restart or end.

print("Progarm stoping.")
#States The progarm ends.
