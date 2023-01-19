import unittest
import functions
import requests

class pms_functions(unittest.TestCase):
     def test_leaked(self):
          home = 'http://127.0.0.1:8000'
          response = requests.get(f'{home}/check_leak', {
               'password': 'mylestone1897'
          })
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.text, 'true')
         
    
     def test_Password_length(self):
       home = 'http://127.0.0.1:8000'
       params = {'password': 'mylestone1897', 'min_length': 8, 'max_length': 50}
       response = requests.get(f'{home}/check_length', params=params)
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.text, '"ok"')
 
          
     def test_special_characters(self):
          home = 'http://127.0.0.1:8000'
          passwordLst = ["!","@","$","&"]
          params = {'password':'mylestone@1897'}
          response = requests.get(f'{home}/check_specialcharacters',params=params)
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.text, '"ok"')


     
     def test_update_policy(self):
          home = 'http://127.0.0.1:8000'
          polices_dct={"minLength":8,"maxLength":50,"specialCharacters":1,"upperCase":1,"lowerCase":1}
          self.assertEqual(functions.updatePolicy("minLength",10),"Update Success")

     def test_genPass(self):
          home = 'http://127.0.0.1:8000'
          response = requests.get(f'{home}/generatePassword')
          #  params ={'password':'mylestone1897','minLength':8,'maxLength':50,"specialCharacters":1,"upperCase":1,"lowerCase":1}
          self.assertEqual(response.status_code,200) 
          
if __name__ == '__main__':
     unittest.main()
 