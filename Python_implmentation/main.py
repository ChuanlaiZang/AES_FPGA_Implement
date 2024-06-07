from time import time
from BitVector import *
'''
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
'''

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

AES_modulus = BitVector(bitstring='100011011')


def ROTL8(x, shift):
    value = BitVector(intVal=x.intValue(), size=8)
    return value << shift


def generate_boxes():
    s_box = [0 for _ in range(256)]
    inv_sbox = [0 for _ in range(256)]

    p = BitVector(intVal=1, size=8)
    q = BitVector(intVal=1, size=8)

    while True:
        p = p.gf_multiply_modular(BitVector(intVal=0x03, size=8), AES_modulus, 8)

        q = q.gf_multiply_modular(BitVector(intVal=0xf6, size=8), AES_modulus, 8)

        xformed = q ^ ROTL8(q, 1) ^ ROTL8(q, 2) ^ ROTL8(q, 3) ^ ROTL8(q, 4)

        s_box[p.intValue()] = (xformed ^ BitVector(intVal=0x63, size=8)).intValue()
        inv_sbox[s_box[p.intValue()]] = p.intValue()

        if p.intValue() == 1:
            break

    s_box[0] = 0x63
    inv_sbox[0x63] = 0
    return s_box, inv_sbox


def make_matrix(data_in_hex, chunk_size):
    chunks = [(data_in_hex[k:k + chunk_size]) for k in range(0, len(data_in_hex), chunk_size)]
    chunks[-1] = chunks[-1] + BitVector(textstring=' ').get_bitvector_in_hex() * ((chunk_size - len(chunks[-1])) // 2)

    blocks = []
    for chunk in chunks:
        word_size = 8  # word contains 4 bytes, so total 4*2=8 Hex characters
        words = [(chunk[k:k + word_size]) for k in range(0, len(chunk), word_size)]

        byte_size = 2  # byte contains 8 bits, so 2 Hex characters
        result = []
        for word in words:
            result.append([BitVector(hexstring=(word[k:k + byte_size])) for k in range(0, len(word), byte_size)])
        # print(result)
        blocks.append(result)

    # print(blocks, print_matrix(blocks))
    return blocks


def key_scheduling(key, key_len):
    if len(key) > key_len:
        key = key[:key_len]
    else:
        key = key + '0' * (key_len - len(key))
    print('key:', key, 'len:', len(key))

    key_in_hex = BitVector(textstring=key).get_bitvector_in_hex()

    return generate_round_keys(key_in_hex)


def generate_round_constant(i, prev_round_constant):
    rc = [BitVector(hexstring='00'), BitVector(hexstring='00'), BitVector(hexstring='00'), BitVector(hexstring='00')]
    if i == 1:
        rc[0] = BitVector(hexstring='01')
    else:
        rc[0] = prev_round_constant[0].gf_multiply_modular(BitVector(hexstring='02'), AES_modulus, 8)

    return rc


def generate_g(root_word, round_no, current_rc):
    root_word = root_word[1:] + root_word[:1]
    g = []
    for byte_value in root_word:
        g.append(byte_substitute(byte_value))

    rc = generate_round_constant(round_no, current_rc)
    g = [i ^ j for i, j in zip(g, rc)]

    return g, rc


def generate_round_keys(key_in_hex):
    w_key = make_matrix(key_in_hex, chunk_size=len(key_in_hex))
    w_key = w_key[0]

    round_constant = []
    for i in range(1, total_rounds):
        g, round_constant = generate_g(w_key[i * 4 - 1], i, round_constant)
        w_key.append([x ^ y for x, y in zip(g, w_key[(i - 1) * 4])])
        for j in range(3):
            w_key.append([x ^ y for x, y in zip(w_key[i * 4 + j], w_key[i * 4 + j - 3])])

    return w_key


def byte_substitute(byte_value):
    s = Sbox[byte_value.intValue()]
    return BitVector(intVal=s, size=8)


def byte_substitute_inverse(byte_value):
    s = InvSbox[byte_value.intValue()]
    return BitVector(intVal=s, size=8)


def left_shift(state):
    t = [BitVector(intVal=0, size=8) for _ in range(len(state))]
    for i in range(len(state[0])):
        for j in range(len(t)):
            t[j] = state[j][i]
        t = t[i:] + t[:i]
        for j in range(len(t)):
            state[j][i] = t[j]

    return state


def right_shift(state):
    t = [BitVector(intVal=0, size=8) for _ in range(len(state))]
    for i in range(len(state[0])):
        for j in range(len(t)):
            t[j] = state[j][i]
        t = t[len(t)-i:] + t[:len(t)-i]
        for j in range(len(t)):
            state[j][i] = t[j]

    return state


def matrix_multiplication(mixer, state):
    rows, cols = (len(mixer[0]), len(state))
    result = [[BitVector(hexstring='00') for _ in range(rows)] for _ in range(cols)]

    for i in range(len(mixer)):
        for j in range(len(state)):
            for k in range(len(state[j])):
                # print('multiplying ', mixer[i][k].get_bitvector_in_hex(), state[j][k].get_bitvector_in_hex(), i, j, k)
                result[j][i] ^= mixer[i][k].gf_multiply_modular(state[j][k], AES_modulus, 8)
            # print('found: ', result[j][i].get_bitvector_in_hex())

    return result


def encrypt(block):
    # round 0
    state = []
    for i in range(len(block)):
        state.append([x ^ y for x, y in zip(w[i], block[i])])
    # print('round 0:', print_matrix(state))

    # round 1-10
    for r in range(1, total_rounds):

        # byte substitute
        for state_col in state:
            for j in range(len(state_col)):
                state_col[j] = byte_substitute(state_col[j])
        # print('byte sub:', print_matrix(state))

        # shift row
        state = left_shift(state)
        # print(row shift', print_matrix(state))

        # mix columns
        if r != total_rounds - 1:
            state = matrix_multiplication(Mixer, state)
            # print('mix column', print_matrix(state))

        # add round key
        for i in range(len(state)):
            state[i] = [x ^ y for x, y in zip(state[i], w[i + (4 * r)])]
        # print('round', r, print_matrix(state))

    return state


def decrypt(block):
    state = []
    for i in range(len(block)):
        state.append([x ^ y for x, y in zip(block[i], w[i + (4 * (total_rounds - 1))])])
    # print('round 0', print_matrix(state))

    # round 1-10
    for r in range(total_rounds - 1, 0, -1):

        # inverse shift row
        state = right_shift(state)
        # print('inverse shift row', print_matrix(state))

        # inverse byte substitute
        for state_col in state:
            for j in range(len(state_col)):
                state_col[j] = byte_substitute_inverse(state_col[j])
        # print('inverse byte shift', print_matrix(state))

        # add round key
        for i in range(len(state)):
            # print('adding w', i + (4 * (r-1)))
            state[i] = [x ^ y for x, y in zip(state[i], w[i + (4 * (r - 1))])]

        # inverse mix columns
        if r != 1:
            state = matrix_multiplication(InvMixer, state)
            # print('inverse mix column', print_matrix(state))

        # print('round', r, print_matrix(state))
    return state


def encryption(blocks):
    cipher_text_in_hex = []
    for block in blocks:
        cipher_text_in_hex.append(encrypt(block))

    return matrix_to_hex_data_in_string(cipher_text_in_hex)


def decryption(blocks):
    retrieved_text_in_hex = []
    for block in blocks:
        retrieved_text_in_hex.append(decrypt(block))

    return matrix_to_hex_data_in_string(retrieved_text_in_hex)


def print_matrix(block):
    for word in block:
        for byte in word:
            print(byte.get_bitvector_in_hex(), end=' ')
    print()
    return ''


def matrix_to_hex_data_in_string(data_in_hex):
    data = []
    for block in data_in_hex:
        for word in block:
            for byte in word:
                data.append(byte.get_bitvector_in_hex())
    return ''.join(data)


Sbox, InvSbox = generate_boxes()
config = [(128, 16, 11), (192, 24, 13), (256, 32, 15)]

try:
    '''
    key = 'Thats My Kung Fu'
    # data_in_hex = BitVector(textstring='Two Three Five Four Ten').get_bitvector_in_hex()

    filename = 'love.png'
    with open(filename, 'rb') as f:
        file_data = f.read()
        data_in_hex = file_data.hex()
    op = '2'
    '''

    # input_prompt = f'Enter your key({key_len} characters at most):'
    key = input('Enter your key: ')

    print('\nChoose an option:')
    print('1.Text', '2.File')
    op = input('Enter your option: ')

    filename = 'text.txt'
    if int(op) == 1:
        text = input('Enter you text: ')
        data_in_hex = BitVector(textstring=text).get_bitvector_in_hex()
    else:
        filename = input('Enter File name:')
        with open(filename, 'rb') as f:
            file_data = f.read()
            data_in_hex = file_data.hex()

    for value in config:
        config_mode, key_len, total_rounds = value

        start = time()
        w = key_scheduling(key, key_len)
        end = time()

        key_scheduling_time = end - start

        # print(print_matrix(w[0:4]))
        # print('generated keys:')
        # for i in range(0, len(w), 4):
        #    print_matrix(w[i:i+4])

        if int(op) == 1:
            print('data_in_hex: ', data_in_hex, '\n')

        # Encryption Process
        start = time()
        cipher_text = encryption(make_matrix(data_in_hex, chunk_size=key_len*2))
        end = time()

        encryption_time = end - start

        with open(f'encrypted_{config_mode}_bits_' + filename, 'w') as f:
            f.write(cipher_text)

        if int(op) == 1:
            print('cipher text:', cipher_text, '[IN HEX]')

        # Decryption Process
        with open(f'encrypted_{config_mode}_bits_' + filename, 'rb') as f:
            file_data = f.read()
            file_data_in_hex = file_data.decode()

        start = time()
        retrieved_hex = decryption(make_matrix(file_data_in_hex, chunk_size=key_len*2))
        end = time()

        decryption_time = end - start

        with open(f'{config_mode}_bits_decrypted_' + filename, 'wb') as f:
            f.write(bytes.fromhex(retrieved_hex))

        if int(op) == 1:
            print('\ndeciphered text:')
            print(retrieved_hex, '[IN HEX]')
            print(bytes.fromhex(retrieved_hex).decode(), '[IN ASCII]')

        print('\nExecution Time:', f'[{config_mode} bits]')
        print('key_scheduling_time:', key_scheduling_time, 'seconds')
        print('encryption_time:', encryption_time, 'seconds')
        print('decryption_time:', decryption_time, 'seconds\n')

except Exception as e:
    print(str(e))