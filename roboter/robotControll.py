import string

from roboter import robotHandler as robHandle
from roboter import robotData as robData
from roboter import robotTalk as robTalk
from roboter import robotWriter as robWrite

class Conversation(object):
    write_people = robWrite.RobotWriter()
    write_rest = robWrite.RobotWriter()

    file_check = robHandle.FileCheck()

    is_people = file_check.fileExist(write_people.PEOPLE)
    is_rest = file_check.fileExist(write_rest.RANK)

    def initFile(self):
        self.write_people.InitFileWriter(self.write_people.PEOPLE_FILE_LOCATION)
        self.write_rest.InitFileWriter(self.write_rest.RANKING_FILE_LOCATION)

    if not is_people:
        initFile()

    handle_people = robHandle.HandleRobot(write_people.PEOPLE_FILE_LOCATION)
    handle_ranking = robHandle.HandleRobot(write_rest.RANKING_FILE_LOCATION)

    talk = robTalk.Script()

    people = robData.People()
    rest = robData.Rest()

    USER_ANSWER = ["yes", "no"]

    def isYesOrNo(self, answer):

        if answer in self.USER_ANSWER or answer in self.USER_ANSWER[0] or answer in self.USER_ANSWER[1]:
            
            if answer in self.USER_ANSWER[0]:
                return True

            elif answer in self.USER_ANSWER[1]:
                return False

        else:
            print("잘못된 답변입니다. [yes/no, y/n] 중에서 답변해주세요.")
            answer = input()
            return self.isYesOrNo(answer)

    def TalkAboutRestaurant(self):
        try:
            while True:
                people_text = self.handle_people.textChange()
                ranking_text = self.handle_ranking.textChange()

                user_answer = ""
                is_yes = False
                contents = ""
                template_text = ""

                for row in people_text:
                    self.people.appendGroup(row[0], row[1])

                for row in ranking_text:
                    self.rest.appendGroup(row[0], row[1])

                print(self.talk.blue(self.talk.welcome))
                name = input()

                    
                if not self.people.isHadName(name):
                    self.people.appendGroup(name, "1")

                else:
                    template_text = string.Template(self.talk.welcome_back)
                    contents = template_text.substitute(name = name)
                    print(self.talk.yellow(contents))

                    self.people.countPlus(name)

                    
                if self.rest.isRestExist():
                    template_text = string.Template(self.talk.recommand_script)
                    contents = template_text.substitute(restaurant = self.rest.Name[0])
                    print(self.talk.green(contents))

                    answer = input()

                    if self.isYesOrNo(answer):
                        answer = self.rest.Name[0]

                    else:
                                
                        if self.rest.isHadSecond():
                            template_text = string.Template(self.talk.recommand_script)
                            contents = template_text.substitute(restaurant = self.rest.Name[1])
                            print(self.talk.red(contents))
                                
                            answer = input()

                            if self.isYesOrNo(answer):
                                answer = self.rest.Name[1]

                            else:
                                template_text = string.Template(self.talk.restaurant_script)
                                contents = template_text.substitute(name = name)
                                print(self.talk.yellow(contents))
                                    
                                restaurant = input()
                                answer = restaurant

                        else:
                            template_text = string.Template(self.talk.restaurant_script)
                            contents = template_text.substitute(name = name)
                            print(self.talk.yellow(contents))
                                
                            restaurant = input()
                            answer = restaurant

                else:
                    template_text = string.Template(self.talk.restaurant_script)
                    contents = template_text.substitute(name = name)
                    print(self.talk.green(contents))
                        
                    restaurant = input()
                    answer = restaurant

                if self.rest.isHadName(answer):
                    self.rest.countPlus(answer)

                else:
                    self.rest.appendGroup(answer, "1")

                
                self.handle_people.saveFile(self.people.Group())
                self.rest.setGroupSorted()
                self.handle_ranking.saveFile(self.rest.Group())

                template_text = string.Template(self.talk.end)
                contents = template_text.substitute(name = name)
                print(self.talk.blue(contents))
                    
                break

        except Exception as error:
            self.write_people.InitFileWriter(self.write_people.PEOPLE_FILE_LOCATION)
            self.write_rest.InitFileWriter(self.write_rest.RANKING_FILE_LOCATION)

            print(error.with_traceback)
            print(error)

