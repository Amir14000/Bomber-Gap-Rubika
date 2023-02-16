
your_auths_list = ['ciaouhqzjvszhcxduegkroarkblpmvhf','ciaouhqzjvszhcxduegkroarkblpmvhf', 'ghplwqwmitcyujywfljfrlytutfwakjb', 'iwteabrqeroxydvcwduflpyctnjwekko', 'gkxtljcgqijylikiqytydbvoclrtrehk', 'zivegmkngxmditfzorziwttqffhccqck', 'angpcnnbxiqjvwmjbrdmllytoucpoizy', 'wokzjociuwsswxioljccxwbpheyeuaui', 'kjfkcwkzolhbausmyctvnsvynxqstwhc']
from time import *;from os import *
from platform import node, system, release; Node, System, Release = node(), system(), release() 
from os import system, name
try:
    from libraryArsein.Arsein import Robot_Rubika
except:
        system("python -m pip install ArseinRubika==4.8.2")
# --------------------------------------------------
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'
def slow_print(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.02)
def clear():
    system('clear' if name == 'posix' else 'cls')
# -------------------------------------------------
# --------------------------------------------------
clear()
slow_print(f"""{g}╔═╗┌─┐┌─┐┌┬┐┌─┐┬─┐\n{w}╚═╗├─┘├─┤│││├┤ ├┬┘\n{r}╚═╝┴  ┴ ┴┴ ┴└─┘┴└─\n{w}""")
slow_print(f"""{y}Info: \n\t{r}[+]Creator: {w}Amir\n\t{r}[+]Rubika: {w}@kali_bad_boy\n{y}system:\n\t{r}[+]System: {w}{System}\n\t{r}[+]Node: {w}{Node}\n\t{r}[+]Release: {w}{Release}\n{r}Options: \n\t{r}[1]{w}Join And Leave group\n{r}\t[2]{w}Send Message And Join,Leave Group\n{w}""")
# 
user = int(input(f"{y}Enter Number : "))
user_input_link = input(f"{y}Enter The Target group link : ")
if user == 1:
    while True:
        for auth in your_auths_list:
            try:
                bot = Robot_Rubika(auth)
                target = bot.joinGroup(user_input_link);print(f"{g}joinded to {r}(victim){w}")
                if target['status'] =='ERROR_ACTION':
                    your_auths_list.remove(auth)
                mty = target['data']['group']['group_guid']
                bot.leaveGroup(mty);print(f"{y}left the group {r}(victim){w}")
            except:
                continue
if user == 2:
    message = input(f"{y}Enter Your Message For victim : ")
    while True:
        for auth in your_auths_list:
            try:
                bot = Robot_Rubika(auth)
                target = bot.joinGroup(user_input_link)
                if target['status'] =='ERROR_ACTION':
                    your_auths_list.remove(auth)
                mty = target['data']['group']['group_guid']
                bot.sendMessage(mty,message);print(f"{g}Message was send{r}(victim){w}",end=" ")
                print(f"and left The Group")
                bot.leaveGroup(mty)
            except:
                continue
else:
    slow_print(f"{y}Error Enter Number ")
    exit(2)





#  coder = amir
#  rubika = @kali_bad_boy

