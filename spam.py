import tkinter as tk
from tkinter import filedialog
import pyautogui as auto
import time
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import threading
import keyboard 


# =========================Define file path to the UI =====================================
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\GIGABYTE\Desktop\spam\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# =======================================Create the window ======================================
window = tk.Tk()
window.title("Spam Furry By uki")
window.geometry("777x453")
window.configure(bg="#1C1C1C")

# =========================================Global variables==============================================
selected_file = None
stop_flag = False

# ========================================= Choose file function =========================================
def choose_file():
    global selected_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        selected_file = file_path
        entry_1.config(state="normal")  # Enable before modifying
        entry_1.delete("1.0", tk.END)  # Deleting  Existing text
        entry_1.insert(tk.END, f"Chosen file: {Path(file_path).name}\n")  # Choosed file show in log 
        entry_1.config(state="disabled")  # Disable after modification


# Get sleep time
def get_sleep_time():
    try:
        return int(entry_2.get()) if entry_2.get().strip() else 1 #Getting the sleep time and if nothing given it defult value is 1 
    except ValueError:
        return 1  # Default sleep time


# Typing process in a separate thread
def typing_process(file_path, sleep_time):
    global stop_flag  #Cheack stop is hit or not 
    time.sleep(sleep_time)
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if stop_flag:
                break
            auto.typewrite(line.strip())
            auto.press('enter') #press Enter in each line 
    stop_flag = False  # Reset stop flag after process ends

def start():
    global selected_file, stop_flag
    if not selected_file:
        return  # Exit if no file selected

    stop_flag = False  # Reset stop flag
    sleep_time = get_sleep_time()

    # Ensure text box is enabled before updating logs
    entry_1.config(state="normal")  #enable to modify
    entry_1.insert(tk.END, "Starting process...\n")
    entry_1.insert(tk.END, "Press esc to stop the  process...\n")
    entry_1.config(state="disabled") #Disabling modifying access beacuse it can be acidently type 
    entry_2.config(state="disabled") #Disabling modifying access beacuse it can be acidently type 

    # Start the process in a new thread
    thread = threading.Thread(target=typing_process, args=(selected_file, sleep_time))
    thread.start()

def listen_for_hotkey():
    keyboard.wait("esc")  # Press "Esc" to stop the attack
    stop()  # Call the stop function

# Start hotkey listener in a separate thread
hotkey_thread = threading.Thread(target=listen_for_hotkey, daemon=True)
hotkey_thread.start()


def stop():
    entry_1.config(state="normal")
    entry_1.insert(tk.END, "process stopped...\n")  # Fixed typo in "stopped"
    entry_1.config(state="disabled")
    global stop_flag
    stop_flag = True # Set the stop flag to True to halt the process

#====================================== basic UI made with coustem tinker===================================

canvas = Canvas(
    window,
    bg = "#1C1C1C",
    height = 453,
    width = 777,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    147.0,
    204.0,
    image=image_image_1
)

canvas.create_rectangle(
    346.0,
    39.0,
    762.0,
    441.0,
    fill="#2E2D2D",
    outline="")

canvas.create_text(
    447.0,
    83.0,
    anchor="nw",
    text="Choose the File : ",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

#===================== File Choose Button =================================
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=choose_file,
    relief="flat"
)
button_1.place(
    x=578.0,
    y=74.0,
    width=99.0,
    height=29.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    539.5,
    344.0,
    image=entry_image_1
)

#================================== Log text area=========================

entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#FF0000",
    highlightthickness=0
)
entry_1.place(
    x=365.0,
    y=255.0,
    width=349.0,
    height=176.0
)

canvas.create_text(
    359.0,
    232.0,
    anchor="nw",
    text="Logs",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    454.0,
    124.0,
    anchor="nw",
    text="Sleep Time (in S) :",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    597.0,
    131.0,
    image=entry_image_2
)

 #============================= Sleep Time text box ============================
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=583.0,
    y=123.0,
    width=28.0,
    height=14.0
)

#============================  Stop Button ==============================

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=stop, #funtion calling 
    relief="flat"
)
button_2.place(
    x=636.0,
    y=205.0,
    width=50.0,
    height=20.0
)


#=============================== Start Button =============================  
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=start,  #funtion calling 
    relief="flat"
)
button_3.place(
    x=636.0,
    y=171.0,
    width=50.0,
    height=20.0
)
window.resizable(False, False)
window.mainloop()