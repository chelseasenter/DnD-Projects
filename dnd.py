import random

# generic dice roller

# run = 'y'
# while run == 'y':
#     dice_type = input("Please select the dice you'd like to roll. 20 for D20, 10 for D10, and so on...  ")
#     mod = input("Please enter any modifier for this roll. (0 for no mod, max mod 20)  ")
#     try:
#         dice_type = int(dice_type)
#         mod = int(mod)
#         if dice_type == 20:
#             result = int(random.randint(1,20))
            # if result == 20:
            #     print("------------RESULTS------------")
            #     print(" ")
            #     print("WOAHHH BUDDY! THAT'S A CRITICAL HIT!")
            #     print(f"You rolled {result} + {mod} = {result + mod}")
            #     print(" ")
            #     run = input("Would you like to roll again? y for yes, n for no:  ")
#             elif result == 1:
#                 print("------------RESULTS------------")
#                 print(" ")
#                 print("Aw shit. That's a NAT ONE.")
#                 print(f"You rolled {result} + {mod} = {result + mod}")
#                 print(" ")
#                 run = input("Would you like to roll again? y for yes, n for no:  ")
#             else:
#                 print("------------RESULTS------------")
#                 print(" ")
#                 print(f"You rolled {result} + {mod} = {result + mod}")
#                 print(" ")
#                 run = input("Would you like to roll again? y for yes, n for no:  ")
#         elif dice_type == 12:
#             result = random.randint(1,12)
#             print("------------RESULTS------------")
#             print(" ")
#             print(f"You rolled {result} + {mod} = {result + mod}")
#             print(" ")
#             run = input("Would you like to roll again? y for yes, n for no:  ")
#         elif dice_type == 10:
#             result = random.randint(1,10)
#             print("------------RESULTS------------")
#             print(" ")
#             print(f"You rolled {result} + {mod} = {result + mod}")
#             print(" ")
#             run = input("Would you like to roll again? y for yes, n for no:  ")
#         elif dice_type == 8:
#             result = random.randint(1,8)
            # print("------------RESULTS------------")
            # print(" ")
            # print(f"You rolled {result} + {mod} = {result + mod}")
            # print(" ")
            # run = input("Would you like to roll again? y for yes, n for no:  ")
#         elif dice_type == 6:
#             result = random.randint(1,6)
#             print("------------RESULTS------------")
#             print(" ")
#             print(f"You rolled {result} + {mod} = {result + mod}")
#             print(" ")
#             run = input("Would you like to roll again? y for yes, n for no:  ")
#         elif dice_type == 4:
#             result = random.randint(1,4)
#             print("------------RESULTS------------")
#             print(" ")
#             print(f"You rolled {result} + {mod} = {result + mod}")
#             print(" ")
#             run = input("Would you like to roll again? y for yes, n for no:  ")
#         else:
#             print("------------RESULTS------------")
#             again = input(f"I'm sorry, your input was not recognized. Would you like to try again? y for yes, n for no:  ")
#             if again == 'y':
#                 run = 'y'
#             else:
#                 run = 'n'
#     except ValueError:
#         print("------------RESULTS------------")
#         print(" ")
#         print(f"I'm sorry, either {dice_type} or {mod} is not a valid entry. ")
#         print(" ")
#         print("Please enter 20 for D20, 12 for D12, 10 for D10, 8 for D8, 6 for D6 or 4 for D4,")
#         print("and make sure your modifier is just a number between 0 and 20.")
#         run = input("Would you like to roll again? y for yes, n for no:  ")

run = 'y'
while run == 'y':
    dice_type = input("Please indicate the dice you'd like to roll. 20 for D20, 10 for D10, and so on...  ")
    print(" ")
    dice_quantity = input("Please indicate how many of this dice type you'd like to roll. A number between 1 and INFINITY!")
    mod = input("Please enter any modifier for this roll. (0 for no mod, max mod 20)  ")
    print(" ")
    try:
        dice_type = int(dice_type)
        mod = int(mod)
        dice_quantity = int(dice_quantity)
        print(" ")
        print("------------RESULTS------------")
        print(" ")
        dice_list = []
        for dice in range(dice_quantity):
            result = random.randint(1,dice_type)
            dice_list.append(result)
        accepted_dice_types = [20, 12, 10, 8, 6, 4]
        for dice in dice_list:
            if dice_type in accepted_dice_types and dice == 20:
                print("WOAHHH BUDDY! THAT'S A CRITICAL HIT!")
                print(f"You rolled {dice} + {mod} = {dice + mod}")
                print(" ")
            elif dice_type in accepted_dice_types and dice == 1:
                print(f"You rolled {dice} + {mod} = {dice + mod}")
                print("Aw shit. That's a NAT ONE.")
            elif dice_type in accepted_dice_types:
                print(f"You rolled {dice} + {mod} = {dice + mod}")
            else:
                print(f"I'm sorry, either {dice_type} or {mod} is not a valid entry. ")
                print('')
                print("Please enter 20 for D20, 12 for D12, 10 for D10, 8 for D8, 6 for D6 or 4 for D4")
                print("and make sure your modifier is just a number between 0 and 20.")
        if len(dice_list) > 0:
            print(" ")
            print(f"Sum of rolls: {sum(dice_list)}")
            print(f"Highest Roll: {max(dice_list)}")
            print(f"Lowest Roll: {min(dice_list)}")
        print(" ")
        print("-------------------------------")   
        run = input("Would you like to roll again? y for yes, n for no:  ") 
    except ValueError:
        print(" ")
        print("------------RESULTS------------")
        print(" ")
        print(f"I'm sorry, either {dice_type} or {mod} is not a valid entry. ")
        print(" ")
        print("-------------------------------")
        print("Please enter 20 for D20, 12 for D12, 10 for D10, 8 for D8, 6 for D6 or 4 for D4")
        print("and make sure your modifier is just a number between 0 and 20.")
        run = input("Would you like to roll again? y for yes, n for no:  ")

## ask how many dice they want to roll