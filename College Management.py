import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkcalendar import Calendar
from tkinter import messagebox


def search_student():
    print("Searching student...")

def search_staff():
    print("Searching staff...")

def show_misc_management_frame():
    global misc_management_frame

    close_attendance_management()
    close_staff_management()
    close_fees_management()
    close_student_management()

    if 'misc_management_frame' in globals():
        misc_management_frame.destroy()
    misc_management_frame = tk.Toplevel(root)
    misc_management_frame.title("Miscellaneous Management")
    misc_management_frame.geometry("1093x550")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - 1076) // 2 + 128
    y_coordinate = (screen_height - 550) // 2 + 32
    misc_management_frame.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    notebook = ttk.Notebook(misc_management_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

    tabs = ["Student Data", "Staff Data", "Add Course", "Add Section", "Add Subject"]
    frames = [tk.Frame(notebook) for _ in range(len(tabs))]

    for i, tab in enumerate(tabs):
        notebook.add(frames[i], text=tab)

    staff_tab = frames[1]
    search_label = tk.Label(staff_tab, text="Search by Name:")
    search_label.grid(row=0, column=0, padx=10, pady=10)

    search_entry = tk.Entry(staff_tab)
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button = tk.Button(staff_tab, text="Search", command=search_staff)
    search_button.grid(row=0, column=2, padx=10, pady=10)

    table = ttk.Treeview(staff_tab, columns=("Name", "Qualification", "Subject", "Phone Number", "Email Address"), show="headings")
    table.grid(row=1, column=0, columnspan=3, padx=10, pady=(10, 30), sticky="nsew")

    for column in table['columns']:
        table.heading(column, text=column)  # Restore column names

    vsb = ttk.Scrollbar(staff_tab, orient="vertical", command=table.yview)
    vsb.grid(row=1, column=3, sticky='ns')
    table.configure(yscrollcommand=vsb.set)

    student_tab = frames[0]
    search_label_student = tk.Label(student_tab, text="Search by Name:")
    search_label_student.grid(row=0, column=0, padx=10, pady=10)

    search_entry_student = tk.Entry(student_tab)
    search_entry_student.grid(row=0, column=1, padx=10, pady=10)

    search_button_student = tk.Button(student_tab, text="Search", command=search_student)
    search_button_student.grid(row=0, column=2, padx=10, pady=10)

    table_student = ttk.Treeview(student_tab, columns=("Serial No.", "Student Name", "Phone", "Course", "D.O.B"), show="headings")
    table_student.grid(row=1, column=0, columnspan=3, padx=10, pady=(10, 30), sticky="nsew")

    for column in table_student['columns']:
        table_student.heading(column, text=column)  # Restore column names

    vsb_student = ttk.Scrollbar(student_tab, orient="vertical", command=table_student.yview)
    vsb_student.grid(row=1, column=3, sticky='ns')
    table_student.configure(yscrollcommand=vsb_student.set)

    add_course_tab = frames[2]
    course_label = tk.Label(add_course_tab, text="Course:")
    course_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    course_entry = tk.Entry(add_course_tab)
    course_entry.grid(row=0, column=1, padx=10, pady=10)

    button_frame_course = tk.Frame(add_course_tab)
    button_frame_course.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="e")

    save_button_course = tk.Button(button_frame_course, text="Save")
    save_button_course.grid(row=0, column=0, padx=5, pady=10)

    delete_button_course = tk.Button(button_frame_course, text="Delete")
    delete_button_course.grid(row=0, column=1, padx=5, pady=10)

    add_section_tab = frames[3]
    section_label = tk.Label(add_section_tab, text="Section:")
    section_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    section_entry = tk.Entry(add_section_tab)
    section_entry.grid(row=0, column=1, padx=10, pady=10)

    button_frame_section = tk.Frame(add_section_tab)
    button_frame_section.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="e")

    save_button_section = tk.Button(button_frame_section, text="Save")
    save_button_section.grid(row=0, column=0, padx=5, pady=10)

    delete_button_section = tk.Button(button_frame_section, text="Delete")
    delete_button_section.grid(row=0, column=1, padx=5, pady=10)

    add_subject_tab = frames[4]
    subject_label = tk.Label(add_subject_tab, text="Subject:")
    subject_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    subject_entry = tk.Entry(add_subject_tab)
    subject_entry.grid(row=0, column=1, padx=10, pady=10)

    button_frame_subject = tk.Frame(add_subject_tab)
    button_frame_subject.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="e")

    save_button_subject = tk.Button(button_frame_subject, text="Save")
    save_button_subject.grid(row=0, column=0, padx=5, pady=10)

    delete_button_subject = tk.Button(button_frame_subject, text="Delete")
    delete_button_subject.grid(row=0, column=1, padx=5, pady=10)

def hide_indicators():
    Student_indicate.config(bg='#c3c3c3')
    Staff_indicate.config(bg='#c3c3c3')
    Fees_indicate.config(bg='#c3c3c3')
    Attendance_indicate.config(bg='#c3c3c3')
    Miscellaneous_indicate.config(bg='#c3c3c3')

def indicate(lb):
    hide_indicators()
    lb.config(bg='#158aff')

def show_attendance_management_frame():
    global number_var
    global number_present_var
    global total_days_var
    global attendance_management_frame

    close_misc_management()
    close_staff_management()
    close_fees_management()
    close_student_management()

    if 'attendance_management_frame' in globals():
        attendance_management_frame.destroy()
    attendance_management_frame = tk.Toplevel(root)
    attendance_management_frame.title("Attendance Management")
    attendance_management_frame.geometry("1093x550")

    # Calculate the position to center the window
    screen_width = attendance_management_frame.winfo_screenwidth()
    screen_height = attendance_management_frame.winfo_screenheight()
    x_coordinate = (screen_width - 1076) // 2 + 128  # Shifted 128 pixels from the left
    y_coordinate = (screen_height - 550) // 2 + 32  # Shifted 32 pixels from the top
    attendance_management_frame.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    # Adding tabs
    tab_control = ttk.Notebook(attendance_management_frame)

    student_tab = ttk.Frame(tab_control)
    tab_control.add(student_tab, text='Student')

    staff_tab = ttk.Frame(tab_control)
    tab_control.add(staff_tab, text='Staff')

    data_tab = ttk.Frame(tab_control)
    tab_control.add(data_tab, text='Data')

    tab_control.pack(expand=1, fill="both")

    # Labels, Buttons, Combo Boxes, and Calendar in Student tab
    label_name = ttk.Label(student_tab, text="Name:")
    label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_name = ttk.Entry(student_tab)
    entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    btn_search_student = ttk.Button(student_tab, text="Search Student", command=search_student)
    btn_search_student.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    label_number = ttk.Label(student_tab, text="Number:")
    label_number.grid(row=0, column=3, padx=10, pady=10, sticky="w")

    number_var = tk.StringVar()
    entry_number = ttk.Entry(student_tab, textvariable=number_var)
    entry_number.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    entry_number.bind("<KeyRelease>", lambda event: calculate_total_days())

    label_from = ttk.Label(student_tab, text="From:")
    label_from.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    cal_from = DateEntry(student_tab, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal_from.grid(row=1, column=1, padx=10, pady=10, sticky="w", ipadx=20)

    label_to = ttk.Label(student_tab, text="To:")
    label_to.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    cal_to = DateEntry(student_tab, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal_to.grid(row=1, column=3, padx=10, pady=10, sticky="w", ipadx=20)

    # Table in Student tab
    table = ttk.Treeview(student_tab, columns=("Number", "Name", "Course"), show="headings")
    table.heading("Number", text="Number")
    table.heading("Name", text="Name")
    table.heading("Course", text="Course")
    table.column("#1", width=100, anchor="w")  # Adjusting column width and anchor for 'Number'
    table.column("#2", width=200, anchor="w")  # Adjusting column width and anchor for 'Name'
    table.column("#3", width=150, anchor="w")  # Adjusting column width and anchor for 'Course'
    table.bind('<Button-1>', prevent_edit)  # Bind the left-click event to prevent editing
    table.grid(row=1, column=4, rowspan=7, padx=10, pady=10, sticky="nsew")  # Placed on the right side

    # Buttons in Student tab
    btn_save = ttk.Button(student_tab, text="Save", command=save_student)
    btn_save.grid(row=6, column=0, padx=10, pady=(20, 10), sticky="w")

    btn_update = ttk.Button(student_tab, text="Update", command=update_student)
    btn_update.grid(row=6, column=1, padx=10, pady=(20, 10), sticky="w")

    btn_delete = ttk.Button(student_tab, text="Delete Student", command=delete_student)
    btn_delete.grid(row=6, column=2, padx=10, pady=(20, 10), sticky="w")

    # Labels and Entries in Student tab
    label_total_days = ttk.Label(student_tab, text="Total Number of Days:")
    label_total_days.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    total_days_var = tk.StringVar()
    entry_total_days = ttk.Entry(student_tab, textvariable=total_days_var, state='readonly')
    entry_total_days.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    label_type = ttk.Label(student_tab, text="Type:")
    label_type.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    btn_type = ttk.Button(student_tab, text="Student", state='disabled')
    btn_type.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    label_days_present = ttk.Label(student_tab, text="Number of Days Present:")
    label_days_present.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    number_present_var = tk.StringVar()
    entry_days_present = ttk.Entry(student_tab, textvariable=number_present_var)
    entry_days_present.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    entry_days_present.bind("<KeyRelease>", lambda event: calculate_total_days())

    label_days_absent = ttk.Label(student_tab, text="Number of Days Absent:")
    label_days_absent.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    entry_days_absent = ttk.Entry(student_tab)
    entry_days_absent.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Copying elements from Student Tab to Staff Tab
    label_name_staff = ttk.Label(staff_tab, text="Name:")
    label_name_staff.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_name_staff = ttk.Entry(staff_tab)
    entry_name_staff.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    btn_search_staff = ttk.Button(staff_tab, text="Search Staff", command=search_staff)
    btn_search_staff.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    label_number_staff = ttk.Label(staff_tab, text="Number:")
    label_number_staff.grid(row=0, column=3, padx=10, pady=10, sticky="w")

    number_var_staff = tk.StringVar()
    entry_number_staff = ttk.Entry(staff_tab, textvariable=number_var_staff)
    entry_number_staff.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    entry_number_staff.bind("<KeyRelease>", lambda event: calculate_total_days())

    label_from_staff = ttk.Label(staff_tab, text="From:")
    label_from_staff.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    cal_from_staff = DateEntry(staff_tab, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal_from_staff.grid(row=1, column=1, padx=10, pady=10, sticky="w", ipadx=20)

    label_to_staff = ttk.Label(staff_tab, text="To:")
    label_to_staff.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    cal_to_staff = DateEntry(staff_tab, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal_to_staff.grid(row=1, column=3, padx=10, pady=10, sticky="w", ipadx=20)

    # Table in Staff tab
    table_staff = ttk.Treeview(staff_tab, columns=("Name", "Number", "Course"), show="headings")
    table_staff.heading("Name", text="Name")
    table_staff.heading("Number", text="Number")
    table_staff.heading("Course", text="Course")
    table_staff.column("#1", width=150, anchor="w")  # Adjusting column width and anchor for 'Number'
    table_staff.column("#2", width=150, anchor="w")  # Adjusting column width and anchor for 'Name'
    table_staff.column("#3", width=150, anchor="w")  # Adjusting column width and anchor for 'Course'
    table_staff.bind('<Button-1>', prevent_edit)  # Bind the left-click event to prevent editing
    table_staff.grid(row=1, column=4, rowspan=7, padx=10, pady=10, sticky="nsew")  # Placed on the right side

    # Buttons in Staff tab
    btn_save_staff = ttk.Button(staff_tab, text="Save", command=save_student)
    btn_save_staff.grid(row=6, column=0, padx=10, pady=(20, 10), sticky="w")

    btn_update_staff = ttk.Button(staff_tab, text="Update", command=update_student)
    btn_update_staff.grid(row=6, column=1, padx=10, pady=(20, 10), sticky="w")

    btn_delete_staff = ttk.Button(staff_tab, text="Delete Staff", command=delete_student)
    btn_delete_staff.grid(row=6, column=2, padx=10, pady=(20, 10), sticky="w")

    # Labels and Entries in Staff tab
    label_total_days_staff = ttk.Label(staff_tab, text="Total Number of Days:")
    label_total_days_staff.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    total_days_var_staff = tk.StringVar()
    entry_total_days_staff = ttk.Entry(staff_tab, textvariable=total_days_var_staff, state='readonly')
    entry_total_days_staff.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    label_type_staff = ttk.Label(staff_tab, text="Type:")
    label_type_staff.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    btn_type_staff = ttk.Button(staff_tab, text="Staff", state='disabled')
    btn_type_staff.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    label_days_present_staff = ttk.Label(staff_tab, text="Number of Days Present:")
    label_days_present_staff.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    number_present_var_staff = tk.StringVar()
    entry_days_present_staff = ttk.Entry(staff_tab, textvariable=number_present_var_staff)
    entry_days_present_staff.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    entry_days_present_staff.bind("<KeyRelease>", lambda event: calculate_total_days())

    label_days_absent_staff = ttk.Label(staff_tab, text="Number of Days Absent:")
    label_days_absent_staff.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    entry_days_absent_staff = ttk.Entry(staff_tab)
    entry_days_absent_staff.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Combo box and Table in Data tab
    combo_type = ttk.Combobox(data_tab, values=["Student", "Staff"])
    combo_type.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    table_data = ttk.Treeview(data_tab,
    columns=("Name", "Number", "Attend From", "Attend To", "Present Days", "Absent Days"),
              show="headings")
    table_data.heading("Name", text="Name")
    table_data.heading("Number", text="Number")
    table_data.heading("Attend From", text="Attend From")
    table_data.heading("Attend To", text="Attend To")
    table_data.heading("Present Days", text="Present Days")
    table_data.heading("Absent Days", text="Absent Days")
    table_data.column("#1", width=150, anchor="center")  # Name
    table_data.column("#2", width=150, anchor="center")  # Number
    table_data.column("#3", width=150, anchor="center")  # Attend From
    table_data.column("#4", width=150, anchor="center")  # Attend To
    table_data.column("#5", width=150, anchor="center")  # Present Days
    table_data.column("#6", width=150, anchor="center")  # Absent Days
    table_data.bind('<Button-1>', prevent_edit)  # Bind the left-click event to prevent editing
    table_data.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Placed on the right side



def show_staff_management_frame():
    global staff_management_frame

    close_attendance_management()
    close_misc_management()
    close_fees_management()
    close_student_management()

    if 'staff_management_frame' in globals():
        staff_management_frame.destroy()
    staff_management_frame = tk.Toplevel(root)
    staff_management_frame.title("Staff Management")
    staff_management_frame.geometry("1093x550")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - 1076) // 2 + 128
    y_coordinate = (screen_height - 550) // 2 + 32
    staff_management_frame.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    notebook = ttk.Notebook(staff_management_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Create tabs
    tabs = ["Info", "Search"]
    frames = [tk.Frame(notebook) for _ in range(len(tabs))]

    for i, tab in enumerate(tabs):
        notebook.add(frames[i], text=tab)

    # Add elements to the Info tab
    info_tab = frames[0]

    # Elements for Info tab
    first_name_label = tk.Label(info_tab, text="First Name:")
    first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    first_name_entry = tk.Entry(info_tab)
    first_name_entry.grid(row=0, column=1, padx=10, pady=5)

    qualification_label = tk.Label(info_tab, text="Qualification:")
    qualification_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    qualification_entry = tk.Entry(info_tab)
    qualification_entry.grid(row=1, column=1, padx=10, pady=5)

    data_structure_label = tk.Label(info_tab, text="Subject:")
    data_structure_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    data_structure_combobox = ttk.Combobox(info_tab, values=["Data Structure", "Array", "Linked List", "Stack", "Queue"])
    data_structure_combobox.grid(row=2, column=1, padx=10, pady=5)
    data_structure_combobox.current(0)

    dob_label = tk.Label(info_tab, text="DOB:")
    dob_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    dob_combobox = DateEntry(info_tab)
    dob_combobox.grid(row=3, column=1, padx=10, pady=5)

    course_label = tk.Label(info_tab, text="Course:")
    course_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    course_combobox = ttk.Combobox(info_tab, values=["Choose Course", "Computer Science", "Engineering", "Business"])
    course_combobox.grid(row=4, column=1, padx=10, pady=5)
    course_combobox.current(0)

    phone_label = tk.Label(info_tab, text="Phone Number:")
    phone_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
    phone_entry = tk.Entry(info_tab)
    phone_entry.grid(row=5, column=1, padx=10, pady=5)

    address_label = tk.Label(info_tab, text="Address:")
    address_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
    address_entry = tk.Entry(info_tab, width=50)  # Increased width for address entry
    address_entry.grid(row=6, column=1, padx=10, pady=5)

    # Elements for Last Name, Email Address, Salary, and Gender
    last_name_label = tk.Label(info_tab, text="Last Name:")
    last_name_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")
    last_name_entry = tk.Entry(info_tab)
    last_name_entry.grid(row=0, column=3, padx=10, pady=5)

    email_label = tk.Label(info_tab, text="Email Address:")
    email_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")
    email_entry = tk.Entry(info_tab)
    email_entry.grid(row=1, column=3, padx=10, pady=5)

    salary_label = tk.Label(info_tab, text="Salary:")
    salary_label.grid(row=2, column=2, padx=10, pady=5, sticky="e")
    salary_entry = tk.Entry(info_tab)
    salary_entry.grid(row=2, column=3, padx=10, pady=5)

    gender_label = tk.Label(info_tab, text="Gender:")
    gender_label.grid(row=3, column=2, padx=10, pady=5, sticky="e")

    gender_var = tk.StringVar()
    male_radio = ttk.Radiobutton(info_tab, text="Male", variable=gender_var, value="Male")
    male_radio.grid(row=3, column=3, padx=(5, 2), pady=5, sticky="w")
    female_radio = ttk.Radiobutton(info_tab, text="Female", variable=gender_var, value="Female")
    female_radio.grid(row=3, column=3, padx=(70, 2), pady=5, sticky="w")

    # Save button
    save_button = tk.Button(info_tab, text="Save")
    save_button.grid(row=7, column=1, columnspan=2, pady=10, sticky="w")

    # Additional label on the right side
    additional_label = tk.Label(info_tab, text="Additional Options:")
    additional_label.grid(row=0, column=4, padx=(200, 150), pady=5, sticky="e")

    # Upload button on the bottom right
    upload_button = tk.Button(info_tab, text="Upload")
    upload_button.grid(row=2, column=4, padx=(200, 150), pady=(0, 10), sticky="se")

    # Add elements to the Search tab
    search_tab = frames[1]

    # Elements for Search tab
    first_name_label_search = tk.Label(search_tab, text="First Name:")
    first_name_label_search.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    first_name_entry_search = tk.Entry(search_tab)
    first_name_entry_search.grid(row=0, column=1, padx=10, pady=5)

    qualification_label_search = tk.Label(search_tab, text="Qualification:")
    qualification_label_search.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    qualification_entry_search = tk.Entry(search_tab)
    qualification_entry_search.grid(row=1, column=1, padx=10, pady=5)

    choose_subject_label_search = tk.Label(search_tab, text="Choose Subject:")
    choose_subject_label_search.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    choose_subject_combobox_search = ttk.Combobox(search_tab, values=["Choose Subject", "Data Structure", "Array", "Linked List", "Stack", "Queue"])
    choose_subject_combobox_search.grid(row=2, column=1, padx=10, pady=5)
    choose_subject_combobox_search.current(0)

    dob_label_search = tk.Label(search_tab, text="DOB:")
    dob_label_search.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    dob_combobox_search = DateEntry(search_tab)
    dob_combobox_search.grid(row=3, column=1, padx=10, pady=5)

    course_label_search = tk.Label(search_tab, text="Course:")
    course_label_search.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    course_combobox_search = ttk.Combobox(search_tab, values=["Choose Course", "Computer Science", "Engineering", "Business"])
    course_combobox_search.grid(row=4, column=1, padx=10, pady=5)
    course_combobox_search.current(0)

    phone_label_search = tk.Label(search_tab, text="Phone Number:")
    phone_label_search.grid(row=5, column=0, padx=10, pady=5, sticky="e")
    phone_entry_search = tk.Entry(search_tab)
    phone_entry_search.grid(row=5, column=1, padx=10, pady=5)

    address_label_search = tk.Label(search_tab, text="Address:")
    address_label_search.grid(row=6, column=0, padx=10, pady=5, sticky="e")
    address_entry_search = tk.Entry(search_tab, width=50)  # Increased width for address entry
    address_entry_search.grid(row=6, column=1, padx=10, pady=5)

    # Elements for Last Name, Email Address, Salary, and Gender
    last_name_label_search = tk.Label(search_tab, text="Last Name:")
    last_name_label_search.grid(row=0, column=2, padx=10, pady=5, sticky="e")
    last_name_entry_search = tk.Entry(search_tab)
    last_name_entry_search.grid(row=0, column=3, padx=10, pady=5)

    email_label_search = tk.Label(search_tab, text="Email Address:")
    email_label_search.grid(row=1, column=2, padx=10, pady=5, sticky="e")
    email_entry_search = tk.Entry(search_tab)
    email_entry_search.grid(row=1, column=3, padx=10, pady=5)

    salary_label_search = tk.Label(search_tab, text="Salary:")
    salary_label_search.grid(row=2, column=2, padx=10, pady=5, sticky="e")
    salary_entry_search = tk.Entry(search_tab)
    salary_entry_search.grid(row=2, column=3, padx=10, pady=5)

    gender_label_search = tk.Label(search_tab, text="Gender:")
    gender_label_search.grid(row=3, column=2, padx=10, pady=5, sticky="e")

    gender_var_search = tk.StringVar()
    male_radio_search = ttk.Radiobutton(search_tab, text="Male", variable=gender_var_search, value="Male")
    male_radio_search.grid(row=3, column=3, padx=(5, 2), pady=5, sticky="w")
    female_radio_search = ttk.Radiobutton(search_tab, text="Female", variable=gender_var_search, value="Female")
    female_radio_search.grid(row=3, column=3, padx=(70, 2), pady=5, sticky="w")

    # Buttons for Search tab
    update_button = tk.Button(search_tab, text="Update")
    update_button.grid(row=7, column=0, pady=10, padx=5, sticky="w")

    delete_button = tk.Button(search_tab, text="Delete")
    delete_button.grid(row=7, column=1, pady=10, padx=5, sticky="w")

    search_button = tk.Button(search_tab, text="Search")
    search_button.grid(row=7, column=2, pady=10, padx=5, sticky="w")

    # Add a table on the bottom right corner of the Search tab
    table_frame = tk.Frame(search_tab)
    table_frame.grid(row=8, column=2, columnspan=3, padx=10, pady=10, sticky="se")

    # Create a Treeview widget
    table = ttk.Treeview(table_frame, columns=("Name", "Phone", "Subject"), show="headings")
    table.grid(row=0, column=0, sticky="nsew")

    # Define column headings
    table.heading("Name", text="Name")
    table.heading("Phone", text="Phone")
    table.heading("Subject", text="Subject")

    # Add some dummy data for demonstration purposes
    table.insert("", "end", values=("John Doe", "1234567890", "Data Structure"))
    table.insert("", "end", values=("Jane Smith", "0987654321", "Array"))

def show_student_management_frame():
    global student_management_frame

    close_attendance_management()
    close_staff_management()
    close_fees_management()
    close_misc_management()

    if 'student_management_frame' in globals():
        student_management_frame.destroy()
    student_management_frame = tk.Toplevel(root)
    student_management_frame.title("Student Management")
    student_management_frame.geometry("1093x550")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - 1076) // 2 + 128
    y_coordinate = (screen_height - 550) // 2 + 32
    student_management_frame.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    def show_calendar():
        dob_calendar.place(relx=0, rely=1, anchor="sw")

    def select_date():
        selected_date = dob_calendar.get_date()
        dob_combo.set(selected_date)
        dob_calendar.place_forget()

    # Create a notebook (tabs)
    notebook = ttk.Notebook(student_management_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

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
    dob_combo_search = ttk.Combobox(search_tab)
    dob_combo_search.grid(row=3, column=1, padx=5, pady=5)
    dob_calendar_search = Calendar(search_tab)
    dob_calendar_search.place_forget()  # Initially hide the calendar
    dob_combo_search.bind("<Button-1>", lambda event: show_calendar())
    dob_calendar_search.bind("<<CalendarSelected>>", lambda event: select_date())

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


def show_fees_management_frame():
    global fees_management_frame

    close_attendance_management()
    close_staff_management()
    close_student_management()
    close_misc_management()

    if 'fees_management_frame' in globals():
        fees_management_frame.destroy()
    fees_management_frame = tk.Toplevel(root)
    fees_management_frame.title("Fees Management")
    fees_management_frame.geometry("1093x550")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - 1076) // 2 + 128
    y_coordinate = (screen_height - 550) // 2 + 32
    fees_management_frame.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    def save_data():
        # Placeholder function to save data, you can implement the actual save functionality here
        messagebox.showinfo("Save", "Data saved!")

    def search_data():
        # Placeholder function for searching data
        messagebox.showinfo("Search", "Searching...")

    def prevent_edit(event):
        # Function to prevent editing in specified columns
        table = event.widget
        column_id = table.identify_column(event.x)
        if column_id in ['#1', '#2', '#3', '#4', '#5', '#6', '#7']:  # Columns to be non-editable
            return 'break'  # Prevent editing

   # Adding tabs
    tab_control = ttk.Notebook(fees_management_frame)

    fees_tab = ttk.Frame(tab_control)
    tab_control.add(fees_tab, text='Fees')

    data_tab = ttk.Frame(tab_control)
    tab_control.add(data_tab, text='Data')

    tab_control.pack(expand=1, fill="both")

    # Labels, Buttons, Combo Boxes, and Radio Buttons in Fees tab
    label_search_name = ttk.Label(fees_tab, text="Search by Name:")
    label_search_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_search_name = ttk.Entry(fees_tab)
    entry_search_name.grid(row=0, column=1, padx=10, pady=10, sticky="w", ipadx=20)  # Making the entry longer

    # Label "Admission Number" and button
    label_admission_number = ttk.Label(fees_tab, text="Admission Number:")
    label_admission_number.grid(row=0, column=2, padx=10, pady=10, sticky="e")  # Positioned next to the Search button

    entry_admission_number = ttk.Entry(fees_tab)
    entry_admission_number.grid(row=0, column=3, padx=10, pady=10, sticky="w", ipadx=10)  # Adjusted width

    btn_admission_search = ttk.Button(fees_tab, text="Search", command=search_data)
    btn_admission_search.grid(row=0, column=4, padx=(0, 10), pady=10, sticky="w")  # Positioned next to the Admission Number label

    label_total_fees = ttk.Label(fees_tab, text="Total Fees:")
    label_total_fees.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    entry_total_fees = ttk.Entry(fees_tab)
    entry_total_fees.grid(row=1, column=1, padx=10, pady=10, sticky="w", ipadx=20)  # Making the entry longer

    label_semester = ttk.Label(fees_tab, text="Semester:")
    label_semester.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    combo_semester = ttk.Combobox(fees_tab, values=["Choose Semester", "Semester 1", "Semester 2", "Semester 3"])
    combo_semester.current(0)
    combo_semester.grid(row=2, column=1, padx=10, pady=10, sticky="w", ipadx=20)  # Making the combo box longer

    label_paid = ttk.Label(fees_tab, text="Paid:")
    label_paid.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    entry_paid = ttk.Entry(fees_tab)
    entry_paid.grid(row=3, column=1, padx=10, pady=10, sticky="w", ipadx=20)  # Making the entry longer

    label_paid_date = ttk.Label(fees_tab, text="Paid Date:")
    label_paid_date.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Add DateEntry widget from tkcalendar
    paid_date_entry = DateEntry(fees_tab, width=12, background='darkblue', foreground='white', borderwidth=2)
    paid_date_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w", ipadx=20)  # Making the DateEntry widget longer

    label_mode_payment = ttk.Label(fees_tab, text="Mode of Payment:")
    label_mode_payment.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    var_mode_payment = tk.StringVar()
    rad_cheque = ttk.Radiobutton(fees_tab, text="Cheque", variable=var_mode_payment, value="Cheque")
    rad_cheque.grid(row=5, column=1, padx=(10, 5), pady=10, sticky="w")

    rad_cash = ttk.Radiobutton(fees_tab, text="Cash", variable=var_mode_payment, value="Cash")
    rad_cash.grid(row=5, column=1, padx=(90, 5), pady=10, sticky="w")

    label_due_amount = ttk.Label(fees_tab, text="Due Amount:")
    label_due_amount.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    entry_due_amount = ttk.Entry(fees_tab)
    entry_due_amount.grid(row=6, column=1, padx=10, pady=10, sticky="w", ipadx=20)  # Making the entry longer

    # Buttons in Fees tab
    btn_save = ttk.Button(fees_tab, text="Save", command=save_data)
    btn_save.grid(row=7, column=0, padx=(10, 5), pady=10, sticky="w")

    btn_update = ttk.Button(fees_tab, text="Update", width=15)
    btn_update.grid(row=7, column=1, padx=5, pady=10, sticky="w")

    btn_delete = ttk.Button(fees_tab, text="Delete", width=15)
    btn_delete.grid(row=7, column=1, padx=(95, 5), pady=10, sticky="w")

    # Adjusting positions of buttons
    btn_save.grid(row=8, column=0, padx=(10, 5), pady=10, sticky="w")
    btn_update.grid(row=8, column=1, padx=5, pady=10, sticky="w")
    btn_delete.grid(row=8, column=1, padx=(95, 5), pady=10, sticky="w")

    # Table in Fees tab
    columns = ("Sr No.", "Student Name", "Phone", "Course")  # Adjusted column names
    table = ttk.Treeview(fees_tab, columns=columns, show="headings", height=10)

    for col in columns:
        table.heading(col, text=col, anchor="w")  # Align column names to the left

    table.grid(row=1, column=2, columnspan=3, rowspan=7, padx=10, pady=10, sticky="nsew")  # Adjusted column position and span
    fees_tab.grid_columnconfigure(2, weight=1)  # Adjusting column width

    # Labels, Buttons, Combo Boxes, and Radio Buttons in Data tab
    label_search_name = ttk.Label(data_tab, text="Search by Name:")
    label_search_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_search_name = ttk.Entry(data_tab)
    entry_search_name.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="w", ipadx=20)  # Making the entry longer

    btn_search = ttk.Button(data_tab, text="Search", command=search_data)
    btn_search.grid(row=0, column=2, padx=10, pady=10, sticky="w")  # Positioned next to the entry box

    # Table in Data tab
    columns = ("Serial No.", "Student Name", "Total Fees", "Semester", "Fees Paid", "Payment Date", "Mode of Payment", "Fees Due")  # Adjusted column names
    table = ttk.Treeview(data_tab, columns=columns, show="headings", height=10)

    for col in columns:
        table.heading(col, text=col, anchor="w")  # Align column names to the left

    table.bind('<Button-1>', prevent_edit)  # Bind the left-click event to prevent editing
    table.column("#1", width=100, anchor="w")  # Adjusting column width and anchor for 'Serial No.'
    table.column("#2", width=200, anchor="w")  # Adjusting column width and anchor for 'Student Name'
    table.column("#3", width=100, anchor="w")  # Adjusting column width and anchor for 'Total Fees'
    table.column("#4", width=100, anchor="w")  # Adjusting column width and anchor for 'Semester'
    table.column("#5", width=100, anchor="w")  # Adjusting column width and anchor for 'Fees Paid'
    table.column("#6", width=100, anchor="w")  # Adjusting column width and anchor for 'Payment Date'
    table.column("#7", width=120, anchor="w")  # Adjusting column width and anchor for 'Mode of Payment'
    table.column("#8", width=100, anchor="w")  # Adjusting column width and anchor for 'Fees Due'
    table.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Adjusted column position and span
    data_tab.grid_columnconfigure(0, weight=1)  # Adjusting column width

def close_misc_management():
    if 'misc_management_frame' in globals():
        misc_management_frame.destroy()
def close_attendance_management():
    if 'attendance_management_frame' in globals():
        attendance_management_frame.destroy()

def close_staff_management():
    if 'staff_management_frame' in globals():
        staff_management_frame.destroy()

def close_student_management():
    if 'student_management_frame' in globals():
        student_management_frame.destroy()

def close_fees_management():
    if 'fees_management_frame' in globals():
        fees_management_frame.destroy()


def close_misc_management_and_indicate(lb):
    close_misc_management()
    indicate(lb)

def close_attendance_management_and_indicate(lb):
    close_attendance_management()
    indicate(lb)

def close_staff_management_and_indicate(lb):
    close_staff_management()
    indicate(lb)

def close_student_management_and_indicate(lb):
    close_student_management()
    indicate(lb)

def close_fees_management_and_indicate(lb):
    close_fees_management()
    indicate(lb)

#def main() MO TO BOUNG TO HANGANG 726

root = tk.Tk()
root.geometry('1700x1700')
root.title('College Management')

options_frame = tk.Frame(root, bg='#c3c3c3')

Student_Management_btn = tk.Button(options_frame, text='Student Management', font=('bold', 15),
                                   fg='#158aff', bd=0, bg='#c3c3c3',
                                   command=show_student_management_frame)
Student_Management_btn.place(x=10, y=240)

Student_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
Student_indicate.place(x=3, y=240, width=5, height=40)

Staff_Management_btn = tk.Button(options_frame, text='Staff Management', font=('bold', 15),
                                 fg='#158aff', bd=0, bg='#c3c3c3',
                                 command=show_staff_management_frame)
Staff_Management_btn.place(x=10, y=310)

Staff_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
Staff_indicate.place(x=3, y=310, width=5, height=40)

Fees_Management_btn = tk.Button(options_frame, text='Fees Management', font=('bold', 15),
                                fg='#158aff', bd=0, bg='#c3c3c3',
                                command=show_fees_management_frame)
Fees_Management_btn.place(x=10, y=380)

Fees_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
Fees_indicate.place(x=3, y=380, width=5, height=40)

Attendance_Management_btn = tk.Button(options_frame, text='Attendance Management', font=('bold', 15),
                                      fg='#158aff', bd=0, bg='#c3c3c3',
                                      command=show_attendance_management_frame)

Attendance_Management_btn.place(x=10, y=450)

Attendance_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
Attendance_indicate.place(x=3, y=450, width=5, height=40)

Miscellaneous_Management_btn = tk.Button(options_frame, text='Miscellaneous Management', font=('bold', 15),
                                         fg='#158aff', bd=0, bg='#c3c3c3',
                                         command=show_misc_management_frame)
Miscellaneous_Management_btn.place(x=10, y=530)

Miscellaneous_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
Miscellaneous_indicate.place(x=3, y=530, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=270, height=1700)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1700, width=1300)

college_label = tk.Label(root, text='College Management', font=('Arial', 30, 'bold'), bg='#c3c3c3', fg='black')
college_label.place(relx=0.5, rely=0.05, anchor=tk.N)

back_button = tk.Button(root, text="<", bg='#c3c3c3', fg='black', bd=2, relief=tk.SOLID)
back_button.place(relx=0.88, rely=0.06, anchor=tk.NW)

change_password_button = tk.Button(root, text="Change Password", bg='#c3c3c3', fg='black', bd=2, relief=tk.SOLID)
change_password_button.place(relx=0.85, rely=0.06, anchor=tk.NE)

def save_data():
    print("Data saved!")


def calculate_total_days():
    # Calculate the total number of days from the "Number" and "Number of Days Present" entries
    number_value = int(number_var.get()) if number_var.get().isdigit() else 0
    number_present_value = int(number_present_var.get()) if number_present_var.get().isdigit() else 0
    total_days_var.set(str(number_value + number_present_value))

def save_student():
    # Placeholder function for saving student data
    print("Saving student data...")

def update_student():
    # Placeholder function for updating student data
    print("Updating student data...")

def delete_student():
    # Placeholder function for deleting student data
    print("Deleting student data...")

def prevent_edit(event):
    # Prevent editing of specific columns
    if event.widget.identify_region(event.x, event.y) == "heading":
        return "break"





root.mainloop()

