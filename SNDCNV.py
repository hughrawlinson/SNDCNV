import wave, aifc, sys, sndhdr

def convert(input, output):
	"""Converts between wav and aiff files"""
	if sndhdr.what(location)[0] == 'wav':
		#from Wav to Aiff.
		input = wave.open(input, 'r')
		output = wave.open(output, 'w')
	
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
	
	for i in range(1,nframes + 1):
		location.setpos(i)
		dataval = input.readframes(1)
		dataset.append(dataval)
		
	valuestr = ''.join(dataset)
	output.writeframes(valuestr)
	
	input.close()
	output.close()
	
if __name__ == "__main__":
	import sys
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	convert(input,output)