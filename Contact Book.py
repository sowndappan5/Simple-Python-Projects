from tkinter import *
from tkinter import messagebox

# Initialize window
root = Tk()
root.geometry('750x600')
root.config(bg='#cce7ff')  # Light Blue background
root.title('PythonGeeks Contact Book')
root.resizable(0, 0)

# Updated contact list with Tamil Nadu-specific names and numbers
contactlist = [
    ['Arun Kumar', '9876543210'],
    ['Bala Raj', '9345678901'],
    ['Suresh Natarajan', '9448493847'],
    ['Mani Karthik', '9567890123'],
    ['Nisha Ravi', '9678901234'],
    ['Ramesh Kumar', '9765432109'],
    ['Priya Anbalagan', '9678321098'],
    ['Karthik Selvan', '9845763491'],
    ['Deepika Reddy', '9001234567']
]

Name = StringVar()
Number = StringVar()

# Create frame for listbox
frame = Frame(root)
frame.pack(side=RIGHT, padx=20)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Arial', 14), bg="#f4faff", width=25, height=20, borderwidth=2, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Function to get selected value
def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select a Contact")
    else:
        return int(select.curselection()[0])

# Function to add new contact
def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Contact Added Successfully!")
    else:
        messagebox.showerror("Error", "Please fill in both Name and Contact Number.")

# Function to update existing contact
def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Contact Updated Successfully!")
        EntryReset()
        Select_set()
    else:
        messagebox.showerror("Error", "Please fill in the fields or select a contact.")

# Reset the entry fields
def EntryReset():
    Name.set('')
    Number.set('')

# Function to delete selected contact
def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'Are you sure you want to delete this contact?')
        if result:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select a contact.')

# Function to view selected contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

# Function to exit the application
def EXIT():
    root.destroy()

# Function to refresh the contact list
def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

Select_set()

# Label for Name field
Label(root, text='Name', font=("Arial", 20, "bold"), bg='#4caf50', fg='white').place(x=30, y=30)
Entry(root, textvariable=Name, width=35, font=("Arial", 14), borderwidth=2, relief="solid").place(x=200, y=30)

# Label for Contact No. field
Label(root, text='Contact No.', font=("Arial", 20, "bold"), bg='#4caf50', fg='white').place(x=30, y=80)
Entry(root, textvariable=Number, width=35, font=("Arial", 14), borderwidth=2, relief="solid").place(x=200, y=80)

# Buttons with rounded corners and hover effects
def button_hover(event, button):
    button.config(bg="#81c784")

def button_leave(event, button):
    button.config(bg="#66bb6a")

# Add Contact button
add_button = Button(root, text="ADD CONTACT", font='Arial 16 bold', bg='#66bb6a', fg='white', width=20, height=2, command=AddContact)
add_button.place(x=50, y=140)
add_button.bind("<Enter>", lambda e, b=add_button: button_hover(e, b))
add_button.bind("<Leave>", lambda e, b=add_button: button_leave(e, b))

# Edit Contact button
edit_button = Button(root, text="EDIT CONTACT", font='Arial 16 bold', bg='#66bb6a', fg='white', width=20, height=2, command=UpdateDetail)
edit_button.place(x=50, y=200)
edit_button.bind("<Enter>", lambda e, b=edit_button: button_hover(e, b))
edit_button.bind("<Leave>", lambda e, b=edit_button: button_leave(e, b))

# Delete Contact button
delete_button = Button(root, text="DELETE CONTACT", font='Arial 16 bold', bg='#f44336', fg='white', width=20, height=2, command=Delete_Entry)
delete_button.place(x=50, y=260)
delete_button.bind("<Enter>", lambda e, b=delete_button: button_hover(e, b))
delete_button.bind("<Leave>", lambda e, b=delete_button: button_leave(e, b))

# View Contact button
view_button = Button(root, text="VIEW CONTACT", font='Arial 16 bold', bg='#42a5f5', fg='white', width=20, height=2, command=VIEW)
view_button.place(x=50, y=320)
view_button.bind("<Enter>", lambda e, b=view_button: button_hover(e, b))
view_button.bind("<Leave>", lambda e, b=view_button: button_leave(e, b))

# Reset button
reset_button = Button(root, text="RESET FIELDS", font='Arial 16 bold', bg='#ffeb3b', fg='black', width=20, height=2, command=EntryReset)
reset_button.place(x=50, y=380)
reset_button.bind("<Enter>", lambda e, b=reset_button: button_hover(e, b))
reset_button.bind("<Leave>", lambda e, b=reset_button: button_leave(e, b))

# Exit button
exit_button = Button(root, text="EXIT", font='Arial 18 bold', bg='#e57373', fg='white', width=20, height=2, command=EXIT)
exit_button.place(x=250, y=470)
exit_button.bind("<Enter>", lambda e, b=exit_button: button_hover(e, b))
exit_button.bind("<Leave>", lambda e, b=exit_button: button_leave(e, b))

root.mainloop()
