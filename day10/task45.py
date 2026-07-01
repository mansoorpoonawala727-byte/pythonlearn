
def security_check(func):
    def wrapper():
        print("access granted")
        func()
        print("Access logged")
    return wrapper
@security_check
def view_dashboard():
    print("showing dashboard")
view_dashboard()