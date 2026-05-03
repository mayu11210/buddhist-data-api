#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
地名 seed データ（横断索引化 Tier 3-6）

性霊集向け `_tmp_extract_places.py`（gitignored・list 型 112 篇用）と
dict 型向け `extract_places_dict.py`（git 追跡）が共有する seed dictionary。

PLACES の各エントリ：
  canonical : 代表表記
  aliases   : 別表記
  subcategory : temple_china/japan / mountain_china/japan/buddhist /
                country_china / dynasty / country_western_region /
                country_india / capital_china/japan / province_japan /
                mythological / cosmological_realm / sacred_site_indian
  definition : 簡潔な地名紹介
  is_single_kanji : 1 文字王朝/国名（殷・周・夏 等）の場合 True
"""

import re

RE_KANJI = re.compile(r'[一-鿿]')


def is_safe_single_char(text: str, p: int, ch: str) -> bool:
    before = text[p - 1] if p > 0 else ''
    after = text[p + 1] if p + 1 < len(text) else ''
    return not (RE_KANJI.match(before) or RE_KANJI.match(after))


# 1 文字王朝/国名の文脈判定用辞書
DYNASTY_OK_AFTER = set('のがをにて、。」』のはも王代朝末初年人室都'
                       '紂湯文武穆桓寒幽厲懿恵成宣景平荘哀恵昭幽商'
                       'ニンクェの')
# 1 文字王朝/国名の許容直前文字
DYNASTY_OK_BEFORE = set('・「『（、。 \n\t　')

# 1 文字王朝/国名の活用語尾による除外
# 「越え/越ゆ/越し/越す/越さ」（動詞）、「斉しく/斉（ひと」（形容詞）等
DYNASTY_REJECT_AFTER = {
    '越': set('えゆしすさ'),
    '斉': set('しひ'),
}


def is_dynasty_context(text: str, p: int, surface: str) -> bool:
    """1 文字王朝名の文脈ホワイトリスト判定。
    DYNASTY_REJECT_AFTER の該当直後文字（動詞・形容詞活用）は除外。
    """
    before = text[p - 1] if p > 0 else ''
    after = text[p + 1] if p + 1 < len(text) else ''
    # 前が漢字なら除外（複合語の途中に紛れる「殷」など）
    if before and RE_KANJI.match(before):
        return False
    # 動詞・形容詞活用語尾による除外
    reject = DYNASTY_REJECT_AFTER.get(surface, set())
    if after in reject:
        return False
    # 後ろが漢字の場合、許容セットに含まれていなければ除外
    if after and RE_KANJI.match(after):
        if after not in DYNASTY_OK_AFTER:
            return False
    return True


def collect_match_intervals(text: str, surface: str, single_kanji: bool):
    intervals = []
    start = 0
    while True:
        p = text.find(surface, start)
        if p < 0:
            break
        if single_kanji:
            if not is_dynasty_context(text, p, surface):
                start = p + 1
                continue
        intervals.append((p, p + len(surface)))
        start = p + len(surface)
    return intervals




PLACES = [
    # === 中国仏教の寺院 ===
    {
        'canonical': '青龍寺', 'aliases': [],
        'subcategory': 'temple_china',
        'definition': '長安にあった密教の中心寺院。恵果阿闍梨の住所。',
    },
    {
        'canonical': '大興善寺', 'aliases': [],
        'subcategory': 'temple_china',
        'definition': '長安。不空三蔵の住所。密教伝来の中心。',
    },
    {
        'canonical': '大慈恩寺', 'aliases': ['慈恩寺'],
        'subcategory': 'temple_china',
        'definition': '長安。玄奘の住所。',
    },
    # === 日本の寺院 ===
    {
        'canonical': '東大寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '奈良。華厳宗大本山。',
    },
    {
        'canonical': '東寺', 'aliases': ['教王護国寺'],
        'subcategory': 'temple_japan',
        'definition': '京都。空海に下賜された真言宗根本道場。',
    },
    {
        'canonical': '西寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '京都。東寺と並立する官寺。',
    },
    {
        'canonical': '神護寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '高雄山。空海の主要拠点の一つ。',
    },
    {
        'canonical': '高雄山寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '神護寺の旧称。',
    },
    {
        'canonical': '元興寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '奈良の南都七大寺の一。',
    },
    {
        'canonical': '興福寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '奈良。法相宗大本山。',
    },
    {
        'canonical': '法隆寺', 'aliases': [],
        'subcategory': 'temple_japan',
        'definition': '奈良斑鳩。聖徳太子建立。',
    },
    # === 中国の山 ===
    {
        'canonical': '五台山', 'aliases': ['清涼山'],
        'subcategory': 'mountain_china',
        'definition': '山西省。文殊菩薩の聖地。',
    },
    {
        'canonical': '天台山', 'aliases': [],
        'subcategory': 'mountain_china',
        'definition': '浙江省。天台宗の発祥地。',
    },
    {
        'canonical': '廬山', 'aliases': ['盧山'],
        'subcategory': 'mountain_china',
        'definition': '江西省。中国の名山。',
    },
    {
        'canonical': '崑崙', 'aliases': ['崑崙山'],
        'subcategory': 'mountain_china',
        'definition': '中国西方の霊山。神仙の住所。',
    },
    # === 日本の山 ===
    {
        'canonical': '高野山', 'aliases': [],
        'subcategory': 'mountain_japan',
        'definition': '紀伊。空海開創の真言密教の根本道場。',
    },
    {
        'canonical': '比叡山', 'aliases': ['叡山', '北嶺'],
        'subcategory': 'mountain_japan',
        'definition': '近江・山城。最澄開創の天台宗根本道場。',
    },
    {
        'canonical': '吉野', 'aliases': ['吉野山'],
        'subcategory': 'mountain_japan',
        'definition': '大和。山岳信仰の聖地。',
    },
    {
        'canonical': '室生', 'aliases': ['室生山'],
        'subcategory': 'mountain_japan',
        'definition': '大和。山岳寺院の聖地。',
    },
    # === 仏教の山 ===
    {
        'canonical': '霊鷲山', 'aliases': ['霊山', '耆闍崛山', 'gṛdhrakūṭa'],
        'subcategory': 'mountain_buddhist',
        'definition': '王舎城東北の山。釈迦が法華経などを説いた地。',
    },
    {
        'canonical': '須弥山', 'aliases': ['須弥', 'sumeru', 'meru'],
        'subcategory': 'mountain_buddhist',
        'definition': '仏教世界観の中心の山。',
        'sanskrit_canonical': 'sumeru',
    },
    {
        'canonical': '雪山', 'aliases': ['ヒマーラヤ', 'himālaya'],
        'subcategory': 'mountain_buddhist',
        'definition': 'ヒマーラヤ山脈。仏典でしばしば言及される聖山。',
    },
    {
        'canonical': '香山', 'aliases': [],
        'subcategory': 'mountain_buddhist',
        'definition': '雪山の北に位置する伝説の山。',
    },
    # === 中国の王朝・国 ===
    {
        'canonical': '殷', 'aliases': ['商'], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '中国古代王朝。湯王が建国。',
    },
    {
        'canonical': '周', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '中国古代王朝。文王・武王が建国。',
    },
    {
        'canonical': '夏', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '中国伝説的な最古の王朝。禹が建国。',
    },
    {
        'canonical': '秦', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '中国王朝。始皇帝による天下統一。',
    },
    {
        'canonical': '漢', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '中国王朝。前漢・後漢。',
    },
    {
        'canonical': '隋', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '中国王朝。唐の前。',
    },
    {
        'canonical': '梁', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '南朝の王朝。',
    },
    {
        'canonical': '陳', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '南朝の王朝。',
    },
    {
        'canonical': '魏', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '三国時代の魏。曹操の国。',
    },
    {
        'canonical': '宋', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_dynasty',
        'definition': '南朝の宋（または春秋宋）。',
    },
    {
        'canonical': '北魏', 'aliases': [],
        'subcategory': 'country_dynasty',
        'definition': '南北朝時代の王朝。',
    },
    # 春秋戦国諸国
    {
        'canonical': '燕', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '春秋戦国の北方の国。',
    },
    {
        'canonical': '趙', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '戦国七雄の一。',
    },
    {
        'canonical': '斉', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '春秋戦国の東方の大国。',
    },
    {
        'canonical': '魯', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '春秋の国。孔子の出身地。',
    },
    {
        'canonical': '楚', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '春秋戦国の南方の大国。',
    },
    {
        'canonical': '韓', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '戦国七雄の一。',
    },
    {
        'canonical': '呉', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '春秋の国。三国時代の呉も。',
    },
    {
        'canonical': '越', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '春秋の国。',
    },
    {
        'canonical': '蜀', 'aliases': [], 'is_single_kanji': True,
        'subcategory': 'country_china',
        'definition': '三国時代の蜀。または春秋蜀。',
    },
    # === 西域諸国 ===
    {
        'canonical': '于闐', 'aliases': [],
        'subcategory': 'country_western_region',
        'definition': '西域の王国。コータン。',
    },
    {
        'canonical': '亀茲', 'aliases': [],
        'subcategory': 'country_western_region',
        'definition': '西域の王国。クチャ。',
    },
    {
        'canonical': '高昌', 'aliases': [],
        'subcategory': 'country_western_region',
        'definition': '西域の王国。トルファン。',
    },
    {
        'canonical': '吐蕃', 'aliases': [],
        'subcategory': 'country_western_region',
        'definition': '古代チベット王国。',
    },
    {
        'canonical': '波斯', 'aliases': [],
        'subcategory': 'country_western_region',
        'definition': 'ペルシア。',
    },
    {
        'canonical': '西域', 'aliases': [],
        'subcategory': 'country_western_region',
        'definition': '中国西方諸国の総称。',
    },
    # === インド系 ===
    {
        'canonical': '天竺', 'aliases': ['印度', '身毒'],
        'subcategory': 'country_india',
        'definition': 'インドの古称。',
    },
    {
        'canonical': '南天竺', 'aliases': [],
        'subcategory': 'country_india',
        'definition': '南インド。',
    },
    {
        'canonical': '中天竺', 'aliases': [],
        'subcategory': 'country_india',
        'definition': '中インド。',
    },
    {
        'canonical': '震旦', 'aliases': ['支那', '神州', '唐土', '中華', '華夏'],
        'subcategory': 'country_china',
        'definition': '中国の異称。',
    },
    # === 中国の都城 ===
    {
        'canonical': '長安', 'aliases': [],
        'subcategory': 'capital_china',
        'definition': '唐の都。陝西省西安。',
    },
    {
        'canonical': '洛陽', 'aliases': [],
        'subcategory': 'capital_china',
        'definition': '中国古都。漢魏隋唐の副都。',
    },
    # === 日本の都城・地域 ===
    {
        'canonical': '平安', 'aliases': ['平安京'],
        'subcategory': 'capital_japan',
        'definition': '平安京。京都。',
    },
    {
        'canonical': '平城', 'aliases': ['平城京'],
        'subcategory': 'capital_japan',
        'definition': '平城京。奈良。',
    },
    {
        'canonical': '奈良', 'aliases': [],
        'subcategory': 'capital_japan',
        'definition': '奈良の都。',
    },
    {
        'canonical': '南都', 'aliases': [],
        'subcategory': 'capital_japan',
        'definition': '奈良。北嶺（比叡山）に対する呼称。',
    },
    {
        'canonical': '日本', 'aliases': ['日域', '本朝', '我朝', '皇朝', '神国'],
        'subcategory': 'country_japan',
        'definition': '日本国。',
    },
    # === 日本の旧国 ===
    {
        'canonical': '大和', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '奈良県。',
    },
    {
        'canonical': '山城', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '京都南部の旧国。',
    },
    {
        'canonical': '河内', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '大阪府東部の旧国。',
    },
    {
        'canonical': '摂津', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '大阪府北中部・兵庫県の旧国。',
    },
    {
        'canonical': '近江', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '滋賀県の旧国。',
    },
    {
        'canonical': '伊勢', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '三重県の旧国。',
    },
    {
        'canonical': '紀伊', 'aliases': ['紀州'],
        'subcategory': 'province_japan',
        'definition': '和歌山県・三重県南部の旧国。',
    },
    {
        'canonical': '伊予', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '愛媛県の旧国。',
    },
    {
        'canonical': '阿波', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '徳島県の旧国。',
    },
    {
        'canonical': '讃岐', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '香川県の旧国。空海生地。',
    },
    {
        'canonical': '土佐', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '高知県の旧国。',
    },
    {
        'canonical': '播磨', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '兵庫県南西部の旧国。',
    },
    {
        'canonical': '陸奥', 'aliases': [],
        'subcategory': 'province_japan',
        'definition': '東北地方の旧国。',
    },
    # === 神泉苑 ===
    {
        'canonical': '神泉苑', 'aliases': [],
        'subcategory': 'sacred_site_japan',
        'definition': '平安京の禁苑。空海の祈雨儀礼の地。',
    },
    # === 神話・仙境 ===
    {
        'canonical': '蓬莱', 'aliases': ['蓬萊'],
        'subcategory': 'mythological',
        'definition': '東海の仙島。',
    },
    {
        'canonical': '方丈', 'aliases': [],
        'subcategory': 'mythological',
        'definition': '東海の仙島。蓬莱・瀛洲と並ぶ。',
    },
    {
        'canonical': '瀛洲', 'aliases': [],
        'subcategory': 'mythological',
        'definition': '東海の仙島。',
    },
    # === 河川 ===
    {
        'canonical': '黄河', 'aliases': [],
        'subcategory': 'river_china',
        'definition': '中国北部の大河。',
    },
    {
        'canonical': '長江', 'aliases': ['揚子江'],
        'subcategory': 'river_china',
        'definition': '中国南部の大河。',
    },
    {
        'canonical': '渭水', 'aliases': [],
        'subcategory': 'river_china',
        'definition': '長安付近の河川。',
    },
    # === 仏教宇宙論の界 ===
    {
        'canonical': '欲界', 'aliases': [],
        'subcategory': 'cosmological_realm',
        'definition': '三界の最下。欲望が支配する世界。',
    },
    {
        'canonical': '色界', 'aliases': [],
        'subcategory': 'cosmological_realm',
        'definition': '三界の中。色身があるが欲望のない世界。',
    },
    {
        'canonical': '無色界', 'aliases': [],
        'subcategory': 'cosmological_realm',
        'definition': '三界の最上。色身のない世界。',
    },
    {
        'canonical': '兜率', 'aliases': ['兜率天', 'tuṣita'],
        'subcategory': 'cosmological_realm',
        'definition': '欲界第四天。弥勒菩薩の住所。',
    },
    {
        'canonical': '極楽', 'aliases': [],
        'subcategory': 'cosmological_realm',
        'definition': '阿弥陀如来の西方浄土。',
    },
    {
        'canonical': '安楽', 'aliases': ['安楽国'],
        'subcategory': 'cosmological_realm',
        'definition': '極楽浄土の異称。',
    },
    # === インド仏教聖地 ===
    {
        'canonical': '祇園精舎', 'aliases': [],
        'subcategory': 'sacred_site_indian',
        'definition': '舎衛国に建立された釈迦説法の地。',
    },
    {
        'canonical': '舎衛城', 'aliases': ['舎衛国', '舎衛'],
        'subcategory': 'sacred_site_indian',
        'definition': 'コーサラ国の都。釈迦の主要説法地。',
    },
    {
        'canonical': '王舎城', 'aliases': [],
        'subcategory': 'sacred_site_indian',
        'definition': 'マガダ国の都。霊鷲山の麓。',
    },
    {
        'canonical': '迦毘羅', 'aliases': ['迦毘羅城', 'kapilavastu'],
        'subcategory': 'sacred_site_indian',
        'definition': '釈迦族の都。釈迦生誕地。',
    },
    {
        'canonical': '伽耶', 'aliases': ['ブッダガヤ'],
        'subcategory': 'sacred_site_indian',
        'definition': '釈迦成道の地。',
    },
]

SINGLE_KANJI_PLACES = {p["canonical"] for p in PLACES if p.get("is_single_kanji")}
