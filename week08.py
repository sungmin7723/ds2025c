class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='-')

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    # 2번째 원소 부터 마지막 원소 까지
    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root
        while True:
            if number < current.data:
                if current.left is None:
                    current.left = root
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = root
                    break
                current = current.right  # move
    print("BST 구성 완료")