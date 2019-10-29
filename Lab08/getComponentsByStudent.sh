#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/23/2019>
#######################################################

id=$(grep -i -E "$1" "maps/students.dat" | cut --complement -f 1 -d "|")
comp_list=()

for file in ./circuits/*
do
  if grep -q -i -o $id $file
  then
    comp=$(grep -i -E -o "[A-Z]{3}-[0-9]{3}" $file)
    comp_list+=("$comp")
  fi
done

printf "%s\n" "${comp_list[@]}" | sort -u

exit 0