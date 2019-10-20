import requests


def main():

    file1 = open("disney_links.txt", "r")

    for line in file1:
        print("This line is " + line)

if __name__ == "__main__":
    main()


