from pwn import *
import cmds
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

dot = '\033[31m.'

logo = f"""
\033[33m
                      _
                   _oo0oo_
                  o8888888o
                 88"  {dot}\033[33m  "88
                 (|  -_-  |)
                 0\   =   /0
             _____/\_____/\_____
          ."    \\\|       |//    ".
         /     \\||   :   |||//     \                 
        /   _||||||  -:-  ||||||_   \\
       |     |  \\\\\   _   ///  |     | 
       |  \__|   `\`-----`/`   |__/  |
       \    '-\__  `.....`  __/-'    /
        `     /  /----.----\  \     .`
  .-----`. .`    \__ <|> __/   `..,`-----.
(""  '<        \             /           "")
 \   \  `.      \_\ _ . ,;/_/         /   /
  `._'____`_____;  ,,.,,.'/___________'_.`
\033[0m
"""
print (f'{logo} \033[36m\t\t\t@4t0 g3t fl@g 13@nd1t\033[0m')

class Loader:
    def __init__(self, desc="Loading...", end="[\033[36m*\033[0m] - Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = [
            "\033[32m⢿\033[0m", 
            "\033[33m⣻\033[0m", 
            "\033[34m⣽\033[0m", 
            "\033[35m⣾\033[0m", 
            "\033[36m⣷\033[0m", 
            "\033[36m⣯\033[0m", 
            "\033[38m⣟\033[0m", 
            "\033[39m⡿\033[0m"
        ]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


class BanditAuto:
    def __init__(self) -> None:
        self.level = 0
        self.password = 'bandit0'
        self.host = 'bandit.labs.overthewire.org'
        self.connection()

    def connection(self):
        try:
            self.session = ssh(user='bandit%d' % self.level, host=self.host, port=2220, password=self.password)
            self.io = self.session.process('bash')
        except:
            print (f'[\033[31m!\033[0m] - Authentication failed!')
        time.sleep(0.5)
        print (f'[\033[36m*\033[0m] - Level {self.level} && password \033[36m{self.password}\033[0m')

    def execute (self, list_command):
        for command in list_command:
            with Loader('[\033[36m*\033[0m] - Sending %s\'%s\'%s to the terminal' % ('\033[93m', command.decode('utf-8'), '\033[0m')):
                self.io.sendline(command)
                self.io.recv()
                for i in range (3):
                    time.sleep(0.6)

        passwd = self.io.recvline().decode('utf-8')
        self.password = passwd.strip()
        self.level += 1
        print (f'[\033[36m*\033[0m] - The password for next level is: \033[36m{passwd}\033[0m')
        print (f'\033[36m \t\t ------ \033[0m')

    def run (self):
        print (f'[\033[36m*\033[0m] - Start solved bandit challenge from 0-10 level')
        for list_command in cmds.solutions.values():
            self.execute(list_command=list_command)
            self.connection()


if __name__ == '__main__':
    bandit = BanditAuto()
    bandit.run()







