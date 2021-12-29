
'''Author: Sherifdeen Lawal, kbr552
cs5123 Project II, Fall 2017.'''

import sys
import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice



'''Function to automate logcat with file_name and monkeyrunner device handle as input
parameters'''

def log(file_name, device):
    log_stream = device.shell('logcat -d')
    write_log_to_file = open(file_name, 'at')
    if log_stream is None:
        log_stream = 'None'
    write_log_to_file.write(log_stream.encode('utf-8'))
    write_log_to_file.close()    
    device.shell('logcat -c')

if __name__ == '__main__':
	device = MonkeyRunner.waitForConnection()
	device.shell('logcat -c') # Clear logs buffer


	device.touch(545, 1839, MonkeyDevice.DOWN_AND_UP)   #home
	time.sleep(1)


	device.touch(545, 1630, MonkeyDevice.DOWN_AND_UP)	#app list
	time.sleep(2)


	device.touch(179, 704, MonkeyDevice.DOWN_AND_UP)   #calender
	time.sleep(12)



	'''User accounts creation '''

	device.touch(122, 1273, MonkeyDevice.DOWN_AND_UP)  #click to enter email/phone#
	time.sleep(2)

	device.type('kbr552.testscript@gmail.com')
	time.sleep(1)

	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(4)


	device.type('KgX-Ere-caw-BU3')
	time.sleep(2)

	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(2)

	device.touch(813, 1718, MonkeyDevice.DOWN_AND_UP)  #accept
	time.sleep(8)


	device.touch(933, 1687, MonkeyDevice.DOWN_AND_UP)  #drop down
	time.sleep(1)

	device.touch(933, 1687, MonkeyDevice.DOWN_AND_UP) #next, to calendar
	time.sleep(2)

	device.touch(991, 137, MonkeyDevice.DOWN_AND_UP) 	#menu
	time.sleep(2)


	device.touch(698, 859, MonkeyDevice.DOWN_AND_UP)	#setting
	time.sleep(2)


	device.touch(942, 150, MonkeyDevice.DOWN_AND_UP)	#add acct
	time.sleep(2)

	device.touch(90, 677, MonkeyDevice.DOWN_AND_UP)	#click to type
	time.sleep(1)

	device.type('kbr552.testscript@outlook.com')
	time.sleep(1)

	device.touch(197, 1023, MonkeyDevice.DOWN_AND_UP)	#manual setup
	time.sleep(2)

	device.touch(512, 1164, MonkeyDevice.DOWN_AND_UP)	#exchange
	time.sleep(2)

	device.touch(950, 535, MonkeyDevice.DOWN_AND_UP)	#click to enter passwd
	time.sleep(1)

	device.type('GYd-4KZ-5da-pTL')
	time.sleep(1)



	device.touch(835, 1031, MonkeyDevice.DOWN_AND_UP)	#next
	time.sleep(2)

	device.drag((840, 1421), (840, 553), 0.5, 50)    #drag to server
	time.sleep(2)

	device.touch(259, 996, MonkeyDevice.DOWN)	#highlight field
	time.sleep(3)
	device.touch(259, 996, MonkeyDevice.UP)
	time.sleep(1)

	device.touch(166, 704, MonkeyDevice.DOWN_AND_UP)	#cut
	time.sleep(1)

	device.type('s.outlook.com')
	time.sleep(1)


	device.touch(849, 1000, MonkeyDevice.DOWN_AND_UP)	#next
	time.sleep(10)

	device.touch(862, 1687, MonkeyDevice.DOWN_AND_UP)	#next
	time.sleep(4)

	device.touch(862, 1687, MonkeyDevice.DOWN_AND_UP)	#next
	time.sleep(2)



	'''UI testing of stock calendar app featues'''

	device.touch(24, 146, MonkeyDevice.DOWN_AND_UP)	#back to cal
	time.sleep(2)

	device.touch(826, 150, MonkeyDevice.DOWN_AND_UP)	#today
	time.sleep(2)


	device.touch(991, 1510, MonkeyDevice.DOWN)	#time of event
	time.sleep(3)
	device.touch(991, 1510, MonkeyDevice.UP)
	time.sleep(1)


	device.touch(210, 1014, MonkeyDevice.DOWN_AND_UP)	#add event
	time.sleep(2)

	device.touch(73, 487, MonkeyDevice.DOWN_AND_UP)	#click to type
	time.sleep(1)


	device.type('Grocery')
	time.sleep(1)


	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)


	device.touch(73, 628, MonkeyDevice.DOWN_AND_UP) #click to type
	time.sleep(1)

	device.type('HEB')
	time.sleep(1)


	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)

	device.touch(853, 146, MonkeyDevice.DOWN_AND_UP)	#Done
	time.sleep(2)
	
	device.touch(999, 146, MonkeyDevice.DOWN_AND_UP)	#option
	time.sleep(2)

	device.touch(623, 287, MonkeyDevice.DOWN_AND_UP)	#new event
	time.sleep(2)

	device.touch(853, 385, MonkeyDevice.DOWN_AND_UP)	#acct drop down
	time.sleep(2)

	device.touch(308, 673, MonkeyDevice.DOWN_AND_UP)	#bday
	time.sleep(2)


	device.touch(90, 500, MonkeyDevice.DOWN_AND_UP)	#click to type
	time.sleep(1)


	device.type('RandomBirthday')
	time.sleep(1)

	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)


	device.touch(658, 863, MonkeyDevice.DOWN_AND_UP)	#date dropdown
	time.sleep(2)

	device.touch(538, 1333, MonkeyDevice.DOWN_AND_UP)	#pick date
	time.sleep(2)

	device.touch(547, 1682, MonkeyDevice.DOWN_AND_UP)	#Done
	time.sleep(2)



	device.touch(1022, 863, MonkeyDevice.DOWN_AND_UP)	#drop down
	time.sleep(2)


	device.touch(534, 1240, MonkeyDevice.DOWN_AND_UP)	#pick time
	time.sleep(2)


	device.touch(534, 1240, MonkeyDevice.DOWN_AND_UP)	#pick time
	time.sleep(2)


	device.touch(521, 1479, MonkeyDevice.DOWN_AND_UP)	#done
	time.sleep(2)


	device.touch(858, 146, MonkeyDevice.DOWN_AND_UP)	#Done
	time.sleep(2)


	device.touch(999, 150, MonkeyDevice.DOWN_AND_UP)	#cal menu
	time.sleep(2)

	device.touch(760, 420, MonkeyDevice.DOWN_AND_UP)	#refresh
	time.sleep(2)

	device.touch(999, 150, MonkeyDevice.DOWN_AND_UP)	#cal menu
	time.sleep(2)

	device.touch(809, 557, MonkeyDevice.DOWN_AND_UP)	#search
	time.sleep(2)

	device.type('Grocery')
	time.sleep(1)

	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)


	

	device.touch(28, 141, MonkeyDevice.DOWN_AND_UP)	#back
	time.sleep(2)

	device.touch(991, 154, MonkeyDevice.DOWN_AND_UP)	#options
	time.sleep(2)

	device.touch(738, 739, MonkeyDevice.DOWN_AND_UP)	#cal to display
	time.sleep(2)


	device.touch(28, 141, MonkeyDevice.DOWN_AND_UP)	#back
	time.sleep(2)

	device.touch(991, 154, MonkeyDevice.DOWN_AND_UP)	#options
	time.sleep(2)

	device.touch(702, 872, MonkeyDevice.DOWN_AND_UP)	#setting
	time.sleep(2)

	device.touch(348, 296, MonkeyDevice.DOWN_AND_UP)	#gen setting
	time.sleep(2)

	device.touch(924, 602, MonkeyDevice.DOWN_AND_UP)	#check week #
	time.sleep(2)

	device.touch(28, 141, MonkeyDevice.DOWN_AND_UP)	#back
	time.sleep(2)

	device.touch(28, 141, MonkeyDevice.DOWN_AND_UP)	#back
	time.sleep(2)


	device.touch(560, 181, MonkeyDevice.DOWN_AND_UP) #drop down
	time.sleep(2)


	device.touch(286, 292, MonkeyDevice.DOWN_AND_UP)	#day
	time.sleep(2)


	device.touch(822, 150, MonkeyDevice.DOWN_AND_UP)	#today
	time.sleep(2)


	device.touch(485, 1666, MonkeyDevice.DOWN)	#right click
	time.sleep(3)
	device.touch(485, 1666, MonkeyDevice.UP)

	device.touch(190, 1006, MonkeyDevice.DOWN_AND_UP)	#new event
	time.sleep(2)

	device.touch(90, 500, MonkeyDevice.DOWN_AND_UP)	#click to type
	time.sleep(1)


	device.type('Movie')
	time.sleep(1)

	device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
	time.sleep(1)


	device.touch(760, 141, MonkeyDevice.DOWN_AND_UP)	#done
	time.sleep(2)

	
	device.touch(560, 181, MonkeyDevice.DOWN_AND_UP) #drop down
	time.sleep(2)


	device.touch(241, 580, MonkeyDevice.DOWN_AND_UP)	#month
	time.sleep(2)


	device.touch(569, 1399, MonkeyDevice.DOWN)	#right click day
	time.sleep(3)
	device.touch(569, 1399, MonkeyDevice.UP)


	device.touch(139, 819, MonkeyDevice.DOWN_AND_UP)	#click to type
	time.sleep(1)


	device.type('cs5123')
	time.sleep(1)


	device.touch(844, 1219, MonkeyDevice.DOWN_AND_UP)	#save
	time.sleep(3)


	device.touch(560, 181, MonkeyDevice.DOWN_AND_UP) #drop down
	time.sleep(3)


	device.touch(352, 743, MonkeyDevice.DOWN_AND_UP)	#agenda
	time.sleep(2)


	device.touch(560, 181, MonkeyDevice.DOWN_AND_UP) #drop down
	time.sleep(3)

	device.touch(303, 420, MonkeyDevice.DOWN_AND_UP)	#week
	time.sleep(2)


	device.touch(826, 141, MonkeyDevice.DOWN_AND_UP)	#today
	time.sleep(1)



	device.touch(246, 1846, MonkeyDevice.DOWN_AND_UP)	#back
	time.sleep(2)



	'''user accounts removal'''

	device.touch(545, 1839, MonkeyDevice.DOWN_AND_UP)  #home
	time.sleep(2)

	device.touch(545, 1630, MonkeyDevice.DOWN_AND_UP)	#app list
	time.sleep(2)

	device.drag((0, 1463), (0, -456), 0.5, 50)
	time.sleep(1)

	device.touch(658, 1248, MonkeyDevice.DOWN_AND_UP)  #settings
	time.sleep(2)

	device.drag((724, 1718), (724, 314), 0.5, 50)    #drag to account
	time.sleep(1)

	device.touch(618, 1394, MonkeyDevice.DOWN_AND_UP)  #account
	time.sleep(2)


	device.touch(423, 358, MonkeyDevice.DOWN_AND_UP)  #acct1
	time.sleep(2)

	device.touch(82, 456, MonkeyDevice.DOWN_AND_UP)	#refresh
	time.sleep(2)

	device.touch(1008, 163, MonkeyDevice.DOWN_AND_UP)	#options
	time.sleep(2)

	device.touch(667, 309, MonkeyDevice.DOWN_AND_UP)	#remove acct
	time.sleep(2)

	device.touch(760, 1116, MonkeyDevice.DOWN_AND_UP)	#confirm
	time.sleep(2)


	device.touch(423, 358, MonkeyDevice.DOWN_AND_UP)  #acct2
	time.sleep(1)


	device.touch(1004, 153, MonkeyDevice.DOWN_AND_UP) #options
	time.sleep(1)

	device.touch(707, 301, MonkeyDevice.DOWN_AND_UP) #remove acct
	time.sleep(1)

	device.touch(716, 1111, MonkeyDevice.DOWN_AND_UP) #confirm remove
	time.sleep(1)




	'''System clean-up'''

	device.touch(545, 1839, MonkeyDevice.DOWN_AND_UP)  #home
	time.sleep(1)

	log('calendar_event.log', device) # Write logs
	device.shell('shell pm clear com.android.calendar && com.android.providers.calendar')
	device.shell('am force-stop com.android.calendar && am force-stop com.android.providers.calendar')
	device.shell('am restart com.android.calendar && am restart com.android.providers.calendar')
