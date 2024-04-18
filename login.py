from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Documents\Tkinter-Designer-master\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("400x300")
window.configure(bg="#FFFFFF")
window.title("Login")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=300,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

def make_acc(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if check_entry(username, password):
        text1 = Label(window, text="* You successfully made an account pls login")
        text1.place(x=85, y=140)
        window.after(3000, text1.destroy)
        return username, password
    else:
        return None, None
    
def check_entry(username, password):
    if not username or not password:
        text3 = Label(window, text="*Please fill in the information")
        text3.place(x=140, y=140)
        window.after(3000, text3.destroy)
        return False
    return True

def storage(username, password, accounts):
    stored = {"Username": username, "Password": password}
    accounts.append(stored)
    return False

def create_account():
    global accounts
    username, password = make_acc(username_entry, password_entry)
    if username and password:
        storage(username, password, accounts)
        print(accounts)
        for i, acc in enumerate(accounts, 1):
            print(f"{i}. Username: {acc['Username']}, Password: {acc['Password']}")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        canvas.delete(text2)
        button_1.destroy()

accounts = []
username_entry = Entry(window, bg="#FAF8F8", bd=0, font=("Inter", 12))
canvas.create_window(220, 60, window=username_entry)
password_entry = Entry(window, bg="#FAF8F8", bd=0, font=("Inter", 12), show="*")
canvas.create_window(220, 125, window=password_entry)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    text="Create an account",
    compound="center",  # Align text and image in the center
    borderwidth=0,
    highlightthickness=0,
    command=create_account,
    relief="flat"
)
button_1.place(
    x=50.0,
    y=172.0,
    width=300.0,
    height=30.0
)

def login(username, password):
    global accounts
    if len(accounts) > 0:
        stored_username = accounts[0]["Username"]
        stored_password = accounts[0]["Password"]
        if username == stored_username and password == stored_password:
            window.destroy()
            new_window = Tk()
            new_window.geometry("400x300")
            new_window.configure(bg="#FFFFFF")
            new_window.title("New Window")
            new_window.mainloop()
        else:
            text4 = Label(window, text="*Invalid email or password")
            text4.place(x=140, y=140)
            window.after(300, text4.destroy)
    else:
        print("No accounts created yet")

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    text="Login",
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(username_entry.get(), password_entry.get()),
    relief="flat"
)
button_2.place(
    x=50.0,
    y=222.0,
    width=300.0,
    height=30.0
)

text2 = canvas.create_text(
    150.0,
    179.0,
    anchor="nw",
    text="Create an account",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    150.0,
    230.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    190,
    0.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    40.0,
    51.0,
    anchor="nw",
    text="username: ",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    40.0,
    116.0,
    anchor="nw",
    text="password: ",
    fill="#000000",
    font=("Inter", 14 * -1)
)

window.resizable(False, False)
window.mainloop()
