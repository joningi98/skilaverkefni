def resume():
    x = input("Continue: ")
    if x != 'y':
        quit()


def calculate_total_value(shares):
    while True:
        try:
            p, n, d = input("Enter price (dollars, numerator, denominator): ").split(' ')
            price, numerator, denominator = float(p), float(n), float(d)
            total_value = float(shares * (price + (numerator / denominator)))
            total_value = ("%.2f" % total_value)
            total_value = (str(round(shares)) + " shares with market price " + str(round(price)) + " " + str(round(numerator)) + "/" +
                           str(round(denominator)) + " have value $" + str(total_value))
            print(total_value)
            break
        except ValueError:
            print("Invalid price!")


def enter_shares():
    while True:
        try:
            x = float(input("Enter number of shares: "))
            calculate_total_value(x)
            break
        except ValueError:
            print("Invalid number!")


while True:
    enter_shares()
    resume()
