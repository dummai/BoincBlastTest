file = open("stage_file.sh","w") #Create bash file "stage_file.sh" for running "stage_file" commands in batch. 
file.write("#!/bin/bash\n")
for i in range(some_number): #some_number = the running number for files containing data chunks (e.g. File_Name_1.fa, File_Name_2.fa).
    stage = "./bin/stage_file --copy --gzip ~/path/to/file/File_Name_%i.fa" % (i+1)
    file.write(stage)
file.close()
