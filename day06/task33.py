def read_file(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        print("Operation complete")
read_file("server.log")   
read_file("missing.txt")          