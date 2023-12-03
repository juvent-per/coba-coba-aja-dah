from jose import jwe

token = "<eyJhbGciOiJBMTI4S1ciLCJjdHkiOiJhcHBsaWNhdGlvbi9qc29uIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImtpZCI6IjEzMzM3IiwiemlwIjoiREVGIn0.Uyew5xk3UFmaMSe4nL4-07A6NpBRr0DuqiqjwWhqyyKcbQ21dJ4nCw.rm2ziWEm6c4gr6AlKeGeag.vTxlO0fB-iDYMmAejg6QV6FHT9Rc-LlZpcm2OiXQzCf4vVt8vLneW3R-beSIhsBPq_Mjq29PZIis90v7fU_sFZNFqXBwQKGaH2IkM1E9iJNUuecG7afUHHSNHQAC4Yq0oZAmm9CZiXJ6zCqTnoW0xq8Qe1VNH5iFN_6aI4UEznYE3tfldzZ95nBbtrkitTco.b2fZYPv1_t4hfD5aBQRNbA
>"
key = ('13337' * 4)[:16].encode()

try:
    decrypted_data = jwe.decrypt(token, key)
    print(decrypted_data)
except Exception as e:
    print(f"Error: {e}")
