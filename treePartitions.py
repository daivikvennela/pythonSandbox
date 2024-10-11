def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [root_label] + list(branches)
def label(tree):
    return tree[0]
    
def branches(tree):
    return tree[1:]
    
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def partition_tree(n, m):
        print(n, m)
        if n == 0:
            return tree(True)
        elif n < 0 or m == 0:
            return tree(False)
        else:
            #splits up the partions into two options 
            #the first case is where m stays the same
            """
            In this case of (6,4) there are 3 situations 3 recursive calls where M stays the same 
            (6,4)
            (2,4)
            (-2,4)
            """
            left = partition_tree(n-m, m)
            right = partition_tree(n, m-1)
            return tree(m, [left, right])


partition_tree(5,1)