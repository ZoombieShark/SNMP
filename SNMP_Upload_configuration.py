from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.setCmd(
    cmdgen.CommunityData('private', mpModel=0),
    cmdgen.UdpTransportTarget(('10.90.90.90', 161)),
    ('1.3.6.1.4.1.171.12.1.2.18.1.1.3.3', rfc1902.IpAddress('10.90.90.100')),
    ('1.3.6.1.4.1.171.12.1.2.18.1.1.5.3', rfc1902.OctetString('des3810backup.cfg')),
    ('1.3.6.1.4.1.171.12.1.2.18.1.1.7.3', rfc1902.OctetString('des3810.cfg')),
    ('1.3.6.1.4.1.171.12.1.2.18.1.1.8.3', rfc1902.Integer(2)),
    ('1.3.6.1.4.1.171.12.1.2.18.1.1.12.3', rfc1902.Integer(3))
)

# Check for errors and print out results
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))