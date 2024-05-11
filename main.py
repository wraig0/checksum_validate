import sys
import hashlib

def validate_args(args):
  if not isinstance(args, list) or len(args) < 3:
    return 1
  
  for arg in args:
    if not isinstance(arg, str):
      return 1
  
  return 0        

def get_hash(target, alg):
  if not isinstance(target, str):
    raise TypeError("target is not a string")
  
  if not isinstance(alg, str):
    raise TypeError("hash algorithm                                                      is not a string")
  
  try:
    with open(target, 'rb') as file:
      data = file.read()
      hash_object = hashlib.new(alg)
      hash_object.update(data)
      return hash_object.hexdigest()
    
  except FileNotFoundError:
    print("Target file not found.")
    return None
  except:
    print("An error occurred while hashing the file.")
    return None
  
  
def main(hash_target, hash_algo, hash_expected):
  if validate_args([hash_target, hash_algo, hash_expected]) == 1:
    raise RuntimeError("Args not valid.")
    
  hash = get_hash(hash_target, hash_algo)
  if isinstance(hash, str):
    if hash == hash_expected:
      return "Hash matches."
    return "Hash does not match."
  
  raise RuntimeError("Hash result was not valid.")
  
  
if __name__ == "__main__":
  if validate_args([sys.argv[1], sys.argv[2], sys.argv[3]]) == 1:
    raise RuntimeError("Args not valid.")
  
  exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))