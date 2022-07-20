from hashlib import sha256
from datetime import datetime
import json
class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.chain.append(self.new_block())

  def new_block(self):
    block = {
      'timestamp': datetime.utcnow().isoformat(),
      'prev_hash': self.chain[-1]["hash"] if len(self.chain)>0 else None,
      'nonce': len(self.chain)
    }
    block["hash"] = sha256(json.dumps(block).encode()).hexdigest()
    return block

  def proof_of_work(self):
    while True:
      new_block = self.new_block()
      if new_block["hash"].startswith("00"):
        break
    self.chain.append(new_block)