'''
Saya Kahmidah Ahmad Syauqi mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class App(Tk):
    # contructor
    def __init__(self, name, *args, **kwargs):
        Tk.__init__(self, name, *args, **kwargs)
        self.title("Form")
        self.newSubmitted = False

    # frame
        self.left_fr = Frame(self, bg='#c4ffd2', width=388, height=400, padx=10, pady=20)
        self.left_fr.grid(row=0, column=0)
        self.left_fr.grid_propagate(0)

        self.rigth_fr = Frame(self, bg='#ffffff', width=255, height=400, padx=5, pady=10)
        self.rigth_fr.grid(row=0, column=1)
        self.rigth_fr.grid_propagate(0)

    # in left frame
        self.frames = {}
        for F in (Form, SeeSbm):
            frame = F(self.left_fr, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[F] = frame
        self.show_leftFr(Form)

    # in rigth frame
        ## App name
        self.appName = Label(self.rigth_fr, text=name, bg='#ffffff', font=("Arial", 16, "bold")).grid(row=0, column=0, padx=20, pady=0, sticky=W)
        ## short descripition
        self.shortDesc = Label(self.rigth_fr, text="The app for the biggest art contest of\nthe century", bg='#ffffff').grid(row=1, column=0, padx=20, pady=5, sticky=W+E)
        ## button see all submission
        self.btnSeeAll = Button(self.rigth_fr, text="SEE ALL SUBMISSION", command=self.seeAll)
        self.btnSeeAll.grid(row=2, column=0, padx=20, pady=5, sticky=W+E)
        ## button clear submission
        self.btnClear = Button(self.rigth_fr, text="CLEAR SUBMISSION", command=self.clear).grid(row=3, column=0, padx=20, pady=5, sticky=W+E)
        ## button about
        self.btnAbout = Button(self.rigth_fr, text="ABOUT", command=self.about).grid(row=4, column=0, padx=20, pady=5, sticky=W+E)
        ## button exit
        self.btnExit = Button(self.rigth_fr, text="EXIT", command=self.exit).grid(row=6, column=0, padx=20, pady=5, sticky=W+E)

    # a function to indicate whether the user has ever newSubmitted data
    def isNewSubmitted(self):
        return self.newSubmitted

    # function move to other frame in left frame
    def show_leftFr(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # function submit
    def submit(self):
        data = self.frames[Form].getData()
        if((data["entry1"]=="") or (data["entry2"]=="") or (data["inputDD"]=="Select your region") or ((data["inputCB"][0]==False ) and (data["inputCB"][1]==False ) and (data["inputCB"][2]==False )) or (data["radiobtn"] == "X") or (data["filename"] == None)):
            mb.showwarning("Warning!!!", "Please fill in all the blanks!")
        else:
            ## add to record data
            frame = self.frames[SeeSbm]
            frame.addItem(data)
            self.frames.update(SeeSbm = frame)
            ## clear form
            frame = self.frames[Form]
            frame.clearForm()
            self.frames.update(Form = frame)
            ## change newSubmitted property to true
            self.newSubmitted = True
            print(data)

    # function to update the items view on the canvas
    def seeAll(self):
        if self.isNewSubmitted() is True:
            #update frame see all submission's view
            frame = self.frames[SeeSbm]
            print(frame.items)
            frame.updateView()
            self.frames.update(SeeSbm = frame)
            ## change newSubmitted property to true
            self.newSubmitted = False
        #Bring to front frame see all submission
        self.title("See All Submission")
        self.show_leftFr(SeeSbm)
        self.btnSeeAll["text"] = "Back to form"
        self.btnSeeAll["command"] = self.showForm

    # function see all submission
    def showForm(self):
        #Bring to front frame form
        self.title("Form")
        self.show_leftFr(Form)
        self.btnSeeAll["text"] = "SEE ALL SUBMISSION"
        self.btnSeeAll["command"] = self.seeAll

    # function clear submission
    def clear(self):
        frame = self.frames[SeeSbm]
        if(frame.isEmpty() == True):
            mb.showinfo("Info", "Your data is empty")
        else:
            if mb.askokcancel("Clear all submission", "Are you sure?"):
                frame = SeeSbm(self.left_fr, self)
                frame.grid(row=0, column=0, sticky="nsew")
                print(frame.items)
                self.newSubmitted = True
                self.frames.pop(SeeSbm)
                self.frames[SeeSbm] = frame
                mb.showinfo("Info", "All data has been deleted successfully")

    # function about
    def about(self):
        mb.showinfo("About this app", "The CUBE art contest is the biggest art contest of this century involving all artists from all over the world. This contest covers 3 categories, namely nature, illustration, and modern.\nThis application will help you to save data on participants who take part in the CUBE art contest. You as an admin can add data to this application, view all data and also delete that data.\n\nHow to fill out the form:\n- Enter the participant's full name\n- Enter the title of the participant's artwork\n- Enter the participant region (Western part: America; Central part: Europe and Africa; Eastern part: Asia and Australia)\n- Enter the category of participant's artwork, it is allowed to choose more than 1\n- Enter the gender of the participant\n- Enter a photo of the participant's artwork\n- Click submit to save participants\nall rights reserved © 2021\nRegards\nSyauqi from Cube Group")

    # function exit
    def exit(self):
        if mb.askokcancel("Close the program", "Are you sure?"):
            self.destroy()

# left frame page form
class Form(Frame):
    # contructor
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='#c4ffd2')
        ## inputan 1
        self.label1 = Label(self, text='Full name', bg='#c4ffd2').grid(row=0, column=0, padx=20, pady=5, sticky=W)
        self.entry1 = Entry(self, width=35)
        self.entry1.grid(row=0, column=1, sticky=W)

        ## inputan 2
        self.label2 = Label(self, text='Title of artwork', bg='#c4ffd2').grid(row=1, column=0, padx=20, pady=5, sticky=W)
        self.entry2 = Entry(self, width=35)
        self.entry2.grid(row=1, column=1, sticky=W)

        ## dropdown menu
        self.optionsDD = ["Western", "Middle", "Eastern"] #opsi untuk dropdown menu
        self.inputDD = StringVar()
        self.inputDD.set("Select your region")

        self.label3 = Label(self, text='Region', bg='#c4ffd2').grid(row=2, column=0, padx=20, pady=5, sticky=W)
        self.dropdown = OptionMenu(self, self.inputDD, *self.optionsDD)
        self.dropdown.config(width=28)
        self.dropdown.grid(row=2, column=1, sticky=W)

        ## checkbox
        self.label4 = Label(self, text='Category', bg='#c4ffd2').grid(row=3, column=0, padx=20, pady=5, sticky=W)
        self.frame_cb = Frame(self, pady=5, bg='#c4ffd2')
        self.frame_cb.grid(row=3, column=1, sticky=W)
        self.optionsCB = ["Nature", "Illustration", "Modern"] #opsi untuk checkbox menu
        self.inputCB = []
        for i in range(3):
            self.inputCB.append(BooleanVar())
            self.inputCB[i].set(False)

        self.cb1 = Checkbutton(self.frame_cb, text = self.optionsCB[0], variable = self.inputCB[0], bg='#c4ffd2').grid(row=0, column=0, sticky=W)
        self.cb2 = Checkbutton(self.frame_cb, text = self.optionsCB[1], variable = self.inputCB[1], bg='#c4ffd2').grid(row=0, column=1, sticky=W)
        self.cb3 = Checkbutton(self.frame_cb, text = self.optionsCB[2], variable = self.inputCB[2], bg='#c4ffd2').grid(row=0, column=2, sticky=W)

        ## radio button
        self.label5 = Label(self, text='Sex', bg='#c4ffd2').grid(row=4, column=0, padx=20, pady=5, sticky=W)
        self.frame_rb = Frame(self, pady=5, bg='#c4ffd2')
        self.frame_rb.grid(row=4, column=1, sticky=W)
        self.radiobtn = StringVar()
        self.radiobtn.set("X")
        self.rb1 = Radiobutton(self.frame_rb, text = "Men", variable = self.radiobtn, value="Men", bg='#c4ffd2').grid(row=0, column=0, sticky=W)
        self.rb2 = Radiobutton(self.frame_rb, text = "Woman", variable = self.radiobtn, value="Woman", bg='#c4ffd2').grid(row=0, column=1, sticky=W)

        ## button open photo file
        self.btnOpenPhoto = Button(self, text="Open Photo File", command=self.openFile).grid(row=5, columnspan=2, padx=20, pady=5, sticky=W+E)
        self.filename = None

        ## button submit
        self.btnSubmit = Button(self, text="Submit", command=controller.submit).grid(row=6, columnspan=2, padx=20, pady=5, sticky=W+E)

    # function openFile
    def openFile(self):
        self.filename = fd.askopenfilename(initialdir="./", title="Select a photo file", filetypes=(("jpg file", "*.jpg"), ("png file", "*.png"), ("all file", "*.*")))

    # function get data from form
    def getData(self):
        data = {}
        data["entry1"] = self.entry1.get()
        data["entry2"] = self.entry2.get()
        data["inputDD"] = self.inputDD.get()
        data["inputCB"] = []
        data["optionsCB"] = []
        for i in range(3):
            data["inputCB"].append(self.inputCB[i].get())
            data["optionsCB"].append(self.optionsCB[i])
        data["radiobtn"] = self.radiobtn.get()
        data["filename"] = self.filename
        return data

    # function clear form
    def clearForm(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.inputDD.set("Select your region")
        for i in range(3):
            self.inputCB[i].set(False)
        self.radiobtn.set("X")
        self.filename = None

# left frame show all submission page
class SeeSbm(Frame):

    # contructor
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        Frame.__init__(self, parent, bg='#c4ffd2')
        self.items = []
        self.image = []

        canvas = Canvas(self, bg="yellow", width=345, height=340)
        xscrollBar = Scrollbar(self, orient = "horizontal", command=canvas.xview)
        xscrollBar.grid(row=1, column=0, sticky="we")
        yscrollBar = Scrollbar(self, orient = "vertical", command=canvas.yview)
        yscrollBar.grid(row=0, column=1, sticky="ns")

        self.scrollable_fr = Frame(canvas)
        self.scrollable_fr.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0,0), window=self.scrollable_fr, anchor="nw")
        canvas.configure(xscrollcommand=xscrollBar.set)
        canvas.configure(yscrollcommand=yscrollBar.set)
        canvas.grid(row=0, column=0)

        title = ["Full name", "Title of artwork", "Region", "Category", "Sex", "Photo of art"]
        for i in range(len(title)):
            mytext = Text(self.scrollable_fr, width=20, height=1, bg="yellow")
            mytext.grid(row=0, column=i, sticky="nsew")
            mytext.insert(1.0, title[i])
            mytext.configure(state="disabled")

    # function for update the items view on the canvas
    def updateView(self):
        for i in range(len(self.items)):
            col1 = Text(self.scrollable_fr, width=20, height=1, bg="yellow")
            col1.grid(row=i+1, column=0, sticky="nsew")
            col1.insert(1.0, self.items[i]["entry1"])
            col1.configure(state="disabled")

            col2 = Text(self.scrollable_fr, width=20, height=1, bg="yellow")
            col2.grid(row=i+1, column=1, sticky="nsew")
            col2.insert(1.0, self.items[i]["entry2"])
            col2.configure(state="disabled")

            col3 = Text(self.scrollable_fr, width=20, height=1, bg="yellow")
            col3.grid(row=i+1, column=2, sticky="nsew")
            col3.insert(1.0, self.items[i]["inputDD"])
            col3.configure(state="disabled")

            category = ""
            for j in range(3):
                if(self.items[i]["inputCB"][j] == True):
                    if(len(category) > 0):
                        category += ", "
                    category += self.items[i]["optionsCB"][j]
            col4 = Text(self.scrollable_fr, width=20, height=1, bg="yellow")
            col4.grid(row=i+1, column=3, sticky="nsew")
            col4.insert(1.0, category)
            col4.configure(state="disabled")

            col5 = Text(self.scrollable_fr, width=20, height=1, bg="yellow")
            col5.grid(row=i+1, column=4, sticky="nsew")
            col5.insert(1.0, self.items[i]["radiobtn"])
            col5.configure(state="disabled")

            self.image.append(ImageTk.PhotoImage(Image.open(self.items[i]["filename"]).resize((50,50), Image.ANTIALIAS)))
            col6 = Text(self.scrollable_fr, width=20, height=3, bg="yellow")
            col6.grid(row=i+1, column=5, sticky="nsew")
            col6.image_create(1.0, image = self.image[i])
            col6.configure(state="disabled")

    # function for add the item to property items
    def addItem(self, item):
        self.items.append(item)

    # function that indicates if property A is empty
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    

startApp = App("CUBE Art Contest")
startApp.mainloop()
