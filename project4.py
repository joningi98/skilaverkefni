while True:
    try:
        shares = float(input("Enter number of shares: "))
    except ValueError:
        print("Invalid number!")
        break
    try:
        price, numerator, denominator = input("Enter price (dollars, numerator, denominator): ").split(' ')
    except ValueError:
        print("Invalid price!")
        break
    price_int = float(price)
    numerator_int = float(numerator)
    denominator_int = float(denominator)
    total_value = shares * (price_int + (numerator_int / denominator_int))
    total_value = float(total_value)
    print("%.2f" % total_value)
    resume = input("Continue: ")
  
    if resume != 'y':
        break
