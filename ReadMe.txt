Author: Sherifdeen Lawal, kbr552
cs5123 Project II, Fall 2017.

The kbr552_test_script.py file is a monkey runner automated UI test script for the stock calendar app of the android studio emulator. The AVD under test is of the specs: 1080 x 1920: xxhdpi resolution, 23 API, Android 6.0 target, and x86 CPU/ABI.

After the creation of the monkey runner handle, the operation on the emulator starts from the home page.

The remaining part of the scripts is in this order:

1. user’s accounts creation (gmail and outlook) to sync calendar

2. UI interaction with stock calendar app

3. removal of user’s accounts

4. calendar and system clean-up to enable easy re-run of the script

NOTE: there’re couple of occasions where the microsoft outlook exchange server failed to connect and it’s not within my control. Also, in order for the script not to outpace the calendar app, inputs/interactions related to network and user authentication were deliberately slowed down.