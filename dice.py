import random

run='y'
while run == 'y':

## introduction for user --------------------------------------------------------------------------------------------
    # print(".")
    # print(".")
    # print(".")
    # print(".")
    # print(".")
    # print(".")
    # print(".-------------------------------------------------------------------------------------------------------*")
    # print("| Welcome to the Dice Roller 5000! There are several different ways to roll dice. See below for details.|")
    # print("*-------------------------------------------------------------------------------------------------------.")
    # print(" ")
    # print("_._._._._._._._._._._._._._._._._._._._._._")
    # print(" ")
    # print("5e Rolls")
    # print(" ")
    # print("To roll a pre-created D20 dice roll (initiative, saving throws, attack rolls, skill checks):")
    # print("1. decide the type of roll you want: i = _I_nitiative, c = skill _C_heck, t = saving _T_hrow, or a = _A_ttack roll")
    # print("2. followed by a = advantage, d = disadvantage, n = none")
    # print("3. add any modifiers at the end with a + or - followed by the value of your modifier.")
    # print("**check out these examples:**")
    # print("      id+3 means rolling initiative at disadvantage adding a +3 modifier")
    # print("      tn-1 means rolling a normal saving throw with a -1 modifier")
    # print(" ")
    # print("_._._._._._._._._._._._._._._._._._._._._._")
    # print(" ")
    # print("Custom Dice")
    # print(" ")
    # print("To roll a custom dice:")
    # print("1. Input your dice type (D4, D6, D8, D10, D12, D20, or custom)")
    # print("2. Input the number of dice you'd like to roll (ie. 1, 3, infinity and beyond")
    # print("3. Indicate what kind of modifier (if any) you are using and if you'd like it ")
    # print("   added to each dice roll or just once at the end of the calculation.")
    # print(".")
    # print(".")
    # print(".")
    # print(".")
    # print(".")
    # print(".")

## dice type --------------------------------------------------------------------------------------------
    dice_type = input("Which would you like to use? Type e for 5e Rolls, c for Custom Dice, a number to roll a basic dice or n to end this script:    ")
    dice_type = dice_type.lower()

## 5e Roller logic --------------------------------------------------------------------------------------------
    if dice_type == "e": 
        # print("_._._._._._._._._._._._._._._._._._._._._._") 
        # print("5e Roller")
        # print(' ')
        # print("Type out your preferences using the following instructions:")
        # print("1. decide the type of roll you want: ")
        # print("   i = _I_nitiative, c = skill _C_heck, t = saving _T_hrow, or a = _A_ttack roll")
        # print("2. followed by a = advantage, d = disadvantage, or n = none")
        # print("3. add any modifiers at the end with a + or - followed by the value of your modifier.")
        # print("**check out these examples:**")
        # print("      id+3 means rolling initiative at disadvantage adding a +3 modifier")
        # print("      tn-1 means rolling a normal saving throw with a -1 modifier")
        try: 
            formula = input("Enter your preferences here:   ")
            print(' ')
            formula = formula.lower().strip()
            print(formula)
            output = list(formula)
            number1 = random.randint(1,20)
            onewithmod = number1 + int(output[3])
            number2 = random.randint(1,20)
            twowithmod = number2 + int(output[3])
            roll_types = {'i': 'initiative', 'c': 'skill check', 't': 'saving throw', 'a': 'attack roll'}
            adv_dis_num = {'a': max([onewithmod, twowithmod]), 'd': min([onewithmod, twowithmod])}
            adv_dis = {'a' : 'advantage', 'd' : 'disadvantage'}
            if output[1] == 'a' or output[1] == 'd':
                print(' ')
                print(f"{number1} {output[2]} {output[3]} = {onewithmod}")
                print(f"{number2} {output[2]} {output[3]} = {twowithmod}")
                print(' ')
                # new advantage/disadvantage logic 
                print(f"Final results ({roll_types.get(output[0])}, {adv_dis.get(output[1])}): {adv_dis_num.get(output[1])}")
                print(' ')
                # old advantage/disadvantage logic
                # if output[1] == 'a':
                #     print(' ')
                #     print(f"Final results ({roll_types.get(output[0])}, advantage): {max([onewithmod, twowithmod])}")
                #     print(' ')
                # elif output[1] == 'd':
                #     print(' ')
                #     print(f"Final results ({roll_types.get(output[0])}, disadvantage): {min([onewithmod, twowithmod])}")
                #     print(' ')
            else:
                print(' ')
                print(f"Your roll result for {roll_types.get(output[0])}: {number1} {output[2]} {output[3]} = {onewithmod}")
        finally:
            run='n'

## FUTURE: Custom Dice --------------------------------------------------------------------------------------------
    elif dice_type == "c":
        # print("_._._._._._._._._._._._._._._._._._._._._._") 
        # print("Custom Dice")
        # print(" ")
        # print("To roll a custom dice:")
        # print("1. If more than one dice: Start with the number of dice you'd like to roll (1, 5, 100) followed by an 'x'")
        # print("2. Type the dice type you'd like to use (ie. 20 for D20, 10 for D10, 100 for D100)")
        # print("3. Include the modifier you are using (ie. +1, 0, -2). If you'd like it used just once at the end,")
        # print("   include a space between the dice type number and modifier number.")
        # print(' ')
        formula = input("Enter your custom roll here:   ")
        print(' ')
        formula = formula.lower().strip()
        print(formula)
        output = list(formula)
        find_x = formula.find('x') #
        find_mod_type = formula.find(' ')
        find_mod_plus = formula.find('+')
        find_mod_minus = formula.find('-')
## stopped here: need to figure out way to pull dice face number from ALL inputs
        # dice_faces = 
        mod_dict = {'+': output[find_mod_plus], '-': output[find_mod_minus]}
        #find function note: .find(value, start, end) if value doesn't exist in string, comes back -1
        if '+' in formula or '-' in formula:
            print("this string contains a modifier")
        else:
            print("this string doesn't contain a modifier")
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