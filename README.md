# SNDCNV

## About

A python soundfile converter that will convert between Wave and Aiff formats. The program finds the file type of the file pointed to in the first argument, and converts it to the other.

I use Nilton Volpato's progressbar, which is available at http://code.google.com/p/python-progressbar/
Naturally, no copyright infringement is intended. I release my code as open source, as did Nilton Volpato with progressbar, and I only include it here for ease of use of my program.

## Usage

```python
import SNDCNV

SNDCNV.convert("inputFile","outputFile",samplesPerCycle)
```

Command line use is also possible in the form:
python SNDCNV.py inputfile.aiff/wav outputfile.aiff/wav samplesPerCycle

A note on samplesPerCycle:
This variable affects the performance of the module. The greater the number the faster the program will run, but this will have an effect on the performance of your computer. The defailt value is 441

## Version Notes

This version has implemented basic functonality, and is intended for public testing. A pre-compiled .pyc file has been included for ease of use.

##Copyright Notice

Copyright Hugh Rawlinson, 2012. The code is open source. It may be used freely in open source software. When used, it must be attributed, and the using program must be open source, and non commercial. I reserve the right to profit from this software, and to use it in my own projects that may be commercial, proprietary, and closed-sourced.
