from datetime import datetime  # Importing datetime module to work with dates and times

customer_name = "Rıdvan"
customer_surname = "Aslan"
customer_full_name = customer_name + " " + customer_surname

print("Customer Full Name:", customer_full_name)

customer_gender = "M"
customer_birth_year = 2003

current_year = datetime.now().year
customer_age = current_year - customer_birth_year

print("Customer Age:", customer_age)

# Order details

order_1 = 110
order_2 = 1100.5
order_3 = 356.95

order_total = order_1 + order_2 + order_3
print("Order Total:", order_total)
