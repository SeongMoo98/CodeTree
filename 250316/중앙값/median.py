# 홀수번째 원소를 읽을 때마다 지금까지 입력된 수들 중 중앙값을 출력하는 프로그램

# 중앙값 : 오름차순으로 정렬했을 때 가장 중앙에 위치한 값
import heapq

T = int(input())

for t in range(T):
    # 수열의 크기
    M = int(input())

    nums = list(map(int, input().split()))
    mid = nums[0]
    print(mid, end=' ')
    # 현재 Mid 값보다 작은 수들로 구성된 Max - Heap
    # 현재 Mid 값보다 큰 수들로 구성된 Min - Heap
    max_heap = []
    min_heap = []
    # 이 양 옆으로 자료구조를 놔두는 문제는 저번에도 풀었었는데..!

    for i in range(1, M):
        # Max Heap
        if mid > nums[i]:
            heapq.heappush(max_heap, -nums[i])
        # Min Heap
        elif mid < nums[i]:
            heapq.heappush(min_heap, nums[i])

        # 홀수번째 원소
        if i % 2 == 0:
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, mid)
                mid = - heapq.heappop(max_heap)
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -mid)
                mid = heapq.heappop(min_heap)
            print(mid, end=' ')
    print()


