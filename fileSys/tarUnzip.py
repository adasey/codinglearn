import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('fileSys/test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    #tr.extractall(path='test_tar')
    with tr.extractfile('fileSys/test_dir/sub_dir/sub.txt') as f:
        print(f.read())