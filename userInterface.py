from colorama import Fore, Back, Style
import os
import time


class UserInterface:

    def __init__(self ):
        pass

    def printWarning(self, msg):
        print(Fore.YELLOW+msg+Style.RESET_ALL)

    def printError(self, msg):
        print(Fore.RED+msg+Style.RESET_ALL)

    def logo(self):
            l = Fore.RED
            r = Fore.LIGHTRED_EX
            g = Fore.GREEN
            y = Fore.YELLOW
            s = Style.RESET_ALL
            turbo ="___ _  _ ____ ___  ____\n"+\
                   " |  |  | |__/ |__] |  |\n"+\
                   " |  |__| |  \ |__] |__|\n"
            spymer=r+"  @@@@@@ @@@@@@@  @@@ @@@ @@@@@@@@@@  @@@@@@@@ @@@@@@@ \n"+\
                   r+" !@@     @@!  @@@ @@! !@@ @@! @@! @@! @@!      @@!  @@@\n"+\
                   r+"  !@@!!  @!@@!@!   !@!@!  @!! !!@ @!@ @!!!:!   @!@!!@! \n"+\
                   l+"     !:! !!:        !!:   !!:     !!: !!:      !!: :!! \n"+\
                   l+" ::.: :   :         .:     :      :   : :: :::  :   : :\n"
            logo=turbo+spymer+Style.RESET_ALL
            # logo = " ___  ____  _  _  __  __  ____  ____ \n"+\
                    # "/ __)(  _ \( \/ )(  \/  )( ___)(  _ \ \n"+\
                    # "\__ \ )___/ \  /  )    (  )__)  )   /\n "+\
                    # "(___/(__)   (__) (_/\/\_)(____)(_)\_)\n "
            # logo = r+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░"+g+"██████"+r+"╗"+g+"██████"+r+"╗░"+g+"██"+r+"╗░░░"+g+"██"+r+"╗"+g+"███"+r+"╗░░░"+g+"███"+r+"╗"+g+"███████"+r+"╗"+g+"██████"+r+"╗░\n"+g+"██"+r+"╔════╝"+g+"██"+r+"╔══"+g+"██"+r+"╗╚"+g+"██"+r+"╗░"+g+"██"+r+"╔╝"+g+"████"+r+"╗░"+g+"████"+r+"║"+g+"██"+r+"╔════╝"+g+"██"+r+"╔══"+g+"██"+r+"╗\n"+r+"╚"+g+"█████"+r+"╗░"+g+"██████"+r+"╔╝░"+r+"╚"+g+"████"+r+"╔╝"+r+"░"+g+"██"+r+"╔"+g+"████"+r+"╔"+g+"██"+r+"║"+g+"█████"+r+"╗░░"+g+"██████"+r+"╔╝\n░"+r+"╚═══"+g+"██"+r+"╗"+g+"██"+r+"╔═══╝░░░"+r+"╚"+g+"██"+r+"╔╝░░"+g+"██"+r+"║╚"+g+"██"+r+"╔╝"+g+"██"+r+"║"+g+"██"+r+"╔══╝░░"+g+"██"+r+"╔══"+g+"██"+r+"╗\n"+g+"██████"+r+"╔╝"+g+"██"+r+"║░░░░░░░░"+g+"██"+r+"║░░░"+g+"██"+r+"║░"+r+"╚═╝░"+g+"██"+r+"║"+g+"███████"+r+"╗"+g+"██"+r+"║░░"+g+"██"+r+"║\n"+r+"╚═════╝░"+r+"╚═╝░░░░░░░░"+r+"╚═╝░░░"+r+"╚═╝░░░░░"+r+"╚═╝╚══════╝╚═╝░░"+r+"╚═╝\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"+r+"░░░░░░░░░░░░░░░\n"+y+"[ SMS Spammer ~ v.9.0 ~ MPL-2.0 ]\n"+s
            print(logo)

    def clear(self):
            os.system('cls' if os.name=='nt' else 'clear')

    def getUserInput(self, question, options):
        availibleAnswer = []
        for i in range(len(options)):
            availibleAnswer.append(i+1)

        for x in range(len(options)):
            print(str(availibleAnswer[x])+". "+options[x]) 

        choice=-1
        while choice not in availibleAnswer:
            userInput=input(Fore.BLUE+question+Style.RESET_ALL+"~/")
            try:
                choice=int(userInput)
                if choice not in availibleAnswer:
                    self.printError("Неверный выбор, попробуйте еще раз! (Чтобы выйти нажмите CTRL-Z)")
            except:
                self.printError("Неверный выбор, попробуйте еще раз! (Чтобы выйти нажмите CTRL-Z)")

        return choice
