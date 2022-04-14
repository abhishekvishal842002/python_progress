#old approach (untidy)

# def abhi(vish):
#     def shek():
#         print("abhishek")
#         vish()
#         print("vishal")
#     return shek

# def al():
#     print("abhishek vishal")
# al=abhi(al)
# al()




# decorator approach (tidy)
def abhi(vish):
    def shek():
        print("abhishek")
        vish()
        print("vishal")
    return shek

@abhi
def al():
    print("abhishek vishal")
al()