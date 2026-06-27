#raw data generator to simulate the retail system

import csv 

def my_generator():
  yield 1, 13, 500, 'USD', 'T-shirt'
  yield 2, 4, 600, 'USD', 'Jeans'
  yield 3, 10, 700, 'USD', 'Pants'
  yield 4, 44, 300, 'USD', 'T-shirt'
  yield 5, 25, 800, 'USD', 'Jacket'

with open ('/opt/airflow/data/raw_data.csv', "w") as outfile:
    writer = csv.writer(outfile)
    header = ['transaction_id', 'customer_id', 'price', 'currency', 'product_category']
    writer.writerow(header)
    for value in my_generator():
        writer.writerow(value)
