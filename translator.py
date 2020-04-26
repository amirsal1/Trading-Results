import os

word = str("")
final_word = str(input())
while final_word != word:
    Trigger = float(input("Enter your Trigger: "))
    Stop = float(input("Enter your Stop: "))
    Executed_trigger = float(input("When did Trigger execute?"))
    Trade_Type = input("Is the trade Long or Short? ")
    Stock_Symbol = input("Enter stock symbol (ALL CAPS): ")
    Date_of_trade = input("Enter trade's date: ")

    # Code for Long trades:

    if Trade_Type == "Long":
        Shares = (abs(50 / (Trigger - Stop)))
        one_one_partial = input("Did you reach your 1:1 target of " + str(((Trigger - Stop) + Trigger)) + str("?"))

        # first "if" checks if any of the trade succeeded

        if one_one_partial == "no":
            Executed_stop = float(input("When did Stop execute?"))
            loss = abs(Executed_trigger - Executed_stop) * Shares
            print("You lost " + str(loss) + "$ on all trades")
            partial_methods = ["1:1 75% 25%", "Long/Short", "1st Partial 75%", "2nd Partial 25%", "Total Profit/Loss",
                               " ", "1:1 100%", "Long/Short", "Cover", " ", "2:1 50% 50%", "Long/Short",
                               "1st Partial 50%", "2nd Partial 50%", "Total Profit/Loss", " ", "2:1 50% 25% 25%",
                               "Long/Short", "1st Partial 50%", "2nd Partial 25%", "3rd Partial 25%",
                               "Total Profit/Loss"
                               ]
            methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "-" + str(loss) + "$",
                              " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "-" + str(loss) + "$", " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "-" + str(loss) + "$",
                              " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "0",
                              "-" + str(loss) + "$"
                              ]
            with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results", "PartialProfitPython.csv"),
                      "w+") as f:
                f.write(",".join(partial_methods))
                f.write("\n")
                f.write(",".join(methods_profit))
            print("Finished writing to Trade Tracker")
        elif one_one_partial == "yes":
            one_one_partial_profit = "%.2f" % ((((Trigger - Stop) + Trigger) - Executed_trigger) * 0.75 * Shares)
            one_one_full_profit = "%.2f" % ((((Trigger - Stop) + Trigger) - Executed_trigger) * Shares)
            remainder_one_one = float(input("Where did you cover remainder of 1:1 trade: "))
            remainder_one_one_profit = "%.2f" % ((remainder_one_one - Executed_trigger) * 0.25 * Shares)

            # This "if" checks if a 2:1 type of trade succeeded

            two_one_partial = input("Did you reach your 2:1 target of " + str("%.2f" % ((Trigger - Stop) * 2 + Trigger)
                                                                              + str("?"))
                                    )
            if two_one_partial == "no":
                Executed_stop = float(input("When did Stop execute?"))
                loss = abs(Executed_trigger - Executed_stop) * Shares
                print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + " +
                      str(remainder_one_one_profit) + "$"
                      )
                print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                print("If you traded 2:1 you lost: " + str(loss))
                partial_methods = ["1:1 75% 25%", "1st Partial 75%", "2nd Partial 25%", "Total Profi/Loss", " ",
                                   "1:1 100%", "Cover", " ", "2:1 50% 50%", "1st Partial 50%", "2nd Partial 50%",
                                   "Total Profit/Loss", " ", "2:1 50% 25% 25%", "1st Partial 50%", "2nd Partial 25%",
                                   "3rd Partial 25%", "Total Profit/Loss"
                                   ]
                methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                  str(one_one_partial_profit) + "$",
                                  str(remainder_one_one_profit) + "$",
                                  str("%.2f" % (float(one_one_partial_profit) + float(remainder_one_one_profit))) + "$",
                                  " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                  Trade_Type, str(one_one_full_profit) + "$", " ",
                                  str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0",
                                  "-" + str("%.2f" % loss) + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                  Trade_Type,
                                  "0", "0", "0", "-" + str("%.2f" % loss) + "$"
                                  ]
                with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results",
                                       "PartialProfitPython.csv"), "a") as f:
                    # f.write(",".join(partial_methods))
                    f.write("\n")
                    f.write(",".join(methods_profit))
                print("Finished writing to Trade Tracker")

            elif two_one_partial == "yes":
                two_one_partial_profit = "%.2f" % ((((Trigger - Stop) * 2 + Trigger) - Executed_trigger) * 0.5 * Shares)
                four_one_partial = input("Did you reach your 4:1 target of " + str("%.2f" % ((Trigger - Stop) * 4 +
                                                                                             Trigger)) + str("?")
                                         )
                if four_one_partial == "no":
                    # if trade didn't make it to 1:4 = all positions closed. Printing results.
                    print("All trades concluded:")
                    print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + " +
                          str(remainder_one_one_profit) + "$"
                          )
                    print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                    print("If you traded 2:1 variation you earned " + str(two_one_partial_profit) + "$")
                    partial_methods = ["1:1 75% 25%", "1st Partial 75%", "2nd Partial 25%", "Total Profit/Loss", " ",
                                       "1:1 100%", "Cover", " ", "2:1 50% 50%", "1st Partial 50%", "2nd Partial 50%",
                                       "Total Profit/Loss", " ", "2:1 50% 25% 25%", "1st Partial 50%",
                                       "2nd Partial 25%", "3rd Partial 25%", "Total Profit/Loss"
                                       ]
                    methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_partial_profit)
                                      + "$", str(remainder_one_one_profit) + "$",
                                      str("%.2f" % (float(one_one_partial_profit) + float(remainder_one_one_profit)))
                                      + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit) + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit) + "$", "0",
                                      str(two_one_partial_profit) + "$",
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit) + "$", "0", "0", str(two_one_partial_profit) + "$"
                                      ]

                    with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results",
                                           "PartialProfitPython.csv"), "a") as f:
                        # f.write(",".join(partial_methods))
                        f.write("\n")
                        f.write(",".join(methods_profit))
                    print("Finished writing to Trade Tracker")

                elif four_one_partial == "yes":

                    # This "if" is for fully successfull 2:1 trades. I will calculate and print results.

                    four_one_partial_profit = "%.2f" % ((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.25
                                                        * Shares)
                    four_one_full_profit = "%.2f" % ((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.5
                                                     * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = "%.2f" % ((remainder_four_one - Executed_trigger) * 0.25 * Shares)

                    print("All trades concluded:")
                    print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + "
                          + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                    print("If you traded 1:2 50% 50% you earned " + str(two_one_partial_profit) + "$ + "
                          + str(four_one_full_profit) + "$.")
                    print("If you traded 1:2 50% 25% 25% you earned " + str(two_one_partial_profit) + "$ + "
                          + str(four_one_partial_profit) + "$ + " + str(remainder_four_one_profit) + "$.")
                    partial_methods = ["1:1 75% 25%", "1st Partial 75%", "2nd Partial 25%", "Total Profi/Loss", " ",
                                       "1:1 100%", "Cover", " ", "2:1 50% 50%", "1st Partial 50%", "2nd Partial 50%",
                                       "Total Profit/Loss", " ", "2:1 50% 25% 25%", "1st Partial 50%",
                                       "2nd Partial 25%", "3rd Partial 25%", "Total Profit/Loss"
                                       ]
                    methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_partial_profit) + "$", str(remainder_one_one_profit) + "$",
                                      str("%.2f" % (float(one_one_partial_profit) + float(
                                          remainder_one_one_profit))) + "$",
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit) + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit) + "$", str(four_one_full_profit) + "$",
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_full_profit))) + "$",
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit) + "$", str(four_one_partial_profit) + "$",
                                      str(remainder_four_one_profit) + "$",
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_partial_profit)
                                                    + float(remainder_four_one_profit))) + "$"]
                    with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results",
                                           "PartialProfitPython.csv"), "a") as f:
                        # f.write(",".join(partial_methods))
                        f.write("\n")
                        f.write(",".join(methods_profit))
                    print("Finished writing to Trade Tracker")
    # Code for Short trades:

    elif Trade_Type == "Short":
        Shares = (abs(50 / (Stop - Trigger)))
        target_below = "%.2f" % (Trigger - (Stop - Trigger))
        one_one_partial = input("Did you reach your 1:1 target of " + str(target_below) + "?")

        # first "if" checks if any of the trade succeeded

        if one_one_partial == "no":
            Executed_stop = float(input("When did Stop execute?"))
            loss = abs(Executed_stop - Executed_trigger) * Shares
            print("You lost " + str("%.2f" % loss) + "$ on all trades")
            methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "-" + str(loss) + "$",
                              " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "-" + str(loss) + "$", " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "-" + str(loss) + "$",
                              " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "0", "-"
                              + str(loss) + "$"]
            with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results", "PartialProfitPython.csv"),
                      "a") as f:
                # f.write(",".join(partial_methods))
                f.write("\n")
                f.write(",".join(methods_profit))
            print("Finished writing to Trade Tracker")
        elif one_one_partial == "yes":
            one_one_partial_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger))) * 0.75 * Shares)
            one_one_full_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger))) * Shares)
            remainder_one_one = float(input("Where did you cover remainder of 1:1 trade: "))
            remainder_one_one_profit = "%.2f" % ((Executed_trigger - remainder_one_one) * 0.25 * Shares)

            # This "if" checks if a 2:1 type of trade succeeded
            target_beloww = "%.2f" % (Trigger - 2 * (Stop - Trigger))
            two_one_partial = input("Did you reach your 2:1 target of " + str(target_beloww) + str("?"))
            if two_one_partial == "no":
                Executed_stop = float(input("When did Stop execute?"))
                loss = "%.2f" % (abs(Executed_stop - Executed_trigger) * Shares)
                print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + "
                      + str(remainder_one_one_profit) + "$")
                print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                print("Your 2:1 trades have lost: " + loss + "$")
                methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                  str(one_one_partial_profit) + "$",
                                  str(remainder_one_one_profit) + "$", str("%.2f" % (float(one_one_partial_profit)
                                                                                     + float(remainder_one_one_profit)))
                                  + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                  str(one_one_full_profit) + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                  Trade_Type, "0", "0", "-" + str(loss) + "$", " ", str(Stock_Symbol) + " "
                                  + str(Date_of_trade), Trade_Type, "0", "0", "0", "-" + str(loss) + "$"]
                with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results",
                                       "PartialProfitPython.csv"), "a") as f:
                    # f.write(",".join(partial_methods))
                    f.write("\n")
                    f.write(",".join(methods_profit))
                print("Finished writing to Trade Tracker")
            elif two_one_partial == "yes":
                two_one_partial_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger) * 2)) * 0.5 * Shares)
                target_belowww = "%.2f" % (Trigger - 4 * (Stop - Trigger))
                four_one_partial = input("Did you reach your 4:1 target of " + str(target_belowww) + str("?"))
                if four_one_partial == "no":

                    # if trade didn't make it to 1:4 = all positions covered. Printing results.

                    print("All trades concluded:")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + "
                          + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 2:1 variation you made " + str(two_one_partial_profit) + "$")
                    methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_partial_profit)
                                      + "$", str(remainder_one_one_profit) + "$",
                                      str("%.2f" % (float(one_one_partial_profit) + float(
                                          remainder_one_one_profit))) + "$",
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit) + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit) + "$", "0",
                                      str(two_one_partial_profit) + "$",
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit) + "$", "0", "0", str(two_one_partial_profit) + "$"
                                      ]
                    with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results",
                                           "PartialProfitPython.csv"), "a") as f:
                        # f.write(",".join(partial_methods))
                        f.write("\n")
                        f.write(",".join(methods_profit))
                    print("Finished writing to Trade Tracker")

                elif four_one_partial == "yes":

                    # This "if" is for fully successful 2:1 trades. I will calculate and print results.

                    four_one_partial_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger) * 4)) * 0.25
                                                        * Shares)
                    four_one_full_profit = "%.2f" % ((Executed_trigger - (Trigger - (Stop - Trigger) * 4)) * 0.5
                                                     * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = "%.2f" % ((Executed_trigger - remainder_four_one) * 0.25 * Shares)

                    print("All trades concluded:")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + "
                          + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 1:2 50% 50% you made " + str(two_one_partial_profit) + "$ + "
                          + str(four_one_full_profit) + "$.")
                    print("If you traded 1:2 50% 25% 25% you made " + str(two_one_partial_profit) + "$ + "
                          + str(four_one_partial_profit) + "$ + " + str(remainder_four_one_profit) + "$.")
                    methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_partial_profit)
                                      + "$", str(remainder_one_one_profit) + "$",
                                      str("%.2f" % (float(one_one_partial_profit) + float(remainder_one_one_profit)))
                                      + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit) + "$", " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit) + "$", str(four_one_full_profit) + "$",
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_full_profit))) + "$",
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit) + "$", str(four_one_partial_profit) + "$",
                                      str(remainder_four_one_profit) + "$",
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_partial_profit)
                                                    + float(remainder_four_one_profit))) + "$"]
                    with open(os.path.join("C:\\", "Users", "amirs", "projects", "Trading-Results",
                                           "PartialProfitPython.csv"), "a") as f:
                        # f.write(",".join(partial_methods))
                        f.write("\n")
                        f.write(",".join(methods_profit))
                    print("Finished writing to Trade Tracker")
                    clear = lambda: os.system('cls')
                    ending_command = input("What do you want to do next? Clear/Close/Continue\n")
                    if ending_command == "Close":
                        exit()
                    elif ending_command == "Clear":
                        clear()
                    elif ending_command == "Continue":
                        print("\n\n\n\n\n")
