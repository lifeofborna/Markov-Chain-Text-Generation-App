

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
                default = input("Do you wish to select default values for generating text?: yes/no: ")
                if default == "yes":
                    default_value = random.choice(self.default_values)
                    print("----------------------------------------------------------")
                    print(f"Default value has been set to '{default_value}', ngram=2 ")
                    print("----------------------------------------------------------")
                    print("")
                    text = data_analysis.read_from_file()
                    markov.construct_markov_model(text,ngram=2,start=default_value,limit=8)

                else:
                    self.create_text()
                    continue
                


    def create_text(self):
        while True:
            try:
                ngram = int(input("Please select the ngram size 1-5 (2 preferred): "))
                start = input("Please select the starting state based on the ngram size. For example: If you chose 2: 'this time' would be valid: ")
                start +=" "
                
            except ValueError:
                print("Please select a integer value! for the ngram! ")
                continue

            if ngram < 0 or ngram >5:
                print("Please select a ngram from 1-5")
                continue
            
            words = start.split()
            if len(words) != ngram:
                print("The word count of the start input should be same as ngram!")
                continue
            
            text = data_analysis.read_from_file()

            try:
                markov.construct_markov_model(text,ngram,start,8)
            except:
                print("Please try a different start input!")

            return
            

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
