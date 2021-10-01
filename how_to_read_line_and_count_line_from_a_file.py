lines = []
with open('/content/drive/MyDrive/Dataset/imagenet100/text_file/imgnet_all_2.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    # print(f'line {count}: {line}')
    # break
print(count)
