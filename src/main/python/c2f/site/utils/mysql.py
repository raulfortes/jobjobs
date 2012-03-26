## -*- coding: utf-8 -*-

import MySQLdb
  
class MySQL( object ):  
    ''''' 
        Construtor da classe 
    '''  
    def __init__( self ):  
        self.host   = "localhost"
        self.user   = "jobjobs"
        self.passwd = "jobjobs"
        self.db     = "jobjobs"
  
        self.conn   = MySQLdb.connect(self.host,  
                                      self.user,  
                                      self.passwd,  
                                      self.db)    
  
        self.cursor = self.conn.cursor ( MySQLdb.cursors.DictCursor )  
  
    ''''' 
        Destroi os objetos da memoria 
    '''  
    def __del__( self ):  
        self.cursor.close()  
        self.conn.close()
