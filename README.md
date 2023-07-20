# grpc-hello

### First, let's install the required dependencies using pip:
```bash
pip install grpcio grpcio-tools
```

### Build protoc file.
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. messages.proto
```