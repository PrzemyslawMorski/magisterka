import subprocess
import time
import paramiko

test_file = r'C:\GIT\magisterka\network_test\Network test.jmx'
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

    _, ssh_stdout, ssh_stderr = ssh.exec_command(command)

    stdout = ssh_stdout.readlines()
    stderr = ssh_stderr.readlines()

    ssh.close()
    return (stdout, stderr)


if setup_script != '':
    sftp_put(setup_script, 'setup.sh')
    (out_, err_) = ssh_exec('bash setup.sh')

if teardown_script != '':
    sftp_put(teardown_script, 'teardown.sh')

sftp_put(run_script, 'run.sh')
sftp_put(stop_script, 'stop.sh')


for i in range(num_tests):
    results_file = r'C:\GIT\magisterka\network_test\results_'+str(i+1)+".csv"
    usage_file = "usage_"+str(i+1)+".csv"

    (out_, err_) = ssh_exec(
        "glances --export csv --export-csv-file " + usage_file + " --time 0.1 -q &")

    time.sleep(10)

    (out_, err_) = ssh_exec('bash run.sh')

    time.sleep(30)

    subprocess.run(["jmeter",  "-n", "-t", test_file,
                    "-l", results_file])

    subprocess.run(["mv", "summary.csv", "summary_"+i+".csv"])

    time.sleep(30)

    (out_, err_) = ssh_exec('bash stop.sh')

    time.sleep(10)

    (out_, err_) = ssh_exec('pkill glances')

    sftp_get(usage_file, usage_file)

if teardown_script != '':
    (out_, err_) = ssh_exec('bash teardown.sh')
