registration_fee = float(input("Enter registration fee: "))
monthly_fee = float(input("Enter monthly fee: "))
months = int(input("Enter number of months to pay for: "))

total_cost = registration_fee + (monthly_fee * months)

coupon = input("Do you have a discount coupon? (yes/no): ").lower()

total_cost *= 1 - 0.10 * (coupon == "yes")

print("Final amount to be paid:", total_cost)

