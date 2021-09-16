from tkinter import filedialog as fd
from tkinter import *
from geocoding_change import *

root = Tk()

root.title("군사좌표 생성기")
root.geometry("540x380")


def get_file_path():
    filename = fd.askopenfilename()
    ent_file_name.insert(0, filename)


btn_get_file = Button(root, padx=20, pady=20,
                      text="파일 불러오기", command=get_file_path)
btn_get_file.pack(side="top", fill="x")

ent_file_name = Entry(root)
ent_file_name.pack(fill="x")


btn_save_file = Button(root, padx=20, pady=20,
                       text="파일 생성하기", command=lambda: change_MGRS(ent_file_name.get()))
btn_save_file.pack(side="top", fill="x")

root.mainloop()
