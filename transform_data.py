import csv

def convert_to_EUR(price):
    return price*0.92

def calculate_tax(price):
    return price*0.20

with open ('/opt/airflow/data/raw_data.csv', 'r') as infile:
    infile_reader = csv.reader (infile)
    next(infile_reader)
    with open ('/opt/airflow/data/transformed_data.csv', 'w') as outfile:
        header = ['transaction_id', 'customer_id', 'price', 'vat_amount', 'currency', 'product_category']
        outfile_writer = csv.writer (outfile)
        outfile_writer.writerow(header)
        for line in infile_reader:
            new_price = convert_to_EUR(float(line[2]))
            vat_amount = calculate_tax(new_price)
            new_line = [ line[0], line[1], new_price, vat_amount, 'eur', line[4] ]
            outfile_writer.writerow(new_line)


