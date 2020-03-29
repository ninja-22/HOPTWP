import sys
import csv

class CSVParser():
    def __init__(self, csv_):
        self.csv_ = csv_
        self.employees = []

    def parse_basic(self):
        print("\n(M1): Reading with reader...")
        with open(self.csv_) as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ',')
            header = next(readCSV)
            print(f"Header is: {header}")
            print()
            hdr = header[0] + "\t" + header[1] + "\t" + header[2] + "\t" + header[3] + "\t" + header[4]
            print(hdr)
            for ind, row in enumerate(readCSV):
                values = row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4]
                print(values)
                emp = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3], header[4]: row[4]}
                self.employees.append(emp)

            print("\n(M2): Reading with DictReader...")
            with open(self.csv_) as csvfile:
                reader = csv.DictReader(csvfile)
                header = reader.fieldnames
                hdr = header[0] + "\t" + header[1] + "\t" + header[2] + "\t" + header[3] + "\t" + header[4]
                print("\n" + hdr)
                for ind, row in enumerate(reader):
                    values = row["Name"] + "\t" + row["Age"] + "\t" + row["Salary"] + "\t" + row["M_id"] + "\t" + row["Slab"]
                    print(values)

    def process(self):
        for emp in self.employees:
            if int(emp["Salary"]) >= 30000:
                emp["Slab"] = "A"
            else:
                emp["Slab"] = "B"
        header = self.employees[0].keys()
        print("\n(M1): Writing with DictWriter...")
        with open(self.csv_, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(self.employees)
        print("Data written...!")
        self.parse_basic()

obj = CSVParser(sys.argv[1])
obj.parse_basic()
obj.process()


