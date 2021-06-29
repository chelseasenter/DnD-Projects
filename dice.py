import random

run='y'
while run == 'y':

## introduction for user --------------------------------------------------------------------------------------------
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".-------------------------------------------------------------------------------------------------------*")
    print("| Welcome to the Dice Roller 5000! There are several different ways to roll dice. See below for details.|")
    print("*-------------------------------------------------------------------------------------------------------.")
    print(" ")
    print("_._._._._._._._._._._._._._._._._._._._._._")
    print(" ")
    print("5e Rolls")
    print(" ")
    print("To roll a pre-created D20 dice roll (initiative, saving throws, attack rolls, skill checks):")
    print("1. decide the type of roll you want: i = _I_nitiative, c = skill _C_heck, t = saving _T_hrow, or a = _A_ttack roll")
    print("2. followed by a = advantage, d = disadvantage, n = none")
    print("3. add any modifiers at the end with a + or - followed by the value of your modifier.")
    print("**check out these examples:**")
    print("      id+3 means rolling initiative at disadvantage adding a +3 modifier")
    print("      tn-1 means rolling a normal saving throw with a -1 modifier")
    print(" ")
    print("_._._._._._._._._._._._._._._._._._._._._._")
    print(" ")
    print("Custom Dice")
    print(" ")
    print("To roll a custom dice:")
    print("1. Input your dice type (D4, D6, D8, D10, D12, D20, or custom)")
    print("2. Input the number of dice you'd like to roll (ie. 1, 3, infinity and beyond")
    print("3. Indicate what kind of modifier (if any) you are using and if you'd like it ")
    print("   added to each dice roll or just once at the end of the calculation.")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")

## dice type --------------------------------------------------------------------------------------------
    dice_type = input("Which would you like to use? Type e for 5e Rolls, c for Custom Dice, a number to roll a basic dice or n to end this script:    ")
    dice_type = dice_type.lower()

## 5e Roller logic --------------------------------------------------------------------------------------------
    if dice_type == "e": 
        print("Type out your preferences using the following instructions:")
        print("1. decide the type of roll you want: ")
        print("   i = _I_nitiative, c = skill _C_heck, t = saving _T_hrow, or a = _A_ttack roll")
        print("2. followed by a = advantage, d = disadvantage, or n = none")
        print("3. add any modifiers at the end with a + or - followed by the value of your modifier.")
        print("**check out these examples:**")
        print("      id+3 means rolling initiative at disadvantage adding a +3 modifier")
        print("      tn-1 means rolling a normal saving throw with a -1 modifier")
        try: 
            formula = input("Enter your preferences here:   ")
            formula = formula.lower()
            output = list(formula)
            number1 = random.randint(1,20)
            onewithmod = number1 + int(output[3])
            number2 = random.randint(1,20)
            twowithmod = number2 + int(output[3])
            if output[1] == 'a' or output[1] == 'd':
                print(' ')
                print(f"{number1} {output[2]} {output[3]} = {onewithmod}")
                print(f"{number2} {output[2]} {output[3]} = {twowithmod}")
                if output[1] == 'a':
                    print(' ')
                    print(f"Final results (advantage): {max([onewithmod, twowithmod])}")
                    print(' ')
                elif output[1] == 'd':
                    print(' ')
                    print(f"Final results (disadvantage): {min([onewithmod, twowithmod])}")
                    print(' ')
            print(output)
        finally:
            run='n'

## FUTURE: Custom Dice --------------------------------------------------------------------------------------------
    elif dice_type == "c":
        print(' ')
        print("custom dice logic here")
        print(' ')
        run='n'
    elif dice_type == "n":
        run='n'
    elif dice_type.isdigit():
        print(" ")
        print(f"Roll results: {random.randint(1,int(dice_type))}")
        print(" ")
    else:
        print("input not recognized")
    run='n'
    # elif dice_type == "c":

    # elif dice_type == "n":
    #     run='n'
