total_sales=0
highest_sale=0
highest_seller=""
invalid_entries=[]

from pathlib import Path

base = Path("D:/Python Automation/Sales Tracker")
input_file = base / "sales.txt"
output_file = base / "cleaned_sales_data.txt"
invalid_file = base / "invalid_sales_data.txt"

with open(input_file, "r") as file, open(output_file, "w") as cleaned_file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        try:
            name, amount = line.split(",")
            name = name.strip()
            amount = int(amount.strip())
            total_sales += amount
            if amount > highest_sale:
                highest_sale = amount
                highest_seller = name
            cleaned_file.write(f"{name},{amount}\n")
        except Exception:
            invalid_entries.append(line)

with open(invalid_file, "w") as invalid_file:
    for entry in invalid_entries:
        invalid_file.write(f"{entry}\n")

print(f"Total Sales: ${total_sales}")
print(f"Highest Sale: ${highest_sale} by {highest_seller}")
print(f"Invalid Entries: {len(invalid_entries)}")