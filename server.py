import grpc
import concurrent.futures  # Add this line to import the concurrent module
import messages_pb2
import messages_pb2_grpc

class MessageServiceServicer(messages_pb2_grpc.MessageServiceServicer):
    def SendMessage(self, request, context):
        content = request.content
        print(f"Received message: {content}")
        return messages_pb2.MessageResponse(acknowledgement="Message received successfully")

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessageServiceServicer_to_server(MessageServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
