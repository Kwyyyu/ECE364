#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/18/2019>
#######################################################

count1=0
count2=0

for file in ./circuits/*
do
  if grep -q -i $1 $file
  then
    count1=$((count1+1))
  fi
  if grep -q -i $2 $file
  then
    count2=$((count2+1))
  fi
done

if (($count1>$count2))
then
  echo $1
else
  echo $2
fi

exit 0