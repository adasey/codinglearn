import string

#s = 
"""\
    
Hi. $name.

$contents

Have a good day
"""
# {name} 등과 다르게 완전히 읽기 전용으로 사용할 땐 template 사용 
# {}안의 변수를 우연히 바꾸게 될 수 있으므로 

with open('fileSys/design/email_template.txt') as f:
    t = string.Template(f.read()) # with에서 선언 시 지역변수가 아닌 외부에서도 참고가능

contents = t.substitute(name='Mike', contents='who are you')
print(contents)