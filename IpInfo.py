def getAddress(ip, mask):
    address = []
    for i, val in enumerate(ip):
        address.append( int(ip[i]) & int(mask[i]) )
    return address

def getBroadcast(ip, mask):
    broadcast = []
    for i, val in enumerate(ip):
        intermidiary = int(mask[i]) ^ 255
        broadcast.append( intermidiary | int(ip[i]))
    return broadcast

def getClas(ip):
    ips = ip.split('.', 4)
    if (int(ips[0]) >= 0 and int(ips[0]) <= 127):
        return "Class A"
    elif (int(ips[0]) >= 128 and int(ips[0]) <= 191):
        return "Class B"
    elif (int(ips[0]) >= 192 and int(ips[0]) <= 223):
        return "Class C"
    elif (int(ips[0]) >= 224 and int(ips[0]) <= 239):
        return "Class D"
    else :
        return "Class E"

def expandMask(mask):
    MaskIP = []
    res = 0
    IP = [1] * mask
    for i in range(len(IP)):
        Bits = i % 8
        if Bits == 0:
            if i >= 8:
                    MaskIP.append(res)
                    res = 0
        res += pow(2, 7 - Bits)
    MaskIP.append(res)

    [MaskIP.append(0) for i in range(4 - len(MaskIP))]
    return MaskIP

def getRange(network, broadcast):
    for i in range(int(network[0]), int(broadcast[0])+1):
        for j in range(int(network[1]), int(broadcast[1])+1):
            for k in range(int(network[2]), int(broadcast[2])+1):
                for l in range(int(network[3]), int(broadcast[3])+1):
                    print "Available: ", i, j, k, l

def info(ip, mask):
    separateIp = ip.split('.', 3)
    separateMask = expandMask(mask)
    
    address = getAddress(separateIp, separateMask)
    broadcast = getBroadcast(separateIp, separateMask)
    clas = getClas(ip)
    
    print clas
    print "network: ", address[0], '.', address[1], '.', address[2], '.', address[3]
    print "mask: ", broadcast[0], '.', broadcast[1], '.', broadcast[2], '.', broadcast[3]
    if mask % 8 == 0 and mask < 32:
        print "Classful type"
    else:
        print "Classless type"
    getRange(address, broadcast)
    
mask = 12
ip = "192.168.10.10"
info(ip, mask)