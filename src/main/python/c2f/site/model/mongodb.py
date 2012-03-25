## -*- coding: utf-8 -*-
import pymongo 
  
class MongoDB( object ):  
    ''''' 
        Construtor da classe 
    '''  
    def __init__( self ):  
        
        self.mongo = pymongo.Connection('localhost')
        # Returns Database Object
        self.mongodb = self.mongo['teste']
  