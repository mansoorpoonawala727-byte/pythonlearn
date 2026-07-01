def count_items(func):
    def wrapper():
        count=0
        logs=func()
        for log in logs:
            print(log)
            count +=1
        print(f"Total logs processed: {count}")    
    return wrapper
@count_items
def security_logs():
   yield "INFO 192.168.1.1 login success"
   yield "ERROR 192.168.1.2 login failed"
   yield "WARNING 192.168.1.3 slow response"
   yield "INFO 192.168.1.1 login success"
   yield "ERROR 192.168.1.2 login failed"
security_logs()   
