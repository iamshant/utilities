import os

# List all subdirectories using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)


data_file = 'home/data.txt'

# If the file exists, delete it
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')


all_files_train_x1 = []
for dirpath, dirnames, files in os.walk('/content/gdrive/MyDrive/Dataset/imagenet100/train.X1'):
    print(f'Found directory: {dirpath}')
    # for file_name in files:
    # print(file_name)
    # for dirpath, dirnames, files in os.walk('.'):
    # print(f'Found directory: {dirpath}')
    for file_name in files:
        all_files_train_x1.append(file_name)
        print(file_name)
