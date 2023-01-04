def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    rm = []
    tally = 0
    for index, item in enumerate(sequence):
        tally += item
        latest = round(tally / (index + 1), 2)
        rm.append(latest)
    
    return rm

if __name__ == "__main__":
    print(running_mean([1,2,3]))
