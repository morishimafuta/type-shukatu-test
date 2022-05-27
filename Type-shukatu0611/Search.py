def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = search_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def search_index(sorted_array, target_number):

    # ここから記述

    # 配列中のidx探索範囲をstart_idx~end_idxとして範囲を狭めていくアプローチ
    start_idx = 0
    end_idx = len(sorted_array)-1

    while end_idx - start_idx >= 0 : # start_idxとend_idxの位置が逆転したら探索終了   

        middle_idx = start_idx + ((end_idx - start_idx + 1) // 2) # 探索範囲の中央に位置するidxを取得
        middle_number = sorted_array[middle_idx]

        # 探索範囲の更新
        if middle_number > target_number:
            end_idx = middle_idx - 1

        elif middle_number < target_number:
            start_idx = middle_idx + 1

        if middle_number == target_number:
            return middle_idx

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()