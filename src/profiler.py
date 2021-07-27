# This is a simple profiler tool that runs a command and tracks memory usage, cpu usage, and monotonic time
import os
import sys
import time
import subprocess
import time
import resource
from datetime import timedelta
import psutil

STDOUT_FILENO = 1
STDERR_FILENO = 2
def fprintf(pipe, string):
    print(string, file=pipe)

def CMD(cmd_str, arr=None):
    cmd_arr = cmd_str.split(' ') if arr == None else arr
    pipes = [0,0]
    pipes[0], pipes[1] = os.pipe()
    pid = os.fork()
    start_time = time.monotonic()
    if pid < 0:
        fprintf(sys.stderr, ("cannot fork child process, pid = %d" % pid))
        sys.exit(1)
    elif not pid:
        os.dup2(pipes[1], STDOUT_FILENO)
        os.close(pipes[0])
        os.close(pipes[1])
        os.execvp(cmd_arr[0], cmd_arr)
        fprintf(sys.stderr, ("Failed to exec program, pid = %d" % pid))
        sys.exit(1)
    else:
        print("\033[1m %s:\033[0m" % cmd_str)
        os.close(pipes[1])
        fp = os.fdopen(pipes[0])
        for line in fp:
            print("    %s" % line, end='')
        os.close(pipes[0])


    status = os.waitpid(-1, 0)[1]
    if (status != 0):
        fprintf(sys.stderr, ("process exited with exit code %d\n" % status))
        sys.exit(1)
    return start_time, time.monotonic()


def profile_cmd(cmd, arr=None):
    print()
    s, e = CMD(cmd, arr=arr)
    print()
    # Time in hh:mm:ss.00ms
    process_execution_time = timedelta(seconds=e - s)
    total_process_memory = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024 / 1024
    print("\033[1mThe process finished executing in %s seconds..." % str(process_execution_time))
    print("The process used %d megabytes of memory" % total_process_memory)
    total_machine_memory = psutil.virtual_memory().total / 1024 / 1024
    print("The total memory usage of the process was %0.2f%%\033[0m" % ((total_process_memory / total_machine_memory) * 100))

def profile_function(fun):
    def exec_profile():
        start = time.monotonic()
        print("\033[1m%s:\033[0m" % "OUTPUT")
        fun()
        total_process_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
        end = time.monotonic()
        process_execution_time = timedelta(seconds=end - start)
        print()
        print("\033[1mThe process finished executing in %s seconds..." % str(process_execution_time))
        print("The process used %d megabytes of memory" % total_process_memory)
        total_machine_memory = psutil.virtual_memory().total / 1024 / 1024
        print("The total memory usage of the process was %0.2f%%\033[0m" % ((total_process_memory / total_machine_memory) * 100))
    return exec_profile


def usage(stream):
    fprintf(stream, "usage: python profiler.py [-fh] [file]")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage(sys.stderr)
        sys.exit(1)
    else:
        if(sys.argv[1] == '-f'):
            exec_file = sys.argv[2]
            profile_cmd('python %s' % exec_file)
        elif(sys.argv[1] == '-h'):
            usage(sys.stdout)
        else:
            fprintf(sys.stderr, "Unknown option %s" % sys.argv[1]);
            usage(sys.stderr)
            sys.exit(1)
