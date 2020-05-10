import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# values for using google sheets with code.
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"
         ]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Partial Statistics").sheet1
data = sheet.get_all_records()
word = str("")
final_word = str(input())
while final_word != word:
    # Trading terms used to determine and calculate each and every trades' results.
    Trigger = float(input("Enter your Trigger: "))
    Stop = float(input("Enter your Stop: "))
    Executed_trigger = float(input("When did Trigger execute?"))
    Trade_Type = input("Is the trade Long or Short? ")
    Stock_Symbol = input("Enter stock symbol (ALL CAPS): ")
    Date_of_trade = input("Enter trade's date: ")
    one_one_partial_balance = float(sheet.cell(2, 1).value)
    one_one_full_balance = float(sheet.cell(2, 7).value)
    two_one_full_balance = float(sheet.cell(2, 11).value)
    two_one_partial_balance = float(sheet.cell(2, 17).value)

    # Code for Long trades:
    if Trade_Type == "Long":
        Shares = (abs(50 / (Trigger - Stop)))
        one_one_partial = input("Did you reach your 1:1 target of " + str(((Trigger - Stop) + Trigger))
                                + str("? yes/no"))

        # first "if" checks if any form of trade has succeeded.

        if one_one_partial == "no":
            Executed_stop = float(input("When did Stop execute?"))
            loss = float(Executed_trigger - Executed_stop) * Shares * (-1)
            print("You lost " + str(loss) + "$ on all trades")
            methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", str(loss),
                              " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, str(loss), " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", str(loss),
                              " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "0", str(loss)
                              ]
            # Code shows results to user and asks for confirmation before adding to google sheet.
            confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
            if confirm == "yes":
                sheet.update_cell(2, 1, str(one_one_partial_balance + loss))
                sheet.update_cell(2, 7, str(one_one_full_balance + loss))
                sheet.update_cell(2, 11, str(two_one_full_balance + loss))
                sheet.update_cell(2, 17, str(two_one_partial_balance + loss))
                sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                print("Finished writing to Trade Tracker")
            elif confirm == "no":
                break

        elif one_one_partial == "yes":
            one_one_partial_profit = float((((Trigger - Stop) + Trigger) - Executed_trigger) * 0.75 * Shares)
            one_one_full_profit = float((((Trigger - Stop) + Trigger) - Executed_trigger) * Shares)
            remainder_one_one = float(input("Where did you cover remainder of 1:1 trade: "))
            remainder_one_one_profit = float((remainder_one_one - Executed_trigger) * 0.25 * Shares)
            # Results for trading using 1:1 partial taking have been calculated.
            # This "if" checks if a trade using 2:1 partial taking method has succeeded.

            two_one_partial = input("Did you reach your 2:1 target of " + str("%.2f" % ((Trigger - Stop) * 2 + Trigger)
                                                                              + str("? yes/no"))
                                    )
            if two_one_partial == "no":
                Executed_stop = float(input("When did Stop execute?"))
                loss = float(Executed_trigger - Executed_stop) * Shares * (-1)
                print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) +
                      str(remainder_one_one_profit)
                      )
                print("If you traded 1:1 100% you earned " + str(one_one_full_profit))
                print("If you traded 2:1 you lost: " + str(loss))
                partial_methods = ["1:1 75% 25%", "1st Partial 75%", "2nd Partial 25%", "Total Profi/Loss", " ",
                                   "1:1 100%", "Cover", " ", "2:1 50% 50%", "1st Partial 50%", "2nd Partial 50%",
                                   "Total Profit/Loss", " ", "2:1 50% 25% 25%", "1st Partial 50%", "2nd Partial 25%",
                                   "3rd Partial 25%", "Total Profit/Loss"
                                   ]
                methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                  str(one_one_partial_profit),
                                  str(remainder_one_one_profit),
                                  str("%.2f" % (float(one_one_partial_profit) + float(remainder_one_one_profit))),
                                  " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                  Trade_Type, str(one_one_full_profit), " ",
                                  str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0",
                                  str("%.2f" % loss), " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                  Trade_Type,
                                  "0", "0", "0", str("%.2f" % loss)
                                  ]
                # Code shows results to user and asks for confirmation before adding to google sheet.
                confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
                if confirm == "yes":
                    sheet.update_cell(2, 1, str(one_one_partial_balance + float(one_one_partial_profit
                                                + remainder_one_one_profit)))
                    sheet.update_cell(2, 7, str(one_one_full_balance + float(one_one_full_profit)))
                    sheet.update_cell(2, 11, str(two_one_full_balance + loss))
                    sheet.update_cell(2, 17, str(two_one_partial_balance + loss))
                    sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                    print("Finished writing to Trade Tracker")
                elif confirm == "no":
                    break

            elif two_one_partial == "yes":
                two_one_partial_profit = float((((Trigger - Stop) * 2 + Trigger) - Executed_trigger) * 0.5 * Shares)
                four_one_partial = input("Did you reach your 4:1 target of " + str("%.2f" % ((Trigger - Stop) * 4
                                                                                             + Trigger))
                                         + str("? yes/no")
                                         )
                # Results for trading using 2:1 partial taking have been calculated.
                # if a trade didn't cover a 4:1 partial it means all positions have already been closed.
                if four_one_partial == "no":
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
                                      , str(remainder_one_one_profit),
                                      str("%.2f" % (float(one_one_partial_profit) + float(remainder_one_one_profit)))
                                      , " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit), " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit), "0",
                                      str(two_one_partial_profit),
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit), "0", "0", str(two_one_partial_profit)
                                      ]
                    # Code shows results to user and asks for confirmation before adding to google sheet.
                    confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
                    if confirm == "yes":
                        sheet.update_cell(2, 1, one_one_partial_balance + one_one_partial_profit
                                          + remainder_one_one_profit)
                        sheet.update_cell(2, 7, one_one_full_balance + one_one_full_profit)
                        sheet.update_cell(2, 11, two_one_full_balance + two_one_partial_profit)
                        sheet.update_cell(2, 17, two_one_partial_balance + two_one_partial_profit)
                        sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                        print("Finished writing to Trade Tracker")
                    elif confirm == "no":
                        break

                elif four_one_partial == "yes":

                    # This "if" is for fully successful 2:1 trades. I will calculate and print results.

                    four_one_partial_profit = float((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.25
                                                    * Shares)
                    four_one_full_profit = float((((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.5 * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = float((remainder_four_one - Executed_trigger) * 0.25 * Shares)

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
                                      str(one_one_partial_profit), str(remainder_one_one_profit),
                                      str("%.2f" % (float(one_one_partial_profit) + float(
                                          remainder_one_one_profit))),
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit), " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit), str(four_one_full_profit),
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_full_profit))),
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit), str(four_one_partial_profit),
                                      str(remainder_four_one_profit),
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_partial_profit)
                                                    + float(remainder_four_one_profit)))
                                      ]
                    # Code shows results to user and asks for confirmation before adding to google sheet.
                    confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
                    if confirm == "yes":
                        sheet.update_cell(2, 1, one_one_partial_balance + float(one_one_partial_profit
                                                                                + remainder_one_one_profit))
                        sheet.update_cell(2, 7, one_one_full_balance + float(one_one_full_profit))
                        sheet.update_cell(2, 11, two_one_full_balance + float(two_one_partial_profit
                                                                              + four_one_full_profit))
                        sheet.update_cell(2, 17,
                                          two_one_partial_balance + float(two_one_partial_profit
                                                                          + four_one_partial_profit
                                                                          + remainder_four_one_profit)
                                          )
                        sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                        print("Finished writing to Trade Tracker")
                    elif confirm == "no":
                        break

    # Code for Short trades:

    elif Trade_Type == "Short":
        Shares = (abs(50 / (Stop - Trigger)))
        target_below = "%.2f" % (Trigger - (Stop - Trigger))
        one_one_partial = input("Did you reach your 1:1 target of " + str(target_below) + "? yes/no")

        #  first "if" checks if any form of trade has succeeded.

        if one_one_partial == "no":
            Executed_stop = float(input("When did Stop execute?"))
            loss = "%.2f" % float((Executed_stop - Executed_trigger) * Shares * (-1))
            print("You lost " + str("%.2f" % float(loss)) + "$ on all trades")
            methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", str(loss),
                              " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, str(loss), " ",
                              str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", str(loss),
                              " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type, "0", "0", "0", str(loss)
                              ]
            # Code shows results to user and asks for confirmation before adding to google sheet.
            confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
            if confirm == "yes":
                sheet.update_cell(2, 1, one_one_partial_balance + float(loss))
                sheet.update_cell(2, 7, one_one_full_balance + float(loss))
                sheet.update_cell(2, 11, two_one_full_balance + float(loss))
                sheet.update_cell(2, 17, two_one_partial_balance + float(loss))
                sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                print("Finished writing to Trade Tracker")
            elif confirm == "no":
                break

        elif one_one_partial == "yes":
            one_one_partial_profit = float((Executed_trigger - (Trigger - (Stop - Trigger))) * 0.75 * Shares)
            one_one_full_profit = float((Executed_trigger - (Trigger - (Stop - Trigger))) * Shares)
            remainder_one_one = float(input("Where did you cover remainder of 1:1 trade: "))
            remainder_one_one_profit = float((Executed_trigger - remainder_one_one) * 0.25 * Shares)
            # Results for trading using 1:1 partial taking have been calculated.
            # This "if" checks if a trade using 2:1 partial taking method has succeeded.
            target_beloww = "%.2f" % (Trigger - 2 * (Stop - Trigger))
            two_one_partial = input("Did you reach your 2:1 target of " + str(target_beloww) + str("? yes/no"))
            if two_one_partial == "no":
                Executed_stop = float(input("When did Stop execute?"))
                loss = "%.2f" % (float(Executed_stop - Executed_trigger) * Shares * (-1))
                print("If you traded 1:1 75% 25% you earned " + str(one_one_partial_profit) + "$ + "
                      + str(remainder_one_one_profit) + "$")
                print("If you traded 1:1 100% you earned " + str(one_one_full_profit) + "$")
                print("Your 2:1 trades have lost: " + loss + "$")
                methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                  str(one_one_partial_profit),
                                  str(remainder_one_one_profit), str("%.2f" % (float(one_one_partial_profit)
                                                                               + float(remainder_one_one_profit)))
                                  , " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                  str(one_one_full_profit), " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                  Trade_Type, "0", "0", str(loss), " ", str(Stock_Symbol) + " "
                                  + str(Date_of_trade), Trade_Type, "0", "0", "0", str(loss)
                                  ]
                # Code shows results to user and asks for confirmation before adding to google sheet.
                confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
                if confirm == "yes":
                    sheet.update_cell(2, 1, one_one_partial_balance + float(one_one_partial_profit
                                                                            + remainder_one_one_profit))
                    sheet.update_cell(2, 7, one_one_full_balance + float(one_one_full_profit))
                    sheet.update_cell(2, 11, two_one_full_balance + float(loss))
                    sheet.update_cell(2, 17, two_one_partial_balance + float(loss))
                    sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                    print("Finished writing to Trade Tracker")
                elif confirm == "no":
                    break

            elif two_one_partial == "yes":
                two_one_partial_profit = float((Executed_trigger - (Trigger - (Stop - Trigger) * 2)) * 0.5 * Shares)
                target_belowww = float(Trigger - 4 * (Stop - Trigger))
                four_one_partial = input("Did you reach your 4:1 target of " + str(target_belowww) + str("? yes/no"))
                # Results for trading using 2:1 partial taking have been calculated.
                if four_one_partial == "no":

                    # if a trade didn't cover a 4:1 partial it means all positions have already been closed.

                    print("All trades concluded:")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + "
                          + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 2:1 variation you made " + str(two_one_partial_profit) + "$")
                    methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_partial_profit)
                                      , str(remainder_one_one_profit),
                                      str("%.2f" % (float(one_one_partial_profit) + float(
                                          remainder_one_one_profit))),
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit), " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit), "0",
                                      str(two_one_partial_profit),
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit), "0", "0", str(two_one_partial_profit)
                                      ]
                    # Code shows results to user and asks for confirmation before adding to google sheet.
                    confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
                    if confirm == "yes":
                        sheet.update_cell(2, 1, one_one_partial_balance + float(one_one_partial_profit
                                                                                + remainder_one_one_profit))
                        sheet.update_cell(2, 7, one_one_full_balance + float(one_one_full_profit))
                        sheet.update_cell(2, 11, two_one_full_balance + float(two_one_partial_profit))
                        sheet.update_cell(2, 17, two_one_partial_balance + float(two_one_partial_profit))
                        sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                        print("Finished writing to Trade Tracker")
                    elif confirm == "no":
                        break

                elif four_one_partial == "yes":
                    # This "if" is for fully successful 2:1 trades. I will calculate and print results.
                    four_one_partial_profit = float((Executed_trigger - (Trigger - (Stop - Trigger) * 4)) * 0.25
                                                    * Shares)
                    four_one_full_profit = float((Executed_trigger - (Trigger - (Stop - Trigger) * 4)) * 0.5 * Shares)
                    remainder_four_one = float(input("Where did you cover remainder of 1:2 trade: "))
                    remainder_four_one_profit = float((Executed_trigger - remainder_four_one) * 0.25 * Shares)

                    print("All trades concluded:")
                    print("If you traded 1:1 75% 25% you made " + str(one_one_partial_profit) + "$ + "
                          + str(remainder_one_one_profit) + "$")
                    print("If you traded 1:1 100% you made " + str(one_one_full_profit) + "$")
                    print("If you traded 1:2 50% 50% you made " + str(two_one_partial_profit) + "$ + "
                          + str(four_one_full_profit) + "$.")
                    print("If you traded 1:2 50% 25% 25% you made " + str(two_one_partial_profit) + "$ + "
                          + str(four_one_partial_profit) + "$ + " + str(remainder_four_one_profit) + "$.")
                    methods_profit = [str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_partial_profit), str(remainder_one_one_profit),
                                      str("%.2f" % (float(one_one_partial_profit) + float(remainder_one_one_profit)))
                                      , " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(one_one_full_profit), " ", str(Stock_Symbol) + " " + str(Date_of_trade),
                                      Trade_Type, str(two_one_partial_profit), str(four_one_full_profit),
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_full_profit))),
                                      " ", str(Stock_Symbol) + " " + str(Date_of_trade), Trade_Type,
                                      str(two_one_partial_profit), str(four_one_partial_profit),
                                      str(remainder_four_one_profit),
                                      str("%.2f" % (float(two_one_partial_profit) + float(four_one_partial_profit)
                                                    + float(remainder_four_one_profit)))
                                      ]
                    # Code shows results to user and asks for confirmation before adding to google sheet.
                    confirm = input("Add " + str(methods_profit) + "to sheet? yes/no")
                    if confirm == "yes":
                        sheet.update_cell(2, 1, one_one_partial_balance + one_one_partial_profit
                                          + remainder_one_one_profit)
                        sheet.update_cell(2, 7, one_one_full_balance + one_one_full_profit)
                        sheet.update_cell(2, 11, two_one_full_balance + two_one_partial_profit
                                          + four_one_full_profit)
                        sheet.update_cell(2, 17, two_one_partial_balance + two_one_partial_profit
                                          + four_one_partial_profit + remainder_four_one_profit
                                          )
                        sheet.append_row(methods_profit, table_range="A1", value_input_option='USER_ENTERED')
                        print("Finished writing to Trade Tracker")
                    elif confirm == "no":
                        break

clear = lambda: os.system('cls')
ending_command = input("What do you want to do next? Clear/Close/Continue\n")
if ending_command == "Close":
    exit()
elif ending_command == "Clear":
    clear()
elif ending_command == "Continue":
    print("\n\n\n\n\n")
