
import os

class OsDirectories():
    def __init__(self):
        self.path_parent_0 = os.getcwd
        self.file_path = os.path.realpath(__file__)
        self.pr = os.path.dirname(self.file_path)

    def Traverse(self, path, tr_all = False):
        if tr_all == False:
            files = os.listdir(path)
            for i in files:
                if os.path.isdir(os.path.join(path, i)):
                    dir = os.path.join(path, i)
                    print(f"Dir: {dir}")
                    self.Traverse(os.path.join(path, i))
                else:
                    print(os.path.join(path, i))
        else:
            for root, dirs, files in os.walk(path):
                for f in files:
                    print(f)

yo = OsDirectories()
yo.Traverse('/Users/ninja/Documents/HelloTest')