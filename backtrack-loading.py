#coding=utf-8

'''
author: Abby Liu

Backtrack Algorithm

For loading problem. 
'''

import copy

i = 0
dic_list = []

def Loading(W, X, B, best):
    '''
    W: weight of every item 每項的重量列表
    X: item's permutation, 1 means load, 0 means unload 每項的排列方式
    B: c1 - current_weight 空隙（目前裝載量與最大裝載量之差距）
    best: the best weight(minimun) 最佳空隙（最小）
    '''
    global i    # use global variable i, initialize to 0 in line 5
    global dic_list     # a list to put dictionary of 'best' and 'X'

    while i < len(W):
        current_weight = 0
        for w in range(i):
            current_weight += W[w]      # Compute current total weight
        if B-W[i]>=0:       # if there's a space for i-st item, then put and compute its weight
            print("current weight: ", current_weight)
            B = B-W[i]
            print("Put X[%d], Now B is %d"%(i, B))
            X[i] = 1        # update X[i] value, 1 means put it
            print("X: ", X, end="\n\n")
            i += 1      # try to put next item
        else:       # if there's no space fo i-st item, update X[i] value, 0 means didn't put it
            print("Because %d-%d <0"%(B, W[i]))
            print("Didn\'t put X[%d], Now B is %d"%(i, B))
            X[i] = 0
            print("X: ", X, end="\n\n")
            i += 1    # try to put next item

    if B < best and sum(X)!=0 :     # if B is less than best, then we've found a feasible solution
        best = B    # update best value
        
        tmp_dic = {'best':best, 'X':X}      # create a temporary dictionary
        best_dic = copy.deepcopy(tmp_dic)   # deep copy in case of overriding

        dic_list.append(best_dic)           # append dictionary to dic_list
        print(best_dic)
        print("Find feasible solution", end="\n\n")
        i -= 1      # For backtracking, go back to upper node

    B = BackTracking(W, X, B)   # Do backtracking

    if i == 0:
        print(dic_list)
        min_best_item = min(dic_list, key=lambda x:x['best'])

        print("Find optimal solution:", min_best_item['X'], "best is", min_best_item['best'], end="\n\n")

    else:
        print("重新計算第%d個 此時B=%d\n\n"%(i,B))
        Loading(W, X, B, best)

def BackTracking(W,X,B):
    global i        # use global variable i
    print("BackTrack(%d)........"%i)
    while i>0 and X[i] == 0:
        # print("X[%d]=0"%i,end="\t")
        i -= 1
        # print("i-1=",i)
        if i <= 0:
            break
    if X[i] == 1:
        X[i] = 0
        # print("X: ", X, end=" ")
        B = B+W[i]
        # print("Now B is %d"%B, end="\n\n")
        i += 1
        # print("i+1=",i)
        return B
    return B

def main():
    '''
    W: weight of every item 每項的重量列表
    X: item's permutation, 1 means load, 0 means unload 每項的排列方式
    c1: the max weight of a ship（最大裝載量）
    B: c1 - current_weight 空隙（目前裝載量與最大裝載量之差距）
    best: the best weight(minimun) 最佳空隙（最小）
    '''
    weights = [10, 25, 30]
    xs = [0,0,0,0]
    c1 = 40
    B = c1; best = c1; 
    weights.sort()

    print("W is ",weights)
    Loading(weights, xs, B, best)

if __name__ == '__main__':
    main()