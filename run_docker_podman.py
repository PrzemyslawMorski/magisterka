import subprocess
import time
import paramiko
import shutil
import os
import sys

jmeter_path = "C:\Program Files\\apache-jmeter-5.2.1\\bin\jmeter.bat"
num_tests = 10
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


def run_test(test_file, results_path, teardown_script=None, seed_script=None, run_script=None, stop_script=None):

    if teardown_script != None:
        sftp_put(teardown_script, 'teardown.sh')

    if seed_script != None:
        sftp_put(seed_script, 'seed.sh')

    if run_script != None:
        sftp_put(run_script, 'run.sh')
        ssh_exec('bash run.sh')

    if stop_script != None:
        sftp_put(stop_script, 'stop.sh')

    for i in range(num_tests):
        results_file = "results_"+str(i+1)+".csv"
        usage_file = "usage_"+str(i+1)+".csv"

        if seed_script != None:
            print("Seeding")
            ssh_exec('bash seed.sh')
            time.sleep(10)

        ssh_exec(
            "glances --stdout-csv now,cpu,mem,network,diskio -t 1 > " + usage_file + " &")

        print("Started glances")
        time.sleep(5)

        subprocess.run([jmeter_path,  "-n", "-t", test_file,
                        "-l", results_path+results_file])
        print("Finished jmeter")

        time.sleep(5)

        if teardown_script != None:
            print("Tearing down")
            ssh_exec('bash teardown.sh')
            time.sleep(10)

        ssh_exec('kill $(pgrep -f glances)')
        print("Killed glances")

        time.sleep(5)

        sftp_get(usage_file, results_path+usage_file)
        ssh_exec('rm ' + usage_file)

    if teardown_script != None:
        ssh_exec('bash stop.sh')

# docker
# run_test(test_file=r"C:\GIT\magisterka\network_test\Network test podman.jmx",
#          results_path="C:\\GIT\\magisterka\\network_test\\docker\\",
#          run_script=r'C:\GIT\magisterka\network_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\network_test\stop_docker.sh')

# run_test(test_file=r"C:\GIT\magisterka\compute_test\Compute test.jmx",
#          results_path="C:\\GIT\\magisterka\\compute_test\\docker\\",
#          run_script=r'C:\GIT\magisterka\compute_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\compute_test\stop_docker.sh')

# run_test(test_file=r"C:\GIT\magisterka\io_test\Search test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\query\\docker\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_docker.sh',
#          teardown_script=r'C:\GIT\magisterka\io_test\teardown.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# run_test(test_file=r"C:\GIT\magisterka\io_test\Index test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\index\\docker\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_docker.sh',
#          teardown_script=r'C:\GIT\magisterka\io_test\teardown.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# podman
run_test(test_file=r"C:\GIT\magisterka\network_test\Network test podman.jmx",
         results_path="C:\\GIT\\magisterka\\network_test\\podman\\")

# run_test(test_file=r"C:\GIT\magisterka\compute_test\Compute test.jmx",
#          results_path="C:\\GIT\\magisterka\\compute_test\\podman\\")

# run_test(test_file=r"C:\GIT\magisterka\io_test\Search test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\query\\podman\\")

# run_test(test_file=r"C:\GIT\magisterka\io_test\Index test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\index\\podman\\",
#          teardown_script=r'C:\GIT\magisterka\io_test\teardown.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

