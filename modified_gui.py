import tkinter as tk
from tkinter import ttk
import pandas as pd

# Data from your script
roll_no = [1, 2, 3, 4]
names = ['A', 'B', 'F', 'Z']
dob = ['2004-04-08', '2001-04-25', '2005-02-03', '2007-01-29']
yos = [1, 3, 2, 4]

# Adding new elements directly to the lists
roll_no.extend([5, 6, 7])
names.extend(['G', 'H', 'I'])
dob.extend(['2004-04-08', '2002-05-21', '2006-07-30'])
yos.extend([2, 1, 3])

mapping = {}
for i in range(len(roll_no)):
    mapping[roll_no[i]] = {'RollNo': roll_no[i], 'Names': names[i], 'DOB': dob[i], 'YOS': yos[i]}

data_frame = pd.DataFrame.from_dict(mapping, orient='index')

def sort_by(column, ascending=True):
    sorted_df = data_frame.sort_values(by=column, ascending=ascending)
    update_treeview(sorted_df)

def update_treeview(data):
    for i in tree.get_children():
        tree.delete(i)
    for row in data.itertuples():
        tree.insert('', tk.END, values=(row.RollNo, row.Names, row.DOB, row.YOS))

root = tk.Tk()
root.title("DataFrame GUI")

tree = ttk.Treeview(root, columns=('RollNo', 'Names', 'DOB', 'YOS'), show='headings')
tree.heading('RollNo', text='Roll No')
tree.heading('Names', text='Names')
tree.heading('DOB', text='DOB')
tree.heading('YOS', text='YOS')

tree.column('RollNo', width=80, anchor=tk.CENTER)
tree.column('Names', width=100, anchor=tk.CENTER)
tree.column('DOB', width=100, anchor=tk.CENTER)
tree.column('YOS', width=80, anchor=tk.CENTER)

update_treeview(data_frame)

tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Adding buttons for ascending and descending sorting
sort_options = ['RollNo', 'Names', 'DOB', 'YOS']
for option in sort_options:
    asc_button = tk.Button(root, text=f"Sort {option} Asc", command=lambda o=option: sort_by(o, True))
    desc_button = tk.Button(root, text=f"Sort {option} Desc", command=lambda o=option: sort_by(o, False))
    asc_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
    desc_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

root.mainloop()
