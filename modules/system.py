import commands
import re

ErrorCodes = []
Output = str()

def CheckSystem():
        # Check SELinux Disabled
        status, SELinuxDisabling = commands.getstatusoutput("/usr/sbin/sestatus")
        MatchSELinuxDisabling = re.search('disabled$', SELinuxDisabling)
        if not MatchSELinuxDisabling:
                ErrorCodes.insert(len(ErrorCodes),'SYS001')
                return ErrorCodes

        # Check Motd
        MotdConfiguration = open('/etc/motd', 'r')
        LastMotdLine = MotdConfiguration.readlines()[-1]
        if not LastMotdLine in ['\n', '\r\n']:
                ErrorCodes.insert(len(ErrorCodes),'SYS002')

        MotdConfiguration = open('/etc/motd', 'r')
        for line in MotdConfiguration:
                MatchMotdConfiguration = re.search('Template', line)
                if MatchMotdConfiguration:
                        ErrorCodes.insert(len(ErrorCodes),'SYS003')
        MotdConfiguration.close()
        return ErrorCodes

