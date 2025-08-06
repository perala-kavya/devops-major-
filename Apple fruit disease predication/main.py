from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model('weights.best.hdf5')


bgcolor="white"

root=Tk()
root.title("Apple disease detection")
root.geometry("750x500+150+180")
root.resizable(False,False)
root.configure(bg=bgcolor)

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("JPG File","*.jpg")
                                                                                                   ,("PNG file","*.jpg"),("All file ","how are you .txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

    



def check():
    # img_path = '9.jpg'  # Replace with the path to your image
    img = image.load_img(filename, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)  # Add a batch dimension
    img = img / 255.0  # Normalize pixel values




    prediction = model.predict(img)
    print(prediction)
    prediction1=format(prediction[0][0], 'f')
    prediction2=format(prediction[0][1], 'f')
    prediction3=format(prediction[0][2], 'f')
    prediction4=format(prediction[0][3], 'f')
    print(prediction1)
    print(prediction2)
    print(prediction3)
    print(prediction4)

    a=prediction1[:len(prediction1)-4]
    b=prediction2[:len(prediction2)-4]
    c=prediction3[:len(prediction3)-4]
    d=prediction4[:len(prediction4)-4]

    print(a)
    print(b)
    print(c)
    print(d)


    largest=max(a,b,c,d)
    print("largest number is :",largest)

    if b==largest:
        print("Apple is healthy")
        print(float(largest)*100)
        result.config(text=f"The apple fruit appears to be healthy {float(largest)*100}%")
    else:
        print("It contain disease")
        result.config(text="The apple fruit appears to be diseased.")
            

    

    


   
    
    
    
    
    

#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg=bgcolor).place(x=10,y=0)

Label(root,text="Apple Disease Detection",bg=bgcolor,fg="#e11e40",font="arial 25 bold").place(x=100,y=20)

#first frame
f=Frame(root,bd=3,bg="#ededed",width=340,height=280,relief=GROOVE)
f.place(x=10,y=140)

lbl=Label(f,bg="#ededed")
lbl.place(x=40,y=10)


#Second frame 
result=Label(root,fg="black",font="arial 12",bg=bgcolor)
result.place(x=350,y=300)


####Ending second frame######

#third frame
frame3=Frame(root,bd=3,bg=bgcolor,width=330,height=100,relief=GROOVE)
frame3.place(x=370,y=140)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=20)
Button(frame3,text="Check",width=10,height=2,bg="lightgreen",font="arial 14 bold",command=check).place(x=180,y=20)






root.mainloop()
