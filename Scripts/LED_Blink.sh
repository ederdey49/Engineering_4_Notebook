gpio mode 0 out
gpio write 0 0
gpio mode 1 out
gpio write 1 0

for i in {0..9}
do
	gpio write 0 1
	gpio write 1 0
	sleep .51s
	gpio write 0 0
	gpio write 1 1
	sleep .51s
done

gpio write 1 0
