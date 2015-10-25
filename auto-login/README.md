Auto Login
How to automatically login to Raspberry Pi text console as pi user.
Step 1: Open a terminal session and edit inittab file.
sudo nano /etc/inittab
Step 2: Disable the getty program.
Navigate to the following line in inittab
1:2345:respawn:/sbin/getty 115200 tty1

And add a # at the beginning of the line to comment it out
#1:2345:respawn:/sbin/getty 115200 tty1
Step 3: Add login program to inittab.
Add the following line just below the commented line1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1
This will run the login program with pi user and without any authentication
Step 4: Save and Exit.
Press Ctrl+X to exit nano editor followed by Y to save the file and then press Enter to confirm the filename.
Reboot the pi and it will boot straight on to the shell prompt pi@raspberrypi without prompting you to enter username or password. But this isn't enough; you need your Pi to automatically run some command or a script. which is explained in the next section.
