from pycipher import Beaufort
from pycipher import Vigenere
from pycipher import SimpleSubstitution
from pycipher import Playfair
from pycipher import Railfence
from pycipher import Enigma



print(Beaufort('NEU').encipher("WANGWENJIE")) # 加密：密钥 ，明文
# print(Beaufort('GIRL').decipher("YVYHVXJFCVY")) # 解密：密钥 ，密文 

# print(Playfair().encipher(""))
# print(Playfair().decipher(""))

# print(Vigenere('hanxu').encipher('')) #加密
# print(Vigenere('NEU').decipher('qinrgnvsh fcmgig')) #解密

# print(SimpleSubstitution('hanxu').encipher(''))
# print(SimpleSubstitution('hanxu').decipher(''))

# print(Railfence().encipher(''))
# print(Railfence().decipher(''))




