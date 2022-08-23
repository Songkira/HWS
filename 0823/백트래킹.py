# 선택을 잘못하면(답을 구하는 길이 아니면) 되돌아가서 다시 찾는 기법.
# 그래프 없음/ 하지만 그래프, 트리를 찾는 듯이 탐색하는 것.
# 그래서 만들어진 것이 상태공간 그래프, 상태공간 트리
# 조사해야될 모든 후보들을 만들어내는/탐색하는 과정을 모델링하는 것
# 너비 우선/깊이 우선 중 하나를 사용하게됨.
# 깊이 우선 탐색이 너비우선 탐색보다 탐색 성능이 일반적으로 더좋다 / 가지치기에 더 유리하기 때문
# 답을 찾을때까지 다 해보는것(완전탐색과 비슷한가?)
# 잘못 선택하면 취소하고 빨리 새로운 것을 선택.(선택을 되돌리는 것)
# 내가 한 선택(이동한 좌표)을 저장 => 어떠한 선택을 이어왔는지
# 스택에 저장할때 행과 열을 묶어서 정하고 # 행과 열의 값을 매개변수로 넘김
# 인접 정점이 선택지가 됨. 이미 지나온 길은 배제.
# 풀이할때 재귀나 스택이나 아무거나 사용해도 됨.
# 어떤 노드의 유망성 -> 상태 공간 트리
# 내가 가고 있는 선택이 맞는지 항상 의심하면서 진행.
# 틀리면 부모로 되돌아감(취소) -> 안가본 선택지로 진행
#----------------------------ㅉ--------------------
def checknode(v): # node
    if promising(v):
        if there is a solution at v:
            write th solution
        else:
            for u in each child of v:
                checknode(u)

# 4Queen => 4개의 킹을 두는 방법(서로 위협이 되지 않게) 16C4 만큼의 경우의 수 / 1820
# 1820 가지 중 조건에 맞는 것만 골라내기
# 조건
# 1.같은행에는 2개 이상의 퀸이 있으면 안됨
# 2. 퀸은 구별되진 않음. 각행마다 하나씩 둔다고 가정
# 행값을 고정시켜두면, 열 값만 변경시키면됨.

# 처음 queen은 1행 몇열에 먼저 선택 < - 이걸 결정하는 과정을 여러번 반복
# 자식이 4개인 트리(n개의 queen 만큼) # 256가지
# 어떤게 답인지 모르니 처음부터 모든케이스를 빠짐없이 완전탐색을 트리과정으로 작성<- 가상 트리
# 첫번째 과정을 진행할때 queen1: (0,0) -> queen2: (1, 0) 
# 조건이 안맞으면(일렬, 대각선 +1의 자리에 있으면 안됨) 더 아래 자식 노드를 진행하지 않고(취소) 되돌아감
# 그리고 조건이 맞으면 진행 (그림 보면 이해하기 쉬움. 손으로 그려보면서 하기)
# (답으로 가는 선택이)== 놓을때 마다 이전에 놓은 퀸들의 위치와 충돌이 일어나는지 않일어나는지 체크

# 방문한 노드가 많을 수록 하는 일이 많아지는것=> 시간이 길어짐
# 백트래킹은 경우의 수를 줄인다. 그래서 시간이 줄어듬

# v의 인접정점(자식노드)을 찾아서 재귀함수 호출?
# 트리는 유향 그래프와 비슷함. 진행하는게

# 그리디(탐욕) 알고리즘 => 난 항상 올바른 선택을 한다 가정하고 진행(난 이미 답을 알고있따)
# 한번 했던 선택은 절대로 뒤로 무르지 않음.
