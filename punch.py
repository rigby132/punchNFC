from datetime import date, datetime
import time
import math


def read_tag():
    input("jo: ")

    # TODO: read nfc tags.
    id = 12342
    return id


def write_id(id, duration, start, end):
    today = date.today().strftime("%Y%m%d")

    line = str(id) + ", " + str(int(math.ceil(duration))) + \
        ", " + str(start) + ", " + str(end) + "\n"
    with open(today+".csv", "a") as file:
        file.write(line)


def main():
    start_times = {}
    start_durations = {}

    try:
        while(True):
            id = read_tag()

            if id in start_times:
                duration = time.monotonic() - start_durations[id]
                write_id(id, duration, start_times[id], datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"))
                del start_times[id]
                del start_durations[id]
            else:
                start_times[id] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                start_durations[id] = time.monotonic()
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
