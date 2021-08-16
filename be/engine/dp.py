import pymysql


class dataProcess:

    def __init__(self):
        self.dbc = None

    def db(self, **kwargs):
        dbhost = kwargs["dbhost"]
        dbuser = kwargs["dbuser"]
        dbpass = kwargs["dbpass"]
        dbname = kwargs["dbname"]
        connection = pymysql.connect(host=dbhost,
                                     user=dbuser,
                                     password=dbpass,
                                     database=dbname,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.dbc = connection
        return True

    def pro(self, qid, answer):
        cursor = self.dbc.cursor()
        sql = "INSERT into yesorno.answer VALUES('{}','{}');".format(qid, answer)
        cursor.execute(sql)
        self.dbc.commit()
