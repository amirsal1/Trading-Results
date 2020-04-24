import os
word = str("")
final_word = str(input())
while final_word != word:
    Trigger = float(input("Enter your Trigger: "))
    Stop = float(input("Enter your Stop: "))
    Executed_trigger = float(input("When did Trigger execute?"))
    Trade_Type = input("Is the trade Long or Short? ")

    #Code for Long trades:

    if Trade_Type == "Long":
        Shares = (abs(50 / (Trigger - Stop)))
        one_one_partial = input("Did you reach your 1:1 target of " + str(((Trigger - Stop) + Trigger)) + str("?"))

        #first "if" checks if any of the trade succeeded

        if  one_one_partial == "no":
            Executed_stop = float(input("When did Stop execute?"))
            loss = abs(Executed_trigger - Executed_stop) * Shares
            print("You lost " + str(loss) + "$ on all trades")
        elif one_one_partial == "yes":
            one_one_partial_profit = "%.2f" %((((Trigger - Stop) + Trigger) - Executed_trigger) * 0.75 * Shares)
            one_one_full_profit = "%.2f" %((((Trigger - Stop) + Trigger) - Executed_trigger) * Shares)
            remainder_one_one = float(input("Where did you cover remainder of 1:1 trade: "))
            remainder_one_one_profit = "%.2f" %((remainder_one_one - Executed_trigger) * 0.25 * Shares)

            #This "if" checks if a 2:1 type of trade succeeded

            two_one_partial = input("Did you reach your 2:1 target of " + str(((Trigger - Stop) * 2 + Trigger)) + str("?"))
            if two_one_partial == "no":
                Executed_stop = float(input("When did Stop execute?"))
                loss = abs(Executed_trigger - Executed_stop) * Shares
                print("If you traded 2:1 you lost: " + str(loss))
                print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
            elif two_one_partial == "yes":
                two_one_partial_profit = "%.2f" % ((((Trigger - Stop) * 2 + Trigger) - Executed_trigger) * 0.5 * Shares)
                four_one_partial = input("Did you reach your 4:1 target of " + str(((Trigger - Stop) * 4 + Trigger)) + str("?"))
                if four_one_partial == "no":



                    #if trade didn't make it to 1:4 it means all trades have been covered at this stage. I will print results.

                    print("All trades concluded:")
                    print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                    print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
                    print("If you traded 2:1 variation you earned " + str(two_one_partial_profit) + "$")

                elif four_one_partial == "yes":

                    #This "if" is for fully successfull 2:1 trades. I will calculate and print results.

                    four_one_partial_profit = "%.2f" %((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.25 * Shares)
                    four_one_full_profit = "%.2f" % ((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.5 * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = "%.2f" %((remainder_four_one - Executed_trigger) * 0.25 * Shares)

                    print("All trades concluded:")
                    print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                    print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:2 50% 25% 25% you earned " + str(two_one_partial_profit) + "$ + " + str(four_one_partial_profit) + "$ + " + str(remainder_four_one_profit) + "$.")
                    print("If you traded 1:2 50% 50% you earned " + str(two_one_partial_profit) + "$ + " + str(four_one_full_profit) + "$.")

    #Code for Short trades:

    elif Trade_Type == "Short":
        Shares = (abs(50 / (Stop - Trigger)))
        target_below = "%.2f" %(Trigger - (Stop - Trigger))
        one_one_partial = input("Did you reach your 1:1 target of " + str(target_below) + "?")

        # first "if" checks if any of the trade succeeded

        if one_one_partial == "no":
            Executed_stop = float(input("When did Stop execute?"))
            loss = abs(Executed_stop - Executed_trigger) * Shares
            print("You lost " + str(loss) + "$ on all trades")
        elif one_one_partial == "yes":
            one_one_partial_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger))) * 0.75 * Shares)
            one_one_full_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger))) * Shares)
            remainder_one_one = float(input("Where did you cover remainder of 1:1 trade: "))
            remainder_one_one_profit = "%.2f" % ((Executed_trigger - remainder_one_one) * 0.25 * Shares)

            # This "if" checks if a 2:1 type of trade succeeded
            target_beloww = "%.2f" %((Trigger - 2 * (Stop - Trigger)))
            two_one_partial = input("Did you reach your 2:1 target of " + str(target_beloww) + str("?"))
            if two_one_partial == "no":
                Executed_stop = float(input("When did Stop execute?"))
                loss = "%.2f" % (abs(Executed_stop - Executed_trigger) * Shares)
                print("Your 2:1 trades have lost: " + str(loss) + "$")
                print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
            elif two_one_partial == "yes":
                two_one_partial_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger) * 2)) * 0.5 * Shares)
                target_belowww = "%.2f" % (Trigger - 4 * (Stop - Trigger))
                four_one_partial = input("Did you reach your 4:1 target of " + str(target_belowww) + str("?"))
                if four_one_partial == "no":

                    # if trade didn't make it to 1:4 it means all trades have been covered at this stage. I will print results.

                    print("All trades concluded:")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
                    print("If you traded 2:1 variation you made " + str(two_one_partial_profit) + "$")

                elif four_one_partial == "yes":

                    # This "if" is for fully successfull 2:1 trades. I will calculate and print results.

                    four_one_partial_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger) * 4)) * 0.25 * Shares)
                    four_one_full_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger) * 4)) * 0.5 * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = "%.2f" % ((Executed_trigger - remainder_four_one ) * 0.25 * Shares)

                    print("All trades concluded:")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:2 50% 25% 25% you made " + str(two_one_partial_profit) + "$ + " + str(four_one_partial_profit) + "$ + " + str(remainder_four_one_profit) + "$.")
                    print("If you traded 1:2 50% 50% you made " + str(two_one_partial_profit) + "$ + " + str(four_one_full_profit) + "$.")

                    clear = lambda: os.system('cls')
                    ending_command = input("What do you want to do next? Clear/Close/Continue\n")
                    if ending_command == "Close":
                        exit()
                    elif ending_command == "Clear":
                        clear()
                    elif ending_command == "Continue":
                        print("\n\n\n\n\n")