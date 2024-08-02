from typing import Literal
from threading import Thread
from base64 import b64encode,b64decode,b32encode,b32decode,b16encode,b16decode

#numbers
HUNDRED = "hundred"
TEN = "ten"

#orders
LIST1_FIRST = "1first"
LIST2_FIRST = "2first"


ASCII = "ascii"
BASE64 = "base64"
BASE32 = "base32"
BASE16 = "base16"


class StringObject:
    def __init__(self):
        self.value = ""
    
    def get(self):
        return self.value
    
    def set(self,value:str=""):
        self.value = value

    def replace(self,old:str="",new:str=""):
        pass

    def compare(self,second):
        if(self.value == second.get() if isinstance(second,StringObject) else self.value == second):
            return 0
        elif(self.value > second.get() if isinstance(second,StringObject) else self.value > second):
            return -1
        else:
            return 1
        
    def encrypt(self,encrypt_method,auto_set=True):
        if encrypt_method == ASCII:
            if auto_set:
                self.set(" ".join([str(ord(i)) for i in self.value]))
            return " ".join([str(ord(i)) for i in self.value])
        elif encrypt_method == BASE64:
            if auto_set:
                self.set(b64encode(self.value.encode()).decode())
            return b64encode(self.value.encode()).decode()
        elif encrypt_method == BASE32:
            if auto_set:
                self.set(b32encode(self.value.encode()).decode())
            return b32encode(self.value.encode()).decode()
        elif encrypt_method == BASE16:
            if auto_set:
                self.set(b16encode(self.value.encode()).decode())
            return b16encode(self.value.encode()).decode()
        else:
            return None
        
    def decrypt(self,decrypt_method,auto_set=True):
        if decrypt_method == ASCII:
            if auto_set:
                self.set("".join([chr(int(i)) for i in self.value.split(" ")]))
            return "".join([chr(int(i)) for i in self.value.split(" ")])
        elif decrypt_method == BASE64:
            if auto_set:
                self.set(b64decode(self.value.encode() if isinstance(self.value,bytes) else self.value).decode())
            return b64decode(self.value.encode() if isinstance(self.value,bytes) else self.value).decode()
        elif decrypt_method == BASE32:
            if auto_set:
                self.set(b32decode(self.value.encode() if isinstance(self.value,bytes) else self.value).decode())
            return b32decode(self.value.encode() if isinstance(self.value,bytes) else self.value).decode()
        elif decrypt_method == BASE16:
            if auto_set:
                self.set(b16decode(self.value.encode() if isinstance(self.value,bytes) else self.value).decode())
            return b16decode(self.value.encode() if isinstance(self.value,bytes) else self.value).decode()
        else:
            return None

class ListDerivation:
    def quickly_create(self,mode:Literal["hundred","ten"]|int):
        if isinstance(mode,str):
            return [i for i in range(100)] if mode == HUNDRED else [i for i in range(10)]
        else:
            return [i for i in range(mode)]
    
    def to_int(self,values):
        return [int(i) for i in values]
    
    def to_str(self,values):
        return [str(i) for i in values]
    
    def to_float(self,values):
        return [float(i) for i in values]
    
    def to_boolean(self,values):
        return [bool(i) for i in values]
    
    def delete_space(self,values):
        new = []
        for i in values:
            if i != "":
                new.append(i)
        return new
    
    def delete_none(self,values):
        new = []
        for i in values:
            if i != None:
                new.append(i)
        return new
    
    def delete_none_space(self,values):
        return self.delete_none(self,self.delete_space(self,values))
    
    def merge_list_to_dict(self,list1,list2,order:Literal["1first","2first"]=LIST1_FIRST):
        return dict(zip(list1,list2)) if order == LIST1_FIRST else list(zip(list2,list1))
    
    def decompose_dict_to_list(self,dict:dict):
        return list(dict.keys()),list(dict.values())
    
    def repeat_list_to_dict(self,list):
        return {i:i for i in list}


def run_function_from_thread(func=None,daemon:bool=False):
    t = Thread(target=func)
    t.daemon = daemon
    t.start()

def def_a_function(*args):
    print(args)
    for i in args:
        exec(i)

def isidle():
    return eval('__name__ == "__main__"')