from parser import parseconnection
import  subprocess, time, os, sys
import re

ms = 50
def run_command(comm_scp, comm_ss, filename):
    proc = subprocess.Popen(comm_scp, stdout=subprocess.PIPE)
    i = 0
    child = os.fork()
    list = []
    while i == 0:
        if child == 0:
            line = proc.stdout.readline()
            if not line:
                exit(0)

        else:
            ss_proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE)
            line_in_ss = ss_proc.stdout.read()
            print line_in_ss
            line_in_ss = re.sub('\A.+\n','',line_in_ss)
            line_in_ss = re.sub('\n\t','',line_in_ss)
            connections = line_in_ss.splitlines()
            for connection in connections:
                # print connection
                ips, ports, tcp, rto, rtt, ato, mss, maxcwnd, ssthresh, send, pace, unacked = parseconnection(connection)
                para_list = [ips, ports, tcp, rto, rtt, ato, mss, maxcwnd, ssthresh, send, pace, unacked]
                list.append(para_list)
                # print ips, ports, mss, rtt, wscaleavg, maxcwnd, unacked, retrans, lost, tcp, send
            time.sleep(1)
            if os.waitpid(child, 1)[0]:
                i = 1
    subprocess.call(['ssh', 'bsainju@134.197.113.68', 'rm', '-f', filename])
    return list
