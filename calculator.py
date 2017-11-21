#!/usr/bin/env python3
import sys
class Arg(object):
    def __init__(self):
        sys.argv = []
        for arg in sys.argv[1:]:
            arg = arg.split(':')
            num = int(arg[0])
            sal = int(arg[1])
    def get_arg(self,num,sal):       
        return(tr(num)+''+format(sl,'.2f'))

class Config(object):
    def __init__(self):
        self._config = {}
        with open('/home/shiyanlou/test.cfg','r') as f:
            for st in f.readlines():
                (key ,value ) = st.strip().split(' = ')
                try:
                    self._config[key] = float(value)
                except ValueError:
                    print('Error')
                    exit()
    def get_config(self,key):
        return self._config(key)        
                
class UserData(object):
    def __init__(self):
        self.userdata = {}
        with open()
    
