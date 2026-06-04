import sys

def average():
    if len(sys.argv) <= 1:
        print("Please pass numbers as command-line arguments")
        return

    l = [int(e) for e in sys.argv[1:]]
    print(sum(l) / len(l))

average()





# -------------- OUTPUT ------

'''
Please pass numbers as command-line arguments
python first.py 10 20 30 40 
25.0

'''