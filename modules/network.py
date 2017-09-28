import commands
import re

ErrorCodes = []
Output = str()

def CheckNetwork():
        # Check NIC Names
        status, NICNameCheck = commands.getstatusoutput("ls /sys/class/net")
        MatchNICNameCheck = re.search('eth\d', NICNameCheck)
        if MatchNICNameCheck:
                ErrorCodes.insert(len(ErrorCodes),'NET001')

        return ErrorCodes

