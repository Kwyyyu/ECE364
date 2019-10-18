#! /bin/bash

# ############################################################################
#
#   This is a common way of commenting in Bash, where the comments are boxed
#   to give a quick clue of the beginning of a script.
#
#   Author:     Alex A Gheith
#   Purpose:    Verify the names of Bash files used in this Prelab.
#   Date:       10/14/2019
# ############################################################################

actual=$(ls)

expected=("getCircuitsByProject.sh getStudentsByProject.sh getCircuitsByStudent.sh getProjectsByStudent.sh getComponentUseCount.sh getMoreUsedComponent.sh")

echo
echo "Checking for required files:"
echo "----------------------------"

for e in $expected
do

  missing=Yes

  for a in $actual
  do

    if [[ $e = $a ]]
    then
      echo "File '$e' located!"
      missing=No
      break
    fi
  done

    if [[ $missing = Yes ]]
    then
      echo "====> Unable to locate the file '$e'!"
    fi

done

echo
exit 0