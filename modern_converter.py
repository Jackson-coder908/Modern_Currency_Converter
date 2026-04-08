import customtkinter as ctk
import requests
from tkinter import messagebox

# Set the look and feel
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class ModernConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pro Currency Converter")
        self.geometry("400x520")
        
        # Fetch Data
        self.fetch_rates()

        # --- UI ELEMENTS ---
        self.label = ctk.CTkLabel(self, text="Currency Converter", font=("Roboto", 24, "bold"))
        self.label.pack(pady=30)

        # Amount Entry
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Enter Amount", width=250, height=45, font=("Roboto", 16))
        self.amount_entry.pack(pady=10)

        # From Dropdown
        self.from_menu = ctk.CTkOptionMenu(self, values=self.currencies, width=250, height=40)
        self.from_menu.set("USD")
        self.from_menu.pack(pady=10)

        # Swap Button (Minimalist)
        self.swap_btn = ctk.CTkButton(self, text="↑↓ Swap", width=100, height=30, fg_color="transparent", border_width=1, command=self.swap)
        self.swap_btn.pack(pady=5)

        # To Dropdown
        self.to_menu = ctk.CTkOptionMenu(self, values=self.currencies, width=250, height=40)
        self.to_menu.set("EUR")
        self.to_menu.pack(pady=10)

        # Result Area
        self.result_label = ctk.CTkLabel(self, text="0.00", font=("Roboto", 32, "bold"), text_color="#3b8ed0")
        self.result_label.pack(pady=30)

        # Convert Button
        self.convert_btn = ctk.CTkButton(self, text="CONVERT", width=250, height=50, font=("Roboto", 16, "bold"), command=self.convert)
        self.convert_btn.pack(pady=10)

    def fetch_rates(self):
        try:
            data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
            self.rates = data['rates']
            self.currencies = sorted(list(self.rates.keys()))
        except:
            messagebox.showerror("Error", "No Internet Connection")
            self.destroy()

    def swap(self):
        f, t = self.from_menu.get(), self.to_menu.get()
        self.from_menu.set(t)
        self.to_menu.set(f)

    def convert(self):
        try:
            amt = float(self.amount_entry.get())
            res = (amt / self.rates[self.from_menu.get()]) * self.rates[self.to_menu.get()]
            self.result_label.configure(text=f"{res:,.2f} {self.to_menu.get()}")
        except:
            messagebox.showwarning("Input Error", "Please enter a valid number")

if __name__ == "__main__":
    app = ModernConverter()
    app.mainloop()