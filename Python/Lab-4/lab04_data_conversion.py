print("=" * 42)
print("             DATA CONVERSION UTILITY")
print("=" * 42)

product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))

total_price = price * quantity
amount_str = str(total_price)

print()
print("-" * 42)
print("             TYPE CASTING SUMMARY")
print("-" * 42)

print("Variable       Value           Python Type")
print("-" * 42)

print("product_name   ", product_name, "       ", type(product_name))
print("price          ", price, "      ", type(price))
print("quantity       ", quantity, "           ", type(quantity))
print("total_price    ", total_price, "       ", type(total_price))
print("amount_str     ", amount_str, "       ", type(amount_str))

print("-" * 42)

#Tax invoice:
print()
print("-" * 42)
print("                 TAX INVOICE")
print("-" * 42)

print(f"  Product Name   :{product_name}")
print(f"  Price per Unit : Rs.{price:.2f}")
print(f"  Quantity       :{quantity}")

print("-" * 42)
print("  Invoice Total  : Rs.", amount_str)
print("=" * 42)
