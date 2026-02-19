# imports
import pandas as pd

# wiki banned requests D; have to work locally
# maybe will work through API in future
FILE_NAME = "tkrb_wiki_sword_stats.html"


#get tables
try:
    tables = pd.read_html(FILE_NAME, encoding = 'utf-8')
    print(f"successfully connected to 本丸! caught {len(tables)} tables.")
    actual_tables = tables[1:39]


    # sword category: 短->胁->打->太->大太->枪->薙->剑
    # sub category: 普->特->特满->极->极满
    STATUS = ['Base', 'Toku', 'Toku_Max', 'Kiwame', 'Kiwame_Max']
    SWORD_TYPES = ['Tantou', 'Wakizashi', 'Uchigatana', 'Tachi', 'Ootachi', 'Yari', 'Naginata', 'Tsurugi']
    updated_list = []

    for i, df in enumerate(actual_tables):
        temp_df = df.copy()
        cur_stat = STATUS[i % 5]
        cur_sword_type = SWORD_TYPES[i // 5]
        temp_df['Status(状态)'] = cur_stat
        temp_df['Type(刀种)'] = cur_sword_type
        updated_list.append(temp_df)

    all_sword_stats = pd.concat(updated_list, ignore_index = True) #join all lists
    all_sword_stats = all_sword_stats[all_sword_stats['Name'] != 'Name'] # clean up headers
    print(all_sword_stats.columns)
    all_sword_stats.to_csv("tkrb_stats_test.csv", index = False) # save
    print("data saved to tkrb_stats_test.csv")



except Exception as e:
    print(f"uh oh, there seems to be an error: {e}")

