Trigger = float(input("Enter your Trigger: "))
Stop = float(input("Enter your Stop: "))
Executed_trigger = float(input("When did Trigger execute?"))
Shares = (abs(50 / (Trigger - Stop)))
print("Taking partials 2:1 50% 25% 25%")
first_partial = input("Did you reach your first target of " + str(((Trigger - Stop) * 2 + Trigger)) + str("?"))
if first_partial == "True":
    first_partial_profit = (((Trigger - Stop) * 2 + Trigger) - Executed_trigger) * 0.5 * Shares
    print(str(first_partial_profit))
    second_partial = input("Did you reach your second target of " + str(((Trigger - Stop) * 4 + Trigger)) + str("?"))
    if second_partial == "True":
        second_partial_profit = (((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.25 * Shares
        print(str(second_partial_profit))
        remainder_cover = float(input("When did you cover remainder?"))
        remainder_profit = (remainder_cover - Executed_trigger) * 0.25 * Shares
        print(remainder_profit)
    else:
        print(str((Trigger-Executed_trigger)*0.5*Shares))
else:
    Executed_stop = float(input("When did Stop execute?"))
    loss = abs(Executed_trigger - Executed_stop) * Shares
    print("You lost " + str(loss))
print(" ")
print(" ")
print("Taking partials 2:1 50% 50%")
first_partial = input("Did you reach your first target of " + str(((Trigger - Stop) * 2 + Trigger)) + str("?"))
if first_partial == "True":
    first_partial_profit = (((Trigger - Stop) * 2 + Trigger) - Executed_trigger) * 0.5 * Shares
    print(str(first_partial_profit))
    second_partial = input("Did you reach your second target of " + str(((Trigger - Stop) * 4 + Trigger)) + str("?"))
    if second_partial == "True":
        second_partial_profit = (((Trigger - Stop) * 4 + Trigger) - Executed_trigger) * 0.5 * Shares
        print(str(second_partial_profit))
    else:
       print(str((Trigger - Executed_trigger)*0.5*Shares))
else:
    Executed_stop = float(input("When did Stop execute?"))
    loss = abs(Executed_trigger - Executed_stop) * Shares
    print("You lost " + str(loss))
print(" ")
print(" ")
print("Taking partials 1:1 75% 25%")
first_partial = input("Did you reach your first target of " + str(((Trigger - Stop) + Trigger)) + str("?"))
if first_partial == "True":
    first_partial_profit = (((Trigger - Stop) + Trigger) - Executed_trigger) * 0.75 * Shares
    print(str(first_partial_profit))
    remainder_cover = float(input("Where did you cover remainder? "))
    remainder_profit = (remainder_cover - Executed_trigger)*0.25*Shares
    print(str(remainder_profit))
else:
    Executed_stop = float(input("When did Stop execute?"))
    loss = abs(Executed_trigger - Executed_stop) * Shares
    print("You lost " + str(loss))
input()