Auto Login
=
How to automatically login to Raspberry Pi text console as pi user.
--
- Open a terminal session and edit inittab file. - `sudo nano /etc/inittab`
- Navigate to the following line in inittab `1:2345:respawn:/sbin/getty 115200 tty1`
- Add a # at the beginning of the line to comment it out `#1:2345:respawn:/sbin/getty 115200 tty1`
- Add login program to inittab.
 - Add the following line just below the commented line. `1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1`. This will run the login program with pi user and without any authentication
- Step 4: Save and Exit.
