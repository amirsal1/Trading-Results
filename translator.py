import os
word = str("")
final_word = str(input())
while final_word != word:
    Trigger = float(input("Enter your Trigger: "))
    Stop = float(input("Enter your Stop: "))
    Executed_trigger = float(input("When did Trigger execute?"))
    Shares = (abs(50 / (Trigger - Stop)))
    Trade_Type = input("Is the trade Long or Short? ")

    #Code for long trades:
    if Trade_Type == "Long":
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
                print(str(loss))
            elif two_one_partial == "yes":
                two_one_partial_profit = "%.2f" % ((((Trigger - Stop) * 2 + Trigger) - Executed_trigger) * 0.5 * Shares)
                four_one_partial = input("Did you reach your 4:1 target of " + str(((Trigger - Stop) * 4 + Trigger)) + str("?"))
                if four_one_partial == "no":

                    #if trade didn't make it to 1:4 it means all trades have been covered at this stage. I will print results.

                    print("All trades concluded:")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
                    print("If you traded 2:1 variation you made " + str(two_one_partial_profit) + "$")

                elif four_one_partial == "yes":

                    #This "if" is for fully successfull 2:1 trades. I will calculate and print results.

                    four_one_partial_profit = "%.2f" %((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.25 * Shares)
                    four_one_full_profit = "%.2f" % ((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.5 * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = "%.2f" %((remainder_four_one - Executed_trigger) * 0.25 * Shares)

                    print("All trades concluded:")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + " + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:2 50% 25% 25% you made " + str(two_one_partial_profit) + "$ + " + str(four_one_partial_profit) + "$ + " + str(remainder_four_one_profit) + "$.")
                    print("If you traded 1:2 50% 50% you made " + str(two_one_partial_profit) + "$ + " + str(four_one_full_profit) + "$.")

