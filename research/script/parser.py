import re

def parseconnection(connection):
    connection = connection.strip()
    ordered = re.sub(':|,|/|Mbps',' ',connection)
    ordered = connection.split()
    ips = re.findall('\d+\.\d+\.\d+\.\d+',connection)
    ports = re.findall('\d:\w+',connection)
    tcp = re.search('\S+\sw',connection)
    wscaleavg = re.search('wscale:\d+',connection)
    rto = re.search('rto:\d+',connection)
    rtt = re.search('rtt:\d+[.]?\d+',connection)
    ato = re.search('ato:\d+',connection)
    mss = re.search('mss:\d+',connection)
    maxcwnd = re.search('cwnd:\d+',connection)
    ssthresh = re.search('ssthresh:\d+',connection)
    send = re.search('send \d+[.]?\d+', connection)
    pace = re.search('pacing_rate \d+[.]?\d+', connection)
    unacked = re.search('unacked:\d+',connection)
    if tcp:
        tcp = tcp.group(0)[:-2]
    else:
        tcp = -1
    if wscaleavg:
        wscaleavg = wscaleavg.group(0)[7:]
    else:
        wscaleavg = -1
    if rto:
        rto = int(rto.group(0)[4:])
    else:
        rto = -1
    if rtt:
        rtt = float(rtt.group(0)[4:])
    else:
        rtt = -1
    if ato:
        ato = int(ato.group(0)[4:])
    else:
        ato = -1
    if mss:
        mss = int(mss.group(0)[4:])
    else:
        mss = -1
    if maxcwnd:
        maxcwnd = float(maxcwnd.group(0)[5:])
    else:
        maxcwnd = -1
    if ssthresh:
        ssthresh =  float(ssthresh.group(0)[9:])
    else:
        ssthresh = -1
    if send:
        send = float(send.group(0)[5:])
    else:
        send = -1
    if pace:
        pace = float(pace.group(0)[12:])
    else:
        pace = -1
    if unacked:
        unacked = int(unacked.group(0)[8:])
    else:
        unacked = -1
    return ips, ports, tcp, rto, rtt, ato, mss, maxcwnd, ssthresh, send/8, pace/8, unacked
