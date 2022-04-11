# WITH BLOCK IS USED FOR OPENING A FILE AND IT ALSO 
# CLOSES THE FILE AUTOMATICALLY.
with open("abhi.txt") as f:
    a=f.readlines()
    print(a)

