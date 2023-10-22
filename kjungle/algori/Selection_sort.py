def selection_sort(arr):
    
    min_idx=0
    
    for i in range(len(arr)-1): # 정렬 기준
        min_idx = i # 첫번째 min을 0번 인덱스로 놓고 시작
        for j in range(i+1,len(arr)): # 비교 인덱스
            if arr[j] < arr[min_idx]: # 더 작은 놈이 나타나면 (min_idx랑 arr[j] 비교)
                min_idx = j # min_idx 업데이트
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # swap    
        

    print(arr)        
        
selection_sort([8,5,2,3])



