from typing import NoReturn

from src.admin.common import SUCCESS, MESSAGE_MAP, ERROR


class ApiResult:
    """
    仿照api方式定一个存放数据结果的类
    """

    def __init__(self):
        self.__code = None
        self.__msg = None
        self.__data = None

    def get_code(self) -> int:
        return self.__code

    def set_code(self, code: int) -> NoReturn:
        self.__code = code

    def get_msg(self) -> str:
        return self.__msg

    def set_msg(self, msg: str) -> NoReturn:
        self.__msg = msg

    def get_data(self) -> {}:
        return self.__data

    def set_data(self, data: {}) -> NoReturn:
        self.__data = data

    def is_success(self):
        return self.__code == SUCCESS

    def get_result(self) -> []:
        return self.get_data().get('result', [])

    @classmethod
    def success(cls, msg: str = '', data=None):
        result = cls()
        result.set_code(SUCCESS)

        if not msg:
            result.set_msg(MESSAGE_MAP[SUCCESS])
        else:
            result.set_msg(msg)

        if data:
            result.set_data(data)

        return result

    @classmethod
    def error(cls, msg: str = '', data=None):
        """
        默认错误方法
        :param msg: 错误信息
        :param data: 数据
        :return:  ApiResult
        """
        result = cls()
        result.set_code(ERROR)

        if not msg:
            result.set_msg(MESSAGE_MAP[ERROR])
        else:
            result.set_msg(msg)

        if data:
            result.set_data(data)

        return result

    @classmethod
    def custom_error(cls, code: int, msg: str = '', data=None):
        """
        自定义code，msg，data错误方法
        :param code:
        :param msg:
        :param data:
        :return: ApiResult
        """
        result = cls()
        result.set_code(code)
        result.set_msg(msg)
        if data:
            result.set_data(data)
        return result
