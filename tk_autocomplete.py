from tkinter import *

root = Tk()

'''
def testfunc(arg):
    print(w.get())
    print(arg.__dir__())
    print(arg.char)

w = Entry(root);
w.bind("<KeyPress>", testfunc)
w.pack()

root.mainloop()
'''

inbox = []  # list for saving


# def set_string_var(from_string_var, to_string_var):
# print(from_string_var.get())
# to_string_var.set(from_string_var.get())
# return to_string_var


# def complete_text(arg):
# print(sv.get() + " test")
# w.config(text=sv.get())
# sv1.set(sv.get())
# sv.set(sv.get() + "TEST")
# e.icursor(len(sv.get()))
# return "break"

def complete_text(text):
    if text.startswith("Tom"):
        return "Tomorrow"
    return text


def save_entry(arg):
    print("SAVE ENTRY")
    inbox.append(sv.get())
    sv.set("")
    return "break"


def main():
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, s=sv: set_string_var(s))
    e = Entry(root, textvariable=sv)
    e.bind("<Tab>", complete_text)
    e.bind("<+>", save_entry)
    e.bind("<Escape>", quit)  # DEBUG
    e.focus_set()
    e.pack(fill='x')

    sv1 = StringVar()
    sv1.set("test")
    w = Label(root, text="test", textvariable=sv1)
    w.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
