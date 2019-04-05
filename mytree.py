class BSTMap :
    def __init__( self ):
        self._root = None
        self._size = 0
    def __len__( self ):
        return self._size
    def __iter__( self ):
        return _BSTMapIterator( self._root )

    def add( self, key, value ):
        node = self._bstSearch( key )
        if node is not None :
            node.value = value
            return False
        else :
            self._root = self._bstInsert(self._root, key, value )
            self._size += 1
            return True
    def _bstInsert( self, subtree, key, value ):
        if subtree is None :
            subtree = _BSTMapNode( key, value )
        elif key < subtree.key :
            subtree.left = self._bstInsert( subtree.left, key, value )
        elif key > subtree.key :
            subtree.right = self._bstInsert( subtree.right, key, value )
        return subtree

    
    def remove( self, key ):
        assert key in self, "Invalid map key."
        self._root = self._bstRemove( self._root, key )
        self._size -= 1
    def _bstRemove( self, subtree, target):
        if subtree is None :
            return subtree
        elif target < subtree.key :
            subtree.left = self._bstRemove( subtree.left, target )
            return subtree
        elif target > subtree.key :
            subtree.right = self._bstRemove( subtree.right, target )
            return subtree
        else :
            if subtree.left is None and subtree.right is None :
                return None
            elif subtree.left is None or subtree.right is None :
                if subtree.left is not None :
                    return subtree.left
                else :
                    return subtree.right
            else:
                successor = self._bstMinimum( subtree.right )
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bstRemove( subtree.right, successor.key )
                return subtree

    def _bstMinumum( self, subtree ):
        if subtree is None :\
           return None
        elif subtree.left is None :
            return subtree
        else :
            return self._bstMinimum( subtree.left )

class _BSTMapNode :
    def __init__( self, key, value ):
                self.key = key
                self.value = value
                self.left = None
                self.right = None
