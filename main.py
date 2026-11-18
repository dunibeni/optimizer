import os
import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("OPT utility")
app.geometry("500x400")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
button1 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button1.grid(row=0, column=0, padx=(15, 5), pady=6, sticky="ew")
button2 = customtkinter.CTkButton(app, text="setting2", command=button_callback)
button2.grid(row=0, column=1, padx=(5, 15), pady=6, sticky="ew")
button3 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button3.grid(row=1, column=0, padx=(15, 5), pady=6, sticky="ew")
button4 = customtkinter.CTkButton(app, text="setting2", command=button_callback)
button4.grid(row=1, column=1, padx=(5, 15), pady=6, sticky="ew")

button5 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button5.grid(row=2, column=0, padx=(15, 5), pady=6, sticky="ew")
button6 = customtkinter.CTkButton(app, text="setting2", command=button_callback)
button6.grid(row=2, column=1, padx=(5, 15), pady=6, sticky="ew")
button7 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button7.grid(row=3, column=0, padx=(15, 5), pady=6, sticky="ew")
button8 = customtkinter.CTkButton(app, text="setting2", command=button_callback)
button8.grid(row=3, column=1, padx=(5, 15), pady=6, sticky="ew")
app.mainloop()