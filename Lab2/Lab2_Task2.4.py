from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 1. Tạo dữ liệu 1000 byte ngẫu nhiên
data = get_random_bytes(1000)

key = get_random_bytes(16)   # AES-128
iv  = get_random_bytes(16)

def pad(data):
    # Đệm cho đủ bội số 16 byte (AES block size), dùng PKCS7 đơn giản
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def flip_bit(ciphertext, byte_index, bit_index=0):
    # Đảo 1 bit tại byte thứ byte_index (giữ nguyên các byte khác)
    ct = bytearray(ciphertext)
    ct[byte_index] ^= (1 << bit_index)
    return bytes(ct)

def count_corrupted_blocks(original, decrypted, block_size=16):
    # Đếm xem có bao nhiêu khối 16-byte bị sai so với bản gốc
    n_blocks = len(original) // block_size
    corrupted = 0
    for i in range(n_blocks):
        start, end = i * block_size, (i + 1) * block_size
        if original[start:end] != decrypted[start:end]:
            corrupted += 1
    return corrupted, n_blocks


def test_mode(mode_name, mode_const, use_iv=True):
    plaintext_padded = pad(data)

    # --- Mã hóa ---
    if use_iv:
        cipher = AES.new(key, mode_const, iv)
    else:
        cipher = AES.new(key, mode_const)
    ciphertext = cipher.encrypt(plaintext_padded)
    #print(ciphertext[:64].hex())

    # --- Làm hỏng bản mã: đảo 1 bit tại byte thứ 26 ---
    corrupted_ct = flip_bit(ciphertext, byte_index=26)

    # --- Giải mã bản mã đã bị lỗi ---
    if use_iv:
        decipher = AES.new(key, mode_const, iv)
    else:
        decipher = AES.new(key, mode_const)
    decrypted = decipher.decrypt(corrupted_ct)
    #print(decrypted[:64].hex())

    # --- So sánh với bản rõ gốc (đã pad) ---
    corrupted_blocks, total_blocks = count_corrupted_blocks(plaintext_padded, decrypted)

    print(f"--- Mode: {mode_name} ---")
    print(f"Tổng số khối: {total_blocks}")
    print(f"Số khối bị hỏng: {corrupted_blocks}")
    print(f"Tỷ lệ: {corrupted_blocks/total_blocks*100:.2f}%\n")
    return corrupted_blocks, total_blocks


# ECB không dùng IV
test_mode("ECB", AES.MODE_ECB, use_iv=False)

# CBC, CFB, OFB dùng IV
test_mode("CBC", AES.MODE_CBC, use_iv=True)
test_mode("CFB", AES.MODE_CFB, use_iv=True)
test_mode("OFB", AES.MODE_OFB, use_iv=True)
