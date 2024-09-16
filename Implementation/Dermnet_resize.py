from PIL import Image,ImageFile
import os

def resize(img,new_wid):
    wid,hei = img.size
    ratio = hei/wid
    new_hei = int(ratio*new_wid)
    resized_image = img.resize((new_wid,new_hei))
    return resized_image

def resize_fix(img):
    resized_image = img.resize((100,100))
    return resized_image

ImageFile.LOAD_TRUNCATED_IMAGES = True
Dermnet_dir_path = '/home/sumon/Desktop/Dataset/Yoga_New_Dataset/'

for Dermnet in os.listdir(Dermnet_dir_path):
    os.makedirs('/home/sumon/Desktop/Dataset/Yoga_New_Dataset_Resized/'+Dermnet)
    for img_dir in os.listdir(Dermnet_dir_path+'/'+Dermnet):
        os.makedirs('/home/sumon/Desktop/Dataset/Yoga_New_Dataset_Resized/'+Dermnet+'/'+img_dir)
        pic_names = os.listdir(Dermnet_dir_path+Dermnet+'/'+img_dir)
        for img in pic_names:
            pic = Image.open(Dermnet_dir_path+Dermnet+'/'+img_dir+'/'+img)
            #pic = pic.convert('RGB')
            pic_resized = resize_fix(pic)
            pic_resized.save('/home/sumon/Desktop/Dataset/Yoga_New_Dataset_Resized/'+Dermnet+'/'+img_dir+'/'+img)
        pic_names = []




