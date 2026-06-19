class loganalyser:
    def __init__(self,filename):
        self.filename=filename
        self.info_count=0
        self.error_count=0
        self.ip_errors={}
    def analyse(self):
        try:
            with open(self.filename,"r") as f:
                  for line in f:
                        if line.startswith("INFO"):
                             self.info_count +=1
                        elif line.startswith("ERROR"):
                             self.error_count+=1
                             ip = line.split()[1]
                             if ip not in self.ip_errors:
                                 self.ip_errors[ip]=1
                             else:
                                 self.ip_errors[ip]+=1
        except FileNotFoundError:
            print("log file not found")
    def generate_report(self):
        if not self.ip_errors:
            print("no errors found or file not analysed")
        suspicious_ip= max(self.ip_errors , key = lambda  x:self.ip_errors[x])   
        suspicious_count = self.ip_errors[suspicious_ip]
        with open("report.txt", "w") as f:
            f.write("=== LOG ANALYSIS REPORT ===\n")
            f.write(f"Total INFO lines: {self.info_count}\n")
            f.write(f"Total ERROR lines: {self.error_count}\n")
            f.write(f"Most suspicious IP: {suspicious_ip} ({suspicious_count} failed attempts)\n")
        
        print("Report generated!")

analyser = loganalyser("server.log")
analyser.analyse()
analyser.generate_report()         

