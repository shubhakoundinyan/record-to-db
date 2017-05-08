#! /usr/bin/python
# encoding: utf-8

import re
import os
import sys
import platform
import psutil
import subprocess
import psycopg2

def lin_process():
	process = psutil.Process(os.getpid())

	# Checking the Physical Memory of the system

	print "\n ##### PHYSICAL MEMORY USAGE #####"
	print "\n Memory currently Used :"+str(process.memory_full_info().rss)
	print "\n PerecentAGE Memory Used :"+str(process.memory_percent())

	# Checking the Hard Disk Spave | AVAILABLE vs USED

	print "\n ########## DISK UTILIZATION for RESIDING FILE SYSTEM ##########"
	bash_command_u = "df -h|grep /dev/sda1|awk '{print $3}' "					# Change the hdd location here. So instead of /dev/sda1|awk - it should reflect your mount address
	c= (subprocess.check_output(['bash', '-c', bash_command_u]))
	print "\n Used Disk Space :"+str(c)
	bash_command_a = "df -h|grep /dev/sda1|awk '{print $4}' "					# Change the hdd location here. So instead of /dev/sda1|awk - it should reflect your mount address
	d = subprocess.check_output(['bash', '-c', bash_command_a])
	print " Available Disk Space :"+str(d)
	
	# Checking for the Virtual and Swap Memory of the system

	print " ########## MEMORY USAGE | VIRTUAL & SWAP ##########"
	print "\n Virtual Memory Used :"+str(psutil.virtual_memory().used)
	print "\n Virtual Memory Available :"+str(psutil.virtual_memory().available)
	print "\n Swap Memory Used :"+str(psutil.swap_memory().used)
	print "\n Swap memory available :"+str(psutil.swap_memory().free)

	# Connect to a database of name db_name as user (specify the user for the DB here)

	conn = psycopg2.connect(database="db_name", user="Configured_User", password = "*****", host="127.0.0.1", port = "5432")	# Make sure to input the user and password correctly
	print "ConnecTION to Database and DB Access SUCCESSFUL!"
	
	cur = conn.cursor()

	# Create a table to insert these values
	cur.execute('''CREATE TABLE SENSOR_VALUES
		   (MEMORY_CURRENTLY_USED double precision NOT NULL,
		    PERCENTAGE_MEMORY_USED double precision NOT NULL,
		    USED_DISK_SPACE double precision NOT NULL,
		    AVAILABLE_DISK_SPACE double precision NOT NULL,
		    VIRTUAL_MEMORY_USED double precision NOT NULL,
		    VIRTUAL_MEMORY_AVAILABLE double precision NOT NULL,
		    SWAP_MEMORY_USED double precision NOT NULL,
		    SWAP_MEMORY_AVAILABLE double precision NOT NULL);''')
	conn.commit()

	print "Table Created Successfully!"

	cur.execute("""INSERT INTO sensor_values VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",(process.memory_full_info().rss,process.memory_percent(),c[:len(c)-2],d[:len(d)-2],
			 psutil.virtual_memory().used, psutil.virtual_memory().available,psutil.swap_memory().used, psutil.swap_memory().free)) 
	conn.commit()
	conn.close() 	
	
def main():

	# Operating system and platform validation

	if platform.system()=="Linux" or platform.system()=="Darwin":
		lin_process()
	elif platform.system()=="Windows":
		win_process()

if __name__=="__main__":
	main()
