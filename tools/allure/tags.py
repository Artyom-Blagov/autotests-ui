from enum import Enum

class AllureTag(str, Enum):
    COURSES = "COURSES"
    DASHBOARD = "DASHBOARD"
    REGRESSION = "REGRESSION"
    USER_LOGIN = "USER_LOGIN"
    NAVIGATION = "NAVIGATION"
    REGISTRATION = "REGISTRATION"

def user_login(role: AllureTag):
    ...


user_login(AllureTag.A)