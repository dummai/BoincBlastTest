# Grid implementation on Basic Local Alignment Search Tool (BLAST) by Berkley Open Infrastructure for Network Computing (BOINC)

## Objectives of this project
1. This project aims to setup BOINC system that distributes tasks of BLAST (e.g. query sequences and databases ) to each computer client node within an organization or institute. 
2. This project aims to use a "grid computing" mode of BOINC. For, a "volunteer computing" mode please refer to references below.

## Prerequisite
1. Several personal computers to serve as clients with:
  1. Microsoft Windows as the main operating system (32-bit or 64-bit is OK)
  2. Installed with BOINC manager (http://boinc.berkeley.edu/wiki/BOINC_Manager)
  3. Full authorization to access each computer during performing BLAST (e.g. during off-hours)
2. One personal computer to serve as the project server with:
  1. Installed with Oracle VM VirtualBox (https://www.virtualbox.org/) or other VM software that can run a '.vdi' file.
  2. VM image of BOINC server (https://boinc.berkeley.edu/dl/debian-7-boinc-server-140412.7z)
  3. Full authorization to access this computer during performing BLAST (e.g. during off-hours)
  4. __OPTIONAL:__ Installed with remote administration software (e.g. NetSupport, TeamViewer, BOINCtasks ) for monitoring and controlling clients, and BOINC manager mass deployment. 
3. Stable network connections among clients
