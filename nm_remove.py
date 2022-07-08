import os

def init(): 
    sendIt = int(input('See node_modules first? \n 1 - Yes, please!  \n 2 - No, send it \n 3 - What have I done?? Get me out of here \n'))

    if sendIt == 1:
        print("You didn't send it :(")
        os.system("find . -name 'node_modules' -type d -prune")

    elif sendIt == 2:
        print("Are you silly? I'm still gonna send it")
        os.system("find . -name 'node_modules' -type d -prune")

        # '{}' is a placeholder which find replaces with the file path it found, while + tells find to append all the file paths to a single command, rather than running rm for each
        os.system("find . -name 'node_modules' -type d -prune -exec rm -rf '{}' +")

        print("node_module pruning complete!!")

    elif sendIt ==3:
        return

    else:
        print('You had 3 valid options, choose one')
        init()


init()