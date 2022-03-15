# 서드파티 라이브러리
from termcolor import colored

#print(colored('test', 'green'))

# how to wright import
# import collections, sys, os  # 비추
import collections
import os
import sys
 # 서드 파티 패키지 import 시 1줄 띄어서 작성 !
import termcolor
 # 자신의 패키지, 로컬 패키지 등 구분하기 - 순서는 알파벳 순
import packages

#print(collections.__file__)
#print(termcolor.__file__)
#print(packages.__file__)

#print(sys.path)

# __name__ and __main__
import config
import packages.talk.animal

def main():
    packages.talk.animal.sing()

if __name__ == '__main__':
    main()
    
print("third : ", __name__)