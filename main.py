import sys
import configure
from detect import detect
import show

DATA_DIRECTORY = "data"


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "config":
        if sys.argv[2] == "spots":
            configure.spots(DATA_DIRECTORY, list(map(int, sys.argv[3].split(","))))
        elif sys.argv[2] == "thresholds":
            configure.threshold(DATA_DIRECTORY, list(map(int, sys.argv[3].split(","))))
    if len(sys.argv) > 2 and sys.argv[1] == "show":
        if sys.argv[2] == "spots":
            show.spots(DATA_DIRECTORY)
        elif sys.argv[2] == "thresholds":
            show.threshold(DATA_DIRECTORY)
    else:
        detect(DATA_DIRECTORY)
