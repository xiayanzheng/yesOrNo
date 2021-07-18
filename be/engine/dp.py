import pymysql


class dataProcess:

    def __init__(self):
        self.dbc = None

    def db(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='lf',
                                     database='yesorno',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.dbc = connection
        return True

    def pro(self, qid, answer):
        cursor = self.dbc.cursor()
        sql = "INSERT into yesorno.answer VALUES('{}','{}');".format(qid, answer)
        cursor.execute(sql)
        self.dbc.commit()
