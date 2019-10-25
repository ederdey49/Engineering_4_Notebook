gpio mode 0 out #Set pin 0 to output
gpio write 0 0 #Turn pin 0 off
gpio mode 1 out #Set pin 1 to output
gpio write 1 0 #Turn pin 1 off

for i in {0..9} #Do this 10 times (0 to 9 inclusive)
do
	gpio write 0 1 #Turn pin 0 on
	gpio write 1 0 #Turn pin 1 off
	sleep .51s #Pause
	gpio write 0 0 #Turn pin 0 off
	gpio write 1 1 #Turn pin 1 on
	sleep .51s #Pause
done

gpio write 1 0 #Turn pin 1 off
