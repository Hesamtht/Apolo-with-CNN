import tkinter as tk
import pandas as pd
from tkinter import messagebox
from openpyxl import Workbook

def read_data():
    try:
        df = pd.read_excel("food_data.xlsx")
        return df
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data found!")
        return pd.DataFrame(columns=["Food Name", "Price", "Preparation Time"])

def write_data(df):
    df.to_excel("food_data.xlsx", index=False)

def manage_food():
        # ایجاد پنجره مدیریت غذا
    food_window = tk.Toplevel(root)
    food_window.title("Manage Food")

    # خواندن داده‌ها از فایل
    df = read_data()

    # اندازه پنجره
    food_window.geometry("1024x865")

        # ایجاد ویرایشگر داده‌ها
    entry_frame = tk.Frame(food_window)
    entry_frame.pack()

    food_name_var = tk.StringVar()
    price_var = tk.StringVar()
    prep_time_var = tk.StringVar()

  

    tk.Label(entry_frame, text="Food Name:").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(entry_frame, textvariable=food_name_var).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Price:").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(entry_frame, textvariable=price_var).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Preparation Time:").grid(row=2, column=0, padx=5, pady=5)
    tk.Entry(entry_frame, textvariable=prep_time_var).grid(row=2, column=1, padx=5, pady=5)
    def save_data():
        food_name = food_name_var.get()
        price = price_var.get()
        prep_time = prep_time_var.get()

        if food_name and price and prep_time:
            new_data = {"Food Name": [food_name], "Price": [price], "Preparation Time": [prep_time]}
            df_new = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
            write_data(df_new)
            messagebox.showinfo("Success", "Data saved successfully.")
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def back():
        food_window.destroy()

    # ایجاد دکمه‌ها
    tk.Button(food_window, text="Save", command=save_data).pack(pady=5)
    tk.Button(food_window, text="Back", command=back).pack(pady=5)

def settings():
        # این قسمت را می‌توانید برای ایجاد صفحه تنظیمات پر کنید
    print("Redirecting to settings page...")

def exit_program():
    # خروج از برنامه
    root.destroy()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Main Page")

# ایجاد دکمه مدیریت غذا
btn_manage_food = tk.Button(root, text="Manage Food", width=20, command=manage_food)
btn_manage_food.pack(pady=5)
# ایجاد یک برچسب
label = tk.Label(root, text="Choose an option:", font=("Arial", 14))
label.pack(pady=10)

# ایجاد دکمه‌ها
btn_manage_food = tk.Button(root, text="Manage Food", width=20, command=manage_food)
btn_manage_food.pack(pady=5)

btn_settings = tk.Button(root, text="Settings", width=20, command=settings)
btn_settings.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=20, command=exit_program)
btn_exit.pack(pady=5)

# اجرای حلقه اصلی
root.mainloop()
