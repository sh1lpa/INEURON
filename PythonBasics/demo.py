
x = 10
def show():
    global x 
    print(x)
    x = x+1

def main():
    print(x)
    print(show())
    print(x)

if __name__ == '__main__':
    main()

