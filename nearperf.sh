x=1
while true; do
x=$(python perfect.py $x | tail -n 1 | awk '{print $1}')
echo $x
done
