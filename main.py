import tkinter as tk
from tkinter import messagebox
import sqlite3
import mysql.connector

def check_database():
    try:
        # Connect to MySQL database
        mysql_conn = mysql.connector.connect(
            host="localhost",
            port="3307",  # Default MySQL port for XAMPP is 3306
            user="root",
            passwd="",
            database="login"  # Changed database name to "login"
        )

        # Check if the table 'admin' exists
        mysql_cursor = mysql_conn.cursor()
        mysql_cursor.execute("SHOW TABLES")
        tables = [table[0] for table in mysql_cursor.fetchall()]
        if 'admin' not in tables:
            # If 'admin' table doesn't exist, create it
            mysql_cursor.execute('''
                CREATE TABLE admin (
                    id INT(11) AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            ''')
            mysql_conn.commit()

        # Close MySQL connection
        mysql_conn.close()
        return True

    except mysql.connector.Error as e:
        print("MySQL error:", e)
        messagebox.showerror("Error", f"MySQL error: {e}")
        return False

def handle_admin_interaction(email_entry, username_entry, password_entry, create=False):
    # Database check
    if not check_database():
        return

    username = username_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not email:
        messagebox.showerror("Error", "Please fill out Email.")
    elif not username:
        messagebox.showerror("Error", "Please fill out Username.")
    elif not password:
        messagebox.showerror("Error", "Please fill out Password.")
    else:
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('login')  # Changed SQLite database name to "login.db"
            cursor = conn.cursor()

            # Check if the username already exists
            cursor.execute('SELECT * FROM admin WHERE username = ?', (username,))
            existing_admin = cursor.fetchone()

            if create:
                if existing_admin:
                    messagebox.showerror("Error", "Username already exists. Please choose a different username.")
                else:
                    # Add the new admin account to the SQLite database
                    cursor.execute('INSERT INTO admin (username, email, password) VALUES (?, ?, ?)',
                                   (username, email, password))
                    conn.commit()
                    messagebox.showinfo("Success", "New admin account created successfully!")
            else:  # Admin login
                if not existing_admin:
                    messagebox.showerror("Error", "Admin not found. Please check your credentials.")
                else:
                    saved_password = existing_admin[2]  # Fetch the password from the database
                    if password != saved_password:
                        messagebox.showerror("Error", "Incorrect password. Please try again.")
                    else:
                        messagebox.showinfo("Success", "Admin logged in successfully!")

            # Close the connection
            conn.close()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            messagebox.showerror("Error", f"SQLite error: {e}")

def show_admin_login_frame():
    root.destroy()  # Close the main window
    admin_login_window = tk.Tk()  # Create the admin login frame
    admin_login_window.title("Admin Login")
    admin_login_window.geometry("500x500")
    admin_login_window.configure(bg='blue')

    # Add widgets for admin login (e.g., labels, entries, buttons)
    # Example:
    admin_label = tk.Label(admin_login_window, text="Admin Login", bg='blue', fg='white')
    admin_label.pack()

    # Create labels, text boxes, buttons, etc. (existing code)
    # Copy and paste from the existing Admin Account System design...

    # Create labels
    email_label = tk.Label(admin_login_window, text="Email:", bg='blue', fg='white')
    email_label.place(relx=0.5, rely=0.3, anchor='center')

    username_label = tk.Label(admin_login_window, text="Username:", bg='blue', fg='white')
    username_label.place(relx=0.5, rely=0.4, anchor='center')

    password_label = tk.Label(admin_login_window, text="Password:", bg='blue', fg='white')
    password_label.place(relx=0.5, rely=0.5, anchor='center')

    # Create text boxes
    email_entry = tk.Entry(admin_login_window)
    email_entry.place(relx=0.5, rely=0.35, anchor='center')

    username_entry = tk.Entry(admin_login_window)
    username_entry.place(relx=0.5, rely=0.45, anchor='center')

    password_entry = tk.Entry(admin_login_window, show="*")
    password_entry.place(relx=0.5, rely=0.55, anchor='center')

    # Create button
    create_button = tk.Button(admin_login_window, text="Login",
                              command=lambda: handle_admin_interaction(email_entry, username_entry, password_entry),
                              bg='white', fg='blue')
    create_button.place(relx=0.5, rely=0.7, anchor='center')

    # Create forgot password label
    forgot_password_label = tk.Label(admin_login_window, text="Forgot Password?", bg='blue', fg='white', cursor="hand2")
    forgot_password_label.place(relx=0.5, rely=0.75, anchor='center')
    forgot_password_label.bind("<Button-1>", lambda event: show_forgot_password_form())

    # Show Password Checkbox
    show_password_var = tk.BooleanVar()
    show_password_checkbox = tk.Checkbutton(admin_login_window, text="Show Password", variable=show_password_var,
                                            command=lambda: password_entry.config(
                                                show="" if show_password_var.get() else "*"), bg='blue', fg='white',
                                            selectcolor='blue')
    show_password_checkbox.place(relx=0.5, rely=0.85, anchor='center')


def show_forgot_password_form():
    # Function to display the forgot password form
    forgot_password_window = tk.Toplevel(root)
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("400x400")

    # Set background color for the forgot password form
    forgot_password_window.configure(bg='#006666')

    # Label and entry for username
    username_label = tk.Label(forgot_password_window, text="Username:", bg='#006666', fg='white')
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    username_entry = tk.Entry(forgot_password_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Button for searching username
    search_username_btn = tk.Button(forgot_password_window, text="Search",
                                    command=lambda: search_username(username_entry.get(), question_entry))
    search_username_btn.grid(row=0, column=2, padx=10, pady=10)

    # Label for question
    question_label = tk.Label(forgot_password_window, text="Question:", bg='#006666', fg='white')
    question_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # Entry for displaying security question
    question_entry = tk.Entry(forgot_password_window, state="readonly", width=23)
    question_entry.grid(row=1, column=1, padx=10, pady=10)

    # Label and entry for answer
    answer_label = tk.Label(forgot_password_window, text="Answer:", bg='#006666', fg='white')
    answer_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    answer_entry = tk.Entry(forgot_password_window)
    answer_entry.grid(row=2, column=1, padx=10, pady=10)

    # Label and entry for new password
    new_password_label = tk.Label(forgot_password_window, text="New Password:", bg='#006666', fg='white')
    new_password_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    new_password_entry = tk.Entry(forgot_password_window, show="*")
    new_password_entry.grid(row=3, column=1, padx=10, pady=10)

    # Buttons for save and back
    save_button = tk.Button(forgot_password_window, text="Save",
                            command=lambda: save_password(username_entry.get(), answer_entry.get(), new_password_entry.get()))
    save_button.grid(row=4, column=1, padx=5, pady=10, sticky="e")
    back_button = tk.Button(forgot_password_window, text="Back", command=forgot_password_window.destroy)
    back_button.grid(row=4, column=2, padx=5, pady=10, sticky="w")

def search_username(username, question_entry):
    # This function would typically query the database to retrieve the security question associated with the username
    # For demonstration purposes, let's assume we found a security question
    question = "What is your pet's name?"
    question_entry.config(state="normal")
    question_entry.delete(0, tk.END)
    question_entry.insert(0, question)
    question_entry.config(state="readonly")

def save_password(username, answer, new_password):
    # This function would typically update the password in the database
    messagebox.showinfo("Success", "Password updated successfully!")

# Create the main window
root = tk.Tk()
root.title("Admin Account System")
root.geometry("500x500")
root.configure(bg='blue')  # Set background color to blue


# Create labels, text boxes, buttons, etc. (your existing code)...

# Create the "Login Admin" label
login_admin_label = tk.Label(root, text="Login Admin", bg='blue', fg='white', cursor="hand2")
login_admin_label.place(relx=1, rely=1, anchor='se', x=-10, y=-10)
login_admin_label.bind("<Button-1>", lambda event: show_admin_login_frame())

# Create labels
email_label = tk.Label(root, text="Email:", bg='blue', fg='white')
email_label.place(relx=0.5, rely=0.3, anchor='center')

username_label = tk.Label(root, text="Username:", bg='blue', fg='white')
username_label.place(relx=0.5, rely=0.4, anchor='center')

password_label = tk.Label(root, text="Password:", bg='blue', fg='white')
password_label.place(relx=0.5, rely=0.5, anchor='center')

# Create text boxes
email_entry = tk.Entry(root)
email_entry.place(relx=0.5, rely=0.35, anchor='center')

username_entry = tk.Entry(root)
username_entry.place(relx=0.5, rely=0.45, anchor='center')

password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.5, rely=0.55, anchor='center')

# Create button
create_button = tk.Button(root, text="Create", command=lambda: handle_admin_interaction(email_entry, username_entry, password_entry, create=True), bg='white', fg='blue')
create_button.place(relx=0.5, rely=0.7, anchor='center')

# Create forgot password label
forgot_password_label = tk.Label(root, text="Forgot Password?", bg='blue', fg='white', cursor="hand2")
forgot_password_label.place(relx=0.5, rely=0.75, anchor='center')
forgot_password_label.bind("<Button-1>", lambda event: show_forgot_password_form())

# Show Password Checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=lambda: password_entry.config(show="" if show_password_var.get() else "*"), bg='blue', fg='white', selectcolor='blue')
show_password_checkbox.place(relx=0.5, rely=0.85, anchor='center')

root.mainloop()

