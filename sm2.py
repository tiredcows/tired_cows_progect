from gmssl import sm2, func

# 1. 生成私钥
private_key = func.random_hex(64)

# 2. 创建 SM2 对象（先留空公钥）
sm2_signer = sm2.CryptSM2(public_key='', private_key=private_key)

# 3. 从私钥推导出公钥
public_key = sm2_signer._kg(int(private_key, 16), sm2_signer.ecc_table['g'])

# 4. 显示密钥对
print(f"Private Key: {private_key}")
print(f"Public Key:  {public_key}")

# 5. 要签名的消息
message = b"Hello, SM2!"

# 6. 签名
k = func.random_hex(64)
signature = sm2_signer.sign(message, k)
print(f"Signature: {signature}")

# 7. 验签（新对象只需要公钥）
sm2_verifier = sm2.CryptSM2(public_key=public_key, private_key='')
verified = sm2_verifier.verify(signature, message)
print(f"Verified: {verified}")
