from termcolor import colored

class Script(object):
    welcome = """\
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        어서오세요. ROBOT 레스토랑 추천 서비스 입니다.

        우선 이름을 말해주세요.
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """

    restaurant_script = """\
        ==============================================================
        $name 씨, 좋아하시는 레스토랑의 이름은 무엇인가요?
        ==============================================================
    """

    recommand_script = """\
        ==============================================================
        추천해드리는 레스토랑은 $restaurant 입니다.
        이 레스토랑을 좋아하시나요? [yes/no]
        ==============================================================
    """

    end = """\
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        $name 씨, 감사합니다.

        좋은 하루 보내세요!
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """

    def blue(script):
        return colored(script, 'blue')

    def green(script):
        return colored(script, 'green')

