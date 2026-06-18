def file():
    with open("server.log", "w") as f:
         f.write("INFO 192.168.1.1 login success\n")
         f.write("ERROR 192.168.1.2 login failed\n")
         f.write("INFO 192.168.1.3 login success\n")
         f.write("ERROR 192.168.1.2 login failed\n")
         f.write("ERROR 192.168.1.4 login failed\n")
    with open("server.log", "r") as f:
         for line in f:
              if line.startswith("ERROR"):
                   print(line.strip())
file()                   