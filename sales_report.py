"""Generate sales report showing total melons each salesperson sold."""

# Initialize two new empty lists for salespeople and melons_sold
salespeople = []
melons_sold = []

# Open the file 'sales-report.txt' and save to variable 'f'
f = open('sales-report.txt')
# Iterate over f line by line, cleaning the files and splitting the lines 
# at the divider (|). salesperson is at index 0 and melons is at index 2.
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    salesperson = entries[0]
    # cast quantity of melons to a number
    melons = int(entries[2])

    # If the salesperson is already in the list
    if salesperson in salespeople:
        # use the existing index for that person...
        position = salespeople.index(salesperson)
        # and add this line's value of melons sold to the existing quantity
        melons_sold[position] += melons
    # Otherwise, the salesperson is a new entry
    else:
        # so add salesperson to the end of the salesperson list
        salespeople.append(salesperson)
        # and add meons to the end of the melons list
        melons_sold.append(melons)

# Iterate over the salespeople list and print data:
for i in range(len(salespeople)):
    # using the same index from salespeople, access melons_sold to print data
    print(f'{salespeople[i]} sold {melons_sold} melons')
