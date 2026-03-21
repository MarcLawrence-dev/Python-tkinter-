import tkinter as TK

root = TK.Tk()
root.title("Log in form")
root.geometry("500x500")

attempts = 0
def loginButton():
    userName = userNameEntry.get()
    userPassword = userPasswordEntry.get()
    
    global attempts
    if userName == "Marc" and userPassword == "123":
        label.config(text=f"Welcome, {userName}")
        attempts = 0
    else:
        attempts += 1
        label.config(text=f"Incorrect username or password. Attempt {attempts}/3")

        if attempts >= 3:
            label.config(text="Too many failed attempts. Please try again later.")
            root.destroy()

#Username and password labels and entry fields
NameLabel = TK.Label(root, text="Username: ")
NameLabel.grid(row=0, column=0)

userNameEntry = TK.Entry(root)
userNameEntry.grid(row=0, column=1)

PasswordLabel = TK.Label(root, text="Password: ")
PasswordLabel.grid(row=1, column=0)

userPasswordEntry = TK.Entry(root, show="*")
userPasswordEntry.grid(row=1, column=1)

#Login button field

LoginButton = TK.Button(root, text="Login", command=loginButton)
LoginButton.grid(row=2, column=1)

quitButton = TK.Button(root, text="Quit", command=root.quit)
quitButton.grid(row=2, column=2, columnspan=2)

label =TK.Label(root, text="")
label.grid(row=4, column=1, columnspan=2)


root.mainloop()