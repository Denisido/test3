class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        alpha = CipherMaster.alphabet
        len1 = len(alpha)
        for letter in text:
            if letter.lower() not in alpha:
                result.append(letter)
            else:
                if is_encrypt:
                    index = (alpha.find(letter.lower()) + shift) % len1
                else:
                    index = (alpha.find(letter.lower()) - shift) % len1
                result.append(alpha[index])
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект '
    'с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — '
    'э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
