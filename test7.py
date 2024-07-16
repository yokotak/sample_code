portfolio = []
with open ("test.csv") as file:
    for line in file:
        row = line.split(",")
        try:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = (name, shares, price)
            portfolio.append(holding)
        except ValueError as err:
            print("bad row:", row)
            print("Reason:", err)