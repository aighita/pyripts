import os
import shutil

# import tkinter

# # get target folder from command line
# print('Select target folder number or enter custom target folder\'s path:')
# print('1. C:\Users\Pc\Downloads')
# print('2. D:\Downloads')

target_folder = input('Enter target folder: ')

# if target_folder == '1':
#     target_folder = 'C:\Users\Pc\Downloads'
# elif target_folder == '2':
#     target_folder = 'D:\Downloads'

extensions = {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

# create folders for each extension type
newDirectories = 0
for extension in extensions:
    if not os.path.exists(os.path.join(target_folder, extension)):
        os.mkdir(os.path.join(target_folder, extension))
        newDirectories += 1

# move files
movedFiles = 0
for item in os.listdir(target_folder):
    if os.path.isfile(os.path.join(target_folder, item)):
        file_extension = item.split('.')[-1]
        shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, item.split('.')[-1]))
        movedFiles += 1

if newDirectories == 0:
    if movedFiles == 0:
        print('No new directories created and no files to be sorted')
else:
    if newDirectories > 0:
        if movedFiles == 0:
            print('Created {} new directories'.format(newDirectories))
            print('No files to be sorted')
        else :
            print('Created {} new directories and moved {} files'.format(newDirectories, movedFiles))

input('Press ENTER to exit...')
exit()