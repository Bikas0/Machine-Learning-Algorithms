import uvicorn
from fastapi import FastAPI, HTTPException, Path
from typing import List
from user_module import UserInfo

# from bike import Bike, UserInfo
# for active server have to run "uvicorn.module_name:app name --reload" in command prompt

app = FastAPI()
fake_user_db = []


@app.get(path="/users/", response_model=UserInfo)
def getUser():
    dummy_user = UserInfo(username="bikas", email="bikas@gmail.com", full_name="Md Bikasuzzaman")
    return dummy_user


@app.post(path="/users/", response_model=UserInfo)
def create_user(person: UserInfo):
    fake_user_db.append(person)
    return person


@app.get(path="/all-user", response_model=List[UserInfo])
def get_all_user():
    return fake_user_db


@app.get(path="/Users/{user_id}", response_model=UserInfo)
def read_user(user_id: int = Path(..., title="The ID of the user to retrieve.", ge=0)):
    if user_id < len(fake_user_db):
        return fake_user_db[user_id]
    raise HTTPException(status_code=404, detail="User not found")


# @app.get(path="/bike/", response_model=Bike)
# def getUser():
#     c = UserInfo(userName="Bikas", userID='121304')
#     bike_info = Bike(VendorName="Bajaj", cc=150, price=19000.0, person_details=c)
#     print(bike_info)
#     return bike_info


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
