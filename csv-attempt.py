import csv
def main():
  with open("./book.csv", 'r') as file:
    csvreader = csv.reader(file)
    vals = []
    for row in csvreader:
      vals.append(row[0])
  if len(vals) == len(set(vals)):
    print(True)
  else:
    print(False)
main()
