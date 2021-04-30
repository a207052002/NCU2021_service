    # 你跟敵人的距離
    rang = abs(enemy_pos - my_pos)
    
    # 敵人在你的右或左的是非判斷
    enemy_on_my_right_bool = enemy_pos > my_pos
    enemy_on_my_right_bool = enemy_pos < my_pos

    # 自動算距離避免浪費 MP
    action = ""
    if(rang <= 6):
        action = action + "R" * rang

    # 搜尋 eventmap，找到有強力攻擊事件(整數 1)的位置並放入陣列
    # e.x. [1, 1, 2, 0, 0, 0, 1, 0]
    # 會產生 [0, 1, 6](在第 0, 1 跟第 6 個 index 格子裡面有強力攻擊)
    power_attack_pos = [idx for idx, position in enumerate(eventmap) if position == 1]

    # 被敵人夾在牆角想要跳離的話，必須多個 "F" 越過他
    if(my_pos <= 2):
        if(rang <= 2 and enemy_on_my_right_bool):
            action = "F" * 6

    # 極限距離的耗盡 MP 的全力攻擊
    R_mp = 10
    if(rang <= 6):
        action += "R" * rang + "A" * int((my_mp - R_mp * rang)/(20/3))