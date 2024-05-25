import tkinter as tk

# Function to generate Fibonacci sequence
def fibi_genera(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Function to handle the button click event and display the result
def generate_fibonacci():
    try:
        num = int(input_number_entry.get())
        if num < 0:
            result.config(text="Please enter a non-negative integer")
        else:
            fibonacci_sequence = fibi_genera(num)
            result.config(text=f"{fibonacci_sequence}")
    except ValueError:
        result.config(text="Please enter a valid number")

# Create the main window
app = tk.Tk()
app.title("FG")
app.geometry("700x400")
app.config(bg="gray2")
# Title Label
title = tk.Label(app, text="FIBONACCI GENERATOR", bg="gray2", fg="gold", font=('Arial', 30))
title.place(x=100, y=30)

# Input Number Label
input_number = tk.Label(app, text="Enter the number to generate Fibonacci ", bg="gray2", fg="gold", font=('Arial', 15))
input_number.place(x=40, y=150)

# Input Number Entry
input_number_entry = tk.Entry(app, width=15, bg="gray20", fg="gold", font=('Arial', 15))
input_number_entry.place(x=400, y=150)

# Result Label
result = tk.Label(app, text="", bg="gray2", fg="gold", font=('Arial', 15))
result.place(x=100,y=280)

# Generate Button
generate_button = tk.Button(app, text="Generate",cursor="hand2", bg="gray2", fg="gold", command=generate_fibonacci, font=('Arial', 15))
generate_button.place(x=250, y=200)

# Run the Tkinter event loop
app.mainloop()
