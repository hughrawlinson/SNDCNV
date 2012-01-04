import wave, aifc, sys, sndhdr
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
                        FileTransferSpeed, FormatLabel, Percentage, \
                        ProgressBar, ReverseBar, RotatingMarker, \
                        SimpleProgress, Timer

FileLocation = sys.argv[1]
FileDestination = sys.argv[2]

print "|| WELCOME TO  SNDCNV ||"
print "|| CONVERTING " + FileLocation.upper() + " TO " + FileDestination.upper() + " ||"

def finished(count,last):
	a = count / 5
	a = round(a,0)
	if last != a:
		print 
	return last
	
def convert(location, destination):
	nframes = location.getnframes()
	
	destination.setnchannels(location.getnchannels())
	destination.setframerate(location.getframerate())
	destination.setsampwidth(location.getsampwidth())
	
	i = 1
	dataset = []
	pbar = ProgressBar().start()
	
	for i in range(1,nframes + 1):
		location.setpos(i)
		dataval = location.readframes(1)
		dataset.append(dataval)
		
		#stri = str(i)
		#strnframes = str(nframes)
		#progress =  "|| " + stri + " OF " + strnframes + " ||"
		fnframes = float(nframes)
		fi = float(i)
		fifr = fi/fnframes
		
		pbar.update(round(fifr*100))
		
	valuestr = ''.join(dataset)
	destination.writeframes(valuestr)
	print ''
	
	return 1

if sndhdr.what(FileLocation)[0] == 'wav':
	#from Wav to Aiff.
	location = wave.open(FileLocation, 'r')
	destination = wave.open(FileDestination, 'w')
	
	if convert(location,destination) == 1:
		print "|| CONVERSION SUCCESSFUL ||"
		
	else:
		print "|| CONVERSION UNSUCCESSFUL ||"
	
	destination.close()
	location.close()
	
elif sndhdr.what(FileLocation)[0] == 'aiff':
	#from Aiff to Wav
	location = aifc.open(FileLocation, 'r')
	destination = wave.open(FileDestination, 'w')
	
	if convert(location,destination) == 1:
		print "|| CONVERSION SUCCESSFUL ||"
		
	else:
		print "|| CONVERSION UNSUCCESSFUL ||"
	
	destination.close()
	location.close()
	
else:
	print "|| ARGUMENTS ARE INVALID. PLEASE TRY AGAIN. ||"