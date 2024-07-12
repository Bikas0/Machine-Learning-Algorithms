import uvicorn
from fastapi import FastAPI
from user_module import UserInfo
# from bike import Bike, UserInfo
# for active server have to run "uvicorn.module_name:app name --reload" in command prompt

app = FastAPI()
fake_user_db = []

@app.get(path="/users/", response_model=UserInfo)
def getUser():
    dummy_user = UserInfo(username = "bikas", email = "bikas@gmail.com", full_name = "Md Bikasuzzaman")
    return dummy_user

# @app.get(path="/bike/", response_model=Bike)
# def getUser():
#     c = UserInfo(userName="Bikas", userID='121304')
#     bike_info = Bike(VendorName="Bajaj", cc=150, price=19000.0, person_details=c)
#     print(bike_info)
#     return bike_info




@app.post(path = "/bike/", response_model= UserInfo)
def create_user(person: UserInfo):
    fake_user_db.append((person))
    return person
















if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
