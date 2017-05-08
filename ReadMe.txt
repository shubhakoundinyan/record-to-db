  ____            _                   ____                            _   _             ____                       _   _             
 / ___| _   _ ___| |_ ___ _ __ ___   |  _ \ _ __ ___  _ __   ___ _ __| |_(_) ___  ___  |  _ \ ___ _ __   ___  _ __| |_(_)_ __   __ _ 
 \___ \| | | / __| __/ _ \ '_ ` _ \  | |_) | '__/ _ \| '_ \ / _ \ '__| __| |/ _ \/ __| | |_) / _ \ '_ \ / _ \| '__| __| | '_ \ / _` |
  ___) | |_| \__ \ ||  __/ | | | | | |  __/| | | (_) | |_) |  __/ |  | |_| |  __/\__ \ |  _ <  __/ |_) | (_) | |  | |_| | | | | (_| |
 |____/ \__, |___/\__\___|_| |_| |_| |_|   |_|  \___/| .__/ \___|_|   \__|_|\___||___/ |_| \_\___| .__/ \___/|_|   \__|_|_| |_|\__, |
        |___/                                        |_|                                         |_|                           |___/ 

OVERVIEW:

The basic system properties that are monitored in this program are,

1. RAM
2. HARD DISK
3. VIRTUAL MEMORY
4. SWAP MEMORY
5. CPU TEMPERATURE

WHAT DOES THIS PROGRAM DO:

A simple script that would help to check and monitor the above system properties, and save them onto a table in a database. The database configured to record the results is PostGreSQL in this case. However, thinking of it : This script can be scheduled as a timed thread, as there might be times when it would be very useful to record the results into a database for a day or a week per requirement, and use any analytics engine on the database later, to analyze and evaluate the system performance.