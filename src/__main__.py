import tkinter as tk
import tkinter.messagebox
from forex_python.converter import CurrencyRates
from currency_list import CURRENCIES, CURRENCY_TO_ASSET
from PIL import Image, ImageTk


# GUI
root = tk.Tk()

root.title("Current-See")

Tops = tk.Frame(root, bg="#e6e5e5", pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(
    Tops,
    font=("lato black", 19, "bold"),
    text="Current-See",
    bg="#e6e5e5",
    fg="black",
    width=40,
)
headlabel.grid(row=1, column=0, sticky="W")

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")


Image_Label_From = tk.Label(
    root,
    padx=2,
)
Image_Label_From.grid(row=2, column=1, sticky="E")
Image_Label_To = tk.Label(
    root,
    padx=2,
)
Image_Label_To.grid(row=8, column=1, sticky="E")


# Function To For Real Time Currency Conversion
def RealTimeCurrencyConversion():
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo(
            "Error !!", "Amount Not Entered.\n Please a valid amount."
        )

    elif from_currency == "currency" or to_currency == "currency":
        tkinter.messagebox.showinfo(
            "Error !!",
            "Currency Not Selected.\n Please select FROM and TO Currency form menu.",
        )

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        # https://stackoverflow.com/a/54040005
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, str(new_amount))


def get_image(s):
    try:
        return ImageTk.PhotoImage(Image.open(CURRENCY_TO_ASSET[s]).resize((350, 150)))
    except (FileNotFoundError, KeyError):
        return None


def update_images(_):
    from_currency = variable1.get()
    to_currency = variable2.get()
    Image_From = get_image(from_currency)
    Image_To = get_image(to_currency)
    Image_Label_From.image = Image_From
    Image_Label_From.configure(image=Image_From)
    Image_Label_To.image = Image_To
    Image_Label_To.configure(image=Image_To)


# clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


root.configure(background="#e6e5e5")
root.geometry("1000x700")

Label_1 = tk.Label(
    root,
    font=("lato black", 27, "bold"),
    text="",
    padx=2,
    pady=2,
    bg="#e6e5e5",
    fg="black",
)
Label_1.grid(row=1, column=0, sticky="W")

label1 = tk.Label(
    root,
    font=("lato black", 15, "bold"),
    text="\t    Amount  :  ",
    bg="#e6e5e5",
    fg="black",
)
label1.grid(row=2, column=0, sticky="W")

label1 = tk.Label(
    root,
    font=("lato black", 15, "bold"),
    text="\t    From Currency  :  ",
    bg="#e6e5e5",
    fg="black",
)
label1.grid(row=3, column=0, sticky="W")

label1 = tk.Label(
    root,
    font=("lato black", 15, "bold"),
    text="\t    To Currency  :  ",
    bg="#e6e5e5",
    fg="black",
)
label1.grid(row=4, column=0, sticky="W")

label1 = tk.Label(
    root,
    font=("lato black", 15, "bold"),
    text="\t    Converted Amount  :  ",
    bg="#e6e5e5",
    fg="black",
)
label1.grid(row=8, column=0, sticky="W")

Label_1 = tk.Label(
    root,
    font=("lato black", 7, "bold"),
    text="",
    padx=2,
    pady=2,
    bg="#e6e5e5",
    fg="black",
)
Label_1.grid(row=5, column=0, sticky="W")

Label_1 = tk.Label(
    root,
    font=("lato black", 7, "bold"),
    text="",
    padx=2,
    pady=2,
    bg="#e6e5e5",
    fg="black",
)
Label_1.grid(row=7, column=0, sticky="W")


FromCurrency_option = tk.OptionMenu(root, variable1, *CURRENCIES, command=update_images)
ToCurrency_option = tk.OptionMenu(root, variable2, *CURRENCIES, command=update_images)

FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky="E")
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky="E")

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky="E")

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky="E")

Label_9 = tk.Button(
    root,
    font=("arial", 15, "bold"),
    text="   Convert  ",
    padx=2,
    pady=2,
    bg="lightblue",
    fg="white",
    command=RealTimeCurrencyConversion,
)
Label_9.grid(row=6, column=0)

Label_1 = tk.Label(
    root,
    font=("lato black", 7, "bold"),
    text="",
    padx=2,
    pady=2,
    bg="#e6e5e5",
    fg="black",
)
Label_1.grid(row=9, column=0, sticky="W")

Label_9 = tk.Button(
    root,
    font=("arial", 15, "bold"),
    text="   Clear All  ",
    padx=2,
    pady=2,
    bg="lightblue",
    fg="white",
    command=clear_all,
)
Label_9.grid(row=10, column=0)


root.mainloop()
