import requests

import api


class ApiEmployee:
    def __init__(self): 
        # 添加员工
        self.url_add = api.BASE_URL + "/api/sys/user"

        self.url_employee = api.BASE_URL + "/api/sys/user/{}"

    # 添加员工
    def api_post_employee(self, username, mobile, workNumber):
        # json数据
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber
                }
        # 调用Post  必须有返回
        return requests.post(url=self.url_add, json=data, headers=api.headers)

    def api_put_employee(self):
        pass

    def api_get_employee(self):
        pass

    def api_delete_employee(self, user_id):
        return requests.delete(url=self.url_employee.format(user_id), headers=api.headers)
