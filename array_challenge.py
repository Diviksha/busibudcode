def ArrayChallenge(strArr):
    parent_of = {}
    children_of = {}
    nodes = set()

    for pair in strArr:
        pair = pair.strip("()")
        child, parent = map(int, pair.split(","))

        nodes.add(child)
        nodes.add(parent)

        if child in parent_of:
            return "false"
        parent_of[child] = parent

        if parent not in children_of:
            children_of[parent] = []
        children_of[parent].append(child)

        if len(children_of[parent]) > 2:
            return "false"

    roots = nodes - set(parent_of.keys())
    if len(roots) != 1:
        return "false"

    return "true"
