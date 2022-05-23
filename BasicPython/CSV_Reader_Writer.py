import csv

# with open('employee.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # Read the content of one file and write to another
#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter=':')

#         for line in csv_reader:
#             csv_writer.writerow(line)




# with open('employee.csv', 'r') as csv_file:
#     # Using Dictionary Reader will return Ordered Dictionary
#     # Helps in easy parsing, don't have to provide the index number instead directly give the interested column name
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line.get('emailid')) # Why using get method? Because it won't break the code with KeyError instead return None if not found


with open('employee.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Read the content of one file and write to another
    with open('new_names.csv', 'w') as new_file:
        field_names = ['First', 'Last', 'emailid']

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter=':')

        # will write the header as first row
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

