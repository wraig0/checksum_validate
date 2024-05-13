from check_hash import main, validate_args, get_hash
import unittest
  
target = "test_bob.txt"
alg_sha512 = "sha512"
alg_sha256 = "sha256"
target_hash_sha512 = "b366c5d529d4f75f2446fdf3b59d560c32ae697ff9f78f062428ba25fa732ba7268d8ad0c9f42043aa2f35619fb7bade667d630a353d720fa593cb91bcb1076a"
target_hash_sha256 = "963cccb82a5525f62079b5a5de9742e4187cbc35107d570714287e0f0d156ddc"
hash_success_msg = "Hash matches."

class TestHashing(unittest.TestCase):
  def test_no_args(self):
    self.assertRaisesRegex(TypeError, "Target is not a string.", get_hash, None, None)
    
  def test_no_path(self):
    self.assertRaisesRegex(TypeError, "Target is not a string.", get_hash, None, alg_sha512)
    
  def test_no_alg(self):
    self.assertRaisesRegex(TypeError, "Hash algorithm is not a string.", get_hash, target, None)
  
  def test_invalid_alg(self):
    self.assertRaises(Exception, get_hash, target, "sha5122", target_hash_sha512)
  
  def test_file_not_found(self):
    self.assertRaises(FileNotFoundError, get_hash, "nope.txt", alg_sha256)    
    
  def test_valid_args(self):
    self.assertEqual(get_hash(target, alg_sha256), target_hash_sha256)
    
  def test_args_validated(self):
    self.assertRaisesRegex(RuntimeError, "Args not valid.", main, None, None, None)
    
  def test_hashes_sha512_0(self):
    self.assertEqual(main(target, alg_sha512, target_hash_sha512), 0)
    
  def test_hashes_sha512_1(self):
    self.assertEqual(main(target, alg_sha512, "foo"), 1)
    
  def test_hashes_sha256_0(self):
    self.assertEqual(main(target, alg_sha256, target_hash_sha256), 0)
    
  def test_hashes_sha256_1(self):
    self.assertEqual(main(target, alg_sha256, "foo"), 1)
    
  def test_validate_args_exist(self):
    self.assertEqual(validate_args(None), 1)
    
  def test_validate_args_type(self):
    self.assertEqual(validate_args(()), 1)
    
  def test_validate_args_count_0(self):
    self.assertEqual(validate_args([]), 1)
    
  def test_validate_args_count_1(self):
    self.assertEqual(validate_args(["a"]), 1)
    
  def test_validate_args_count_2(self):
    self.assertEqual(validate_args(["a", "b"]), 1)
    
  def test_validate_args_count_3(self):
    self.assertEqual(validate_args(["a", "b", "c"]), 0)
    
if __name__ == '__main__':
    unittest.main()