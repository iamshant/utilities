import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#select any index from the whole dataset 
#single image has 5 captions
#so, select indx as: 1,6,11,16...
data_idx = 0

#eg path to be plot: ../input/flickr8k/Images/1000268201_693b08cb0e.jpg
image_path_ = '/content/drive/MyDrive/image_captioning/bangla_dataset/final_image_dataset_7468_with_all_RGB/' +df.iloc[data_idx,0]
img=mpimg.imread(image_path_)
plt.imshow(img)
plt.show()