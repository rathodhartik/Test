import requests
import json 

URL="http://127.0.0.1:8000/student_list"

def data_get(id=None):
    data={}
    if id is not None:
        data={'id':id}
        
    j_data=json.dumps(data)
    r=requests.get(url= URL,data=j_data)
    data=r.json()
    print(data)
    
    
#data_get()

def insert():
    data={'name':'Digjay','address':'Amareli','age':19}
    
    j_data = json.dumps(data)
    r = requests.post(url =URL, data = j_data)
    data=r.json()
    
    print(data)
insert()



def update():
    data={
        'id':2,
        'name':'Divya',
        'address':'Ahmedabad',
        'age':24
    }
    
    j_data=json.dumps(data)
    r=requests.put(url= URL,data=j_data)
    data=r.json()
    print(data)
    
#update()


def delete():
    data={
        'id':4
    }
    
    j_data=json.dumps(data)
    r=requests.delete(url= URL ,data=j_data)
    data=r.json()
    print(data)

#delete()