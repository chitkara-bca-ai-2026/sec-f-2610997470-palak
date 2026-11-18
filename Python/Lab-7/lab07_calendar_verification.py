print("=" * 40)
print("       CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

year = int(input("Enter year: "))

if year <= 0:
    print("Invalid year! Please enter a positive year.")

else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"

    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = " Divisible by 4 and not a century year"

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"

    if status == "LEAP YEAR":
        days = 366
        feb_days = 29
    else:
        days = 365

    print()
    print("-" * 40)
    print(f"Year:{year}")
    print(f"Status:{status}")
    print(f"Days in Year:{days}", "days")
    print(f"Days in February:{feb_days}", "days")
    print(f"Reason:{reason}")
    print("-" * 40)
