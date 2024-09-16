from PIL import Image
import os

def resize(img,new_wid):
    wid,hei = img.size
    ratio = hei/wid
    new_hei = int(ratio*new_wid)
    resized_image = img.resize((new_wid,new_hei))
    return resized_image

def resize_fix(img):
    resized_image = img.resize((100,100,))
    return resized_image


img_dir_path = '/home/sumon/Desktop/Dataset/Yoga_New_Dataset/'
img_label = os.listdir(img_dir_path)

for pose_dir in img_label:
    print('dir :',pose_dir)
    os.makedirs('/home/sumon/Desktop/Dataset/Yoga_New_Dataset_Resized/'+pose_dir)
    pic_names = os.listdir(img_dir_path+pose_dir)
    for img in pic_names:
        print('image-name : ',img)
        pic = Image.open(img_dir_path+pose_dir+'/'+img)
        pic = pic.convert('RGB')
        #pic_resized = resize(pic,64)
        pic_resized = resize_fix(pic)
        print(pic_resized.size)
        print(img.split('.')[0])
        pic_resized.save('/home/sumon/Desktop/Dataset/Yoga_New_Dataset_Resized/'+pose_dir+'/'+img)
    pic_names = []




