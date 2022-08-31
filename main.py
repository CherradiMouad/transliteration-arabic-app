from ArabicTransliterator import ALA_LC_Transliterator
import mishkal.tashkeel.tashkeel as tashkeel
from tkinter import *
import webbrowser

# ***********************



transliterator = ALA_LC_Transliterator()

def transliterate(text, vocalize=True):
    voc = text
    if vocalize:
        vocalizer=tashkeel.TashkeelClass()
        voc = vocalizer.tashkeel(text)
    return transliterator.do(voc.strip())



# ***********************


verify = True

#//////////////////////////////////////// #Funct Guid Button

def btn_clicked1():
    webbrowser.open_new(r'arabic.pdf')

#//////////////////////////////////////// #Funct Arrows Button

def btn_clicked2():
    global verify
    if verify :
        entry0.delete(0,END)
        entry0.insert(0,"FRANCAIS")

        entry1.delete(0,END)
        entry1.insert(0,"ARABE")
        verify = False
    else :
        entry0.delete(0,END)
        entry0.insert(0,"ARABE")

        entry1.delete(0,END)
        entry1.insert(0,"FRANCAIS")
        verify = True

#//////////////////////////////////////// #Funct Trans Button

def btn_clicked3():
    Input=entry3.get()
    out=transliterate(Input,vocalize=True)
    entry2.delete(0,END)
    entry2.insert(0,out)


window = Tk()

#//////////////////////////////////////////////////////////// #BACKGROUND

window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    720.0, 511.0,
    image=background_img)

#//////////////////////////////////////////////////////////// # FR-AR

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    1101.0, 293.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    font=('Arial 24'),
    justify='center')



entry0.insert(0,"FRANCAIS")

entry0.place(
    x = 818.5, y = 276,
    width = 565.0,
    height = 33)


#//////////////////////////////////////////////////////////// # FR-AR

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    338.0, 293.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    font=('Arial 24'),
    justify='center')


entry1.insert(0,"ARABE")
entry1.place(
    x = 55.5, y = 276,
    width = 565.0,
    height = 33)

#//////////////////////////////////////////////////////////// #OUTPUT

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    716.0, 604.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    font=('Helvetica',30))



entry2.place(
    x = 26.0, y = 522,
    width = 1380.0,
    height = 162)

#//////////////////////////////////////////////////////////// # INPUT

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    720.0, 412.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    font=('Helvetica',30))


entry3.place(
    x = 30.0, y = 330,
    width = 1380.0,
    height = 162)


#////////////////////////////////////////////////////////////# Trans Button

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b0.place(
    x = 608, y = 715,
    width = 222,
    height = 63)

#////////////////////////////////////////////////////////////# Guid Button

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 3, y = 13,
    width = 81,
    height = 26)

#////////////////////////////////////////////////////////////# Tow Arrows Button

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 701, y = 276,
    width = 40,
    height = 39)

#////////////////////////////////////////////////////////////

window.resizable(False, False)
window.mainloop()