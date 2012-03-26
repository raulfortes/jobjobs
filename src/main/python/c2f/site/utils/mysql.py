## -*- coding: utf-8 -*-

import MySQLdb


class MySQL(object):
    def __init__(self):
        """
            Construtor da classe
        """
        self.host = "localhost"
        self.user = "jobjobs"
        self.passwd = "jobjobs"
        self.db = "jobjobs"

        self.conn = MySQLdb.connect(self.host,
                                      self.user,
                                      self.passwd,
                                      self.db)

        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    def __del__(self):
        """
            Destroi os objetos da memoria
        """
        self.cursor.close()
        self.conn.close()
