import socket
import sys
from termcolor import colored
from rich.console import Console
from time import sleep
import os
print(colored('=-=-' * 100, 'green'))
print(colored('''
██████╗     ███████╗    ███╗   ███╗       ██╗   ██╗    ██╗    ███╗   ██╗    ██████╗      ██████╗
██╔══██╗    ██╔════╝    ████╗ ████║       ██║   ██║    ██║    ████╗  ██║    ██╔══██╗    ██╔═══██╗
██████╔╝    █████╗      ██╔████╔██║       ██║   ██║    ██║    ██╔██╗ ██║    ██║  ██║    ██║   ██║
██╔══██╗    ██╔══╝      ██║╚██╔╝██║       ╚██╗ ██╔╝    ██║    ██║╚██╗██║    ██║  ██║    ██║   ██║
██████╔╝    ███████╗    ██║ ╚═╝ ██║███████╗╚████╔╝     ██║    ██║ ╚████║    ██████╔╝    ╚██████╔╝
╚═════╝     ╚══════╝    ╚═╝     ╚═╝╚══════╝ ╚═══╝      ╚═╝    ╚═╝  ╚═══╝    ╚═════╝      ╚═════╝

''', 'green'))
sleep(1)
print(colored('''
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗    ██████╗ ██╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝   ██████╔╝ ╚████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗   ██╔═══╝   ╚██╔╝
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║██╗██║        ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝

''', 'green'))
console = Console()
tasks = [f"task {n}" for n in range(1, 7)]
with console.status("Loading....") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
r = 0
while r != 5:
    os.system("cls")
    os.system("clear")
    print(colored('''

          ________  _________  __
        /_  __/ / / / ____/ |/ /
          / / / /_/ / / __ |   /
        / / / __  / /_/ //   |
        /_/ /_/ /_/\____//_/|_|


        ''', 'blue'))
    print(colored('Criado por Thugueda,\Git-hub -> Thu-Gueda', 'blue', 'on_white'))
    s = (input('site:  '))
    portas = [21, 23, 80, 443, 8080, 5555, 22, 3434, 5454, 5334,
                53, 3333, 66, 1080, 3306, 445, 135, 3303, 26, 502, 8443, 9585, ]
    print(colored('RESULTADO DO SITE {}'.format(s), 'blue'))
    for porta in portas:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.4)
            codigo = cliente.connect_ex((s, porta))
            if codigo == 0:
                print(porta, "OPEN")
    j = input('aperte *Enter* para fazer outro Scanner........')
