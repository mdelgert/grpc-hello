import grpc
import messages_pb2
import messages_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = messages_pb2_grpc.MessageServiceStub(channel)
    message = "Hello, gRPC!"
    request = messages_pb2.MessageRequest(content=message)
    response = stub.SendMessage(request)
    print("Response received:", response.acknowledgement)

if __name__ == "__main__":
    run()
