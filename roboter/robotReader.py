class RobotReader():
    def __init__(self, file_location):
        self.file_location = file_location
        self.__text_line = []

    def textLine(self):
        return self.__text_line

    def fileReader(self):
        with open(self.file_location, 'r') as file:
            self.__text_line = self.lineReader(file)

            return self.textLine()

    def lineReader(self, file):
        text_line = []

        while True:
                line = file.readline()

                if not line:
                    break

                excepted_line = self.exceptN(line)

                for line in excepted_line:
                    if line:
                        text_line.append(line)
                    
                    else:
                        break

        return text_line

    def exceptN(self, line):
        return line.split('\n')
