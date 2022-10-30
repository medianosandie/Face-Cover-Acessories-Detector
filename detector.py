from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import glob

import torch
import numpy as np
import cv2

class Window:

    def __init__(self, master):

        root.title("Detector")
        root.minsize(width=800, height=500)
        root.maxsize(width=800,height=500)

        self.master = master

        self.predict_vid_button = Button(master, text = "Video", width=18,height=4, command=self.predict_vid_Page)
        self.predict_img_button = Button(master, text = "Gambar", width=18,height=4, command=self.predict_img_Page)

        self.predict_vid_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.predict_img_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.model = torch.hub.load('ultralytics/yolov5','custom', path='best (1).pt', force_reload=True)

    def BackToMenu(self):
        root.title("Detector")
        self.Restore()
        self.predict_vid_button = Button(self.master, text = "Video", width=18,height=4, command=self.predict_vid_Page)
        self.predict_img_button = Button(self.master, text = "Gambar", width=18,height=4, command=self.predict_img_Page)

        self.predict_vid_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.predict_img_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def ResizeWithAspectRatio(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)   

    def predict_vid_Page(self):
        root.title("Predict Video")
        self.Restore()

        self.back_button = Button(self.master, text = "Back", width=18,height=4, command=self.BackToMenu)
        self.back_button.place(relx=0.1, rely=0.9, anchor=CENTER)
        
        cap = cv2.VideoCapture(1)
        while cap.isOpened():
            ret, frame = cap.read()

            # resize and flip the frame
            resize = self.ResizeWithAspectRatio(frame, width=850)
            flipped = cv2.flip(resize, 1)

            # make detections
            results = self.model(flipped)
            render_results = np.squeeze(results.render())
            
            cv2.imshow('predict', render_results)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()     
        
    def predict_img_Page(self):
        root.title("Predict Image")
        self.Restore()

        self.shuffle_img_button = Button(self.master, text = "Predict Image", width=18,height=4, command=self.detect_img)
        self.shuffle_img_button.place(relx=0.9, rely=0.9, anchor=CENTER)

        self.button_explore = Button(self.master,
                        text = "Browse Image Files",
                        width=18,height=4,
                        command = self.browseFiles)
        self.button_explore.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.back_button = Button(self.master, text = "Back", width=18,height=4, command=self.BackToMenu)
        self.back_button.place(relx=0.1, rely=0.9, anchor=CENTER)

        # Create a File Explorer label
        self.label_file_explorer = Label(self.master,
                            text = "Please select an image to be predicted",
                            width = 100, height = 4,
                            fg = "blue")
        self.label_file_explorer.place(relx=0.5, rely=0.5, anchor=CENTER)


    def browseFiles(self):
        self.filename = filedialog.askopenfilename(
                                    initialdir = os.getcwd(),
                                    title = "Select an image file",
                                    filetypes = [("Image Files",".jpg .jpeg .png")]
        )

        # Display Images With Tkinter’s Label Widget
        image1 = Image.open(self.filename)
        image1 = image1.resize((600, 400), Image.ANTIALIAS)

        # Create a photoimage object of the image in the path
        test = ImageTk.PhotoImage(image1)

        label = Label(image=test)
        label.image = test

        # Position image
        label.place(relx=0.5, rely=0.4, anchor=CENTER)      
        
    def Restore(self):
        for widgets in root.winfo_children():
            widgets.destroy()

    def detect_img(self):
        try:
            # make prediction
            results = self.model(self.filename)
            results_str = results

            # save prediction result as an image
            results_str.save()

            base_path = 'runs\detect'
            exp_dirs = os.listdir(base_path)

            # get the latest exp dir
            formatted_all_subdirs = [os.path.join(base_path,d) for d in exp_dirs]

            latest_dir = sorted(formatted_all_subdirs, key=lambda x: os.path.getctime(x), reverse=True)[0]

            # get the latest img file
            list_of_files = glob.glob(os.path.join(latest_dir,'*.jpg')) # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)

            predicted_img_path = latest_file

            # Display Images With Tkinter’s Label Widget
            image1 = Image.open(predicted_img_path)
            image1 = image1.resize((600, 400), Image.ANTIALIAS)

            # Create a photoimage object of the image in the path
            test = ImageTk.PhotoImage(image1)

            label = Label(image=test)
            label.image = test

            # Position image
            label.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        except AttributeError:
            self.label_file_explorer.configure(text="Can not predict! Image File still has not been selected\nPlease select an image to be predicted")

root = Tk()

run = Window(root)

root.mainloop()