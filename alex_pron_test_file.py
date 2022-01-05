import requests
# r = requests.post('http://127.0.0.1:8000/auth/signup/', data={'u_email': 'gad222@m.ru','u_password':'12345678'})
# r = requests.post('https://dev.lectonic.ru/auth/signup/', data={'u_email': 'gad111@m.ru','u_password':'12345678'})
# r = requests.post('http://127.0.0.1:8000/auth/login/', data={'u_email': 'gad222@m.ru','u_password':'12345678'})
r = requests.post('http://127.0.0.1:8000/auth/logout/', headers={'Authorization': 'Token 2dfd0da32b9db367b1958726515fb19041685719'})
# r = requests.post('http://127.0.0.1:8000/auth/test/')
print (r.text)