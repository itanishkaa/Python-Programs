#----------import libraries-------
import qrcode
from tkinter import *

#-----------create gui----------
root = Tk()
root.title("QR code generator")
root.geometry("400x400")

#--------------functions to use------------------
def qr_generator():
    
    qr_code = qrcode.QRCode(
        version=1,
        box_size=3
    )

    qr_code.add_data(text_box.get("1.0", "end"))
    qr_code.make(fit=True)

    qr_img = qr_code.make_image(fill_color='black', back_color='white')
    qr_img.save("qr_image.png")

Label(
    root,
    text="QR code generator",
    font=("Comic Sans MS", 16, "bold")

).pack(pady=10)

text_box = Text(
    root,
    width=45,
    height=17
)
text_box.pack(pady=3)

Button(
    root,
    text="Generate",
    command=qr_generator,
    font=("Comic Sans MS", 12)

).pack(pady=5)

root.mainloop()