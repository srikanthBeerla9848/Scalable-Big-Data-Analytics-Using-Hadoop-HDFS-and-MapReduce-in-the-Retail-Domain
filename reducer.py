#!/usr/bin/env python3
import sys

current_category = None
current_sum = 0.0

for line in sys.stdin:
    
    line = line.strip()
    if not line:
        continue
    try:
        category, amount_str = line.split('\t', 1)
        amount = float(amount_str)
    except ValueError:
       
        continue

    
    if current_category == category:
        current_sum += amount
    else:
        
        if current_category is not None:
            print(f"{current_category}\t{current_sum}")
        current_category = category
        current_sum = amount


if current_category is not None:
    print(f"{current_category}\t{current_sum}")



!chmod +x mapper.py reducer.py


!hadoop fs -mkdir -p /user/hadoop/input
!hadoop fs -put ecommerce_data.csv /user/hadoop/input/


!hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper.py,reducer.py \
    -mapper mapper.py \
    -reducer reducer.py \
    -input /user/hadoop/input/ecommerce_data.csv \
    -output /user/hadoop/output/category_totals


!hadoop fs -cat /user/hadoop/output/category_totals/part-00000
