

from data_analyzation import data_analysis
from markovchain import markov
import random 
class UserInterface:
    '''
    This class implements the functionality for user interface
    '''
    def __init__(self):
        self.default_values = ['eddard stark ','lord commander ','your grace ','lord of ', 'there were ', 'your brother ','those who ', 'a girl ','the starks ', 'lord commander ', 'this time ']

    def start_ui(self):

        self.print_logo()

        print("Welcome to game of thrones text generation app! ")
        print("")

        while True:
            print("")
            try:
                user_input = int(input("Type 1 to generate text, or 0 to exit: "))
            except:
                print("Please use a valid input!")
                continue

            if user_input == 0:
                break

            elif user_input == 1:
                try:
                    default = int(input("Please select the ngram size recommended (2-5): "))
                    limit = int(input("Please select how many words would you wish to be generated recommended (12-16): "))
                    print("")
                    print("-----------------------------------------------------")
                    print("Dataset consists of 700 000 words! Loading...")
                    print("--------------------------------------------------")
                    print("")
                except ValueError:
                    "Please use a valid input!"
                
                text = data_analysis.read_from_file()
                markov.construct_markov_model(text,default,limit)
                print("-----------------------------------------------")



    def print_logo(self):
        print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣀⠀⠀⠀⠀⠙⣟⡓⠲⠶⠤⠤⠶⠒⠛⠙⢓⣲⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⣯⣉⠉⠉⠩⣭⡭⠴⠶⠶⠿⢄⠀⠀⠀⠀⠀⣀⣀⡤⠽⠿⠿⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣖⣒⠛⠉⢉⡄⢖⠒⠚⠋⣁⣤⣀⣰⣄⣀⣤⠑⠀⠀⠀⢀⣠⡤⣤⣤⠤⢤⣽⡈⠳⠦⣤⣤⣄⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⣀⣀⡤⠤⠖⠛⡽⠋⠉⣹⠏⠀⠀⠙⠲⣄⠰⠬⢭⡀⠁⠈⠁⠑⠲⠯⠑⣦⠀⠙⢄⡈⢙⡾⠷⠒⠉⢉⣉⣀⣉⡉⠛⢷⡶⠦⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣉⣽⡶⠶⠖⣾⠁⠀⠐⠛⡲⠦⠤⢴⠆⠈⠳⣄⠀⠙⠋⠉⠉⠁⠂⠀⠀⠛⢀⣠⠴⠚⣋⡀⠐⠒⠒⠲⣤⡀⠀⠉⠲⡀⠙⣯⠋
⠀⠀⠀⠀⠀⠀⠀⠈⠳⢖⡛⠉⠉⠁⡼⠀⠀⠐⣻⠶⠶⠶⣾⠁⠀⠀⢸⠀⠀⠀⠈⠙⠛⠛⠉⣩⠉⠂⠀⡠⠚⠉⣠⠶⢯⠉⡉⠓⠦⣄⡀⠀⠙⢄⡀⠀⢀⡴⠃⠀
⠀⠀⠀⢀⣀⣀⣠⡤⠴⠒⣻⠟⢛⣽⣃⣀⢀⣼⠃⠀⠀⠀⡏⠀⣀⣀⣼⠴⠒⠒⢶⠁⠀⠀⠉⠁⠀⠀⡘⠁⣠⡎⠙⠦⠚⢯⣩⠷⡖⣬⣭⠷⢦⣤⣤⡤⠞⠀⠀⠀
⠀⠀⠀⠀⠉⢓⡦⢤⣀⡼⠃⠀⢠⠏⠁⠉⣩⣇⣀⣀⣤⡞⠋⠉⠉⢸⠃⠀⠀⠀⢸⠀⠀⠀⢀⡄⠀⠀⠁⡞⠹⡙⢶⣾⣀⡄⠁⠀⠉⠀⠸⠗⢊⣏⡜⠀⠀⠀⠀⠀
⠠⣤⡤⠴⠚⠉⣰⠋⠛⠓⠒⢶⡟⠀⠀⢀⡟⠉⠀⠀⢸⡇⠀⠀⠀⣼⢀⣀⣀⣠⡿⠒⠒⠚⣿⠁⠀⠀⠀⠁⠀⠦⣀⠉⠢⢼⡤⢶⡄⡀⠀⢀⡌⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠲⠤⣼⠃⠀⠀⠀⣐⡿⠒⠶⠶⢾⠀⠀⠀⢀⣾⡥⠤⠴⣾⠛⠉⠉⠉⡏⠀⠀⠀⠀⣿⠀⠀⢀⡰⠀⠀⠀⠀⠙⠲⢄⡈⠛⠯⣼⠚⣡⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠒⢹⡏⠉⠛⠉⡟⠀⠀⠀⢀⣾⡤⠴⠖⡿⠁⠀⠀⠀⡇⠀⠀⠀⢠⣇⣤⣤⡤⢶⡷⠶⡞⠉⢀⡴⠚⠉⠉⠉⠲⡀⠈⠒⠀⠀⡹⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣀⣠⣤⣴⣧⠤⠤⠶⣾⠁⠀⠀⠀⡇⠀⠀⠀⣰⣧⠤⠤⣶⠋⠁⢠⡇⠀⠀⣀⣼⠁⣰⠋⠀⠀⠀⠀⠀⢀⠷⠶⣾⣃⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠁⠀⠀⠀⡟⠀⠀⠀⢀⡇⠀⠀⣀⣰⡷⠖⠒⣻⠏⠀⠀⠀⣿⠀⠀⠸⠗⣻⠋⢉⣼⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠐⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣀⣀⣤⡾⠛⠉⠉⢹⠏⠀⠀⠀⢹⡀⠀⠀⢀⣿⣀⣤⡤⠞⣿⢀⡞⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢸⡇⠀⠀⠀⢸⠀⠀⠀⢀⣸⣧⠴⠖⠋⠁⢸⠃⠀⣴⢿⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⣀⣀⣤⣿⠗⠛⠋⠉⢹⡇⠀⠀⠀⢀⣿⠀⡼⠁⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠰⡏⠀⠀⠀⠀⣼⣇⣤⡴⠖⢋⣽⣶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣀⣀⣤⣶⠋⠁⢸⡇⢀⡞⠁⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⣠⣿⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⡼⠁⠈⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        
        """)
