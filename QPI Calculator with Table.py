import tkinter as tk
from tkinter import ttk

# Quality Point Equivalent for each letter grade
QPE = {'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D': 1.0, 'F': 0, 'FD': 0, 'WP': 0, 'No Grade': 0}

class QPI_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Quality Point Index Calculator")

        # Labels and Entries
        self.grade_label = tk.Label(master, text="Letter Grade")
        self.grade_label.grid(row=0, column=0)
        self.qpe_label = tk.Label(master, text="Quality Point Equivalent")
        self.qpe_label.grid(row=0, column=1)
        self.units_label = tk.Label(master, text="Subject Units")
        self.units_label.grid(row=0, column=2)

        self.grade_entry = tk.Entry(master)
        self.grade_entry.grid(row=1, column=0)
        self.qpe_entry = tk.Entry(master)
        self.qpe_entry.grid(row=1, column=1)
        self.units_entry = tk.Entry(master)
        self.units_entry.grid(row=1, column=2)

        # Table to display added subjects
        self.subject_table = ttk.Treeview(master, columns=("Subject Grade", "QPE", "Units"))
        self.subject_table.heading("#1", text="Subject")
        self.subject_table.heading("#2", text="QPE")
        self.subject_table.heading("#3", text="Units")
        self.subject_table.grid(row=2, column=0, columnspan=3)

        # Buttons
        self.add_subject_button = tk.Button(master, text="Add Another Subject", command=self.add_subject)
        self.add_subject_button.grid(row=3, column=0, columnspan=3)

        self.calculate_button = tk.Button(master, text="Calculate QPI", command=self.calculate_qpi)
        self.calculate_button.grid(row=4, column=0, columnspan=3)

        # Initialize Subject Lists
        self.subjects = []
        self.grades = []
        self.qpes = []
        self.units = []

    def add_subject(self):
        # Add subject to the table and clear the entries
        subject = self.grade_entry.get()
        grade = QPE.get(subject, 0)
        qpe = float(self.qpe_entry.get())
        units = float(self.units_entry.get())

        self.subject_table.insert("", "end", values=(subject, grade, units))

        self.subjects.append(subject)
        self.grades.append(grade)
        self.qpes.append(qpe)
        self.units.append(units)

        self.grade_entry.delete(0, tk.END)
        self.qpe_entry.delete(0, tk.END)
        self.units_entry.delete(0, tk.END)

    def calculate_qpi(self):
        # Calculate the QPI
        total_qpe_units = 0
        total_units = 0
        for i in range(len(self.subjects)):
            total_qpe_units += self.grades[i] * self.units[i]
            total_units += self.units[i]

        qpi = round(total_qpe_units / total_units, 3)

        # Display the QPI
        result_label = tk.Label(self.master, text=f"QPI: {qpi}")
        result_label.grid(row=5, column=0, columnspan=3)

# Create and run the GUI
root = tk.Tk()
app = QPI_Calculator(root)
root.mainloop()
