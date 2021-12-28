import argparse
import configparser
import logging
from simulation import Simulation

##########################################
# CONSTANT
##########################################
ROUND_NUMBER = 50
SHEEP_NUMBER = 15
init_pos_limit = 10.0
sheep_move_dist = 0.5
wolf_move_dist = 1.0
DIR_TO_SAVE = None
WAIT = False
##########################################
# ARG PARSER
##########################################

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument('-c', '--config', type=str, help="Określa plik konfiguracyjny, w którym zapisane są wartości dla "
                                                     "init_pos_limit, sheep_move_dist i wolf_move_dist.")
parser.add_argument('-d', '--dir', type=str, help="Określa podkatalog katalogu bieżącego, w którym mają zostać zapisane"
                                                  " pliki pos.json, alive.csv oraz - opcjonalnie - chase.log.")
parser.add_argument('-l', '--log', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help="Określa poziom zdarzeń, które mają być zapisywane w dzienniku. Podanie tej opcji powoduje, że"
                         " w katalogu bieżącym lub - jeśli została podana opcja -d/--dir - w odpowiednim podkatalogu "
                         "katalogu bieżącego tworzony jest plik dziennika o nazwie chase.log, w którym rejestrowane są "
                         "zdarzenia z działania programu.")
parser.add_argument('-r', '--rounds', type=int, help="Określa liczbę tur.")
parser.add_argument('-s', '--sheep', type=int, help="Określa liczbę owiec.")
parser.add_argument('-w', '--wait', type=int, help="Określa, że po wyświetlaniu podstawowych informacji o stanie "
                                                   "symulacji na zakończenie każdej tury dalszy przebieg symulacji "
                                                   "powinien zostać zatrzymany aż do naciśnięcia przez użytkownika "
                                                   "jakiegoś klawisza. ")

# parser.add_argument('-h', '--help', help="Program przeprowadza symulację gdzie wilk goni najbliższą mu owcę."
#                                          "jeżeli owca jest w zasięgu wilka to ją zjada i staje na jej miejscu, "
#                                          "po każdej turze wszystkie owce się poruszają"
#                                          "i wilk też") TODO

args = parser.parse_args()
if args.dir:
    DIR_TO_SAVE = args.dir  # podkatalog gdzie zapisane są pliki
if args.log:
    logging.basicConfig(filename='chase.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=args.log)  # logi tylko o tej i wyższej własności są zapisywane
if args.rounds:
    ROUND_NUMBER = args.round
if args.sheep:
    SHEEP_NUMBER = args.sheep
if args.wait:
    WAIT = True

##########################################
# CONFIG PARSER
##########################################
if args.config:
    config = configparser.ConfigParser()
    CONFIG_FILE = args.config
    config.read(CONFIG_FILE)

    init_pos_limit = float(config['Terrain']['InitPosLimit'])
    sheep_move_dist = float(config['Movement']['SheepMoveDist'])
    wolf_move_dist = float(config['Movement']['WolfMoveDist'])
    if sheep_move_dist < 0 or wolf_move_dist < 0:
        raise ValueError

##########################################
# LOGGING
##########################################

##########################################
# MAIN
##########################################

# if not args.help:
wolf_and_sheep = Simulation(ROUND_NUMBER, SHEEP_NUMBER, init_pos_limit, sheep_move_dist, wolf_move_dist, WAIT,
                            DIR_TO_SAVE)

wolf_and_sheep.simulate()
