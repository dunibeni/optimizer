import os
import customtkinter
import winreg
import subprocess
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
tm=os.environ.get("TEMP")
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
def clstemp():
    try:
        os.system('del /q /f /s "C:/WINDOWS/Temp\\*.*"')
        os.system(f'del /q /f /s "{tm}\\*.*"')
        os.system('del /q /f /s "C:/WINDOWS/prefetch\\*.*"')
    except Exception:
        pass
def disable():
    os.system("sc stop WSearch & sc config WSearch start= disabled")
    os.system("sc stop SysMain & sc config SysMain start= disabled")
    os.system("sc stop Spooler & sc config Spooler start= disabled")

# !!! Don't change this, whoever you are in the future :D winget doesn't work from the command line in a custom Windows installer. !!!
def oo():
    subprocess.run("winget install -e --id OO-Software.ShutUp10", shell=True)
    
def fire():
    subprocess.run("winget install --id=Mozilla.Firefox -e --silent", shell=True)
def vs():
    subprocess.run("winget install -e --id VSCodium.VSCodium", shell=True)
def ms():
    subprocess.run("winget install -e --id Microsoft.Office", shell=True)
def zi():
    subprocess.run("winget install -e --id 7zip.7zip", shell=True)
def dsinstall():
    subprocess.run("winget install -e --id Discord.Discord", shell=True)
    subprocess.run("winget install -e --id Valve.Steam", shell=True)
def allinstall():
    oo()
    fire()
    vs()
    ms()
    zi()


app = customtkinter.CTk()
app.title("OPT utility")
app.resizable(True, False)
app.geometry("500x400")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
light_mode = customtkinter.CTkButton(app, text="Light mode", fg_color="#474a48", hover_color="#282A28", command=light)
light_mode.grid(row=0, column=0, padx=(15, 5), pady=(12,6), sticky="ew")

dark_mode = customtkinter.CTkButton(app, text="Dark mode", fg_color="#474a48", hover_color="#282A28", command=dark)
dark_mode.grid(row=0, column=1, padx=(5, 15), pady=(12,6), sticky="ew")

cls_temp = customtkinter.CTkButton(app, text="Cleanup", fg_color="#474a48", hover_color="#282A28", command=clstemp)
cls_temp.grid(row=1, column=0, padx=(15, 5), pady=(6, 50), sticky="ew")

dark_moe = customtkinter.CTkButton(app, text="Disable services", fg_color="#474a48", hover_color="#282A28", command=disable)
dark_moe.grid(row=1, column=1, padx=(5, 15), pady=(6, 50), sticky="ew")



ooo = customtkinter.CTkButton(app, text="Install O&O ", command=oo)
ooo.grid(row=2, column=0, padx=(15, 5), pady=6, sticky="ew")
firefox = customtkinter.CTkButton(app, text="Install Firefox", command=fire)
firefox.grid(row=2, column=1, padx=(5, 15), pady=6, sticky="ew")
vscodium = customtkinter.CTkButton(app, text="Install Vscodium", command=vs)
vscodium.grid(row=3, column=0, padx=(15, 5), pady=6, sticky="ew")
msoffice = customtkinter.CTkButton(app, text="Install Ms Office", command=ms)
msoffice.grid(row=3, column=1, padx=(5, 15), pady=6, sticky="ew")
z = customtkinter.CTkButton(app, text="Install 7z", command=zi)
z.grid(row=4, column=0, padx=(15, 5), pady=6, sticky="ew")
ds = customtkinter.CTkButton(app, text="Install Steam and Discord", command=dsinstall)
ds.grid(row=4, column=1, padx=(5, 15), pady=6, sticky="ew")

ds = customtkinter.CTkButton(app, text="Install All", command=allinstall)
ds.grid(row=5, column=1, padx=(5, 15), pady=30, sticky="ew")



reboot_uefi = customtkinter.CTkButton(app, text="Reboot UEFI",fg_color="#991f1d", hover_color="#661109",command=uefi)
reboot_uefi.grid(row=6, column=1, padx=(5, 15), pady=(25,10), sticky="ew")

reboot = customtkinter.CTkButton(app, text="Reboot",fg_color="#167076", hover_color="#0C435F",command=reboot_com)
reboot.grid(row=6, column=0, padx=(15, 5), pady=(25,10), sticky="ew")
app.mainloop()
