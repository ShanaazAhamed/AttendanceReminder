import sqlite3
import io
from client.helper import validate_time


class DB:

    def create_tale(self):
        query = '''
        CREATE TABLE users
        (id     TEXT            PRIMARY KEY NOT NULL,
        in_t    TEXT                NOT NULL,
        out_t   TEXT                NOT NULL,
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

    def insert_data(self, data_dict):
        query = '''INSERT INTO users (id,in_t,out_t,url)
                VALUES (?,?,?,?);'''
        try:
            conn = sqlite3.connect('users.db')
            conn.execute(query, [
                         str(data_dict['id']), data_dict['in_t'], data_dict['out_t'], data_dict['url']])
            conn.commit()
            conn.close()
            return True

        except sqlite3.Error as error:
            return False

    def get_times(self):
        query = '''SELECT in_t,out_t FROM users;'''
        in_times = []
        out_times = []
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.execute(query)
            for row in cursor:
                in_times.append(row[0])
                out_times.append(row[1])
            return list(set(in_times)), list(set(out_times))
        except sqlite3.Error as error:
            return [],[]

    def check_id(self, id):
        query = '''SELECT id FROM users WHERE id=?'''
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.execute(query, [str(id)])
            for row in cursor:
                if row != None:
                    return True
            return False
        except sqlite3.Error as error:
            return False

    def update_intime(self, id, time):
        query = '''UPDATE users SET in_t = ? WHERE id = ?;'''
        try:
            if self.check_id(id) and validate_time(time):
                conn = sqlite3.connect('users.db')
                conn.execute(query, [time, str(id)])
                conn.commit()
                conn.close()
                return True
            else:
                return False

        except sqlite3.Error as error:
            return False

    def update_outtime(self, id, time):
        query = '''UPDATE users SET out_t = ? WHERE id = ?;'''
        try:
            if self.check_id(id) and validate_time(time):
                conn = sqlite3.connect('users.db')
                conn.execute(query, [time, str(id)])
                conn.commit()
                conn.close()
                return True
            else:
                return False

        except sqlite3.Error as error:
            return False

    def update_url(self, id, url):
        query = '''UPDATE users SET url = ? WHERE id = ?;'''
        try:
            if self.check_id(id):
                conn = sqlite3.connect('users.db')
                conn.execute(query, [url, str(id)])
                conn.commit()
                conn.close()
                return True
            else:
                return False

        except sqlite3.Error as error:
            return False

    def get_detialsById(self, id):
        query = '''SELECT * FROM users WHERE id=?'''
        try:
            if self.check_id(id):
                conn = sqlite3.connect('users.db')
                cursor = conn.execute(query, [str(id)])
                for row in cursor:
                    if row != None:
                        return {"id": row[0], "in_time": row[1], "out_time": row[2], "url": row[3]}
            return False
        except sqlite3.Error as error:
            return False

    def get_IdsByInTime(self, time):
        query = '''SELECT id FROM users WHERE in_t = ? '''
        try:
            if validate_time(time):
                ids = []
                conn = sqlite3.connect('users.db')
                cursor = conn.execute(query, [time])
                for row in cursor:
                    ids.append(row[0])
                if len(ids) != 0:
                    return ids
            return []
        except sqlite3.Error as error:
            return []

    def get_IdsByOutTime(self, time):
        query = '''SELECT id FROM users WHERE out_t = ? '''
        try:
            if validate_time(time):
                ids = []
                conn = sqlite3.connect('users.db')
                cursor = conn.execute(query, [time])
                for row in cursor:
                    ids.append(row[0])
                if len(ids) != 0:
                    return ids
            return []
        except sqlite3.Error as error:
            return []


if __name__ == "__main__":
    db = DB()
    # db.create_tale()
    # res3 = db.insert_data(data_dict = {"id":"1111","in_t":'8:30AM',"out_t":"5:00PM","url":"www.wss.com"})
    # res1 = db.insert_data(data_dict = {"id":"1112","in_t":'8:30AM',"out_t":"5:00PM","url":"www.wss.com"})
    # res4 = db.insert_data(data_dict = {"id":"1114","in_t":'8:30AM',"out_t":"5:00PM","url":"www.wss.com"})
    # res5 = db.insert_data(data_dict = {"id":"1113","in_t":'8:30AM',"out_t":"5:00PM","url":"www.wss.com"})
    # res2 = db.insert_data(data_dict = {"id":"1115","in_t":'8:30AM',"out_t":"5:00PM","url":"www.wss.com"})
    # db.backup_data()
    # print(db.get_times())
    # print(db.update_intime(1116, '8:00AM'))
    # print(db.get_detialsById(1115))
    print(db.get_IdsByTime("13:66JM"))
    print(db.update_intime(1115, '8:00AM'))
    print(db.update_url(1115, 'www.gogole.lk'))
