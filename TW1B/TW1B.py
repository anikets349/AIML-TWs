import csv

rows = []

with open('enjoysport.csv') as csvfile:
    next(csvfile) #skips the first row  i.e. the headers
    for row in csv.reader(csvfile):
        rows.append(row)
        
print("Number of training instances: ", len(rows))
numAttributes = len(rows[0]) - 1
print("Number of attributes: ", numAttributes)
hypothesis = [0] * numAttributes
print("Intial hypothesis: ", hypothesis)

print("")

for i in range(0, len(rows)):
    if rows[i][-1] == "yes":
        print(f"Instance {i + 1} is a  positive training example")
        for j in range(0, numAttributes):
            if hypothesis[j] == 0 or hypothesis[j] == rows[i][j]:
                hypothesis[j] = rows[i][j]
            else:
                hypothesis[j] = '?'
    else:
        print(f"Instance {i + 1} is a  negative training example, hence ignored")
    print(f"Instance {i + 1} examined")
    print("Hypothesis is: ", hypothesis)
    print("")
    
print("Maximally specific hypothesis is: ", hypothesis)