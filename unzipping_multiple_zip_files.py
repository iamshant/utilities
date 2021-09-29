from zipfile import ZipFile
from tqdm import tqdm

file_name = "/content/gdrive/MyDrive/Dataset/imagenet100.zip"
target_path = "."

with ZipFile(file_name) as zf:
    for member in tqdm(zf.infolist(), desc='Extracting '):
        try:
            zf.extract(member, target_path)
        except zipfile.error as e:
            print(e)
