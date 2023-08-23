from ImageSteg import ImageSteg
from PIL import Image



img = ImageSteg()
encrypt_pass = input("enter pin to encrypt the message:: ")
img.encrypt_text_in_image("test.jpg", "\n\n\n\t\t\t\t\t\t\t MICROSOFT \n\n\n\t\t\t\t\t\t\tCopyrighted content \n\t Visit Use of Microsoft copyrighted content to learn how to use photography, box shots, and screenshots.\n\n\n\t\t\t\t\t\t\tLegal notice \n\n Any use of Microsofts Brand Assets inures solely to Microsofts benefit and all use must comply with these Trademark Guidelines, or other licensing/contractual arrangements with Microsoft. Third parties, including licensees, may never claim ownership rights in Microsofts Brand Assets, or brands that are confusingly similar to Microsofts Brand Assets, in any manner, including without limitation as a trademark, service mark, company name or designation, domain name, social media profile/handle, or in any other manner.Microsoft expressly reserves the right in its sole discretion to terminate, revoke, modify, or otherwise change permission to use its Brand Assets at any time and expressly reserves the right to object to any use or misuse of its Brand Assets in any jurisdiction worldwide.",encrypt_pass, "static/")




print("The image has been decrypted\nPlease enter the pin to view the secret text ")
decrypt_pass = input("enter pin to encrypt the message:: ")
decrypted_text = img.decrypt_text_in_image("static/test_encrypted.png",encrypt_pass,decrypt_pass)




if decrypted_text:
    print("Decrypted Text:", decrypted_text)
else:
    print("Incorrect password or no message found.")
    print("Content has been erased!!!!")
