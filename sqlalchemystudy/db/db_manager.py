from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbManager:
    def __init__(self):
        self.__db_name = 'myboot'
        self.__db_host = '47.105.50.31'
        self.__db_vendor = 'mysql'
        self.__username = 'root'
        self.__password = 'xl123456?'
        self.engine = self.create_engine()
        self.__session = sessionmaker(bind=self.engine)()

    def create_engine(self):
        if self.__db_vendor == 'mysql':
            return create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s' %
                                 (self.__username, self.__password, self.__db_host, self.__db_name), echo=True)
        else:
            raise NotImplementedError

    def get_session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def close(self):
        self.__session.close()
