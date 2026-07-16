import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3IiwiZXhwIjoxNzg0ODM2MTU0fQ.Wx1cctcyHAsQYPv_PslXn--BBxC3Hz-swznLuGKMiyc"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())