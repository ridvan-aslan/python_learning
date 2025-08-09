# cash machine

account_ridvan = {
    "name": "Rıdvan Aslan",
    "account_number": "123456789",
    "balance": 1000.0,
    "additional_account": 2000
}

account_sadik = {
    "name": "Sadık Turan",
    "account_number": "123456789",
    "balance": 500,
    "additional_account": 1000
}

def withdraw(account, amount):
    if amount <= 0:
        return "Invalid amount. Please enter a positive number."
    if amount > account["balance"]:
        additional_needed = input("Insufficient balance. Do you want to use your additional account? (yes/no): ").strip().lower()
        if additional_needed == "yes":
            if amount <= account["balance"] + account["additional_account"]:
                account["additional_account"] -= (amount - account["balance"])
                account["balance"] = 0
                return f"Withdrawal successful. New balance: {account['balance']}, Additional account balance: {account['additional_account']}"
            else:
                return "Insufficient funds in both accounts."
        else:
            return "Withdrawal cancelled."
    else:
        account["balance"] -= amount
        return f"Withdrawal successful. New balance: {account['balance']}"
    
withdrawal_ridvan = withdraw(account_ridvan, 3000)

print(withdrawal_ridvan)
