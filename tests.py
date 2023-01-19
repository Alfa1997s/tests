import unittest
import functions
import requests
default_server = 'http://127.0.0.1:8000'
class pms_functions(unittest.TestCase):
    
     def test_leaked(self):
          home = default_server
          response = requests.get(f'{home}/check_leak', {
               'password': 'mylestone1897'
          })
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.text, 'true')
         
    
     def test_Password_length(self):
       home = default_server
       params = {'password': 'mylestone1897', 'min_length': 8, 'max_length': 50}
       response = requests.get(f'{home}/check_length', params=params)
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.text, '"ok"')
 
          
     def test_special_characters(self):
          home = default_server
          _ = ["!","@","$","&"]
          params = {'password':'mylestone@1897'}
          response = requests.get(f'{home}/check_specialcharacters',params=params)
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.text, '"ok"')


     
     def test_update_policy(self):
          _ ={"minLength":8,"maxLength":50,"specialCharacters":1,"upperCase":1,"lowerCase":1}
          self.assertEqual(functions.updatePolicy("minLength",10),"Update Success")

     def test_genPass(self):
          home = default_server
          response = requests.get(f'{home}/generatePassword')
          self.assertEqual(response.status_code,200) 
          
if __name__ == '__main__':
     unittest.main()
 