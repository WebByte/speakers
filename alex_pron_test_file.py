import requests

# r = requests.post('http://127.0.0.1:8000/api/auth/login/', data={'u_login': 'Gadya3','u_password':'12345'})
r = requests.post('http://127.0.0.1:8000/api/auth/logout/', headers={'Authorization': 'Token 5f5b4b2e092f901b2fce11a3add6e713769f48ad'})
# r = requests.post('http://127.0.0.1:8000/api/auth/test/')
print (r.text)