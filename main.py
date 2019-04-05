from mytree import BSTMap

folder = open('words_36.txt','r')
lines=folder.readlines()

treeInst = BSTMap()
treeInst._bstRemove(1,3)
treeInst._bstMinimum( )

print(treeInst.print())
    
