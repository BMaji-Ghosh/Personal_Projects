import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image

class_names=['Normal','Pneumonia']
model=tf.keras.models.load_model('pneumonia prediction model.h5')
st.title('Pneumonia detection with chest X-Ray')
st.write('Upload the x-Ray report scanned Image to check whether it shows signs of pneumonia')

uploaded_file=st.file_uploader('choose an X-ray image....')
if uploaded_file is not None:
    img=Image.open(uploaded_file).convert('RGB')
    st.image(img,caption='Succesfully Uploaded Image',use_column_width=True)


    img=img.resize((32,32)) #resizing
    img_array=image.img_to_array(img)/255.0 #rescaling
    img_array=np.expand_dims(img_array,axis=0)# (32,32,3) -->(1,32,32,3)

    prediction=model.predict(img_array)
    confidence=float(prediction[0][0])

    if confidence>0.5:
        st.error(f'prediction : Pneumonia| Model Confidence :{round(confidence*100,2)}')
    else:
        st.error(f'prediction : Pneumonia| Model Confidence :{round(confidence*100,2)}')    



