import os
import customtkinter
import winreg
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
def button_callback():
    print("button pressed")

def light():
    winreg.SetValueEx(winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"), "SystemUsesLightTheme", 0, winreg.REG_SZ, "1")
    os.system("taskkill /f /im explorer.exe & start explorer.exe")
def dark():
    winreg.SetValueEx(winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"), "SystemUsesLightTheme", 0, winreg.REG_SZ, "0")
    os.system("taskkill /f /im explorer.exe & start explorer.exe")
def uefi():
    os.system("shutdown /r /fw /t 0")
def reboot_com():
    os.system("shutdown /r /t 0")
app = customtkinter.CTk()
app.title("OPT utility")
app.geometry("500x400")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
light_mode = customtkinter.CTkButton(app, text="Light mode", fg_color="#474a48", hover_color="#282A28", command=light)
light_mode.grid(row=0, column=0, padx=(15, 5), pady=10, sticky="ew")

dark_mode = customtkinter.CTkButton(app, text="Dark mode", fg_color="#474a48", hover_color="#282A28", command=dark)
dark_mode.grid(row=0, column=1, padx=(5, 15), pady=10, sticky="ew")



button3 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button3.grid(row=1, column=0, padx=(15, 5), pady=(20, 6), sticky="ew")
button4 = customtkinter.CTkButton(app, text="setting2", command=button_callback)
button4.grid(row=1, column=1, padx=(5, 15), pady=(20, 6), sticky="ew")


button5 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button5.grid(row=2, column=0, padx=(15, 5), pady=6, sticky="ew")
button6 = customtkinter.CTkButton(app, text="setting2", command=button_callback)
button6.grid(row=2, column=1, padx=(5, 15), pady=6, sticky="ew")
button7 = customtkinter.CTkButton(app, text="setting1", command=button_callback)
button7.grid(row=3, column=0, padx=(15, 5), pady=6, sticky="ew")
reboot_uefi = customtkinter.CTkButton(app, text="Reboot UEFI",fg_color="#991f1d", hover_color="#661109",command=uefi)
reboot_uefi.grid(row=3, column=1, padx=(5, 15), pady=(210,1), sticky="ew")

reboot = customtkinter.CTkButton(app, text="Reboot",fg_color="#167076", hover_color="#0C435F",command=reboot_com)
reboot.grid(row=3, column=0, padx=(15, 5), pady=(210,1), sticky="ew")
app.mainloop()