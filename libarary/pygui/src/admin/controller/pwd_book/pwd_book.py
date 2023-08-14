from src.admin.common.model.pwd_book import PwdBook
from src.admin.common.response import ApiResult
from src.admin.common.service.pwd_book import PwdBookService


class PwdBookController:

    @staticmethod
    def search_action(**kwargs) -> ApiResult:
        url = kwargs.get('url', '')
        remark = kwargs.get('remark', '')
        print(url, remark)
        selector = PwdBook.select().order_by(PwdBook.created_at.asc())
        if url:
            selector = selector.where(PwdBook.url.contains(url))

        if remark:
            selector = selector.where(PwdBook.remark.contains(remark))

        pwd_books = selector.execute()
        res = []
        for ret in pwd_books:
            res.append(ret.model_to_dict())

        data = {'p': 1, 'pn': 20, 'result': res, 'total': 40}
        return ApiResult.success(data=data)

    @staticmethod
    def create_action(**kwargs) -> ApiResult:
        if not kwargs:
            return ApiResult.error('参数缺失，请重新输入')

        url = kwargs.get('url', '')
        username = kwargs.get('username', '')
        password = kwargs.get('password', '')
        remark = kwargs.get('remark', '')

        if not url:
            return ApiResult.error('账号必填')

        if not username:
            return ApiResult.error('账号必填')

        if not password:
            return ApiResult.error('账号必填')

        data = {'username': username, 'url': url, 'password': password, 'remark': remark}
        res = PwdBook.insert(**data).execute()
        if not res:
            return ApiResult.error('创建失败，请重试')

        return ApiResult.success()

    @staticmethod
    def update_action(**kwargs) -> ApiResult:
        _id = kwargs.get('id', '')
        if not _id:
            return ApiResult.error('缺失id参数')

        pwd_book = PwdBookService.get_by_id(_id)
        if not pwd_book:
            return ApiResult.error('记录不存在，请重试')
        pwd_book.username = kwargs.get('username')
        pwd_book.password = kwargs.get('password')
        pwd_book.url = kwargs.get('url')
        pwd_book.remark = kwargs.get('remark')
        try:
            res = pwd_book.save()
            if not res:
                return ApiResult.error('更新失败，请重试')
        except ValueError:
            return ApiResult.error('更新失败，请重试')

        return ApiResult.success('编辑成功')

    @staticmethod
    def remove_action(_id: str) -> ApiResult:
        if not _id:
            return ApiResult.error('缺失id参数')

        pwd_book = PwdBookService.get_by_id(_id)
        if not pwd_book:
            return ApiResult.error('记录不存在，请重试')

        try:
            res = pwd_book.delete_instance()
            if not res:
                return ApiResult.error('删除失败，请重试')
        except ValueError:
            return ApiResult.error('删除失败，请重试')

        return ApiResult.success('删除成功')
