
'''
Sample Input 

4
3 2 1 3

Sample Output 

2
'''


def birthdayCakeCandles():
        
    candle_nums = int(input())
    candles = list(map(int,input().split()))
    print(candles.count(max(candles)))
        

birthdayCakeCandles()
