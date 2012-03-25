## -*- coding: utf-8 -*-
import MySQLdb
  
class MySQL( object ):  
    ''''' 
        Construtor da classe 
    '''  
    def __init__( self ):  
        self.host   = "localhost"  
        self.user   = "teste"  
        self.passwd = "teste"  
        self.db     = "teste"  
  
        self.conn   = MySQLdb.connect(self.host,  
                                      self.user,  
                                      self.passwd,  
                                      self.db)    
  
        self.cursor = self.conn.cursor ( MySQLdb.cursors.DictCursor )  
  
    ''''' 
        Destroi os objetos da memÃ³ria 
    '''  
    def __del__( self ):  
        self.cursor.close()  
        self.conn.close()