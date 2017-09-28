#!/usr/bin/python

import modules.system
import modules.network
from termcolor import colored, cprint

def CheckAll():
	OutputSystem =  modules.system.CheckSystem()
	OutputNetwork = modules.network.CheckNetwork()
	print
	if OutputSystem:
		OutputSys = 'Check Validation System:\t' + str(OutputSystem)
		cprint (OutputSys, 'red',  attrs=['bold'])
	else:
		cprint ("Check Validation System:\t['OK']", 'green', attrs=['bold'])
	if OutputNetwork:
		OutputNet = 'Check Validation Network:\t' + str(OutputNetwork)
		cprint (OutputNet, 'red',  attrs=['bold'])
	else:
		cprint ("Check Validation Network:\t['OK']", 'green', attrs=['bold'])
	print
CheckAll()
