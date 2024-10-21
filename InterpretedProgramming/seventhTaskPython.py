def decrypt_char(c):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    if c in alphabet:
        index = alphabet.index(c)
        if c == 'я':
            return 'а'
        return alphabet[index - 1]
    else:
        return c

def decrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        encrypted_text = infile.read()

    decrypted_text = ''.join(decrypt_char(c) for c in encrypted_text)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(decrypted_text)

input_filename = 'encrypted.txt'
output_filename = 'decrypted.txt'

decrypt_file(input_filename, output_filename)
