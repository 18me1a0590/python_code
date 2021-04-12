class Node :
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,node):
        self.__next=node

#-------------------------------------------------------------

class LinkedList :
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

