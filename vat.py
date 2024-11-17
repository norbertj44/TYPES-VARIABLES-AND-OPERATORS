amount = input("enter the amount: ")
amount=amount.replace(",",".")
vat = float(amount)*0.23

print(f"Amount : {amount}")
print(f"VAT 23%: {vat}")
