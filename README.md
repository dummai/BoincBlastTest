# Grid implementation on Basic Local Alignment Search Tool (BLAST) by Berkley Open Infrastructure for Network Computing (BOINC)

## Objectives of this project
1. This project aims to setup BOINC system that distributes tasks of BLAST (e.g. query sequences and databases ) to each computer client node within an organization or institute. 
2. This project aims to use a "grid computing" mode of BOINC. For, a "volunteer computing" mode please refer to references below.

## Prerequisites
1. Several personal computers to serve as clients with:
  1. Microsoft Windows as the main operating system (32-bit or 64-bit is OK)
  2. Installed with BOINC manager (http://boinc.berkeley.edu/wiki/BOINC_Manager)
  3. Full authorization to access each computer during performing BLAST (e.g. during off-hours)
  
2. One personal computer to serve as the project server with:
  1. Installed with Oracle VM VirtualBox (https://www.virtualbox.org/) or other VM software that can run a '.vdi' file.
  2. VM image of BOINC server (https://boinc.berkeley.edu/dl/debian-7-boinc-server-140412.7z)
  3. Full authorization to access this computer during performing BLAST (i.e. during off-hours)
  4. __OPTIONAL:__ Installed with remote administration software (e.g. NetSupport, TeamViewer, BOINCtasks ) for monitoring and controlling clients, and BOINC manager mass deployment. 
  
3. Stable network connections among clients and the server (e.g. Wi-Fi, LAN) with:
  1. __OPTIONAL:__ If data protection is required (e.g. analyzing patient sequencing data), the network without a direct Internet connection will be neccesarry.
  
4. Standalone BLAST application. 
  1. version 2.2.30 for Microsoft Windows 32-bit is perfered (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.30/). 
    1. The later versions do not support Microsoft Windows 32-bit
    2. BLAST for Microsoft Windows 32-bit could run on Microsoft Windows 64-bit, but not vice versa.

5. Query sequences for BLAST analysis.
  1. A training dataset from the Genome in a Bottle consortium is used as an example here (NA12878)(ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/NA12878/NIST_NA12878_HG001_HiSeq_300x/131219_D00360_005_BH814YADXX/Project_RM8398/Sample_U0a/U0a_CGATGT_L001_R1_001.fastq.gz).
  
6. Reference database or sequences.
  1. hg38 database is used as an example here (http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz).

## Further reading
1. Computing with BOINC (https://boinc.berkeley.edu/trac/wiki/ProjectMain)
2. BLAST® Command Line Applications User Manual (http://www.ncbi.nlm.nih.gov/books/NBK279690/)
3. Oracle VM VirtualBox documentation (https://www.virtualbox.org/wiki/Documentation)

