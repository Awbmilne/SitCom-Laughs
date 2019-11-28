# SitCom-Laughs
 Code used to analyze the laugh tracks of sitcoms - Used to acquire data for stats project - Univerisity of Waterloo 2019 - Code built upon github.com/jeffgreenca/laughr

 Please reference the laughr-README.md file for further information on the Laughr.py script.

 The laughr.py script has been slightly modified to work for my specific use case, but is fundamentally the same.

 The Silence_Finder.py script analyzes the output of the laughr.py script and lists the laugh segments, counting them and summing the total time. It also some of the false-positives.

 The Muter.py script handles the calling of both of the above scripts to automate the running for each file. It also handles the final output data as a .csv file.