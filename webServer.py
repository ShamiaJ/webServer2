from socket import *
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(("", port))

  serverSocket.listen(1)

  print(f"Ready to serve on port {port}...")

  while True:
    connectionSocket, addr = serverSocket.accept()

    try:
      message = connectionSocket.recv(1024).decode()  # Receive the HTTP request from the client
      filename = message.split()[1]

      with open(filename[1:], 'rb') as f: # Use 'rb' mode for reading binary files
        content = f.read()
        
      headers = "HTTP/1.1 200 OK\r\n"
      headers += "Content-Type: text/html; charset=UTF-8\r\n\r\n"
      connectionSocket.send(headers.encode())
      connectionSocket.send(content)

     # f.close()
    # connectionSocket.close()

    except IOError:
      error_message = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
      connectionSocket.send(error_message.encode())
      connectionSocket.close()


if __name__ == "__main__":
  webServer(13331)
