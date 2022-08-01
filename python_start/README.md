python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. helloworld.proto

protoc -I . helloworld.proto --go_out=plugins=grpc:.