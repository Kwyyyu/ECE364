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

printf "%s\n" "${circuit_list[@]}" | sort -u

exit 0