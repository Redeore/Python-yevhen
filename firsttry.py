import requests

def data():
    
    url='https://jsonplaceholder.typicode.com/todos/27'
    response=requests.get(url)

    data= response.json()
    return data

fetchedData=data()

print(fetchedData)