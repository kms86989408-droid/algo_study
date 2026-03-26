'''
1번. 전체 노드 개수 세기

문제

이진트리의 루트 root가 주어질 때,
트리에 있는 전체 노드 수를 반환하시오.
#     1
#    / \
#   2   3
#  /
# 4

# 정답: 4
'''

class Solution:
    def countNodes(self, root: TreeNode) -> int:  
        if root is None :
            return 0
        
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
    
        return 1 + left_count + right_count
    
    '''
    2번. 트리의 최대 깊이 구하기

문제

이진트리의 루트 root가 주어질 때,
트리의 최대 깊이를 반환하시오.

예시
#     1
#    / \
#   2   3
#  /
# 4

# 정답: 3
    '''

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 1. root가 None이면 깊이는?
        if root is None :
            return 0
        # 2. 왼쪽 깊이 구하기
        left = self.maxDepth(root.left)
        # 3. 오른쪽 깊이 구하기
        right = self.maxDepth(root.right)
        # 4. 현재 노드 포함해서 1 + 더 큰 깊이 반환
        return 1 + max(left, right)
    

'''
3번. 리프 노드 개수 세기

문제

이진트리의 루트 root가 주어질 때,
리프 노드의 개수를 반환하시오.

리프 노드 = 왼쪽 자식도 없고 오른쪽 자식도 없는 노드

예시
#     1
#    / \
#   2   3
#  /
# 4

# 리프 노드: 4, 3
# 정답: 2
'''
class Solution:
    def countLeaves(self, root: TreeNode) -> int:
        # 1. root가 None이면?
        if root is None :
            return 0
        # 2. 현재 노드가 leaf인지 확인
        #    (left도 None, right도 None)
        if root.left and root.right is None
        # 3. 왼쪽 leaf 개수
        
        # 4. 오른쪽 leaf 개수
        
        # 5. 둘을 더해서 반환
        pass