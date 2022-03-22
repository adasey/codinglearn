import string
from roboter import robotHandler as robHandle
from roboter import robotData as robData
from roboter import robotTalk as robTalk
from roboter import robotWriter as robWrite

write_people = robWrite.RobotWriter()
write_rest = robWrite.RobotWriter()

write_people.InitFileWriter(write_people.PEOPLE_FILE_LOCATION)
write_rest.InitFileWriter(write_rest.RANKING_FILE_LOCATION)

handle_people = robHandle.HandleRobot(write_people.PEOPLE_FILE_LOCATION)
handle_ranking = robHandle.HandleRobot(write_rest.RANKING_FILE_LOCATION)

talk = robTalk.Script()

people = robData.Guest()
rest = robData.Guest()

USER_ANSWER = ["yes", "no", 'y', 'n']

while True:
    people_text = handle_people.textChange()
    ranking_text = handle_ranking.textChange()

    user_answer = ""
    is_yes = False
    contents = ""
    template_text = ""

    for row in ranking_text:
        rest.appendGroup(row[0], row[1])

    for row in people_text:
        people.appendGroup(row[0], row[1])

    print(talk.blue(talk.welcome))
    name = input()
    
    if not people.isHadName(name):
        people.appendGroup(name, "1")

    else:
        pass

    if rest.isRestExist():
        template_text = string.Template(talk.recommand_script)
        contents = template_text.substitute(restaurant = rest.Name()[1])
        print(talk.green(contents))
        user_answer = input()

    else:
        template_text = string.Template(talk.restaurant_script)
        contents = template_text.substitute(name = name)
        print(talk.green(contents))
        restaurant = input()

    rest.appendGroup(restaurant, "1")

    handle_people.saveFile(people.Group())
    handle_ranking.saveFile(rest.Group())

    template_text = string.Template(talk.end)
    contents = template_text.substitute(name = name)
    print(talk.blue(contents))
    
    break
