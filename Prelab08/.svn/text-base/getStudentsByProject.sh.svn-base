#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/18/2019>
#######################################################

file="maps/projects.dat"
circuits=$(grep -i -E $1 $file | cut -f5 -d" " | sort -u)

id_list=()
for circuit in $circuits
do
  filename="circuits/circuit_"$circuit".dat"
  id=$(grep -i -E -o "[0-9]{5}-[0-9]{5}" $filename)
  id_list+=" "$id
done

filename2="maps/students.dat"
students=()
for id in $id_list
do
  student=$(grep -i -E $id $filename2 | cut -f1 -d"|")
  students+=("$student")
  # use quotes to prevent space expansion
done

printf "%s\n" "${students[@]}" | sort -u

exit 0