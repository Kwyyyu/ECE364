#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/18/2019>
#######################################################

id=$(grep -i -E "$1" "maps/students.dat" | cut --complement -f 1 -d "|")
circuit_list=()

for file in ./circuits/*
do
  if grep -q -i -o $id $file
  then
      circuit_list+=("${file:19:7}")
  fi
done

for circuit in ${circuit_list[@]}
do
  #project=$(grep -i -E $circuit "maps/projects.dat" | tr -s " " | cut -d " " -f 3)
  project_list+=($(grep -i -E $circuit "maps/projects.dat" | tr -s " " | cut -d " " -f 3))
  #$project_list+=($project) NO $ MARK for project list!!!
done

printf "%s\n" "${project_list[@]}" | sort -u

exit 0