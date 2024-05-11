from main import main, validate_args, get_hash

# check exit code is 1 when no args is wrong type
def expect(label, test, expected_result):
  passed = "pass"
  
  if test != expected_result:
    passed = "fail"
    print(f"{test}")
  
  print(f"{passed} - {label}")
  

hash_nothing = None
try:
  get_hash(None, None)
except TypeError:
  pass

def try_test_hash(arg1, arg2):
  result = None
  try: 
    result = get_hash(arg1, arg2)
  except TypeError:
    pass
  finally:
    return result
  
def try_test_main(arg1, arg2, arg3):
  result = None
  try: 
    result = main(arg1, arg2, arg3)
  except TypeError:
    pass
  except RuntimeError:
    pass
  finally:
    return result
  
target = "test_bob.txt"
alg = "sha512"
target_hash =  "b366c5d529d4f75f2446fdf3b59d560c32ae697ff9f78f062428ba25fa732ba7268d8ad0c9f42043aa2f35619fb7bade667d630a353d720fa593cb91bcb1076a"
hash_success_msg = "Hash matches."

expect("main checks first arg", try_test_main(None, alg, target_hash), None)
expect("main checks second arg", try_test_main(target, None, target_hash), None)
expect("main checks third arg", try_test_main(target, alg, None), None)
expect("main works with valid args", try_test_main(target, alg, target_hash), hash_success_msg)
  
expect("hash double None", try_test_hash(None, None), None)
expect("hash algo None", try_test_hash(target, None), None)
expect("hash path None", try_test_hash(None, alg), None)
expect("hash valid args", try_test_hash(target, alg), target_hash)

expect("validates args none", validate_args(None), 1)
expect("validates args empty list", validate_args([]), 1)
expect("validates args 1 arg", validate_args(["a"]), 1)
expect("validates args 2 args", validate_args(["a", "b"]), 1)
expect("validates args 3 args", validate_args(["a", "b", "c"]), 0)
expect("validates args 4 args", validate_args(["a", "b", "c", "d"]), 0)