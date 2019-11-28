import csv
import argparse

from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.silence import detect_silence


parser = argparse.ArgumentParser()
group = parser.add_argument_group('Commands')
group.add_argument('--arguments', nargs=2, required=False, type=str, metavar=('/path/AUDIO.wav','/path/OUPUT.csv'))
group.add_argument('--batch', required=False, type=bool, metavar=('1 or 0'))
args = parser.parse_args()

try:
    file = args.arguments[0]
    output_file = args.arguments[1]

except:
    file = input("Please input audio.wav path:\n")
    output_file = input("Please input the CSV file for the results:\n")

try:
    if args.batch:
        csvFile = open(output_file, 'a')
        writer = csv.writer(csvFile)
            
    else:
        csvFile = open(output_file, 'w')
        writer = csv.writer(csvFile)
        writer.writerow(["File Name","Seconds of Laughter","Number of segments"])
except:
    csvFile = open(output_file, 'w')
    writer = csv.writer(csvFile)
    writer.writerow(["File Name","Seconds of Laughter","Number of segments"])

audio = AudioSegment.from_wav(file)

dBFS = audio.dBFS
print("dBFS = " + str(dBFS))
ranges = detect_silence(audio, min_silence_len = 500, silence_thresh = dBFS-16)

#print(ranges)

sum = 0
count = 0
for i in range(0,len(ranges)):
    if not i == 0:
        length = ranges[i][0] - ranges[i-1][1]
        if length <= 6500 and length>= 500:
            print(length/1000)
            sum += length/1000
            count += 1

print ("\nSum = " + str(sum))
writer.writerow([file[file.rfind('/')+1:-14], sum, count])

csvFile.close()