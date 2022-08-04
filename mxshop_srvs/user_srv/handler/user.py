import time
from datetime import date
import grpc
from peewee import DoesNotExist
from loguru import logger
from user_srv.model.models import User

from user_srv.proto import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):
    def convert_user_to_rsp(self, user):
        # 将user的model对象转换成message对象
        user_info_rsp = user_pb2.UserInfoResponse()
        user_info_rsp.id = user.id
        user_info_rsp.passWord = user.password
        user_info_rsp.mobile = user.mobile
        user_info_rsp.role = user.role

        if user.nick_name:
            user_info_rsp.nickName = user.nick_name
        if user.gender:
            user_info_rsp.gender = user.gender
        if user.birthday:
            user_info_rsp.birthDay = int(time.mktime(user.birthday.timetuple()))
        return user_info_rsp

    @logger.catch
    def GetUserList(self, request: user_pb2.PageInfo, context):
        # 获取用户的列表
        rsp = user_pb2.UserListResponse()
        users = User.select()
        rsp.total = users.count()

        print("用户列表")
        start = 0
        per_page_nums = 10  # 每一页的数量
        if request.pSize:
            per_page_nums = request.pSize
        if request.pn:
            start = per_page_nums * (request.pn - 1)

        users = users.limit(per_page_nums).offset(start)

        for user in users:
            rsp.data.append(self.convert_user_to_rsp(user))
        return rsp

    @logger.catch
    def GetUserById(self, request: user_pb2.IdRequest, context):
        # 通过id查询用户
        try:
            user = User.get(User.id == request.id)
            return self.convert_user_to_rsp(user)

        except User.DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()

    def GetUserByMobile(self, request: user_pb2.MobileRequest, context):
        # 通过id查询用户
        try:
            user = User.get(User.mobile == request.mobile)
            return self.convert_user_to_rsp(user)

        except User.DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()
