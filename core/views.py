from django.shortcuts import render
from django.http import HttpResponse
import socket
import requests
import time
# Create your views here.



def home(request):
    ipcontext = {}
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    clickmsg = "Click on 'Light Scan' button to start scanning."
    ipcontext["hostaddr"] = host
    ipcontext["ipaddr"] = ip
    ipcontext["msg"] = clickmsg


    return render(request,"home.html",ipcontext)


def scan(request):
    start_time = time.time()
    common_ports = [
        7,19,20,21,23,25,42,43,49,53,67,68,69,70,80,88,102,110,113,113,123,135,137,139,143,161,162,177,179,201,264,318,381,383,389,411,412,443,445,464,465,497,500,512,513,514,515,520,521,540,
        554,546,547,563,587,591,593,631,636,639,646,691,860,873,902,989,990,993,995,1025,1026,1029,1080,1194,1214,1241,1311,1337,1433,1434,1512,1589,1701,1723,1725,1741,1755,1812,1813,1863,1985,
        2000,2049,2082,2083,2100,2222,2302,2483,2484,2745,2745,3050,3074,3124,3127,3128,3222,3260,3306,3389,3689,3690,3724,3784,3785,4333,4444,4664,4672,4899,5000,5001,5004,5005,5050,5060,5190,5222,
        5223,5432,5500,5554,5631,5632,5800,5900,6000,6001,6112,6129,6257,6346,6347,6500,6566,6588,6665,6669,6679,6697,6699,6881,6999,6891,6901,6970,7212,7648,7649,8000,8080,8086,8087,8118,8200,8500,
        8767,8866,9100,9101,9103,9119,9800,9898,9988,9999,10000,10000,10113,10116,11371,19226,20000,27374,33434,
    ]
    service_name = []
    open_ports_list = []
    
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(134,136):
        if sock.connect_ex((ip,port)):
            pass
            #print("{} is closed".format(port))
        else:
            service_name.append(socket.getservbyport(port,"tcp"))
            open_ports_list.append(port)
            #print("{} is open".format(port))
    
    noports = "All Common Ports are closed, refer the image given below for more information."        
    
    for i in open_ports_list:
        print(i)
    return render(request,"home.html",{'open_ports':open_ports_list,'port_name':service_name,'ipaddr':ip,'closed':noports,'time':round(time.time()-start_time,3)})

def rangeScan(request):
    start_time = time.time()
    
    if request.method == 'POST':
        StartValue = request.POST['startValue']
        EndValue = request.POST['endValue']

        service_name = []
        open_ports_list = []
        
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(int(StartValue),int(EndValue)):
            if sock.connect_ex((ip,port)):
                pass
                #print("{} is closed".format(port))
            else:
                service_name.append(socket.getservbyport(port,"tcp"))
                open_ports_list.append(port)
                #print("{} is open".format(port))
        
        noports = "All Ports from the given range are closed, refer the image given below for more information."        
        
        for i in open_ports_list:
            print(i)
        return render(request,"home.html",{'open_ports':open_ports_list,'port_name':service_name,'ipaddr':ip,'closed':noports,'time':round(time.time()-start_time,3)})


