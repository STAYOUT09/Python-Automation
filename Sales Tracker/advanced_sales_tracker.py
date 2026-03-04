from pathlib import Path

def process_sales_data(base):
    total_sales = 0
    highest_sale = 0
    highest_seller = ""
    invalid_entries = []

    combined_file = base / "combined_cleaned_sales.txt"
    invalid_file = base / "all_invalid_sales.txt"

    with open(combined_file, "w") as cleaned:
        for file_path in base.glob("sales_*.txt"):
            with open(file_path, "r") as file:
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
                        cleaned.write(f"{name},{amount}\n")
                    except Exception:
                        invalid_entries.append(line)

    with open(invalid_file, "w") as invalid:
        for entry in invalid_entries:
            invalid.write(f"{entry}\n")

    return total_sales, highest_seller, highest_sale


if __name__ == "__main__":
    base = Path("D:/Python Automation/Sales Tracker")
    total, highest, seller = process_sales_data(base)

    print(f"Total Sales: {total}")
    print(f"Highest Sale: {highest}")
    print(f"Highest Seller: {seller}")