###  基于Socket网络编程的C/S框架

#### 服务端伪代码

```C++
sockfd = socket();
bind(sockfd,ip:port);
listen(sockfd);
while(true){
	connfd = accept(sockfd);
    recv(connfd,buff);
    send(connfd,buff);
    close(connfd);
}

```

**socket()-->bind()-->listen()-->accept()-->recv()-->send()-->close()**



#### 客户端伪代码

```c++
sockfd = socket();
connect(sockfd,ip:port);
scanf("%s",buff);
send(sockfd,buff);
recv(sockfd,buff);
close(sockfd);
```

**socket()-->connect()-->send()-->recv()-->close()**

