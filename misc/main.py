import functions

def main():
    functions.writeName()
    characterName = functions.readName()
    while True:
        if userAction != 'exit':
            userAction = functions.actions()
            if userAction == 'explore':
                userAction = functions.actions()
            elif userAction == 'inv':
                userAction = functions.actions()
            elif userAction == 'level':
                userAction = functions.actions()
            elif userAction == 'help':
                functions.userHelp()
                userAction = functions.actions()
        elif userAction == 'exit':
            print('Saving data')
            functions.saveFile()
            break
        break

main()
