n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int,input())))

class Tree:
    def __init__(self, pos, parent=None, children=None):
        self.parent = parent
        self.pos = pos
        if children is None:
            self.children = []
        else:
            self.children = children

def get_parents_pos(tree, parents):
    if tree.parent is None:
        return parents
    parents.append(tree.parent.pos)
    return get_parents_pos(tree.parent, parents)
    

def get_possible_steps(miro, tree):
    x = tree.pos[1]
    y = tree.pos[0]
    parents = get_parents_pos(tree, [])

    up = (y+1, x)
    down = (y-1, x)
    left = (y, x-1)
    right = (y, x+1)
    directions = [up, down, left, right]

    result = []
    for dir in directions:
        if dir in parents:
            continue
        dir_x = dir[1]
        dir_y = dir[0]
        if not 0 <= dir_x < len(miro[0]):
            continue
        if not 0 <= dir_y < len(miro):
            continue
        if miro[dir_y][dir_x] == 0:
            continue
        result.append(dir)

    return result

def make_tree(miro, pos, parent):
    root = Tree(pos, parent)
    if pos == (len(miro)-1,len(miro[0])-1):
        return root
    
    children_pos = get_possible_steps(miro, root)
    
    for child_pos in children_pos:
        root.children.append(make_tree(miro, child_pos, root))
    return root

def dfs(tree, depth, depth_list): 
    current_depth = depth
    if tree.pos == (len(miro)-1,len(miro[0])-1):
        return depth_list.append(current_depth)
    for child in tree.children:
        dfs(child, current_depth+ 1, depth_list)
    
def print_tree(tree, depth=0):
    print("    " * depth + f"{tree.pos}")

    for child in tree.children:
        print_tree(child, depth + 1)

root = make_tree(miro, (0,0), None)
print_tree(root)
depth_list = []
dfs(root, 0, depth_list)
print(min(depth_list)+1)