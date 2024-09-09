#import logger

class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'userId': 'benny_truong'
        }
    }

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('admin','test1234')
            self._user_list.append(admin)
            self._is_initialized = True
            #self.logger = logger.get_logger(__name__)

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        result = (a+b)
        #self.logger.debug(f"Adding {a} to {b}, resulting in: {a+b}", extra=self.log_properties)
        return result

    def subtract(self, a, b):
        result = (a - b)
        #self.logger.debug(f"Subtracting {a} with {b}, resulting in: {a-b}", extra=self.log_properties)
        return result

    def multiply(self, a, b):
        result = (a * b)
        #self.logger.debug(f"Multiplying {a} with {b}, resulting in: {a*b}", extra=self.log_properties)
        return result

    def divide(self, a, b):
        result = (a / b)
        #self.logger.debug(f"Dividing {a} with {b}, resulting in: {a/b}", extra=self.log_properties)
        return result

    def register_user(self, username, password):
        for user in self._user_list:
            if(user.username == username):
                print("Failed to register user")
                return None
        user = self.User(username, password)
        self._user_list.append(user)
       # self.logger.debug(f"Registering new user: {username}, password: {password}", extra=self.log_properties)
        return username

    def login(self, username, password):
        #self.logger.debug(f"{username} is logging on", extra=self.log_properties)
        for user in self._user_list:
            if(user.username == username and user.password == password):
                self._current_user = user
                return username
        print("Login failed")
        return None
        

    def logout(self):
        user = self._current_user
        self._current_user = None
        #self.logger.debug(f"User {user} is logging off", extra=self.log_properties)
        print("Logout failed")
        return user

    def get_current_user(self):
        return self._current_user