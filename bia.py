from datetime import datetime
print "\n\nB.I.A\n\n"
now = datetime.now()
print "YOU CAN WRITE YOUR REPORT\n\n"
print (now)
report = raw_input("ENTER:\n")
save = open(str(now), "w")
save.write(report)
save.close()
print "\n\nSAVED!\n\n"
