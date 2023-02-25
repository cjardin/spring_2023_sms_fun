#!/usr/bin/python3
from classes.chat_bot import ChatBot
from sys import stdin,stdout

def main():
    bot = ChatBot("local_terminal")
    print("Terminal interface ready.")

    while True:
        print("> ", end="")
        stdout.flush()
        in_msg = stdin.readline()
        if not in_msg: # Exit if we read ^D (End of File)
            print() # Send one last linefeed, as a courtesy to the user.
            break

        out_msg = bot.run(in_msg[:-1])
        bot.save()

        print(
            out_msg,
            end='' if out_msg[-1] == '\n' else '\n')
        stdout.flush()


if __name__ == '__main__': main()
