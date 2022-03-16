import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('fileSys/test_dir')
    # z.write('fileSys/test_dir/test.txt')

    for f in glob.glob('fileSys/test_dir/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz2')

    with z.open('fileSys/test_dir/test.txt') as f:
        print(f.read())