import tkinter as tk
from tkinter import messagebox


def pop_up_message():
    # Creates the main window
    root = tk.Tk()
    root.withdraw()  # Hides the main window

    # Shows the message box
    messagebox.showinfo("You've been infected with the Brazilian Virus!!!"
                        , "Hello, I'm the Brazilian Virus. Due to the constant neglect of science and technology in my country over the decades"
                          ", I am not able to cause any harm to your system. Please be so kind as to destroy it in your preferred manner.")


if __name__ == "__main__":
    pop_up_message()
