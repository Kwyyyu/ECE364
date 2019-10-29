#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/23/2019>
#######################################################

for file in ./circuits/*
do
  bytes=$(wc -c $file | cut -d" " -f 1)
  if (($bytes > 200))
  then
    circuit+=("${file:19:7}")
  fi
done

printf "%s\n" "${circuit[@]}" | sort -u

exit 0