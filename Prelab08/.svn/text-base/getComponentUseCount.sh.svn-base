#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/18/2019>
#######################################################

count=0

for file in ./circuits/*
do
  if grep -q -i -o $1 $file
  then
      count=$((count+1))
  fi
done

echo $count

exit 0