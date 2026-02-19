
# name: row of intended character
# level: int, 1 <= level <= 99 (regular) or 199 (kiwame)
def get_actual_stats(character, level):
    actual_stats = {
        'Name': character['Name'], 
        'Status': character['Status'],
        'Type': character['Type'],
        'Survival(生存)': character['Survival(生存)'],
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
    
    for stat, coeff in STATS_FIX.items():
        base_val = float(character[stat])
        actual_stats[stat] = int(base_val * (level * coeff + 1))

    return actual_stats

