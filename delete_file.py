import os
import threading
import time

global files, number_files, excluding, excluded, stop

files = []
number_files = 0
excluding = 0
excluded = 0
stop = False
    
def print_run():
    while stop == False:
        print(f'Scanning.', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Scanning..', end='\r')        
        time.sleep(1)
        print(f'             ', end='\r')
        print(f'Scanning...', end='\r')
        time.sleep(1)
        print(f'             ', end='\r')

def search_for_files(path, searched_file):
    
    global files, number_files, excluding, stop

    for (dirpath, dirnames, filenames) in os.walk(path):        
        for file in filenames:
            if file == searched_file:
                files.append({"path": dirpath,
                              "file": file})
                excluding = excluding + 1
        number_files = number_files + len(filenames)

    stop = True

def confirm_exluding():

    global files, excluded

    print(f'>Will be excluded {excluding} files.')
    print(f'>Type "Yes" to complete deletion...')

    answer = input()

    if answer != 'Yes':
        print(f'>Canceled!')

    else:
        for file in files:
            full_file = file["path"] + '/' + file["file"]
            os.remove(full_file)
            print(f'>>>Total files deleted: { full_file }')
            excluded = excluded + 1

    print(f'>>>Deleted files: { excluded }')    

print('>>>This program searches for files to delete according to the name')        
print('>Which directory do you want to scan?')

directory = input()

print('>What is the file name?')

filename = input()

threading.Thread(target=print_run).start()

search_for_files(directory, filename)

print(f'>Total files deleted: { number_files }')

if len(files) > 0:
    confirm_exluding()
else:
    print(f'>>>No files found!!')
