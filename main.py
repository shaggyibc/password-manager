from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
SPECIAL_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*"]
LETTERS_CAP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U","V", "W", "X", "Y", "Z"]
LETTERS_LOW = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# -----------------------------DROPDOWN SEARCH FEATURE____________________________________#
def drop_search():
    entered_website = dropdown_var.get()
    try:
        with open("pwdata.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No file found", message="There is no saved data")
    else:
        if entered_website in data:
            search_email = data[entered_website]["email"]
            search_pass = data[entered_website]["password"]
            messagebox.showinfo(title=entered_website, message=f"Email:  {search_email}\nPassword:  {search_pass}")
        else:
            messagebox.showinfo(title="No Account found", message=f"There is no {entered_website} password")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    # nr_Cletters = int(input("How many Capital letters would you like in your password?\n"))
    # nr_lletters = int(input("How many lower letters would you like in your password?\n"))
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))

    password_list = []
    password_list = ([choice(LETTERS_CAP) for i in range(0, randint(4, 5))]) + \
                    ([choice(LETTERS_LOW) for i in range(0, randint(4, 5))]) + \
                    ([choice(SPECIAL_CHARS) for i in range(0, randint(2, 4))]) + \
                    ([choice(NUMBERS) for i in range(0, randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    entered_website = website_entry.get()
    entered_pw = password_entry.get()
    entered_email = email_entry.get()
    new_data = {entered_website: {
        "email": entered_email,
        "password": entered_pw
        }
    }

    if len(entered_website) == 0 or len(entered_pw) == 0:
        messagebox.showwarning(title="oops", message="Please fill in all required fields")
    else:
        try:
            with open("pwdata.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
                with open("pwdata.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
        else:
                data.update(new_data)
                with open("pwdata.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="red")
window.geometry("500x520")

canvas = Canvas(width=200, height=200, background="white", highlightthickness=8, highlightcolor="black")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("New Times Roman", 35, "bold"))
canvas.place(x=120, y=0)

# --------------------- creates drop down of saved sites -------------------
dropdown_label = Label(text="Saved Passwords", font=("Aerial", 10, "bold"), bg="red")
dropdown_label.place(x=0, y=285)
websites_saved = []
with open("pwdata.json", mode="r") as data_file:
    data = json.load(data_file)
    for key, value in data.items():
        websites_saved.append(key)
dropdown_var = StringVar(window)
dropdown_var.set(websites_saved[0])  # default value
saved_sites = OptionMenu(window, dropdown_var, *websites_saved)
saved_sites.config(width=25)
saved_sites.place(x=120, y=280)

dropdown_button = Button(text="Retrieve", command=drop_search, width=18, font=("Aerial", 9, "bold"))
dropdown_button.place(x=325, y=282)

website_label = Label(text="Website/Username", font=("Aerial", 9, "bold"), bg="red")
website_label.place(x=0, y=330)
website_entry = Entry(width=35)
website_entry.place(x=120, y=330)
website_entry.focus()

# search_button = Button(text="Search", command=search_pw, width=16, font=("Aerial", 9, "bold"))
# search_button.place(x=260, y=225)

email_label = Label(text="Email", font=("Aerial", 9, "bold"), bg="red")
email_label.place(x=70, y=370)
email_entry = Entry(width=35)
email_entry.insert(END, string="insservicesinc@gmail.com")
email_entry.place(x=120, y=370)

password_label = Label(text="Password", font=("Aerial", 9, "bold"), bg="red")
password_label.place(x=50, y=410)
password_entry = Entry(width=21)
password_entry.place(x=120, y=410)
password_button = Button(text="Generate Password", command=generate_pw, font=("Aerial", 9, "bold"))
password_button.place(x=260, y=405)

save_button = Button(text="Add", command=save_pw, width=29, font=("Aerial", 9, "bold"))
save_button.place(x=120, y=450)



window.mainloop()