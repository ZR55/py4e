hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
if hours <= 40:
    pay = hours * rate
    print("Pay: ",pay)
else:
    pay = 40 * rate + (hours - 40) * rate*1.5
    print ("Pay: ", pay)
