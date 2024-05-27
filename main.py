from tkinter import *
from tkinter import messagebox, filedialog
import qrcode


# Functioning Part
def generate():
    global qrImage
    data = dataEntry.get()
    backColor = backColorEntry.get()
    foreColor = foreColorEntry.get()
    if backColor == "":
        backColor = "white"
    if foreColor == "":
        foreColor = "black"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    try:
        img = qr.make_image(fill_color=foreColor, back_color=backColor)
    except:
        messagebox.showerror("Error", "Color names are not correct !!!")
        return 0
    else:
        img = img.resize((270, 270))
        img.save("abc.png")
        qrImage = PhotoImage(file="abc.png")
        qrImageLabel.config(image=qrImage)
        return img


def download():
    img = generate()
    if img == 0:
        messagebox.showerror("Error", "File is not downloadable !!!")
    else:
        path = filedialog.asksaveasfilename(defaultextension="png")
        img.save(path)
        messagebox.showinfo("Success", "QR code downloaded successfully...")


# GUI Part
root = Tk()
root.title("QR Generator")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap("qr-code.ico")
# ========================== MAIN HEADING ========================
headLabel = Label(root, text="Q R    G E N E R A T O R", font=("Georgia", 25, "bold"), background="deep sky blue",
                  foreground="white")
headLabel.pack(fill=X, ipady=8)

# ========================= INPUT FRAME ==========================
inputLabelFrame = LabelFrame(root, background="slate gray")
inputLabelFrame.pack(fill=X, pady=5)

dataLabel = Label(inputLabelFrame, text="Link / message for QR code :", font=("Comic Sans MS", 18, "bold"),
                  background="slate gray", foreground="Yellow")
dataLabel.grid(row=0, column=0, padx=25, pady=15, sticky=E)
dataEntry = Entry(inputLabelFrame, font=("Comic Sans MS", 12), background="gray", foreground="blue", width=35)
dataEntry.grid(row=0, column=1, ipady=4)

backColorLabel = Label(inputLabelFrame, text="Background color (Optional) :", font=("Comic Sans MS", 18, "bold"),
                       background="slate gray", foreground="yellow")
backColorLabel.grid(row=1, column=0, padx=25, pady=15, sticky=E)
backColorEntry = Entry(inputLabelFrame, font=("Comic Sans MS", 12), background="gray", foreground="white", width=35)
backColorEntry.grid(row=1, column=1, ipady=4, padx=5)

foreColorLabel = Label(inputLabelFrame, text="Foreground color (Optional) :", font=("Comic Sans MS", 18, "bold"),
                       background="slate gray", foreground="yellow")
foreColorLabel.grid(row=2, column=0, padx=25, pady=15, sticky=E)
foreColorEntry = Entry(inputLabelFrame, font=("Comic Sans MS", 12), background="gray", foreground="white", width=35)
foreColorEntry.grid(row=2, column=1, ipady=4, padx=5)

# ======================== IMAGE SECTION =========================
imageLabelFrame = LabelFrame(root, background="seashell3")
imageLabelFrame.pack(fill=X, pady=5)

generateButton = Button(imageLabelFrame, text="Generate", font=("Comic Sans MS", 15, "bold"), background="gray",
                        activebackground="gray35", command=generate)
generateButton.place(x=180, y=80)

downloadButton = Button(imageLabelFrame, text="Download", font=("Comic Sans MS", 15, "bold"), background="gray",
                        activebackground="gray35", command=download)
downloadButton.place(x=180, y=200)

qrImage = PhotoImage(file="sample.png")
qrImageLabel = Label(imageLabelFrame, image=qrImage, background="black")
qrImageLabel.grid(row=0, column=0, padx=450, pady=15)

root.mainloop()
