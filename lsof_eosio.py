import re
import subprocess
import collectd

HTTP_PORT = '8888'
current_links = ""  
current_linknum = 0  
re4 = r'.* NAME\\nnodeos  (\d+) .*'


def init():
    global nodeos_pid
    ret = ""
    try:
        ret = subprocess.check_output(["lsof", "-i:"+HTTP_PORT])
    except:
        exit(1)
    retstr = str(ret)
    nodeos_pid_match = re.match(re4, retstr)
    nodeos_pid = nodeos_pid_match.group(1)




def config_func(config):
    httpport_set = False

    for node in config.children:
        key = node.key.lower()
        val = node.values[0]

        if key == 'http_port':
            global HTTP_PORT
            HTTP_PORT = val
            httpport_set = True
        else:
            collectd.info('LSOF plugin: Unknown config key "%s"' % key)

    if httpport_set:
        collectd.info('LSOF plugin: Using overridden http port %s' % HTTP_PORT)
    else:
        collectd.info('LSOF plugin: Using default http port %s' % HTTP_PORT)



def read_func():
    global current_links, current_linknum
    count = 0
    links = ""
    ret = subprocess.getoutput(["lsof", "-nP", "-p", str(nodeos_pid) ])
    lines = ret.split("\n")
    for line in lines:
        # Search for TCP connections matching your hostname
        if re.match(r'.*TCP block-producer.*', line):
            count += 1
            cols = re.split(r" +", line)
            links += cols[len(cols) - 2] + "\n"
    current_linknum = count
    current_links = links

    # Dispatch value to collectd
    val = collectd.Values(type='tcp_connections')
    val.plugin = 'lsof_eosio'
    val.dispatch(values=[current_linknum])


# Set init 
init()
# Send values to collectd
collectd.register_config(config_func)
collectd.register_read(read_func)