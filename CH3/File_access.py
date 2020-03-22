
class File:
    def __init__(self, filepath):
        self.path = filepath

    def read(self):
        print("Opening file for Reading...")
        f = open(self.path, "r+")
        all_data = f.read()
        f.seek(0)
        all_lines = f.readlines()
        f.seek(0)
        b_r = f.read(20)
        f.seek(0)
        line_read = f.readline()
        if f.closed == False:
            print("Closing file...")
            f.close()

        print(f"All data: {all_data}")
        print("---------------------------------\n")
        print("Lines:")
        for l,line in enumerate(all_lines):
            print(f"#: {l} : {line}")
        print("---------------------------------\n")
        b_l = str(len(b_r))
        print(f"Buffered: {b_l} - {b_r}")
        print("---------------------------------\n")
        print(f"Line read: {line_read}")
        print("---------------------------------\n")

yo = File('/Users/ninja/Documents/HOPTWP/CH3/hello.txt')                # specify exact path to file
yo.read()                   # invoke read() method so it can read the file