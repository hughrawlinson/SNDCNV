import wave, aifc, sys, sndhdr

def convert(input, output):
	samplePerCycle = 1
	"""Converts between wav and aiff files"""
	if sndhdr.what(input)[0] == 'wav':
		#from Wav to Aiff.
		input = wave.open(input, 'r')
		output = aifc.open(output, 'w')
	
	elif sndhdr.what(output)[0] == 'aiff':
		#from Aiff to Wav
		input = aifc.open(input, 'r')
		output = wave.open(output, 'w')

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