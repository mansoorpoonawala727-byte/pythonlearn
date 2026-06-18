def analyse_log(filename):
    info_count = 0
    error_count = 0
    ip_errors = {}
    
    try:
      
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("INFO"):
                    info_count += 1
                elif line.startswith("ERROR"):
                    error_count += 1
                    ip = line.split()[1] 
                    if ip not in ip_errors:
                        ip_errors[ip] = 1
                    else:
                        ip_errors[ip] += 1
        
       
        suspicious_ip = max(ip_errors, key=lambda x: ip_errors[x])
        suspicious_count = ip_errors[suspicious_ip]
        
       
        with open("report.txt", "w") as f:
            f.write("=== LOG ANALYSIS REPORT ===\n")
            f.write(f"Total INFO lines: {info_count}\n")
            f.write(f"Total ERROR lines: {error_count}\n")
            f.write(f"Most suspicious IP: {suspicious_ip} ({suspicious_count} failed attempts)\n")
        
        print("Report generated! Check report.txt")
        
    except FileNotFoundError:
        print("Log file not found!")

analyse_log("server.log")