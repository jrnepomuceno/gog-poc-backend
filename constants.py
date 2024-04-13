P_SPY = 'SPY'
P_FLG = 'FLG'
P_PVT = 'PVT'
P_SRG = 'SRG'
P_2LT = '2LT'
P_1LT = '1LT'
P_CPT = 'CPT'
P_MAJ = 'MAJ'
P_LTC = 'LTC'
P_COL = 'COL'
P_1SG = '1SG'
P_2SG = '2SG'
P_3SG = '3SG'
P_4SG = '4SG'
P_5SG = '5SG'

arbitration_map = {
    'SPY': ('5SG', '4SG', '3SG', '2SG', '1SG', 'COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'SPY', 'FLG'),
    '5SG': ('5SG', '4SG', '3SG', '2SG', '1SG', 'COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    '4SG': ('4SG', '3SG', '2SG', '1SG', 'COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    '3SG': ('3SG', '2SG', '1SG', 'COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    '2SG': ('2SG', '1SG', 'COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    '1SG': ('1SG', 'COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    'COL': ('COL', 'LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    'LTC': ('LTC', 'MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    'MAJ': ('MAJ', 'CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    'CPT': ('CPT', '1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    '1LT': ('1LT', '2LT', 'SRG', 'PVT', 'FLG'),
    '2LT': ('2LT', 'SRG', 'PVT', 'FLG'),
    'SRG': ('SRG', 'PVT', 'FLG'),
    'PVT': ('SPY', 'PVT', 'FLG'),
    'FLG': ('FLG')
    }