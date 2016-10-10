import sys

exitMenu = False

print('Welcome to Trend Analysis \n')

while(exitMenu != True):
    print('[1] View Trends ')
    print('[2] Mine Captures ')
    print('[3] Edit Daily Manager ')
    print('[4] Preform analysis ')
    choice = input('Type the numeric of your choice, then press Enter \n')

    if(choice == '1'):
        print('\nAvailible Websites: \n')
        print('   We\'re sorry, no currently availible websites \n')


    elif(choice == '2'):
        print('\nEnter Websites to Mine, comma dilimited')
        choice = input('websites must match url exactly* \n')
        print('\nWe\'re sorry, mining is currently unavailible \n')


    elif (choice == '3'):
        print('\n Daily miner is currently not availible \n')


    elif (choice == '4'):
        print('\n[1] correlation + resampling-based confidence intervals')
        print('[2] PCA Analysis')
        choice = input('Type the numeric of your choice, then press Enter \n')
        print('\ncurrently no analysis availible \n')


    elif (choice == '0'):
        exitMenu = True


    else:
        print('\n Non-valid input, please enter valid input: \n')

print('\n Exiting TA')
sys.exit()
