
# name: row of intended character
# level: int, 1 <= level <= 99 (regular) or 199 (kiwame)
def get_actual_stats(character, level):
    actual_stats = {
        'Name': character['Name'], 
        'Status': character['Status'],
        'Type': character['Type'],
        'Survival(生存)': character['Survival(生存)'],
        'Level': level,
    }

    STATS_FIX = {
        'Impact(打撃)': 0.04,
        'Leadership(銃率)': 0.04,
        'Mobility(機動)': 0.04,
        'Impulse(衝力)': 0.04,
        'KillingBlow(必殺)': 0.04,
        'Scouting(偵察)': 0.02,
        'Camouflage(隠蔽)': 0.02,
    }
    SWORD_TYPE_FIX = {
        'Tantou': 1,
        'Wakizashi': 1,
        'Uchigatana': 0.65,
        'Tachi': 0.85,
        'Ootachi': 1,
        'Yari': 0.6,
        'Naginata': 0.35,
        'Tsurugi': 1,
    }
    LEVEL_FIX = 0.1
    
    for stat, coeff in STATS_FIX.items():
        base_val = float(character[stat])
        if level >= 100:
            actual_stats[stat] = int(base_val * (100 * coeff + (level - 100) * coeff * LEVEL_FIX + 1))
        else:
            actual_stats[stat] = int(base_val * (level * coeff + 1))
        if 'Impact' in stat:
            actual_stats[stat] = int(actual_stats[stat] * SWORD_TYPE_FIX.get(character['Type']))
            

    return actual_stats

