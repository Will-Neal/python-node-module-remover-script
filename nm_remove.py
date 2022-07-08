import os
from re import S

def init(): 
    def packageLocks():
        lockThePackage = int(input('Do you want to get rid of the package-lock.jsons too? \n 1 - No, I thought this was just for node_modules, get me outta here!! \n 2 - Yes, delete the pesky package-locks \n'))

        if lockThePackage == 1:
            print('Alright see ya later')
            return

        if lockThePackage == 2:
            print('Yipee ki-yay!')
            os.system("find . -name 'package-lock.json' -type d -prune")
            os.system("find . -name 'package-lock.json' -exec rm -rf '{}' +")
            print("EZPZ package-lock's are no more")
            return


    sendIt = int(input('See node_modules first? \n 1 - Yes, please!  \n 2 - No, send it \n 3 - What have I done?? Get me out of here!! \n'))

    if sendIt == 1:
        print("You didn't send it :(")
        os.system("find . -name 'node_modules' -type d -prune")
        init()

    elif sendIt == 2:
        print("Are you silly? I'm still gonna send it")
        os.system("find . -name 'node_modules' -type d -prune")

        # '{}' is a placeholder which find replaces with the file path it found, while + tells find to append all the file paths to a single command, rather than running rm for each
        os.system("find . -name 'node_modules' -type d -prune -exec rm -rf '{}' +")

        print("no more node_modules!!")
        packageLocks()

    elif sendIt ==3:
        return

    else:
        print('You had 3 valid options, choose one')
        init()


init()