import sqlite3
import io

class DB:
    def __init__(self):
        self.create_tale()

    def create_tale(self):
        query = '''
        CREATE TABLE users
        (id     INT PRIMARY KEY     NOT NULL,
        in_t    TEXT                NOT NULL,
        out_t   INT                 NOT NULL,
        url     TEXT
        );'''
        drop_query = "DROP TABLE IF EXISTS users;"
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute(drop_query)
            conn.execute(query)
            conn.commit()
            conn.close()
            return True

        except sqlite3.Error as error:
            # print('Error occurred - ', error)
            return False

    def backup_data(self):
        conn = sqlite3.connect('users.db')
        with io.open('backupdatabase_dump.sql', 'w') as p: 
            for line in conn.iterdump():    
                p.write('%s\n' % line)
        conn.close()

    def insert_data(self,data_dict):
        query = '''INSERT INTO users (id,in_t,out_t,url)
                VALUES (?,?,?,?)'''
        try:
            conn = sqlite3.connect('users.db')
            conn.execute(query, [str(data_dict['id']), data_dict['in'],data_dict['out'],data_dict['url']])
            conn.commit()
            conn.close()
            return True
                
        except sqlite3.Error as error:
            # print('Error occurred - ', error)
            return False

      
if __name__ == "__main__":
    db = DB()
    db.backup_data()
    res = db.insert_data(data_dict = {"id":1,"in":'8:30AM',"out":"5:00PM","url":"www.wss.com"})
    db.backup_data()
    print(res)