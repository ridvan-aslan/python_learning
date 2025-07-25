from datetime import datetime # Importing datetime module to work with dates and times


customerName = "Rıdvan"
customerSurname = "Aslan"
customerFullName = customerName + " " + customerSurname

print("Customer Full Name:", customerFullName)

customerGender = "M"
customerBirthYear = 2003


current_year = datetime.now().year
customerAge = current_year - customerBirthYear

print("Customer Age:", customerAge)

# Order details

order1 = 110
order2 = 1100.5
order3 = 356.95

orderTotal = order1 + order2 + order3
print("Order Total:", orderTotal)

