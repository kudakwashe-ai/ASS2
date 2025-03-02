num_sheep = int(input("Enter the number of sheep: "))
base_price = 2500000
selling_price = 3000000
total_capital = base_price * num_sheep
total_revenue = selling_price * num_sheep
profit = total_revenue - total_capital
print(f"Total capital spent: {total_capital}")
print(f"Total revenue: {total_revenue}")
print(f"Profit: {profit}")

