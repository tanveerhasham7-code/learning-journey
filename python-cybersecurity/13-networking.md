# 13 — Networking and Sockets

Understand IP addressing, subnetting, DNS, TCP, UDP, ports, routing, TLS and client/server architecture before automating network tasks.

## DNS lookup
~~~python
import socket
print(socket.getaddrinfo("localhost", None))
~~~

## TCP client to localhost
~~~python
import socket

with socket.create_connection(("127.0.0.1", 8000), timeout=3) as client:
    client.sendall(b"Hello from my lab client\n")
    response = client.recv(1024)
    print(response.decode("utf-8", errors="replace"))
~~~

This requires a server you control listening on localhost port 8000. It does not scan other machines.

## TCP and UDP
TCP provides a reliable ordered byte stream. UDP sends datagrams without TCP's built-in delivery guarantees. Applications may add reliability themselves.

Use timeouts and handle OSError. A listening port is not proof of vulnerability; identify the service and intended exposure.

## Authorization
Only connect to localhost, your isolated VMs or approved test systems. Do not build broad internet scanners or scan networks without explicit permission.

## Exercise
Start a simple local server bound only to 127.0.0.1:8000, connect with a client, exchange one message and stop the server. Record what happens when the server is stopped.
