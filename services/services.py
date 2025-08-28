# services.py fayli
import requests
from utils.env import BASE_URL



def check_user(tg_id: int):
    url = f"{BASE_URL}/check-user/"
    payload = {"tg_id": tg_id}

    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"exists": False, "message": "User not found"}
        else:
            return {"exists": False, "message": f"Server error: {response.status_code}"}

    except requests.RequestException as e:
        return {"exists": False, "message": f"Request failed: {e}"}





def check_phone(user):
    url = f"{BASE_URL}/check-user/"
    response = requests.post(url, json=user)
    
    try:
        data = response.json()
        return data
    
    except Exception as e:
        return e
    
    
    
def getUserPoints(tg_id):
    url = f"{BASE_URL}/user-by/?tg_id={tg_id}"
    
    response = requests.get(url)
    
    try:
        data = response.json()
        return data
    except Exception as e:
        return e
    
    
    
    
def TopListUser():
    url = f"{BASE_URL}/top-referrers/"
    
    response = requests.get(url)
    
    try:
        data = response.json()
        return data
    except Exception as e:
        return e
    
    