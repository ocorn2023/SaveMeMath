


import sys
import time
from time import sleep
Print("Hello welcome to SaveMeMath. Input you lesson code and get a generated google document")
print(" ")
assing = input("What Is The Assignment code? (grade, *ac for acc*, unit, : ,lesson).           # ")

#animation = "|/-\\"

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
    sys.stdout.flush()
    
print("\nDone!")

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
