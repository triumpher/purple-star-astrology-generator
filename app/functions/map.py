# 代码与星曜
code_star_map = {
  'm1': '紫微',
  'm2': '天機',
  'm3': '太陽',
  'm4': '武曲',
  'm5': '天同',
  'm6': '廉貞',
  'm7': '天府',
  'm8': '太陰',
  'm9': '貪狼',
  'm10': '巨門',
  'm11': '天相',
  'm12': '天梁',
  'm13': '七殺',
  'm14': '破軍',
  'g1': '文昌',
  'g2': '文曲',
  'g3': '左輔',
  'g4': '右弼',
  'g5': '天魁',
  'g6': '天鉞',
  'g7': '祿存',
  'g8': '天馬',
  'b1': '擎羊',
  'b2': '陀羅',
  'b3': '火星',
  'b4': '鈴星',
  'b5': '地劫',
  'b6': '地空',
  'e1': '化祿',
  'e2': '化權',
  'e3': '化科',
  'e4': '化忌',
  'i1': '廟',
  'i2': '旺',
  'i3': '得',
  'i4': '利',
  'i5': '平闲',
  'i6': '不',
  'i7': '陷',
  'p1': '命宮',
  'p2': '兄弟宮',
  'p3': '夫妻宮',
  'p4': '子女宮',
  'p5': '財帛宮',
  'p6': '疾厄宮',
  'p7': '遷移宮',
  'p8': '奴僕宮',
  'p9': '官祿宮',
  'p10': '田宅宮',
  'p11': '福德宮',
  'p12': '父母宮',
  'p13': '身宮',
  'tg1': '甲',
  'tg2': '乙',
  'tg3': '丙',
  'tg4': '丁',
  'tg5': '戊',
  'tg6': '己',
  'tg7': '庚',
  'tg8': '辛',
  'tg9': '壬',
  'tg10': '癸',
  'dz1': '子',
  'dz2': '丑',
  'dz3': '寅',
  'dz4': '卯',
  'dz5': '辰',
  'dz6': '巳',
  'dz7': '午',
  'dz8': '未',
  'dz9': '申',
  'dz10': '酉',
  'dz11': '戌',
  'dz12': '亥'
}

# 星曜亮度
star_intensity_map = {
  'm1': [5,1,1,2,7,2,1,1,2,5,5,2],
  'm2': [1,7,2,2,1,5,1,7,5,2,1,5],
  'm3': [7,7,2,1,2,2,1,5,5,5,7,7],
  'm4': [2,1,5,7,1,5,2,1,5,2,1,5],
  'm5': [2,7,5,1,5,1,7,7,2,5,5,1],
  'm6': [5,2,1,5,2,7,5,1,1,5,2,7],
  'm7': [1,1,1,5,1,5,2,1,5,7,1,2],
  'm8': [1,1,5,7,5,7,7,5,5,2,2,1],
  'm9': [2,1,5,3,1,7,2,1,5,5,1,7],
  'm10': [2,2,1,1,5,5,2,7,1,1,2,2],
  'm11': [1,1,1,7,2,5,2,5,1,7,5,5],
  'm12': [1,2,1,1,2,7,1,2,7,3,2,7],
  'm13': [2,1,1,7,2,5,2,2,1,5,1,5],
  'm14': [1,2,7,2,2,5,1,1,7,7,2,5]
}

# 生年四化
year_effect_map = {
  1: ['m6','m14','m4','m3'],
  2: ['m2','m12','m1','m8'],
  3: ['m5','m2','g1','m6'],
  4: ['m8','m5','m2','m10'],
  5: ['m9','m8','g4','m2'],
  6: ['m4','m9','m12','g2'],
  7: ['m3','m4','m8','m5'],
  8: ['m10','m3','m8','g1'],
  9: ['m12','m1','g3','m4'],
  0: ['m14','m10','m8','m9']
}
