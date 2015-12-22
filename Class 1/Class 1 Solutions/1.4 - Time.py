"""Write a program that takes the number of seconds as input,
and then converts that to minutes and seconds (for example, 102->1 min, 42 sec)
and prints the result.  Also, if you want, convert it to
hours, minutes, and seconds. """

#Input the time in seconds
time = int(input("Enter the number of seconds: "))

#Calculate the number of seconds
seconds = time % 60

#Subtract out the seconds and calculate how many minutes remain
time = (time - seconds) / 60

#Calculate the number of minutes
minutes = time % 60

#Calculate the number of hours
hours = (time - minutes) / 60

#Print everything out
print("This is equal to " + str(hours) + " hours and " +
    str(minutes) + " minutes and " + str(seconds) + " seconds.")

"""Note: you can split the print statement across several lines
to make it easier to read."""
