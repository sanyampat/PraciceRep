def checkip(ip):
    str(ip)
    valid = True
    if "." in ip:
        x = ip.split(".")
        for i in x:
            if not(i.isdigit() and 0 < int(i) < 255):
                valid = False
                break
        if valid:
            print("this is a valid ip4")
        else:
            print("not a  valid ip")
    elif ":" in ip:
        x=ip.split(':') 
        if len(x)== 8:
            for i in x:
                if len(i) == 4:
                    continue
                else:
                    valid = False
                    break
            if valid:
                print("this is a valid ip6")
            else:
                print("not a  valid ip")
    else:   
        print("not a ip at all")
checkip("192.168.1.1")  
checkip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")  
checkip("not.an.ip") 