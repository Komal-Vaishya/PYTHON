from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()


if __name__ == '__main__':
    with genericFileFunction ('./file.txt', 'w') as f:
        print ('Middle')
        f.write ('Hello from the function')

    with genericFileFunction ('./file.txt', 'r') as f:
        print ('Middle')
        content = f.read()
        print("read file content",content)
    
    with genericFileFunction('./file.txt', 'a') as f:
        print('Appending to the file...')
        f.write('This is appended text!\n')

    with genericFileFunction('./file.txt', 'r') as f:
        print('Reading after append operation...')
        content = f.read()
        print('Final content in the file:', content)