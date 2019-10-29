#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/23/2019>
#######################################################

max=0

for file in ./circuits/*
do
  bytes=$(wc -c $file | cut -d" " -f 1)
  if (($bytes >= $max))
  then
    max=$bytes
    circuit=("${file:19:7}")
  fi
done

grep -i -E $circuit "maps/projects.dat"  | tr -s " " | cut -d " " -f3 | sort -u

exit 0