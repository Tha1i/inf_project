def encrypt(sequence):
    encrypted_seq = [sequence[0]]

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            encrypted_seq.append(1)
        else:
            encrypted_seq.append(0)

    return encrypted_seq


def decrypt(encrypted_seq):
    decrypted_seq = [encrypted_seq[0]]

    for i in range(1, len(encrypted_seq)):
        if encrypted_seq[i] == 1:
            decrypted_seq.append(decrypted_seq[i - 1])
        else:
            decrypted_seq.append(1 - decrypted_seq[i - 1])

    return decrypted_seq


input_ = [0, 1, 1, 0, 0, 1, 1, 1]
encrypted = encrypt(input_)
decrypted = decrypt(encrypted)

print("Исходная последовательность:", input_)
print("Зашифрованная последовательность:", encrypted)
print("Расшифрованная последовательность:", decrypted)
