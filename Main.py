


import tkinter as tk
from time import sleep
Print("Hello welcome to SaveMeMath. Input you lesson code and get a generated google document")
print(" ")
assing = input("What Is The Assignment code? (grade, *ac for acc*, unit, : ,lesson).           # ")

def task():
    # The window will stay open until this function call ends.
    sleep(6) # Replace this with the code you want to run
    root.destroy()

root = tk.Tk()
root.title("loading")

label = tk.Label(root, text="Sanning files for your request")
label.pack()

root.after(200, task)
root.mainloop()

print("compiling data....")
sleep(1)
print("1/3")
sleep(3)
print("2/3")
sleep(7)
print("3/3")
print(" file/jason.compile/google.com.doc/id:", assing, " .savememath/html.file/load")
sleep(1)
print(" send.file")

if assing == "7ac5:1":
  print(" here is your link to the document. :  https://docs.google.com/document/d/108xSJxqkqfkwGnR1Wh_v28T0y_0C6zYbLsqwR01Uva0/view")
