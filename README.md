# OPT utility

This is a simple Windows setup and customization tool that helps me speed up my operating system installations. I created it because I've been installing a lot of Windows-based systems lately, and I need tools like this for those installations. When rating and reviewing this item, please keep in mind that it was created in a single day by a beginner. For some reason, on the custom Windows systems I use, winget doesn't work from the Command Prompt—only from PowerShell—so part of the code looks a little strange.

<img width="770" height="612" alt="image" src="https://github.com/user-attachments/assets/acd87a28-c720-4458-9812-abeaaffabd82" />

## Executing program
1. Download the OPT from the releases page
2. Run it with admin rights
3. Done :)

## Functions in short:
- Cleanup: This deletes the contents of the temp, %temp%, and prefetch folders
- Disable services: Disables Sysmain, Print Services, and Indexer

## Note:
Use this tool at your own risk. Before disabling services or deleting system files, make sure you know what you're doing.

# Used Libraries and Docs

- https://customtkinter.tomschimansky.com/documentation/whats-new
- https://docs.python.org/3/library/winreg.html
- https://docs.python.org/3/library/subprocess.html

# AI usage

Because of my previous bad experiences, I didn't use AI for development—just a simple translator
