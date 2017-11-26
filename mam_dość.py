import os

def get_line(home, user):
    return "{0}, {1}".format(home, user)

if __name__ == '__main__':
    home = os.getenv('HOME')
    user = os.getenv('USER')
    l = get_line(home, user)
    print(l)
