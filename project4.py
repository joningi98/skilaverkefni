keep_going = True

while keep_going:
    shares = float(input("Enter number of shares: "))
    price, numerator, denominator = input("Enter price (dollars, numerator, denominator): ").split(' ')
    price_int = float(price)
    numerator_int = float(numerator)
    denominator_int = float(denominator)
    total_value = shares * (price_int + (numerator_int / denominator_int))
    total_value = float(total_value)
    print("%.2f" % total_value)
    resume = input("Continue: ")
  
    if resume == 'y':
        keep_going = True
    else:
        keep_going = False

    
