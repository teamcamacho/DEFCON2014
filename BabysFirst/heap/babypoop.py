import subprocess
import sys
import signal
from optparse import *
import os

def babby_formed(multiplier):
	shell = 'A'*int(multiplier)
	proc = subprocess.Popen(['./babyfirst-heap',shell],stdout=subprocess.PIPE)
	os.kill(proc.pid, signal.SIGSTOP)
	print "PID is %d"%proc.pid
	sys.stdin.readline()
	#os.kill(proc.pid, signal.SIGCONT)
	for line in iter(proc.stdout.readline,''):
		line=line.strip()
		print "line == %s"%line

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-m", "--multiplier", dest="multiplier",
                  help="file to store")
	(options,args) = parser.parse_args()
	if options.multiplier:
		babby_formed(options.multiplier)