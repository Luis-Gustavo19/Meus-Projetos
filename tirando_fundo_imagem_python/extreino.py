import os
pasta2 = os.getcwd()+'\pasta2'
for c in os.listdir(pasta2):
    os.remove(f"{pasta2}\{c}")