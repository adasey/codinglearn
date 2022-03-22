import string

from roboter import robotHandler as robHandle
from roboter import robotData as robData
from roboter import robotTalk as robTalk
from roboter import robotWriter as robWrite


write_people = robWrite.RobotWriter()
write_rest = robWrite.RobotWriter()

file_check = robHandle.FileCheck()

is_people = file_check.fileExist(write_people.PEOPLE)
is_rest = file_check.fileExist(write_rest.RANK)

def initFile():
    write_people.InitFileWriter(write_people.PEOPLE_FILE_LOCATION)
    write_rest.InitFileWriter(write_rest.RANKING_FILE_LOCATION)

if not is_people:
    initFile()

handle_people = robHandle.HandleRobot(write_people.PEOPLE_FILE_LOCATION)
handle_ranking = robHandle.HandleRobot(write_rest.RANKING_FILE_LOCATION)

talk = robTalk.Script()

people = robData.People()
rest = robData.Rest()

USER_ANSWER = ["yes", "no", 'y', 'n']

try:
    while True:
        people_text = handle_people.textChange()
        ranking_text = handle_ranking.textChange()

        user_answer = ""
        is_yes = False
        contents = ""
        template_text = ""

        for row in people_text:
            people.appendGroup(row[0], row[1])

        for row in ranking_text:
            rest.appendGroup(row[0], row[1])

        print(talk.blue(talk.welcome))
        name = input()

        
        if not people.isHadName(name):
            people.appendGroup(name, "1")

        else:
            template_text = string.Template(talk.welcome_back)
            contents = template_text.substitute(name = name)
            print(talk.yellow(contents))

            people.countPlus(name)

        
        if rest.isRestExist():
            template_text = string.Template(talk.recommand_script)
            recommand = rest.Name()
            contents = template_text.substitute(restaurant = recommand[0])
            print(talk.green(contents))
            user_answer = input()

            while True:

                if user_answer in USER_ANSWER:

                    if user_answer in USER_ANSWER[1] or user_answer in USER_ANSWER[3]:

                        if rest.isHadSecond():
                            template_text = string.Template(talk.recommand_script)
                            contents = template_text.substitute(restaurant = recommand[1])
                            print(talk.green(contents))
                            recommand = input()

                        else:
                            template_text = string.Template(talk.restaurant_script)
                            contents = template_text.substitute(name = name)
                            print(talk.green(contents))
                            recommand = input()
                    
                    
                    elif user_answer not in USER_ANSWER:
                        print("옳은 대답이 아닙니다. [yes/no] 또는 [y/n] 중에서 대답해주세요.")
                        user_answer = input()

                    else:
                        rest.countPlus(recommand)
                        break

                    
                    print(user_answer in USER_ANSWER)
                    if user_answer in USER_ANSWER:
                        rest.appendGroup(recommand, "1")
                        break


                else:
                    print("옳은 대답이 아닙니다. [yes/no] 또는 [y/n] 중에서 대답해주세요.")
                    user_answer = input()


        else:
            template_text = string.Template(talk.restaurant_script)
            contents = template_text.substitute(name = name)
            print(talk.green(contents))
            restaurant = input()
            rest.appendGroup(restaurant, "1")

        handle_people.saveFile(people.Group())
        rest.setGroupSorted()
        handle_ranking.saveFile(rest.Group())

        template_text = string.Template(talk.end)
        contents = template_text.substitute(name = name)
        print(talk.blue(contents))
        
        break


except Exception as ex:
    write_people.InitFileWriter(write_people.PEOPLE_FILE_LOCATION)
    print(ex)
