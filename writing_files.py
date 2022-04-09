# WRITING A NEW FILE 

# f = open("abhishek.papes","w")
# f.write("my name is abhishek vishal.\n")
# f.close()



#WRITING A FILE AND PRINTING THE NO. OF CHARACTERS PRINTED IN THE FILE

# f = open("abhishek.papes","w")
# a=f.write("my name is abhishek vishal.\n")
# print (a)
# f.close()



#APPENDING A FILE WITHOUT AFFECTING THE PREVIOUS CONTENT

# f = open("abhishek.papes","a")
# a=f.write("I am a student of SHRI MATA VAISHNO DEVI UNIVERSITY (SMVDU).\n")
# print (a)
# f.close()



#HANDLING READ AND WRITE BOTH

# f = open("abhishek.papes","r+")
# print(f.read())
# f.write("THANK YOU!")
# f.close()