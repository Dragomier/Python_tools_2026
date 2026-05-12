import argparse
def test_argparse():
    import math
    parser = argparse.ArgumentParser()
    parser.add_argument('echo', help = "Print message you want to send to the world")
    parser.add_argument("square_root", help = "Calculates the square root of our function", type = int)
    args = parser.parse_args()
    print(args.echo)
    print(math.sqrt(args.square_root))


def write_lines(import_file, result_file, how_many_lines, write_mode):
    parser = argparse.ArgumentParser()
    parser.add_argument("import_file", help="The source file of data")
    parser.add_argument("result_file", help="The file where the results will be stored")
    parser.add_argument("how_many_lines", help="How many lines you want to print, default 10", type=int, default=10)
    parser.add_argument("-a", "--append", help="Append to existing file", action="store_const",
                        const='a', default="w", dest="append")

    args = parser.parse_args()
    with open(import_file, "r") as r_f, open(result_file, write_mode) as w_f:
        for _ in range(how_many_lines):
            w_f.write(r_f.readline())

    write_lines(args.import_file, args.result_file, args.how_many_lines, args.append)

# Exercise 1:
import os
import configparser

def existing_file(filename):
    if not os.path.isfile(os.path.join(dir_name,filename)):
        print(os.path.join(dir_name,filename))
        raise FileNotFoundError("File does not exist")
    return filename

pre_parser = argparse.ArgumentParser(add_help = False)
pre_parser.add_argument("-ac", "--alternative-config", help = "Change default config file", default = "sample_config.ini")
args_only_default_files, remaining_to_read = pre_parser.parse_known_args()

config = configparser.ConfigParser()
dir_name = os.path.dirname(__file__)
config.read(os.path.join(dir_name, args_only_default_files.alternative_config))

parser = argparse.ArgumentParser(parents=[pre_parser])

parser.add_argument("-i", "--input", default = config["default"]["input_file"], type = existing_file)
parser.add_argument("-n", "--num", default = config["default"].getint("count_lines", 2137))
parser.add_argument("-o", "--output", default = config["default"]["result_file"])

args = parser.parse_args()

print(args.input, args.num, args.output)



