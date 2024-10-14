def build_family_tree(n, relationships):
    tree = {}
    for child, parent in relationships:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    return tree

def find_ancestors(tree, person, ancestors):
    if person not in tree:
        return
    for child in tree[person]:
        ancestors.add(child)
        find_ancestors(tree, child, ancestors)

def main():
    n = int(input("Введите число элементов в генеалогическом древе: "))
    relationships = []
    for _ in range(n):
        relation = input().strip().split()
        relationships.append((relation[0], relation[1]))
    tree = build_family_tree(n, relationships)
    k = int(input("Введите число запросов: "))
    for _ in range(k):
        person1, person2 = input().strip().split()
        ancestors1 = set()
        find_ancestors(tree, person1, ancestors1)
        ancestors2 = set()
        find_ancestors(tree, person2, ancestors2)
        if person2 in ancestors1:
            print(1)
        elif person1 in ancestors2:
            print(2)
        else:
            print(0)

if __name__ == "__main__":
    main()
