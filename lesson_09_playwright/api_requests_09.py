import pprint
import requests


print("GET Request")
response = requests.get("https://reqres.in/api/users")
pprint.pprint(response.status_code)
pprint.pprint(response.json())
pprint.pprint(response.json()['data'][0]['id'])
pprint.pprint(response.json()['data'][0]['email'])
print(response)

print("\nPOST Requests: ")
new_user= {"name": "Mali", "job": "QA"}
response= requests.post("https://reqres.in/api/users", json=new_user)
print(response.json())
print(response.status_code)
print(response.reason)

print("\nPUT Requests: ")
update_user= {"name": "Mali", "job": "Automation QA"}
response= requests.put("https://reqres.in/api/users/", json=update_user)
print(response.json())
print(response.status_code)
print(response.reason)

print("\nDelete Requests: ")
response= requests.delete("https://reqres.in/api/users/")
print(response.status_code)
print(response.reason)

