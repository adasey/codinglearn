import os
import subprocess

# os.system('dir') 해당 기능을 이용해 프롬프트의 dir 기능 사용가능
#subprocess.run(['dir', '-h'])
# r = subprocess.run(['ipconfig'])
# print(r.returncode) # 해당 코드를 이용해 cmd의 명령어 코드를 출력할 수 있음
# subprocess.run('dir', shell=True, check=True) # 쉘로 넘어감 단 이걸 사용하면 rm -rf 를 사용해 전부 삭제해버릴 수 있음

p1 = subprocess.Popen(['dir'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE) # win환경에서는 실행 불가
p1.stdout.close()
output = p2.communicate() [0]
print(output)