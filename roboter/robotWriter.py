import csv
import robotReader as robRead

class RobotWriter():
    basic_location = "d:/Project/Python/codinglearn/"

    def __init__(self):
        self.ranking_file_location = self.basic_location + "ranking.csv"
        self.people_file_location = self.basic_location + "people.csv"
        self.fieldnames = ["Name", "Count"]

    def InitFileWriter(self, file_location, attribute_1="", attribute_2="Count"):
        with open(file_location, 'w') as file:
            self.fieldnames = [attribute_1, attribute_2]
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def lineAppend(self, location, col):
        with open(location, 'r+') as file:
            line_add = csv.DictWriter(file, fieldnames=self.fieldnames)
            temp_file = csv.DictReader(file)

            for row in temp_file:
                if row["Name"] == col:
                    continue
            
            line_add.writerow({"Name": col, "Count": "1"})

    def lineEditCount(self, location, col):
        line_col = robRead.RobotReader(location)
        line_field = []

        for x in line_col.fileReader():
            if x != 'Name,Count':
                line_field.append(x.split(','))

        for a, b in line_field:
            if b == col:
                line_field[a+1] += 1

        with open(location, "w") as file:
            line_edit = csv.DictWriter(file, fieldnames=self.fieldnames)
            line_edit.writeheader()

            for x in range(0, len(line_field), 2):
                line_edit({"Name": line_field[x], "Count": str(int(line_field[x + 1]) + 1)})


r = robRead.RobotReader("d:/Project/Python/codinglearn/fileSys/test.csv")
w = RobotWriter()
w.lineAppend(w.basic_location+"fileSys/test.csv", "A")
print(r.fileReader())
