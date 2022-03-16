import os
import pathlib
import glob
import shutil

# 라이브러리 참고하여 상세히 사용하면 좋다.

# print(os.path.exists('test.txt')) 파일 존재 유무
# print(os.path.isfile('test.txt')) 파일인지 아닌지
# print(os.path.isdir('fileSys/design')) 파일이 디렉토리인지 아닌지
# os.rename('test.txt', 'renamed.txt') 파일 이름 변경
# os.symlink("renamed.txt", "symlink.txt") # 원래는 symlink.txt 의 내용을 바꾸면 renamed.txt의 내용도 바뀌나 지금은 에러 발생
# os.mkdir('test_dir') 폴더 생성
# os.rmdir('test_dir') 폴더 제거

# pathlib.Path('empty.txt').touch() 파일 생성 구버전
# os.remove("empty.txt") 파일 제거

# os.mkdir('test_dir') 
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir')) 디렉토리 내부 출력
# pathlib.Path('test_dir/test_dir2/empty.txt').touch() 
# print(glob.glob('test_dir/*')) 디렉토리에 어떠한 파일이 있는지 확인 * 를 통해 파일 내의 다른 파일들을 전부 조회
# * 없이 사용 시 해당 파일이 존재하는지, 없을 시 []으로 출력
# shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt') 디렉토리 내의 파일을 다른이름으로 복사
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.rmtree('test_dir') 파일의 내부 디렉토리 모두 삭제 복원은 힘들듯??

# print(os.getcwd()) pwd 같이 현재 디렉토리의 위치 출력