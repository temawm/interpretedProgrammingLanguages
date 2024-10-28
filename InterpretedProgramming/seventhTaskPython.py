def decrypt_char(c):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    if c in alphabet:
        index = alphabet.index(c)
        if c == 'я':
            return 'а'
        return alphabet[index + 1]
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


def count_pairs(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip().split()
        N = int(first_line[0])
        K = int(first_line[1])
        ratings = [int(f.readline().strip()) for _ in range(N)]
    ratings.sort()

    left = 0
    right = N - 1
    count = 0

    while left < right:
        if ratings[left] + ratings[right] >= K:
            count += (right - left)
            right -= 1
        else:
            left += 1

    return count

# Пример использования
input_file = 'ratings.txt'
result = count_pairs(input_file)
print(result)





