#!/usr/bin/env python
from c2f.site.utils.mysql import MySQL


class User (MySQL):

    id = None
    name = None
    email = None
    password = None

    def getAll(self):
        self.cursor.execute(
        "SELECT id,name,email " +
        "FROM user")
        return self.cursor.fetchall()

    def save(self):
        if self.cursor.execute(
        "INSERT INTO user(" +
            "`name`," +
            "`email`" +
        ") VALUES (" +
            "'" + str(self.name) + "'," +
            "'" + str(self.email) + "'" +
        ")"):

            self.id = self.conn.insert_id()
            self.conn.commit()
            return True
        else:
            return False

    def update(self, id, name, email):
        if self.cursor.execute(
            "UPDATE user SET " +
                "`name`  = '" + str(name) + "'," +
                "`email` = '" + str(email) + "' " +
            "WHERE " +
                "`id` = " + str(id)
        ):
            return True
        else:
            return False

    def remove(self, id):
        if self.cursor.execute(
            "DELETE FROM `user` " +
            "WHERE `id` = " + str(id)):
            return True
        else:
            return  False
