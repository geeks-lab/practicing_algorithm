 
/**
 * shiftdown(heapify)제외 하고 일단 작성
*/

void display(int* arr);
void heap_sort(int* arr);

int main() 
{
    int arr[10] = { 6, 3, 4, 5, 8, 7, 1, 9, 2 }
    printf("before the sort");
    display(arr);
    
    heap_sort(arr);
    printf("after the sort");
    display(arr);
}


void display(int* arr)
{
    int i;
    for (i = 0; i < 10; i++)
        printf("%d", arr[i]);
    puts(""); //  str 이 가리키는 주소 부터 널 종료 문자 ('\0') 에 도달할 때 까지 표준 출력에 문자를 복사하지만 마지막 널 문자는 표준 출력에 복사되지 않는다.? 
}

void heap_sort(int* arr)
{
    int len = 10;
    for (i = (len / 2)-1; i >= 0; i--) { // 여기서 i는 parentIndex(배열의 중간부터 0쪽으로 탐색) -> (배열의 크기 / 2) - 1
        shiftdown(arr, i, 10); // 부모노드에서 자식값을 비교 (배열, 부모노드, 사이즈)
    } // maxhip 구조로 변경 완료
    // 구조 변경이 완료 되었으니 맨앞(max)과 맨뒤를 스왑하며 맨 끝부터 정렬 
    // 맨앞 - arr[0], 맨뒤 - arr[len-1]    
    for (i=len-1; i > 0; i--) {
        temp = arr[0];
        arr[0] = arr[len-1];
        arr[len-1] = temp;
        // 바꿨으면 힙구조 변경 되었을 수 있으니 다시 shiftdown with the shrank size****
        shiftdown(arr, 0, i);
    }

}

