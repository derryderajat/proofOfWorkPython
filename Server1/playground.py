import pyperclip
# data  = {
#     "fileName" :{
#         "apa":12,
#         "23":32
#     }
# }

# print(data["fileName"]["apa"])
import base64
from aes import AESCipher
folder = "./upload"
path = folder + "/"+"8b5b9276564e4a4fa1cacbcbdb606046.png"
aes = AESCipher("000")
# img = 
# s1 = "Selaolo"
# pyperclip.copy(s1)
# s2 = pyperclip.paste()
# print(s2)

img = pyperclip.paste()

print(type(img))
decrypt = aes.decrypt(img)
print(len(img))

