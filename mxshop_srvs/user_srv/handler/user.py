import grpc
from user_srv.model.models import User
from user_srv.proto import user_pb2, user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):
    def GetUserList(self, request: user_pb2.PageInfo, context):
        # 获取用户的列表
        rsp = user_pb2.UserListResponse()
        users = User.select()
        for user in users:
            user_info_rsp = user_pb2.UserInfoResponse()

            user_info_rsp.id = user.id
            user_info_rsp.password = user.password
            user_info_rsp.mobile = user.mobile
            user_info_rsp.role = user.role

            if user.nick_name:
                user_info_rsp.nick_name = user.nick_name
            if user.gender:
                user_info_rsp.gender = user.gender
            if user.birthday:
                user_info_rsp.birthday = user.birthday

            rsp.data.append()

