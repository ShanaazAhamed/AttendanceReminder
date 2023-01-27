class user:

    def validate_time(time):
        pass

    def __init__(self,id):
        self.__chat_id = ""
    
    @classmethod
    def new_user(cls,id):
        return cls(id)

    def get_times():
        return [self.in,self.out]

    def set_in_time(self,time):
        self.in = time
        return True

    def set_out_time(self,time):
        self.out = time
        return True
    
    def set_url(self,url):
        self.__url = url  

    def get_id(self):
        return self.__id
    
    def get_url(self):
        return self.__url