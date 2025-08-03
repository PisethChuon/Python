import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Replace with your actual API key from exchangerate-api.com
API_KEY = " "

def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            return data['conversion_rates'][target_currency]
        else:
            raise Exception("Failed to get exchange rates.")
    except Exception as e:
        raise Exception("Error fetching exchange rate: " + str(e))

def convert_currency(amount, rate):
    return round(amount * rate, 2)

def convert():
    try:
        amount = float(entry_amount.get())
        base = combo_base.get()
        target = combo_target.get()

        if base == "" or target == "":
            raise ValueError("Please select both currencies.")

        rate = get_exchange_rate(base, target)
        result = convert_currency(amount, rate)
        label_result.config(text=f"{amount} {base} = {result} {target}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x250")
root.resizable(False, False)

# Amount input
tk.Label(root, text="Amount").grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

# From currency dropdown
tk.Label(root, text="From").grid(row=1, column=0, padx=10, pady=10)
combo_base = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "KHR", "THB"], state="readonly")
combo_base.grid(row=1, column=1)
combo_base.current(0)

# To currency dropdown
tk.Label(root, text="To").grid(row=2, column=0, padx=10, pady=10)
combo_target = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "KHR", "THB"], state="readonly")
combo_target.grid(row=2, column=1)
combo_target.current(1)

# Convert button
tk.Button(root, text="Convert", command=convert).grid(row=3, column=0, columnspan=2, pady=10)

# Result display
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()
