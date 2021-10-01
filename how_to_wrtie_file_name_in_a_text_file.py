import os
all_files_train_x3 = []
for dirpath, dirnames, files in os.walk('imagenet100/'): # directory
    # print(f'Found directory: {dirpath}')
    # print(f'Directory Name: {dirnames}')
    # print(dirpath.split("/")[-1])
    if dirpath.split("/")[-1] not in ['imagemet', 'text_file', 'train.X1', 'train.X2', 'train.X3', 'train.X4', 'val.X']:
        for file_name in files:
            if file_name.split('.')[-1] == "JPEG":
                all_files_train_x3.append(dirpath + '/' + file_name)
                # print(dirpath + '/' + file_name, file=open('imgnet6.txt', 'a') )  

                # print(file_name)
with open('imgnet5.txt', 'a')  as f:
    f.write('\n'.join(all_files_train_x3))
    # f.writelines(all_files_train_x3)
