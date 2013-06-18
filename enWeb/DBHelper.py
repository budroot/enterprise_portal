__author__ = 'Riemannh'

import sqlite3

PROD_INFO_TABLE_CREATE = "CREATE TABLE PROD_INFO(ID VARCHAR2(32), PROD_NAME VARCHAR2(64), PROD_NOTES VARCHAR2(256), PROD_IMAGE VARCHAR2(128))"


class DBHelper:
    def createDB(self):
        self.create_table(PROD_INFO_TABLE_CREATE)

    def create_table(self, create_sentence):
        conn = sqlite3.connect('enterprise_web')
        conn.execute(create_sentence)
