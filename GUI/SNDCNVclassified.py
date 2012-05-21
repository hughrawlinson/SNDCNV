import wave, aifc, sys, sndhdr

def __init__():
	inputFileLocation = ""
	outputFileLocation = ""

def inputFile(a):
	inputFileLocation = a
	
def outputFile(a):
	outputFileLocation = a

def convert():
	samplePerCycle = 1
	"""Converts between wav and aiff files"""
	if sndhdr.what(inputFileLocation)[0] == 'wav':
		#from Wav to Aiff.
		input = wave.open(inputFileLocation, 'r')
		output = aifc.open(outputFileLocation, 'w')
	
	elif sndhdr.what(inputFileLocation)[0] == 'aiff':
		#from Aiff to Wav
		input = aifc.open(inputFileLocation, 'r')
		output = wave.open(outputFileLocation, 'w')

	nframes = input.getnframes()
	
	output.setnchannels(input.getnchannels())
	output.setframerate(input.getframerate())
	output.setsampwidth(input.getsampwidth())
	
	i = 1
	dataset = []
	
	for i in range(0, nframes, samplePerCycle):
		input.setpos(i)
		dataval = input.readframes(samplePerCycle)
		dataset.append(dataval)
		
		#===========================================
		#Implement output(nframes) == input(nframes)
		#===========================================
		#if (nframes % samplePerCycle < samplePerCycle):
		#	if (nframes % samplePerCycle != 0):
		#		samplePerCycle = nframes % samplePerCycle
		
	valuestr = ''.join(dataset)
	output.writeframes(valuestr)
	
	input.close()
	output.close()
	
if __name__ == "__main__":
	import sys
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	convert(inputFile,outputFile)