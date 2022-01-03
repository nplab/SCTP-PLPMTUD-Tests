
tsn = 0
for mtu in range(1200, 1501, 4):
	print("// probe for "+str(mtu))
	print("+0.0 > sctp: HEARTBEAT[flgs=0, HEARTBEAT_INFORMATION[len=..., val=...]];\n\
	     PAD[flgs=0, len="+str(mtu-76)+", val=...]")
	if tsn>0: print("+0.0 < sctp: SACK[flgs=0, cum_tsn="+str(tsn)+", a_rwnd=99999, gaps=[], dups=[]]")
	print("+0.0 write(3, ...,2000) = 2000")
	tsn += 1
	print("+0.0 > sctp: DATA[flgs=B, len="+str(mtu-36)+", tsn="+str(tsn)+", sid=..., ssn=..., ppid=...]")
	tsn += 1
	print("+0.0 > sctp: DATA[flgs=E, len="+str(2032-(mtu-36))+", tsn="+str(tsn)+", sid=..., ssn=..., ppid=...]")
	print("+0.1 < sctp: HEARTBEAT_ACK[flgs=0, HEARTBEAT_INFORMATION[len=..., val=...]]")
	print()

	#print(mtu)