class SecurityLogAnalyser:
    def __init__(self, filename):
        self.filename = filename
        self.info_count = 0
        self.error_count = 0
        self.warning_count = 0
        self.ip_errors = {}
    
    def analyse(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if line.startswith("INFO"):
                        self.info_count += 1
                    elif line.startswith("WARNING"):
                        self.warning_count += 1
                    elif line.startswith("ERROR"):
                        self.error_count += 1
                        ip = line.split()[1]
                        if ip not in self.ip_errors:
                            self.ip_errors[ip] = 1
                        else:
                            self.ip_errors[ip] += 1
        except FileNotFoundError:
            print("Log file not found!")
    
    def get_top_suspicious_ips(self, n=3):
        sorted_ips = sorted(self.ip_errors.items(), key=lambda x: x[1], reverse=True)
        return sorted_ips[:n]
    
    def calculate_risk_score(self, error_count):
        if error_count >= 3:
            return "HIGH"
        elif error_count == 2:
            return "MEDIUM"
        else:
            return "LOW"
    
    def generate_report(self):
        if not self.ip_errors:
            print("No errors found or log not analysed yet.")
            return
        
        top_ips = self.get_top_suspicious_ips(3)
        
        with open("security_report.txt", "w") as f:
            f.write("=== SECURITY LOG ANALYSIS REPORT ===\n\n")
            f.write(f"Total INFO: {self.info_count}\n")
            f.write(f"Total WARNING: {self.warning_count}\n")
            f.write(f"Total ERROR: {self.error_count}\n\n")
            f.write("=== TOP 3 SUSPICIOUS IPs ===\n")
            
            for ip, count in top_ips:
                risk = self.calculate_risk_score(count)
                f.write(f"{ip} — {count} failed attempts — Risk: {risk}\n")
        
        print("Report generated! Check security_report.txt")



def create_log_file():
    log_lines = [
        "INFO 192.168.1.1 login success",
        "ERROR 192.168.1.2 login failed",
        "WARNING 192.168.1.3 slow response",
        "INFO 192.168.1.1 login success",
        "ERROR 192.168.1.2 login failed",
        "ERROR 192.168.1.4 login failed",
        "ERROR 192.168.1.2 login failed",
        "INFO 192.168.1.5 login success",
        "ERROR 192.168.1.4 login failed",
        "WARNING 192.168.1.3 slow response",
        "ERROR 192.168.1.6 login failed",
        "ERROR 192.168.1.4 login failed",
    ]
    
    with open("security.log", "w") as f:
        for line in log_lines:
            f.write(line + "\n")


create_log_file()
analyser = SecurityLogAnalyser("security.log")
analyser.analyse()
analyser.generate_report()