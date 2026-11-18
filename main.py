import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")

# Heading
heading = tk.Label(
    root,
    text="WEATHER APP",
    font=("Arial", 24, "bold")
)
heading.pack(pady=30)

# Welcome message
message = tk.Label(
    root,
    text="Welcome! Check your city's weather.",
    font=("Arial", 12)
)
message.pack(pady=10)

# Run application
root.mainloop()
