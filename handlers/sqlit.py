import sqlite3

def reg_user(id, refka):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS black_list (
            id BIGINT,
            stat
            ) """)
    db.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS trafik (
                        name,
                        link,
                        user_id
                        ) """)

    db.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        prokladka,
        finish_stat
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,refka,'0'))
        db.commit()
# Cоздание отслеживания подписчиков
    sql.execute(""" CREATE TABLE IF NOT EXISTS stata_parthers ( 
            id BIGINT,
            channel_ref
            ) """)
    db.commit()

    sql.execute(f"SELECT id FROM stata_parthers WHERE id ='{0}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO stata_parthers VALUES (?,?)", (0, 0))
        db.commit()

    # АРХИВ ВЫПЛАТ
    sql.execute(""" CREATE TABLE IF NOT EXISTS listpay( 
                        data,
                        schetchik
                        ) """)
    db.commit()

    # СОЗДАНИЕ РАЗРЕШЕННЫХ support
    sql.execute(""" CREATE TABLE IF NOT EXISTS utm_support (
                           name,
                           info,
                           info_pay,
                           status
                           ) """)
    # СЧЕТЧИК ТРАФИКА ОТ КОНКРЕТНОГО ПАРТНЕРА
    sql.execute(""" CREATE TABLE IF NOT EXISTS list_support( 
                    id,
                    name_channel,
                    status,
                    status_sub
                    ) """)
    db.commit()



def regviplata(data): # Регистрация выплатны
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sum = 0
    y = sql.execute(f"SELECT * FROM parthers").fetchall()
    for i in y:
        a = sql.execute(f"SELECT COUNT(*) FROM stata_parthers WHERE channel_ref = '{i[1]}'").fetchone()[0]
        sum+=int(a)

    sql.execute(f"INSERT INTO listpay VALUES (?,?)", (data,sum)) # РЕГИСТРИРУЕМ ДАТУ И КОЛИЧЕСТВО ОПЛАЧЕННОГО ТРАФИКА
    db.commit()

def cheak_viplats():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    y = sql.execute(f"SELECT * FROM listpay").fetchall()
    return y


def reg_utm_support(utm, info, pay_info): # Регистрация РАЗРЕШЕННЫХ support
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT name FROM utm_support WHERE name = '{utm}'")
    if sql.fetchone() is None: #Проверка на наличие канала
        #print('Канал не найден! (То что нам нужно)')
        sql.execute(f"SELECT info FROM utm_support WHERE info = '{info}'")
        if sql.fetchone() is None : #Если чела еще нету с таким id, то  регаем
            #print('Сработала операция (Человек не найден), регистрируем')
            sql.execute(f"INSERT INTO utm_support VALUES (?,?,?,?)", (utm, info, pay_info, '1'))
            db.commit()
        else:
            pass #print('Сработала операция (Человек найден, не регистрируем)')


    else: #Канал найден
        #print('Канал найден! (То что нам не нужно)')
        try:
            int(info)
            sql.execute(f"SELECT info FROM utm_support WHERE name ='{utm}'")
            try:
                int((sql.fetchone())[0][0])
            except:  # У человека Id не в интеджер
                sql.execute(f"UPDATE utm_support SET info = '{info}' WHERE name = '{utm}'")
                sql.execute(f"UPDATE utm_support SET info_pay = '{pay_info}' WHERE name = '{utm}'")
                db.commit()

        except:
            pass
    db.commit()

# РЕГИСТРАЦИЯ ЧЕЛОВЕКА ОТ САППОРТА
def reg_traf_support(id,channel): #Регистрация партнера и его канала и отслеживание счетчика
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT id FROM list_support WHERE id ={id}")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO list_support VALUES (?,?,?,?)", (id, f'@{channel}', 0,0))
        db.commit()

def reg_update_traf_support(id,channel): #Регистрация партнера и его канала и отслеживание счетчика
    pass


def update_list_sub(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE list_support SET status_sub = 1 WHERE id = '{id}'")
    db.commit()


def changee_support_tochka(channel):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE list_support SET status = 1 WHERE name_channel = '{channel}' status_sub = 1")
    db.commit()


def cheak_support(): # Возваращет ютм метку - Количество чел - Инфо об админе
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    c = sql.execute(f"SELECT * FROM utm_support").fetchall()
    ansver = []
    for i in c: #ГЕНЕРИРУЕМ ОТВЕТ ИЗ РУЧНОЙ РЕГИСТРАЦИИ
        if i[3] == '1':
            print(i[0])
            a = sql.execute(f"SELECT COUNT(*) FROM list_support WHERE name_channel ='{i[0]}' and status_sub = 1").fetchone()[0]  # Количество всех пользователей
            b1 = sql.execute(f"SELECT COUNT(*) FROM list_support WHERE name_channel ='{i[0]}' and status_sub = 1 and status = 0").fetchone()[0]  # Количество неоплаченных пользователей
            ansver.append([i[0],i[1],a,b1,i[2]])

    return ansver

# СОЗДАНИЕ ВЫПЛАТЫ = ИЗМЕНЕНИЕ СТАТУСА
def changee_support():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE list_support SET status = 1")
    db.commit()


def info_members(): # Количество челов, запустивших бота
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    b = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE finish_stat = "1"').fetchone()[0]

    return a,b

def change_status(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET finish_stat = '1' WHERE id = '{id}'")
    db.commit()

def get_stat(): # Количество челов, запустивших бота
    env = []
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    data = sql.execute(f'SELECT DISTINCT prokladka FROM user_time').fetchall()

    for d in data:
        i = sql.execute(f'SELECT COUNT(*) FROM user_time WHERE prokladka = "{d[0]}"').fetchone()[0]
        env.append([d[0],i])

    return env

def change_infopay(channel, info): #Канал должен быть через @
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE utm_support SET info_pay = '{info}' WHERE name = '{channel}'")
    db.commit()


def change_prokladka(id, p):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET prokladka = '{p}' WHERE id = '{id}'")
    db.commit()

def add_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (int(id), '0'))
        sql.execute(f"INSERT INTO black_list VALUES (?,?)", (str(id), '0'))
        db.commit()

def get_username(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    q = (sql.execute(f"SELECT prokladka FROM user_time WHERE id = '{id}'").fetchone())[0]
    return q



def cheak_black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT id FROM black_list WHERE id = '{id}'")
    if sql.fetchone() is None: #Список пуст, разрешает
        return 0
    else: #Запрещаем
        return 1


def cheak_traf():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    c1 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel1'").fetchone()[0]
    c2 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel2'").fetchone()[0]
    c3 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel3'").fetchone()[0]
    c4 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel4'").fetchone()[0]
    c5 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel5'").fetchone()[0]
    list = [c1,c2,c3,c4,c5]
    return list

def get_channel_info():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    c1 = sql.execute(f"SELECT * FROM trafik").fetchall()
    return c1


def obnovatrafika1(name,link,chat_id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    chat_id = str(-int(chat_id))
    sql.execute(f"SELECT name FROM trafik WHERE user_id = '{chat_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?)", (name,link,chat_id))
        db.commit()

def delit_trafik(chat_id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(f"DELETE FROM trafik WHERE user_id = '{chat_id}'")
    db.commit()

