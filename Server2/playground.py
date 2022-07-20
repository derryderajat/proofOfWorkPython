from Blockchain import Blockchain as Bc
import uuid
a = Bc()
a.proof_of_work()
result = a.chain[-1]
result['nonce'] = 23
print(result)