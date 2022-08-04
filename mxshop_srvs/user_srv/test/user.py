import google
import grpc
from user_srv.proto import user_pb2_grpc, user_pb2
from google.protobuf import empty_pb2


class UserTest:
    def __init__(self):
        # 连接grpc服务器
        channel = grpc.insecure_channel("127.0.0.1:50051")
        self.stub = user_pb2_grpc.UserStub(channel)

    def user_list(self):
        rsp: user_pb2.UserListResponse = self.stub.GetUserList(user_pb2.PageInfo(pn=2, pSize=2))
        print(rsp.total)
        for user in rsp.data:
            print(user.mobile, user.birthDay)

    def get_user_by_id(self, id):
        rsp: user_pb2.UserInfoResponse = self.stub.GetUserById(user_pb2.IdRequest(id=id))
        print(rsp.mobile)

    def create_user(self, nick_name, mobile, password):
        rsp: user_pb2.UserInfoResponse = self.stub.CreateUser(user_pb2.CreateUserInfo(
            nickName=nick_name,
            passWord=password,
            mobile=mobile
        ))
        print(rsp.id)

    # 不知道咋写...
    # def update_user(self, nick_name, gender, birthday):
    #     rsp: user_pb2.UserInfoResponse = self.stub.UpdateUser(user_pb2.UpdateUserInfo(
    #         nickName=nick_name,
    #         gender=gender,
    #         birthDay=birthday
    #     ))
    #     print(rsp.id)


if __name__ == "__main__":
    users = UserTest()
    # user.user_list()
    # users.get_user_by_id(100)
    # users.create_user("bobby", "12345678901", "admin123")
    users.update_user("jeff1", "男", 46876131034)
