import tkinter as tk 
import tkinter.font as tkFont

app = tk.Tk()
app.title("Student Grader")
app.geometry("520x700")
app.config(bg="skyblue1")

header_font = tkFont.Font(family="Helvetica", size=30, weight="bold")
title = tk.Label(app, text="GRADE CALCULATOR", font=header_font, bg="skyblue1", fg="snow")
title.place(x=40, y=20)
entry_y_position = 200  # Initial y position for the first subject and grade entries

button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
content_font = tkFont.Font(family="Helvetica", size=12)

subject_entries = []
grade_entries = []
subject_labels = []
grade_labels = []

def add_subject():
    global entry_y_position
    
    subject_label = tk.Label(app, text="Subject:", font=content_font, bg="skyblue1")
    subject_label.place(x=30, y=entry_y_position)
    subject_labels.append(subject_label)
    
    subject_entry = tk.Entry(app, font=content_font, width=10)
    subject_entry.place(x=120, y=entry_y_position)
    subject_entries.append(subject_entry)
    
    grade_label = tk.Label(app, text="Grade:", font=content_font, bg="skyblue1")
    grade_label.place(x=280, y=entry_y_position)
    grade_labels.append(grade_label)
    
    grade_entry = tk.Entry(app, font=content_font, width=10)
    grade_entry.place(x=360, y=entry_y_position)
    grade_entries.append(grade_entry)
    
    entry_y_position += 40 

def delete():
    global entry_y_position
    if subject_labels and subject_entries and grade_labels and grade_entries:
        subject_label = subject_labels.pop()
        subject_label.destroy()
        
        subject_entry = subject_entries.pop()
        subject_entry.destroy()
        
        grade_label = grade_labels.pop()
        grade_label.destroy()
        
        grade_entry = grade_entries.pop()
        grade_entry.destroy()
        
        entry_y_position -= 40

def calculate_average():
    total = 0
    count = 0
    for entry in grade_entries:
        try:
            grade = float(entry.get())
            total += grade
            count += 1
        except ValueError:
            result_label.config(text="Please enter valid grades.", fg="red")
            return

    if count > 0:
        average = total / count
        result_label.config(text=f"The Average Grade: {average:.2f}", font=('Helvetica',20))
    else:
        result_label.config(text="No grades to calculate average.", fg="red")

add = tk.Button(app, text="add", command=add_subject, font=button_font, bg="lime green", fg="snow")
add.place(x=260, y=100)

delete_button = tk.Button(app, text="delete", command=delete, font=button_font, bg="tomato", fg="snow")
delete_button.place(x=320, y=100)

calculate = tk.Button(app, text="calculate", command=calculate_average, font=button_font, bg="gray17", fg="snow")
calculate.place(x=400, y=100)

result_label = tk.Label(app, text="", font=content_font, bg="skyblue1")
result_label.place(x=20, y=600)

app.mainloop()
