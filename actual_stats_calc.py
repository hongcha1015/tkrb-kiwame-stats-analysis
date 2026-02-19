
# name: row of intended character
# level: int, 1 <= level <= 99 (regular) or 199 (kiwame)
def get_actual_stats(character, level):
    actual_stats = {
        'Name': character['Name'], 
        'Status': character['Status'],
        'Type': character['Type'],
        'Survival(生存)': character['Survival(生存)']
    }

