import subprocess
import time
import paramiko

jmeter_path = "C:\Program Files\\apache-jmeter-5.2.1\\bin\jmeter.bat"
test_file = r"C:\GIT\magisterka\network_test\Network test.jmx"
results_path = "C:\\GIT\\magisterka\\network_test\\"
num_tests = 10

setup_script = ''
teardown_script = ''
run_script = r'C:\GIT\magisterka\network_test\run_docker.sh'
stop_script = r'C:\GIT\magisterka\network_test\stop_docker.sh'

test_machine_addr = "192.168.0.168"
usr = "pmorski"
password = "pmorski"


def sftp_get(src, target):
    transport = paramiko.Transport(test_machine_addr)
    transport.connect(username=usr, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(src, target)
    transport.close()


def sftp_put(src, target):
    transport = paramiko.Transport(test_machine_addr)
    transport.connect(username=usr, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src, target)
    transport.close()


def ssh_exec(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(test_machine_addr, username=usr, password=password)

    _, _, _ = ssh.exec_command(command)

    ssh.close()


if setup_script != '':
    sftp_put(setup_script, 'setup.sh')
    ssh_exec('bash setup.sh')

if teardown_script != '':
    sftp_put(teardown_script, 'teardown.sh')

sftp_put(run_script, 'run.sh')
sftp_put(stop_script, 'stop.sh')


for i in range(num_tests):
    results_file = "results_"+str(i+1)+".csv"
    usage_file = "usage_"+str(i+1)+".csv"

    ssh_exec(
        "glances --export csv --export-csv-file " + usage_file + " --time 0.1 -q &")

    time.sleep(10)

    ssh_exec('bash run.sh')

    time.sleep(30)

    subprocess.run([jmeter_path,  "-n", "-t", test_file, "-l", results_path+results_file])

    time.sleep(30)

    ssh_exec('bash stop.sh')

    time.sleep(10)

    ssh_exec('pkill glances')

    sftp_get(usage_file, results_path+usage_file)
    ssh_exec('rm ' + usage_file)

if teardown_script != '':
    ssh_exec('bash teardown.sh')
