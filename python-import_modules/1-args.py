from sys import argv

def print_args():
    num_args = len(argv) - 1

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''))

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_args()