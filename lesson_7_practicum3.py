class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        alpha = CipherMaster.alphabet
        len1 = len(alpha)
        for letter in original_text:
            if letter not in alpha:
                result.append(letter)
            else:
                index = (alpha.find(letter.lower()) + shift) % len1
                result.append(alpha[index])
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        result = []
        alpha = CipherMaster.alphabet
        len1 = len(alpha)
        for letter in cipher_text:
            if letter not in alpha:
                result.append(letter)
            else:
                index = (alpha.find(letter.lower()) - shift) % len1
                result.append(alpha[index])
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект '
    'с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — '
    'э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
