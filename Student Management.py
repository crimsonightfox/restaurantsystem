import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


def main():
    def save_data():
        # Placeholder function to save data, you can implement the actual save functionality here
        print("Data saved!")

    def show_calendar():
        dob_calendar.place(relx=0, rely=1, anchor="sw")

    def select_date():
        selected_date = dob_calendar.get_date()
        dob_combo.set(selected_date)
        dob_calendar.place_forget()

    root = tk.Tk()
    root.title("Student Management")
    root.geometry("1093x550")

    # Calculate the position to center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - 1093) // 2 + 128  # Shifted 128 pixels from the left
    y_coordinate = (screen_height - 550) // 2 + 32  # Shifted 32 pixels from the top
    root.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    # Create a notebook (tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # First tab: Admissions
    admissions_tab = ttk.Frame(notebook)
    notebook.add(admissions_tab, text='Admissions')

    # Labels and Entries on the left side
    tk.Label(admissions_tab, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    first_name_entry = tk.Entry(admissions_tab)
    first_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(admissions_tab, text="Father's Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    father_name_entry = tk.Entry(admissions_tab)
    father_name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(admissions_tab, text="Father's Occupation:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    father_occupation_combo = ttk.Combobox(admissions_tab, values=["Engineer", "Doctor", "Teacher", "Others"])
    father_occupation_combo.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(admissions_tab, text="DOB:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    dob_combo = ttk.Combobox(admissions_tab)
    dob_combo.grid(row=3, column=1, padx=5, pady=5)
    dob_calendar = Calendar(admissions_tab)
    dob_calendar.place_forget()  # Initially hide the calendar
    dob_combo.bind("<Button-1>", lambda event: show_calendar())
    dob_calendar.bind("<<CalendarSelected>>", lambda event: select_date())

    tk.Label(admissions_tab, text="Course:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    course_combo = ttk.Combobox(admissions_tab, values=["Engineering", "Medicine", "Law", "Others"])
    course_combo.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(admissions_tab, text="Phone Number:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    phone_entry = tk.Entry(admissions_tab)
    phone_entry.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(admissions_tab, text="Landline Number:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    landline_entry = tk.Entry(admissions_tab)
    landline_entry.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(admissions_tab, text="Address:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
    address_entry = tk.Entry(admissions_tab, width=50)
    address_entry.grid(row=7, column=1, padx=5, pady=2, columnspan=2)  # Reduced pady to 2

    # Upload Button and Label
    upload_button = tk.Button(admissions_tab, text="Upload")
    upload_button.grid(row=8, column=3, padx=5, pady=5, sticky="e")

    upload_label = tk.Label(admissions_tab, text="Upload")
    upload_label.grid(row=8, column=4, padx=5, pady=5, sticky="w")

    save_button = tk.Button(admissions_tab, text="Save", command=save_data)
    save_button.grid(row=8, column=1, padx=5, pady=5, sticky="e")

    # Labels and Entries on the right side
    tk.Label(admissions_tab, text="Admission Date:").grid(row=0, column=3, padx=5, pady=5, sticky="e")
    admission_date_entry = tk.Entry(admissions_tab)
    admission_date_entry.grid(row=0, column=4, padx=5, pady=5)

    tk.Label(admissions_tab, text="Last Name:").grid(row=1, column=3, padx=5, pady=5, sticky="e")
    last_name_entry = tk.Entry(admissions_tab)
    last_name_entry.grid(row=1, column=4, padx=5, pady=5)

    tk.Label(admissions_tab, text="Mother's Name:").grid(row=2, column=3, padx=5, pady=5, sticky="e")
    mother_name_entry = tk.Entry(admissions_tab)
    mother_name_entry.grid(row=2, column=4, padx=5, pady=5)

    tk.Label(admissions_tab, text="Mother's Occupation:").grid(row=3, column=3, padx=5, pady=5, sticky="e")
    mother_occupation_combo = ttk.Combobox(admissions_tab,
                                           values=["Choose Occupation", "House Wife", "Nurse", "Secretary", "Engineer"])
    mother_occupation_combo.grid(row=3, column=4, padx=5, pady=5)

    tk.Label(admissions_tab, text="Gender:").grid(row=4, column=3, padx=5, pady=5, sticky="e")
    gender_frame = ttk.Frame(admissions_tab)
    gender_frame.grid(row=4, column=4, padx=5, pady=5, sticky="w")
    gender_var = tk.StringVar()
    male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
    male_radio.pack(side="left")
    female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
    female_radio.pack(side="left")

    tk.Label(admissions_tab, text="Section:").grid(row=5, column=3, padx=5, pady=5, sticky="e")
    section_combo = ttk.Combobox(admissions_tab, values=["Choose Section", "A", "B", "C", "D"])
    section_combo.grid(row=5, column=4, padx=5, pady=5)

    tk.Label(admissions_tab, text="Blood Group:").grid(row=6, column=3, padx=5, pady=5, sticky="e")
    blood_group_combo = ttk.Combobox(admissions_tab,
                                     values=["Choose Blood Group", "A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])
    blood_group_combo.grid(row=6, column=4, padx=5, pady=5)

    tk.Label(admissions_tab, text="Religion:").grid(row=7, column=3, padx=5, pady=5, sticky="e")
    religion_combo = ttk.Combobox(admissions_tab,
                                  values=["Choose Religion", "Christianity", "Islam", "Hinduism", "Buddhism",
                                          "Judaism"], width=15)
    religion_combo.grid(row=7, column=4, padx=5, pady=5, sticky="w")  # Adjusted sticky

    # Second tab: Search
    search_tab = ttk.Frame(notebook)
    notebook.add(search_tab, text='Search')

    # Labels and Entries on the left side
    tk.Label(search_tab, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    first_name_entry = tk.Entry(search_tab)
    first_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(search_tab, text="Father's Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    father_name_entry = tk.Entry(search_tab)
    father_name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(search_tab, text="Father's Occupation:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    father_occupation_combo = ttk.Combobox(search_tab, values=["Engineer", "Doctor", "Teacher", "Others"])
    father_occupation_combo.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(search_tab, text="DOB:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    dob_combo = ttk.Combobox(search_tab)
    dob_combo.grid(row=3, column=1, padx=5, pady=5)
    dob_calendar = Calendar(search_tab)
    dob_calendar.place_forget()  # Initially hide the calendar
    dob_combo.bind("<Button-1>", lambda event: show_calendar())
    dob_calendar.bind("<<CalendarSelected>>", lambda event: select_date())

    tk.Label(search_tab, text="Course:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    course_combo = ttk.Combobox(search_tab, values=["Engineering", "Medicine", "Law", "Others"])
    course_combo.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(search_tab, text="Phone Number:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
    phone_entry = tk.Entry(search_tab)
    phone_entry.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(search_tab, text="Landline Number:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
    landline_entry = tk.Entry(search_tab)
    landline_entry.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(search_tab, text="Address:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
    address_entry = tk.Entry(search_tab, width=50)
    address_entry.grid(row=7, column=1, padx=5, pady=2, columnspan=2)  # Reduced pady to 2

    # Table at the bottom
    table_frame = ttk.Frame(search_tab)
    table_frame.grid(row=9, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
    table = ttk.Treeview(table_frame, columns=("Sr.No", "Name", "Course"), show="headings")
    table.heading("Sr.No", text="Sr.No", anchor="center")
    table.heading("Name", text="Name", anchor="center")
    table.heading("Course", text="Course", anchor="center")
    table.column("#0", width=0, stretch=False)  # Hide the index column
    table.column("Sr.No", width=50, anchor="center", stretch=False)  # Make column uneditable and unmovable
    table.column("Name", width=200, anchor="center", stretch=False)  # Make column uneditable and unmovable
    table.column("Course", width=150, anchor="center", stretch=False)  # Make column uneditable and unmovable
    table.grid(row=0, column=0, sticky="nsew")
    table_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table_scroll.grid(row=0, column=1, sticky="ns")
    table['show'] = 'headings'
    table_scroll.grid(row=0, column=1, sticky="ns")
    table_scroll.configure(command=table.yview)

    # Disable resizing columns
    table.bind("<Motion>", lambda e: table.configure(cursor="arrow"))

    # Disable moving column headers
    table.bind("<Button-1>", lambda e: "break")

    # Buttons for Update, Delete, and Search
    update_button = tk.Button(search_tab, text="Update")
    update_button.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    delete_button = tk.Button(search_tab, text="Delete")
    delete_button.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    search_button = tk.Button(search_tab, text="Search")
    search_button.grid(row=8, column=2, padx=5, pady=5, sticky="w")

    # Labels and Entries on the right side
    tk.Label(search_tab, text="Admission Date:").grid(row=0, column=3, padx=5, pady=5, sticky="e")
    admission_date_entry = tk.Entry(search_tab)
    admission_date_entry.grid(row=0, column=4, padx=5, pady=5)

    tk.Label(search_tab, text="Last Name:").grid(row=1, column=3, padx=5, pady=5, sticky="e")
    last_name_entry = tk.Entry(search_tab)
    last_name_entry.grid(row=1, column=4, padx=5, pady=5)

    tk.Label(search_tab, text="Mother's Name:").grid(row=2, column=3, padx=5, pady=5, sticky="e")
    mother_name_entry = tk.Entry(search_tab)
    mother_name_entry.grid(row=2, column=4, padx=5, pady=5)

    tk.Label(search_tab, text="Mother's Occupation:").grid(row=3, column=3, padx=5, pady=5, sticky="e")
    mother_occupation_combo = ttk.Combobox(search_tab,
                                           values=["Choose Occupation", "House Wife", "Nurse", "Secretary", "Engineer"])
    mother_occupation_combo.grid(row=3, column=4, padx=5, pady=5)

    tk.Label(search_tab, text="Gender:").grid(row=4, column=3, padx=5, pady=5, sticky="e")
    gender_frame = ttk.Frame(search_tab)
    gender_frame.grid(row=4, column=4, padx=5, pady=5, sticky="w")
    gender_var = tk.StringVar()
    male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
    male_radio.pack(side="left")
    female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
    female_radio.pack(side="left")

    tk.Label(search_tab, text="Section:").grid(row=5, column=3, padx=5, pady=5, sticky="e")
    section_combo = ttk.Combobox(search_tab, values=["Choose Section", "A", "B", "C", "D"])
    section_combo.grid(row=5, column=4, padx=5, pady=5)

    tk.Label(search_tab, text="Blood Group:").grid(row=6, column=3, padx=5, pady=5, sticky="e")
    blood_group_combo = ttk.Combobox(search_tab,
                                     values=["Choose Blood Group", "A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])
    blood_group_combo.grid(row=6, column=4, padx=5, pady=5)

    tk.Label(search_tab, text="Religion:").grid(row=7, column=3, padx=5, pady=5, sticky="e")
    religion_combo = ttk.Combobox(search_tab,
                                  values=["Choose Religion", "Christianity", "Islam", "Hinduism", "Buddhism",
                                          "Judaism"], width=15)
    religion_combo.grid(row=7, column=4, padx=5, pady=5, sticky="w")  # Adjusted sticky

    root.mainloop()


if __name__ == "__main__":
    main()
