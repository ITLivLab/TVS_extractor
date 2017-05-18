import re

header = 'TVS\x0D\x0A'
begin = 'BEGIN\x0D\x0AKEY'
footer = 'END\x0D\x0A'

disk_image = open('myimage','rb').read()

addresses = {}

file_number = 1
for match in re.finditer(header,disk_image):
    addresses[file_number] = {}
    addresses[file_number]['header'] = match.span()[0]
    file_number = file_number+1

file_number = 1
for match in re.finditer(begin,disk_image):
    addresses[file_number]['begin'] = match.span()[0]
    file_number = file_number+1

file_number = 1
for match in re.finditer(footer,disk_image):
    addresses[file_number]['footer'] = (match.span()[0]+3)
    file_number = file_number+1

for address in addresses:
    outfile = open(str(address)+'.tvs','wb')
    reportfile = open(str(address)+'.metadata','w')
    header = addresses[address]['header']
    begin = addresses[address]['begin']
    footer = addresses[address]['footer']

    outfile.write(disk_image[header:footer])
    outfile.close()

    reportfile.write(disk_image[header+3:begin])
    reportfile.close()
