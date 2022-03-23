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

USER_ANSWER = ["yes", "no"]


def userRecommandRestaurant():
    template_text = string.Template(talk.restaurant_script)
    contents = template_text.substitute(name = name)
    print(talk.green(contents))
    restaurant = input()
    rest.appendGroup(restaurant, "1")

def recommandedRestaurant():
    template_text = string.Template(talk.recommand_script)
    contents = template_text.substitute(restaurant = rest.countList[0])
    print(talk.green(contents))
    answer = input()

    if isYesOrNo(answer):
        rest.countPlus(answer)

    else:
        
        if rest.isHadSecond():
            nextRecommanded()

        else:
            userRecommandRestaurant()


def isYesOrNo(answer):

    if answer in USER_ANSWER:
        
        if answer in USER_ANSWER[0]:
            return True

        elif answer in USER_ANSWER[1]:
            return False

    else:
        print("잘못된 답변입니다. [yes/no, y/n] 중에서 답변해주세요.")
        answer = input()
        return isYesOrNo(answer)

def nextRecommanded():
    template_text = string.Template(talk.recommand_script)
    contents = template_text.substitute(restaurant = rest.countList[1])
    print(talk.green(contents))
    answer = input()
    rest.countPlus(answer)


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
            recommandedRestaurant()

        else:
            userRecommandRestaurant()


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
