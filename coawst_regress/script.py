#/usr/bin/env python
#*** These "import" flags = loading "header in C or*****************************
#***"modules" in fortran********************************************************  
import sys   # Used for running system commands 
import os    # Used for running system commands 
import shutil # Used to copy and move files 
import fileinput # Used to edit input files 
import stat # Used to change file permissions 
import time # Used to display time 

#*** This file saves the output from running the scripts ***********************
#f = open('out.txt', 'w')
#print >> f, 'Filename:', filename  # or f.write('...\n')
#f.close()

#*** Should take care of daylights savings *************************************
print time.strftime('%l:%M%p %Z on %b %d, %Y')
timestr = time.strftime("%d%m%Y-%H%M%S") 

#*** Check to see if Python 2.4 & above exists on the system *******************
major, minor = sys.version_info[0:2]
if (major, minor) < (2, 4):
    sys.stderr.write('Python 2.4 or later needed to use the package\n')
    sys.exit(1)
else :
    print "---------------------------------------------------------------------"
    print  "Welcome to the Regression Testing of COAWST"

#*** Let's get path of the current script to put things in context***************
#    script_name = "script.py"
path_script = os.path()
print "---------------------------------------------------------------------"
print "The script should be on this path:"
print path_script 

#*** Let's get path of the COAWST folder which is one level up the project ******
path_coawst = os.getcwd(os.getcwd())
print "---------------------------------------------------------------------"
print "The COAWST folder should be on this path:"
print path_coawst 

#*** Case list should be same to the COAWST Application *************************
case_list = ["UPWELLING", "RIVERPLUME1"]

for each_case in case_list:

#*** MAKE A COAWST.BASH FOR EACH CASE *******************************************
#*** This is the file that would need to be edited ******************************
#*** This should be in the same level as "script.py" ****************************
     orig_makefile = "coawst.bash"

#*** Create "makefile" pertaining to each case***********************************
     case_makefile = each_case + "_" + orig_makefile
     print "--------------------------------------------------------------------"
     print "This is the name of this case's makefile:"
     print case_makefile 
#*** At this point these files are empty *****************************************

#*** Copy the contents of coawst.bash into each case's makefile ******************
     shutil.copyfile(orig_makefile, case_makefile)
#*** FINISHED MAKING COAWST.BASH FOR EACH CASE ***********************************
#*** IT STILL NEEDS TO BE EDITED FOR EACH CASE ***********************************

#*** MAKE RUN DIRECTORIES FOR EACH CASE ******************************************
     rundir_case = "Rundir" + "_" + each_case + "_" + timestr 
     os.makedirs(rundir_case)

     path_case = os.path.join(path_script,rundir_case)
     print "--------------------------------------------------------------------"
     print "This is the location/path for the case:"
     print path_case

#     if os.path.exists(rundir_case):
#*** Edit the coawst.bash for each case ******************************************
     for line in fileinput.input([case_makefile], inplace=True):
          oldinput = "COAWST_APPLICATION="
          newinput = oldinput + each_case
          line     = line.replace(oldinput,newinput) 

          oldinput = "MY_ROOT_DIR="  
          newinput = oldinput + path_coawst # (one level up ie. where coawst is) 
          line     = line.replace(oldinput,newinput) 
 
          oldinput ="MY_PROJECT_DIR="
          newinput = oldinput + path_case
          line     = line.replace(oldinput,newinput) 

#*** sys.stdout is redirected to the file****************************************
          sys.stdout.write(line)

#*** Change user permissions on each case's make file ***************************
#*** This lets one to execute them **********************************************
#*** Time to get out of the makefile editing FOR LOOP ***************************
     st = os.stat(case_makefile)
     os.chmod(case_makefile,st.st_mode | stat.S_IEXEC)

#*** Move the makefile to each run directory ************************************         
     shutil.move(case_makefile, case_path)
     print "--------------------------------------------------------------------"
     print "moving the make files to their respective folders"

#*** Execute the makefile in the case path***************************************
#*** Notice the format "%" and "s" carefully prone to errors*********************
#*** Compiling to get executable file for each case ***************************** 
     print "---------------------------------------------------------------------"
     print "Compiling %(case_makefile)s in %(local_case_directory)s" %locals()
#     os.system('./%(local_case_directory)s/%(case_makefile)s' %locals())
     print "---------------------------------------------------------------------"
     print "Finished compiling %(case_makefile)s" %locals()

