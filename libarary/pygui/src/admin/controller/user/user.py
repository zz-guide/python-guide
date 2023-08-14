from src.admin.common.response import ApiResult
from src.admin.common.model import User
from src.admin.common.service.user import UserService


class UserController:

    @staticmethod
    def login_action(**kwargs) -> ApiResult:
        # 参数校验
        if not kwargs:
            return ApiResult.error('参数缺失，请重新输入')

        username = kwargs['username']
        password = kwargs['password']

        if not username:
            return ApiResult.error('账号必填')

        if not password:
            return ApiResult.error('密码必填')

        user = UserService.get_by_username(username)
        if not user:
            return ApiResult.error('账号不存在，请重新输入')

        if user.password != password:
            return ApiResult.error('密码错误，请重新输入')

        return ApiResult.success('登录成功')

    @staticmethod
    def register_action(**kwargs) -> ApiResult:
        if not kwargs:
            return ApiResult.error('参数缺失，请重新输入')

        name = kwargs.get('name', '')
        username = kwargs.get('username', '')
        password = kwargs.get('password', '')
        confirm_password = kwargs.get('confirm_password', '')

        if not name:
            return ApiResult.error('姓名必填')

        if not username:
            return ApiResult.error('账号必填')

        if not password:
            return ApiResult.error('密码必填')

        if not confirm_password:
            return ApiResult.error('二次确认密码必填')

        if password != confirm_password:
            return ApiResult.error('两次密码输入不一致，请重新输入')

        user = UserService.get_by_username(username)
        if user:
            return ApiResult.error('账号已存在，请重新输入')

        data = {'username': username, 'password': password, 'name': name}
        res = User.insert(**data).execute()
        if not res:
            return ApiResult.error('user记录插入失败')

        return ApiResult.success('注册成功')
