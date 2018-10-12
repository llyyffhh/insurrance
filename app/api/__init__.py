from flask import jsonify

class Api:
    code = {
        'sucess': 200,
        'paramserror' : 400,
        'unautherror' : 401,
        'servererror' : 500
    }

    @staticmethod
    def result(code,msg,data):
        return jsonify({
            'code': code,
            'msg': msg,
            'data': data or {}
        })

    @classmethod
    def success(cls,msg='',data=''):
        return cls.result(cls.code['sucess'],msg=msg,data=data)

    @classmethod
    def params_error(cls,msg='',data=None):
        return cls.result(cls.code['paramserror'],msg=msg,data=data)

    @classmethod
    def unauth_error(cls,msg='',data=None):
        return cls.result(cls.code['unautherror'],msg=msg,data=data)

    @classmethod
    def server_error(cls,msg='',data=None):
        return cls.result(cls.code['servererror'],msg=msg or '服务器内部错误',data=data)
