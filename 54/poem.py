INDENTS = 4

def print_hanging_indents(poem):
    poem = poem.strip()
    lines = poem.split('\n')
    hanging = False
    for line in lines:
        line = line.strip()

        if not line:
            hanging = False
            continue

        if hanging:
            print(f"    {line}")
            continue
        
        print(line)
        hanging = True


rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

if __name__ == "__main__":
    print_hanging_indents(rosetti_unformatted)
