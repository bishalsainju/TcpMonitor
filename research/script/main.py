# from plotter import plot_data
from command import run_command
from inputSetter import get_input
import csv
import re
from os.path import expanduser

home = expanduser('~')
path = home + '/Desktop/research'

def write_to_file(para_list, filename):
    csvfile = path + '/data/'+filename+'.csv'
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(["ips", "ports", "tcp",  "rto", "rtt", "ato", "mss", "maxcwnd", "ssthresh", "send", "pace", "unacked"])
        writer.writerows(para_list)

def main():
    file_list = get_input()['file_list']
    src_ip = get_input()['src_add']
    dst_ip = get_input()['dst_add']
    comm_ss = ['ss', '-t', '-i', 'state', 'ESTABLISHED', 'dst', dst_ip, 'src', src_ip]
    # comm_ss = ['nstat']
    # comm_ss = ['netstat', '--tcp', '--statistics']
    for i in (file_list):
        filename = str(i)
        comm_scp = ['scp', path+'/files/'+filename, 'bsainju@'+dst_ip+':'+filename]
        list = run_command(comm_scp, comm_ss, filename)
        write_to_file(list, filename)
        # plot_data(filename)

main()
