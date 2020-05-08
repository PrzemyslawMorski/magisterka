import subprocess
import time
import paramiko
import shutil
import os
import sys

jmeter_path = "C:\Program Files\\apache-jmeter-5.2.1\\bin\jmeter.bat"
num_tests = 2
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


def run_test(test_file, results_path,  run_script, stop_script, setup_script=None, teardown_script=None, seed_script=None):

    if setup_script != None:
        sftp_put(setup_script, 'setup.sh')
        ssh_exec('bash setup.sh')
        time.sleep(5)

    if teardown_script != None:
        sftp_put(teardown_script, 'teardown.sh')

    if seed_script != None:
        sftp_put(seed_script, 'seed.sh')

    sftp_put(run_script, 'run.sh')
    sftp_put(stop_script, 'stop.sh')

    for i in range(num_tests):
        results_file = "results_"+str(i+1)+".csv"
        usage_file = "usage_"+str(i+1)+".csv"

        print("Starting iteration: "+str(i+1))

        ssh_exec(
            "glances --export csv --export-csv-file " + usage_file + " --time 0.4 -q &")

        print("Started glances")

        ssh_exec('bash run.sh')
        time.sleep(60)

        print("Started container")

        if seed_script != None:
            print("Started seeding the container")
            ssh_exec('bash seed.sh')
            time.sleep(5)

        subprocess.run([jmeter_path,  "-n", "-t", test_file,
                        "-l", results_path+results_file])
        print("Finished jmeter")

        ssh_exec('bash stop.sh')
        print("Stopped container")

        ssh_exec('kill $(pgrep -f glances)')
        print("Killed glances")

        time.sleep(10)

        # shutil.move(".\\summary.csv", results_path+results_file)
        sftp_get(usage_file, results_path+usage_file)
        ssh_exec('rm ' + usage_file)

    if teardown_script != None:
        ssh_exec('bash teardown.sh')


# network
# run_test(test_file=r"C:\GIT\magisterka\network_test\Network test.jmx",
#          results_path="C:\\GIT\\magisterka\\network_test\\docker\\",
#          setup_script=r'C:\GIT\magisterka\network_test\setup_docker.sh',
#          teardown_script=r'C:\GIT\magisterka\network_test\teardown_docker.sh',
#          run_script=r'C:\GIT\magisterka\network_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\network_test\stop_docker.sh')

# run_test(test_file=r"C:\GIT\magisterka\network_test\Network test.jmx",
#          results_path="C:\\GIT\\magisterka\\network_test\\podman\\",
#          setup_script=r'C:\GIT\magisterka\network_test\setup_podman.sh',
#          teardown_script=r'C:\GIT\magisterka\network_test\teardown_podman.sh',
#          run_script=r'C:\GIT\magisterka\network_test\run_podman.sh',
#          stop_script=r'C:\GIT\magisterka\network_test\stop_podman.sh')

run_test(test_file=r"C:\GIT\magisterka\network_test\Network test.jmx",
         results_path="C:\\GIT\\magisterka\\network_test\\singularity\\",
         setup_script=r'C:\GIT\magisterka\network_test\setup_singularity.sh',
         teardown_script=r'C:\GIT\magisterka\network_test\teardown_singularity.sh',
         run_script=r'C:\GIT\magisterka\network_test\run_singularity.sh',
         stop_script=r'C:\GIT\magisterka\network_test\stop_singularity.sh')

# compute
# run_test(test_file=r"C:\GIT\magisterka\compute_test\Compute test.jmx",
#          results_path="C:\\GIT\\magisterka\\compute_test\\podman\\",
#          run_script=r'C:\GIT\magisterka\compute_test\run_podman.sh',
#          stop_script=r'C:\GIT\magisterka\compute_test\stop_podman.sh')

# run_test(test_file=r"C:\GIT\magisterka\compute_test\Compute test.jmx",
#          results_path="C:\\GIT\\magisterka\\compute_test\\docker\\",
#          run_script=r'C:\GIT\magisterka\compute_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\compute_test\stop_docker.sh')

# run_test(test_file=r"C:\GIT\magisterka\compute_test\Compute test.jmx",
#          results_path="C:\\GIT\\magisterka\\compute_test\\singularity\\",
#          setup_script=r'C:\GIT\magisterka\compute_test\setup_singularity.sh',
#          teardown_script=r'C:\GIT\magisterka\compute_test\teardown_singularity.sh',
#          run_script=r'C:\GIT\magisterka\compute_test\run_singularity.sh',
#          stop_script=r'C:\GIT\magisterka\compute_test\stop_singularity.sh')

# io query
# run_test(test_file=r"C:\GIT\magisterka\io_test\Search test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\query\\podman\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_podman.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_podman.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# run_test(test_file=r"C:\GIT\magisterka\io_test\Search test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\query\\docker\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_docker.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# run_test(test_file=r"C:\GIT\magisterka\io_test\Search test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\query\\singularity\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_singularity.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_singularity.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# io index
# run_test(test_file=r"C:\GIT\magisterka\io_test\Index test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\index\\podman\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_podman.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_podman.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# run_test(test_file=r"C:\GIT\magisterka\io_test\Index test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\index\\docker\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_docker.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_docker.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')

# run_test(test_file=r"C:\GIT\magisterka\io_test\Index test.jmx",
#          results_path="C:\\GIT\\magisterka\\io_test\\index\\singularity\\",
#          run_script=r'C:\GIT\magisterka\io_test\run_singularity.sh',
#          stop_script=r'C:\GIT\magisterka\io_test\stop_singularity.sh',
#          seed_script=r'C:\GIT\magisterka\io_test\seed.sh')
