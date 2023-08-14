from src.common import VariableCache
from src.admin.common.model import User
from src.admin.common.model.pwd_book import PwdBook
from src.web.view.login import LoginWidget, RegisterWidget
from src.web.view.pwd_book import PwdBookTableWidget, PwdBookCreateWidget, PwdBookUpdateWidget
from src.web.view.main.main_widget import MainWidget
from src.web.common.signal.signal import SignalBus


class GlobalVariableInit:
    """
    此类用来初始化全局变量
    """

    @classmethod
    def init(cls):
        # todo::此处的顺序切记不能调换
        cls.__init_database()
        cls.__init_widget()
        cls.__init_signal()

    @classmethod
    def __init_widget(cls):
        VariableCache.login_widget = LoginWidget()
        VariableCache.register_widget = RegisterWidget()
        VariableCache.pwd_book_table_widget = PwdBookTableWidget()
        VariableCache.pwd_book_create_widget = PwdBookCreateWidget()
        VariableCache.pwd_book_update_widget = PwdBookUpdateWidget()
        VariableCache.main_widget = MainWidget()

    @classmethod
    def __init_signal(cls):
        VariableCache.signal_bus = SignalBus()

    @classmethod
    def __init_database(cls):
        VariableCache.database.create_tables([User, PwdBook])
