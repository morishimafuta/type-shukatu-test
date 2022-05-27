def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    low_array = [] # pivot以下の部分配列が格納される
    high_array = [] # pivotより大きい部分配列が格納される
  
    partition_idx = 0 # 検索がぶつかるところ

    # low_idxはpivot以上を検索するidx,high_idxはpivot未満を検索するidx
    high_idx = len(array)-1
    for low_idx in range(0,len(array),1): 

        if array[low_idx] >= pivot:
            tmp = array[low_idx]
            for j in range(high_idx,low_idx,-1): # 配列要素の交換
                if array[j] < pivot:
                    array[low_idx] = array[j]
                    array[j] = tmp
                    high_idx = j
                    partition_idx = low_idx
                    break

        if pivot > array[low_idx]:
            partition_idx += 1

        if partition_idx == 0:
            partition_idx = 1

            
        if low_idx == high_idx: # 配列の分割
            low_array = array[0:partition_idx]
            high_array = array[partition_idx:len(array)]     
    
    return sort(low_array) + sort(high_array) #再帰的に配列の分割・統合を行う

    # ここまで記述

if __name__ == '__main__':
    main()