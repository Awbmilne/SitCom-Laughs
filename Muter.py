import laughr
import csv
import sys
import os
import argparse
import ffmpeg

parser = argparse.ArgumentParser()
group = parser.add_argument_group('Commands')
group.add_argument('--arguments', nargs=4, required=False, type=str, metavar=('/path/LAUGHR.py','/path/MODEL.h5', '/path/EPISODES', '/path/OUTPUT'))
group.add_argument('--test', required=False, type=bool, metavar='1 or 0')
group.add_argument('--silence',required=False, nargs=2, type=str,metavar=('/path/SILENCE_FINDER.py', '/path/Laugh_List.csv'))
args = parser.parse_args()

try:
    laugher = args.arguments[0]
    model_path = args.arguments[1]
    directory_of_episodes = args.arguments[2]
    output_directory = args.arguments[3]
except:
    laugher = input("Input the path to the Laughr code:\n")
    model_path = input("\nInput the path to the trained model:\n")
    directory_of_episodes = input("\nInput Episode Directory:\n")
    output_directory = input("\nInput Output Directory:\n")

try:
    silence_finder = args.silence[0]
    laugh_list = args.silence[1]
except:
    None

print("\n---Running Episodes through Neural Network---\n")

directory_of_episodes = directory_of_episodes + "/"
output_directory = output_directory + "/"

list_of_episodes = os.listdir(directory_of_episodes)

try:
    if args.silence[0] and args.silence[1]:
        with open(laugh_list, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["File Name","Seconds of Laughter","Number of segments"])
            csvFile.close()
except: None

for episode in list_of_episodes:
    print("\n------------------------\nRunning: " + episode[0:-4])
    
    if args.test:
        print('python "' + laugher + '" --model "' + model_path + '" --mute-laughs "' + directory_of_episodes + episode + '" "' + output_directory + episode[0:-4] + '_laughless.wav' + '"')
    
    else:
        #print('python "' + laugher + '" --model "' + model_path + '" --mute-laughs "' + directory_of_episodes + episode + '" "' + output_directory + episode[0:-4] + '_laughless.wav' + '"')
        try:
            file = open(output_directory + episode[0:-4] + '_laughless.wav','r')
            file.close()
        except:
            os.system('python "' + laugher + '" --model "' + model_path + '" --mute-laughs "' + directory_of_episodes + episode + '" "' + output_directory + episode[0:-4] + '_laughless.wav' + '"')
        
        try:
            if args.silence[0] and args.silence[1]:
                #print('python "' + args.silence[0] + '" --arguments "' + output_directory + episode[0:-4] + '_laughless.wav' + '" "' + laugh_list + '" --batch 1')
                os.system('python "' + args.silence[0] + '" --arguments "' + output_directory + episode[0:-4] + '_laughless.wav' + '" "' + laugh_list + '" --batch 1')
        
        except:
            None


if args.silence[0] and args.silence[1]:
    with open(laugh_list, 'r') as csvFile:
        reader = csv.reader(csvFile)
        data = []
        for row in reader:
            data.append(row)
        csvFile.close()

    clean_data = []
    for i in range(0,len(data)):
        if len(data[i]) == 3:
            clean_data.append(data[i])

    with open(laugh_list, 'w') as csvFile:
        writer = csv.writer(csvFile)
        data = writer.writerows(clean_data)
        csvFile.close()
