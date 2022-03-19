class RobotReader():
    def __init__(self, file_location):
        self.file_location = file_location
        self.text_line = []

    def fileReader(self):
        with open(self.file_location, 'r') as file:
            self.text_line = self.lineReader(file)

            return self.text_line

    def lineReader(self, file):
        text_line = []

        while True:
                line = file.readline()

                if not line:
                    break

                except_line = self.exceptN(line)

                for i in except_line:
                    if i:
                        text_line.append(i)
                    
                    else:
                        break

        return text_line

    def exceptN(self, line):
        return line.split('\n')
