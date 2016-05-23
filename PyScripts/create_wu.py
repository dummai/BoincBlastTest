file = open("create_work.sh","w") #create a bash file "create_work.sh" for running "create_work" commands in batch.
file.write("#!/bin/bash\n")
for i in range(some_number): #some_number = the last running number of WU name (e.g. work_name_1, work_name_2,...) and files of data chunks (e.g. file_name_1.fa, file_name_2.fa,...) 
    create = """./bin/create_work --appname blastn --wu_name work_name_%i \
    --wu_template templates/blastn_wu --result_template templates/blastn_re \
    --min_quorum 1 --target_nresultq 1 file_name_%i.fa db.nhr db.nin db.nsq blastn.exe\n""" %((i+1),(i+1))
    file.write(create)
file.close()
