import threading
import time

# # функция для отображения информации о потоках
# def get_data(data, value):
#     for _ in range(value):
#         print(f"[{threading.current_thread().name}] - {data}")
#         time.sleep(1)
#
# # список для хранения потоков
# thr_list = []
#
# # создание 3-х потов и добавление в список ссылки на объекты потока
# for i in range(3):
#     thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f'thr_{i}')
#     thr_list.append(thr)
#     thr.start()
#
# # проходимся по списку и делаем сначала выполнение всех потоков, и только после их выполнения, будет
# # выполняться след строка
# for i in thr_list:
#     i.join()
#
# # for i in range(100):
# #     print(i)
# #     time.sleep(1)
# #
# #     if i % 10 == 0:
# #         print('active thread: ', threading.active_count())
# #         print('enumerate: ', threading.enumerate())
# #         print('thr-1 is alive: ', thr.is_alive())
#
#
# # вывод главного потока threading.main_thread().name,
# # изменение названия главного потока на 'result'
# # вывод потока с измененным названием
#
# # print('name: ', threading.main_thread().name)
# # threading.main_thread().name = 'result'
# # print('result: ', threading.main_thread().name)









# # функция для отображения информации о потоках
# def get_data(data):
#     for _ in range(5):
#         print(f"[{threading.current_thread().name}] - {data}")
#         time.sleep(1)
#
#
# thr = threading.Thread(target=get_data, args=(str(time.time()), ), name='thr')
# thr.daemon = True
# thr.start()
# print('finish')




# Блокировка Lock()

# value = 0
# locker = threading.Lock()
#
# def inc_value():
#     global value
#     while True:
#         with locker:
#             value += 1
#             time.sleep(1)
#             print(value)
#
# for _ in range(5):
#     threading.Thread(target=inc_value).start()



# locker = threading.RLock()
#
# def inc_value():
#     print('= Блокировка потока =')
#     locker.acquire()
#     print('= Поток разблокирован =')
#
# t1 = threading.Thread(target=inc_value)
# t2 = threading.Thread(target=inc_value)
# t1.start()
# t2.start()







# import psycopg2
#
#
# def create_connection():
#     connection = None
#     try:
#         connection = psycopg2.connect(database='blog',
#                                       user='postgres',
#                                       password='admin',
#                                       host='localhost',
#                                       port='5432')
#         print("Подключение к базе выполнено успешно")
#     except Exception as e:
#         print(f"Произошла ошибка \n[{e}]")
#     return connection
#
#
# def close_connection(connection):
#     connection.close()
#     print('Соединение закрыто')
#
#
# if __name__ == '__main__':
#     conn = create_connection()
#     if conn:
#         with conn.cursor() as cursor:
#             sql = "CREATE TABLE users (" \
#                   "brand VARCHAR(255), " \
#                   "model VARCHAR(255), " \
#                   "year INT" \
#                   ");"
#             cursor.execute(sql)
#             conn.commit()
#         close_connection(conn)



# class Manager:
#     def __init__(self, param):
#         self.param = param
#
#     def __enter__(self):
#         print(f'файл {self.param} подключился')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print(f'Ошибка: {exc_type}')
#
#         print('info')
#
# with Manager('param') as conn:
#     print(conn)
#     raise ValueError('gello')



# ages = [{'age': 30}, {'age': 50}, {'age': 40}]
# ages.sort(key=lambda x: x['age'], reverse=True)
# print(ages)

#
# class A:
#     def __new__(cls, *args, **kwargs):
#         print('NEW')
#         obj = super().__new__(cls, *args, **kwargs)
#         return obj
#
#     def __init__(self):
#         print('INIT')
#
# print(A())



# def outer(a):
#     def inner(b):
#         return a + b
#     return inner
#
# add = outer(5)
# print(add(4))


# def repeat(n):
#     def dec(func):
#         def wrapper(*args, **kwargs):
#             print('one')
#             for _ in range(n):
#                 func(*args, **kwargs)
#             print('two')
#
#         return wrapper
#     return dec
#
# @repeat(3)
# def some_func(a, b):
#     print(a+b)
#
# some_func(5,3)
#print(some_func(5,3))



# a = [1,2,3]
# i = iter(a)
# try:
#     while True:
#         print(next(i))
# except StopIteration:
#     pass


# class Counter:
#     current: int
#
#     def __init__(self):
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         curr = self.current
#         self.current += 1
#         return curr
#
#
# c = Counter()
# i = iter(c)
# print(next(i))
# print(next(i))
# print(next(i))


# def some(n):
#     for i in range(n):
#         yield i
#
# obj = some(5)
# print(next(obj))
# print(next(obj))
# print('hello')
# print(next(obj))

# a = (i for i in range(5))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# class Connection:
#     def __enter__(self):
#         self.connection = 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection = 0
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#
#
# with Connection() as conn:
#     print('hello')
#     raise Exception('VAL')



















