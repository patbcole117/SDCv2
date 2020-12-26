# Salty Data Controller Redux!

After much consideration I have decided to revamp SDC. This is mainly because i have learned a 
lot in the past few days and believe I can make many improvements.

Most notably, I have removed logging entirely as it was about half the codebase and was a classic
 example of bringing a sledgehammer to crack a nut.

 I also got rid of pycharm and have been using this to experiemnt with VisualStudio Code.

# Config
in app.mnt is a file named config.txt it should look like the following:
{"l_addr": "0.0.0.0", "l_port": "50100", "sql_addr": "SQL_ADDR", "sql_port": "SQL_PORT", "sql_user": "SQL_USER", "sql_secret": "SQL_SECRET}

In its place is a file named "c.txt" this is so git will add /app/mnt. Ill do my best to make
 sure the real config wont be added to the github repo like lasttime.

 # Docker commands:
 sudo docker build -t sdc:latest .
 sudo docker run --name sdc01 -p 50200:50200 --mount source=sdc_data,target=/SDC/app/mnt sdc
