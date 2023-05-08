import pyAesCrypt
import os


var = str(input("\n\nIf creating an AES encrypted message to hold then type the number 1 and confirm with enter. (1) \nIf opening a stored message type the number 2 then confirm with enter. (2) \n\nInput here:  "))

if var == "1":
    #cleanup base 
       
    if os.path.exists("data.txt.aes"):
        os.remove("data.txt.aes")
        
    #create password and file
    password = str(input("\nWhat would you like to set as your encryption password? Press enter to confirm... \n\nInput here:  "))

    responce = str(input("\nPlease type your message below and press enter to confirm... \n\nInput here:  "))

    contents = str(responce)

    with open("data.txt","w") as file:
        file.write(f"{responce}")
        file.close()

    # encrypt
    pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password)
    
    #cleanup
    
    os.remove("data.txt")
    #confirm

    print("\nDone! Please clear your terminal to avoid data retention.\n\n")
elif var == "2":
    #gets key
    password1 = str(input("\nPlease enter your password then press enter to confirm... \n\nInput here:  "))

    # decrypt
    bufferSize = 128 * 1024
    pyAesCrypt.decryptFile("data.txt.aes", "data.txt", password1, bufferSize)

    #cleanup
    os.remove("data.txt.aes")

    #confirm
    print("\nDone! Your data is below:\n")

    f = open('data.txt', 'r')
    decrypted_data = f.read()
    print ("\n--------------\n")
    print (decrypted_data)
    print ("\n--------------\n\n")
    f.close()

    #purge data
    if os.path.exists("data.txt"):
        os.remove("data.txt")
exit
