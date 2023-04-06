from tkinter import *
import cryption

root = Tk()
root.title("Encryption Decryption")
root.geometry("550x650")
root.resizable(False, False)

def main():

    def encrypt():
        eK = cryption.get_key(keyE.get().encode('utf-8'))
        outputE.delete("1.0", "end")
        o = cryption.encrypt(eK, messageE.get().encode('utf-8'))
        outputE.insert(END, o)

    # ===== ENCRYPT =====
    Label(root, text="Encrypt", font=('arial', 25)).place(x=20, y=10)
    
    Label(root, text="Key:", font=('arial', 25)).place(x=220, y=10)
    keyE = Entry(root, font=('arial', 20))
    keyE.place(x=300, y=15, height=35, width=100)
    
    Label(root, text="Message", font=('arial' , 20)).place(x=15, y=75)
    messageE = Entry(root, font=('arial', 20))
    messageE.place(x=150, y=80, height=35, width=360)
    Button(root, text="Encrypt", font=('arial', 25), command=encrypt).place(x=10, y=130, height=35, width=530)
    outputE = Text(root)
    outputE.place(x=0, y=180, height=150, width=550)


    def decrypt():
        dK = cryption.get_key(keyD.get().encode('utf-8'))
        outputD.delete("1.0", "end")
        o = cryption.decrypt(dK, messageD.get().encode('utf-8'))
        outputD.insert(END, o)

    # ===== DECRYPT =====
    Label(root, text="Decrypt", font=('arial', 25)).place(x=20, y=335)
    
    Label(root, text="Key:", font=('arial', 25)).place(x=220, y=335)
    keyD = Entry(root, font=('arial', 20))
    keyD.place(x=300, y=340, height=35, width=100)
    
    Label(root, text="Message", font=('arial' , 20)).place(x=15, y=400)
    messageD = Entry(root, font=('arial', 20))
    messageD.place(x=150, y=405, height=35, width=360)
    Button(root, text="Decrypt", font=('arial', 25), command=decrypt).place(x=10, y=455, height=35, width=530)
    outputD = Text(root)
    outputD.place(x=0, y=505, height=150, width=550)



main()

root.mainloop()


"""
key = get_key("asd".encode('utf-8'))
token = "Bro".encode('utf-8')

print(key)
print(encrypt(key, token))
print(decrypt(key, b'gAAAAABkLvKmIdgstByaj58X5ILUOTpSxeoYrhQawevKQ_d3dvoVaKRKXsczoJ4n2w8tm_PINAHytxeezhLEvYvptv6Mmopi1g=='))
"""