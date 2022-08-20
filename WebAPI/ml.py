import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from numpy import asarray
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import plotly.express as px
from PIL import Image
import pytesseract as pt
import plotly


class ML_Model:
    def image_preprocessing(self,img):
        model= load_model("object_detection_1.h5")
        image_org = Image.open(img)
        image = np.array(image_org,dtype=np.uint8)
        image1 = image_org.resize((224,224),Image.ANTIALIAS)

        image_arr_224 = img_to_array(image1)/255.0 
        h,w,d = image.shape
        test_arr = image_arr_224.reshape(1,224,224,3)
        
        coords = model.predict(test_arr)
        denorm = np.array([w,w,h,h])
        coords = coords * denorm
        coords = coords.astype(np.int32)
        xmin, xmax,ymin,ymax = coords[0]
        pt1 =(xmin,ymin)
        pt2 =(xmax,ymax)
        print(pt1, pt2)
        cv2.rectangle(image,pt1,pt2,(0,255,0),3)
        fig = px.imshow(image)
        fig.update_layout(width=700, height=500, margin=dict(l=10, r=10, b=10, t=10),xaxis_title='pred')
        plotly.offline.plot(fig, filename='fig1.png')
        image3 = np.array(image_org,dtype=np.uint8)
        xmin ,xmax,ymin,ymax = coords[0]
        roi = image3[ymin:ymax,xmin:xmax]
        fig = px.imshow(roi)
        fig.update_layout(width=350, height=250, margin=dict(l=10, r=10, b=10, t=10),xaxis_title='Cropped image')
        plotly.offline.plot(fig, filename='fig2.png')
        import easyocr
        reader = easyocr.Reader(['en'], gpu= False)
        result = reader.readtext(roi)
        print(result[0][1])
        return {'license': result[0][1]}
    
        