import tkinter 

window = tkinter.Tk()

labelNama = tkinter.Label(window, text="Nama saya Fajar")
labelKampus = tkinter.Label(window, text="STIMIK TUNAS BANGSA")
labelKelas = tkinter.Label(window, text="Informatika A")
labelSmt = tkinter.Label(window, text="Semester 4")


labelNama.grid(row=0, column=0)
labelKampus.grid(row=1, column=1)
labelKelas.grid(row=2, column=0)
labelSmt.grid(row=3, column=1)


window.mainloop()