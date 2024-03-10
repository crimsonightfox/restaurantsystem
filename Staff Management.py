import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def main():
    def save_data():
        # Placeholder function to save data, you can implement the actual save functionality here
        print("Data saved!")

    root = tk.Tk()
    root.title("Staff Management")
    root.geometry("1093x550")

    # Calculate the position to center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - 1093) // 2 + 128  # Shifted 128 pixels from the left
    y_coordinate = (screen_height - 550) // 2 + 32   # Shifted 32 pixels from the top
    root.geometry(f"1093x550+{x_coordinate}+{y_coordinate}")

    # Create a notebook (tab control)
    notebook = ttk.Notebook(root)
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

    root.mainloop()

if __name__ == "__main__":
    main()
