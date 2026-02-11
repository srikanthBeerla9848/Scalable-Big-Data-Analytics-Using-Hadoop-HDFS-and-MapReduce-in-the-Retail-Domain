
#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
# Read header line
header = next(reader, None)

cat_idx = 0
amt_idx = 1

if header:
    lower = [h.strip().lower() for h in header]
    if "category" in lower:
        cat_idx = lower.index("category")
    if "amount" in lower:
        amt_idx = lower.index("amount")


for row in reader:
    try:
        category = row[cat_idx].strip()
        amount = float(row[amt_idx])
        if category:
           
            print(f"{category}\t{amount}")
    except Exception:
        
        continue

