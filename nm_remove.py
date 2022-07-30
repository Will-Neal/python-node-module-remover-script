import os
from re import S

def init(): 
    def packageLocks():
        lockThePackage = int(input('\nDo you want to get rid of the package-lock.jsons too? \n \n1 - No, I thought this was just for node_modules \n2 - Yes, delete the pesky package-locks \n \n'))

        if lockThePackage == 1:
            print('Alright see ya later')
            return

        if lockThePackage == 2:
            print('Yipee ki-yay!')
            os.system("find . -name 'package-lock.json' -type d -prune")
            os.system("find . -name 'package-lock.json' -exec rm -rf '{}' +")
            print('Hacking... 5%')
            print('Hacking.... 50%')
            print('Hacking..... 100%')
            print("EZPZ package-lock's are no more")
            return


    sendIt = int(input('\nSee node_modules first? \n \n1 - Yes, please  \n2 - No, send it! \n3 - What have I done?? Get me out of here!! \n \n'))

    if sendIt == 1:
        print("\nYou didn't send it :( \n \nI found the following node_modules folders: \n")
        os.system("find . -name 'node_modules' -type d -prune")
        init()

    elif sendIt == 2:
        print("\nAre you silly? I'm still gonna send it \n ")
        #os.system("find . -name 'node_modules' -type d -prune")
        
        # '{}' is a placeholder which find replaces with the file path it found, while + tells find to append all the file paths to a single command, rather than running rm for each
        os.system("find . -name 'node_modules' -type d -prune -exec rm -rf '{}' +")
        print('Hacking... 5%')
        print('Hacking.... 50%')
        print('Hacking..... 100%')
        print("\nno more node_modules!! \n")
        packageLocks()

    elif sendIt ==3:
        return

    else:
        print('You had 3 valid options, choose one')
        init()


init()