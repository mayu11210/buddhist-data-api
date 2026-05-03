#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人名 seed データ（横断索引化 Tier 3-5）

性霊集向け `_tmp_extract_persons.py`（gitignored・list 型 112 篇用）と
dict 型向け `extract_persons_dict.py`（git 追跡）が共有する seed dictionary。

PERSONS の各エントリ：
  canonical : 代表表記（漢字）
  aliases   : 別表記（追号・尊称・略称・梵語名併記）
  subcategory : buddhist_master_india / buddhist_master_china /
                buddhist_master_japan / buddhist_buddha_bodhisattva /
                buddhist_deva / chinese_classical / chinese_legend /
                japanese_emperor / japanese_aristocrat
  definition : 簡潔な人物紹介
  sanskrit_canonical : index_*_sanskrit.json への canonical リンク（任意）
  is_single_kanji : 1 文字人名（堯・舜・禹 等）の場合 True

cross_index_spec.md §11 Tier 3-5 / §17 G2-D dict 型展開の基盤データ。
"""

import re

# 1 文字人名の前後境界条件（漢字非継続性）
RE_KANJI = re.compile(r'[一-鿿]')


def is_safe_single_char(text: str, p: int, ch: str) -> bool:
    """1 文字人名 ch が text[p] で出現する際、前後が非漢字なら True。
    境界（先頭末尾）も非漢字扱い。
    """
    before = text[p - 1] if p > 0 else ''
    after = text[p + 1] if p + 1 < len(text) else ''
    return not (RE_KANJI.match(before) or RE_KANJI.match(after))


def collect_match_intervals(text: str, surface: str, single_kanji: bool):
    """text 中の surface の出現位置を全列挙。
    single_kanji=True の場合、前後が漢字でない位置のみを返す。
    return: list of (start, end) tuples
    """
    intervals = []
    start = 0
    while True:
        p = text.find(surface, start)
        if p < 0:
            break
        if single_kanji:
            if not is_safe_single_char(text, p, surface):
                start = p + 1
                continue
        intervals.append((p, p + len(surface)))
        start = p + len(surface)
    return intervals


PERSONS = [
    # === 仏教祖師（インド）===
    {
        'canonical': '釈迦', 'aliases': ['釈尊', '釈迦牟尼', '能仁', 'śākyamuni', 'Śākyamuni'],
        'subcategory': 'buddhist_master_india',
        'definition': '仏教の開祖。Śākyamuni。釈迦族の聖者。',
        'sanskrit_canonical': 'śākyamuni',
    },
    {
        'canonical': '迦葉', 'aliases': ['摩訶迦葉', 'kāśyapa', 'Kāśyapa'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子の筆頭。頭陀第一。',
        'sanskrit_canonical': 'kāśyapa',
    },
    {
        'canonical': '阿難', 'aliases': ['阿難陀', 'ānanda', 'Ānanda'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。多聞第一。',
        'sanskrit_canonical': 'ānanda',
    },
    {
        'canonical': '舎利弗', 'aliases': ['舎利子', 'śāriputra', 'Śāriputra'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。智慧第一。',
        'sanskrit_canonical': 'śāriputra',
    },
    {
        'canonical': '目連', 'aliases': ['目犍連', '摩訶目犍連', 'maudgalyāyana'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。神通第一。',
        'sanskrit_canonical': 'maudgalyāyana',
    },
    {
        'canonical': '須菩提', 'aliases': ['subhūti', 'Subhūti'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。解空第一。',
    },
    {
        'canonical': '富楼那', 'aliases': ['pūrṇa', 'Pūrṇa'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。説法第一。',
    },
    {
        'canonical': '優波離', 'aliases': ['upāli', 'Upāli'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。持律第一。',
    },
    {
        'canonical': '羅睺羅', 'aliases': ['rāhula', 'Rāhula'],
        'subcategory': 'buddhist_master_india',
        'definition': '釈迦十大弟子。釈迦の実子。密行第一。',
    },
    {
        'canonical': '龍樹', 'aliases': ['龍猛', 'nāgārjuna', 'Nāgārjuna'],
        'subcategory': 'buddhist_master_india',
        'definition': '中観派の祖。空海から見て付法第三祖（龍猛）。',
        'sanskrit_canonical': 'nāgārjuna',
    },
    {
        'canonical': '龍智', 'aliases': ['nāgabodhi', 'Nāgabodhi'],
        'subcategory': 'buddhist_master_india',
        'definition': '密教付法第四祖。龍樹の弟子。',
    },
    {
        'canonical': '達磨', 'aliases': ['菩提達磨', 'bodhidharma', 'Bodhidharma'],
        'subcategory': 'buddhist_master_china',
        'definition': '中国禅宗の初祖。インドより渡来。',
    },
    {
        'canonical': '慧可', 'aliases': [],
        'subcategory': 'buddhist_master_china',
        'definition': '禅宗第二祖。達磨の法嗣。',
    },
    # === 仏教祖師（中国）===
    {
        'canonical': '不空', 'aliases': ['不空三蔵', '大弁正三蔵', 'amoghavajra', 'Amoghavajra'],
        'subcategory': 'buddhist_master_china',
        'definition': '密教付法第六祖。唐代の訳経僧。恵果の師。',
        'sanskrit_canonical': 'amoghavajra',
    },
    {
        'canonical': '善無畏', 'aliases': ['śubhakarasiṃha', 'Śubhakarasiṃha'],
        'subcategory': 'buddhist_master_china',
        'definition': '中国密教の主要伝来者。胎蔵界の伝持。',
    },
    {
        'canonical': '金剛智', 'aliases': ['vajrabodhi', 'Vajrabodhi'],
        'subcategory': 'buddhist_master_china',
        'definition': '密教付法第五祖。金剛界の伝持。',
        'sanskrit_canonical': 'vajrabodhi',
    },
    {
        'canonical': '恵果', 'aliases': ['恵果阿闍梨', '恵果和尚'],
        'subcategory': 'buddhist_master_china',
        'definition': '密教付法第七祖。空海の師。青龍寺の大徳。',
    },
    {
        'canonical': '玄奘', 'aliases': ['三蔵法師', '玄奘三蔵'],
        'subcategory': 'buddhist_master_china',
        'definition': '唐代の訳経僧。西天取経の主役。',
    },
    {
        'canonical': '法蔵', 'aliases': [],
        'subcategory': 'buddhist_master_china',
        'definition': '華厳宗第三祖。賢首大師。',
    },
    {
        'canonical': '智顗', 'aliases': ['天台大師', '智者大師'],
        'subcategory': 'buddhist_master_china',
        'definition': '天台宗の実質的開祖。',
    },
    {
        'canonical': '澄観', 'aliases': ['清涼大師'],
        'subcategory': 'buddhist_master_china',
        'definition': '華厳宗第四祖。清涼山に住す。',
    },
    {
        'canonical': '湛然', 'aliases': [],
        'subcategory': 'buddhist_master_china',
        'definition': '天台宗中興の祖。妙楽大師。',
    },
    {
        'canonical': '善導', 'aliases': [],
        'subcategory': 'buddhist_master_china',
        'definition': '浄土教の大成者。',
    },
    {
        'canonical': '吉蔵', 'aliases': [],
        'subcategory': 'buddhist_master_china',
        'definition': '三論宗の大成者。嘉祥大師。',
    },
    {
        'canonical': '道宣', 'aliases': [],
        'subcategory': 'buddhist_master_china',
        'definition': '律宗南山律の祖。',
    },
    # === 仏教祖師（日本）===
    {
        'canonical': '空海', 'aliases': ['弘法大師', '遍照金剛', '大遍照金剛'],
        'subcategory': 'buddhist_master_japan',
        'definition': '真言宗開祖。性霊集の主たる撰者。',
    },
    {
        'canonical': '最澄', 'aliases': ['伝教大師'],
        'subcategory': 'buddhist_master_japan',
        'definition': '日本天台宗開祖。比叡山。',
    },
    {
        'canonical': '真済', 'aliases': [],
        'subcategory': 'buddhist_master_japan',
        'definition': '空海十大弟子。性霊集の編者。',
    },
    {
        'canonical': '徳一', 'aliases': [],
        'subcategory': 'buddhist_master_japan',
        'definition': '法相宗の僧。空海・最澄と論争。',
    },
    {
        'canonical': '泰範', 'aliases': [],
        'subcategory': 'buddhist_master_japan',
        'definition': '空海十大弟子。最澄門下より転派。',
    },
    {
        'canonical': '実恵', 'aliases': ['檜尾僧都'],
        'subcategory': 'buddhist_master_japan',
        'definition': '空海十大弟子。東寺第二長者。',
    },
    {
        'canonical': '智泉', 'aliases': [],
        'subcategory': 'buddhist_master_japan',
        'definition': '空海十大弟子。',
    },
    {
        'canonical': '杲隣', 'aliases': ['杲鄰'],
        'subcategory': 'buddhist_master_japan',
        'definition': '空海十大弟子。',
    },
    {
        'canonical': '勤操', 'aliases': [],
        'subcategory': 'buddhist_master_japan',
        'definition': '三論宗・元興寺の僧。空海得度の師ともされる。',
    },
    {
        'canonical': '聖徳太子', 'aliases': [],
        'subcategory': 'buddhist_master_japan',
        'definition': '飛鳥時代の皇族・仏教興隆の祖。',
    },
    {
        'canonical': '鑑真', 'aliases': ['鑒真'],
        'subcategory': 'buddhist_master_japan',
        'definition': '唐より渡来の律僧。日本律宗の祖。',
    },
    # === 仏菩薩・諸尊 ===
    {
        'canonical': '大日如来', 'aliases': ['大日', '毘盧遮那', '盧遮那', 'mahāvairocana', 'Mahāvairocana', 'vairocana', 'Vairocana'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '密教の本尊。法身仏。',
        'sanskrit_canonical': 'vairocana',
    },
    {
        'canonical': '阿弥陀', 'aliases': ['阿弥陀如来', 'amitābha', 'Amitābha', 'amitāyus'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '西方極楽浄土の教主。',
        'sanskrit_canonical': 'amitābha',
    },
    {
        'canonical': '薬師', 'aliases': ['薬師如来', 'bhaiṣajyaguru'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '東方瑠璃光浄土の教主。医王。',
    },
    {
        'canonical': '弥勒', 'aliases': ['弥勒菩薩', '慈氏', 'maitreya', 'Maitreya'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '未来仏。兜率天で待機。',
    },
    {
        'canonical': '観音', 'aliases': ['観世音', '観自在', 'avalokiteśvara', 'Avalokiteśvara'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '慈悲を司る菩薩。',
        'sanskrit_canonical': 'avalokiteśvara',
    },
    {
        'canonical': '文殊', 'aliases': ['文殊師利', 'mañjuśrī', 'Mañjuśrī'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '智慧を司る菩薩。',
        'sanskrit_canonical': 'mañjuśrī',
    },
    {
        'canonical': '普賢', 'aliases': ['samantabhadra', 'Samantabhadra'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '行を司る菩薩。',
    },
    {
        'canonical': '地蔵', 'aliases': ['地蔵菩薩', 'kṣitigarbha'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '六道衆生を救済する菩薩。',
    },
    {
        'canonical': '虚空蔵', 'aliases': ['虚空蔵菩薩', 'ākāśagarbha'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '智慧と福徳を司る菩薩。',
    },
    {
        'canonical': '不動', 'aliases': ['不動明王', 'acala', 'acalanātha'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '五大明王の主尊。',
    },
    {
        'canonical': '勢至', 'aliases': ['勢至菩薩', 'mahāsthāmaprāpta'],
        'subcategory': 'buddhist_buddha_bodhisattva',
        'definition': '阿弥陀三尊の右脇侍。',
    },
    # === 諸天・天部 ===
    {
        'canonical': '梵天', 'aliases': ['brahmā', 'Brahmā'],
        'subcategory': 'buddhist_deva',
        'definition': '色界初禅天の主。',
        'sanskrit_canonical': 'brahmā',
    },
    {
        'canonical': '帝釈天', 'aliases': ['帝釈', 'śakra', 'indra'],
        'subcategory': 'buddhist_deva',
        'definition': '忉利天の主。仏法守護神。',
    },
    {
        'canonical': '夜叉', 'aliases': ['yakṣa'],
        'subcategory': 'buddhist_deva',
        'definition': '八部衆の一。',
    },
    {
        'canonical': '羅刹', 'aliases': ['rākṣasa'],
        'subcategory': 'buddhist_deva',
        'definition': '悪鬼神。',
    },
    {
        'canonical': '阿修羅', 'aliases': ['asura'],
        'subcategory': 'buddhist_deva',
        'definition': '六道の一・阿修羅道の住人。八部衆。',
    },
    {
        'canonical': '迦楼羅', 'aliases': ['garuḍa'],
        'subcategory': 'buddhist_deva',
        'definition': '八部衆。金翅鳥。',
    },
    {
        'canonical': '緊那羅', 'aliases': ['kiṃnara', 'kinnara'],
        'subcategory': 'buddhist_deva',
        'definition': '八部衆。歌神。',
    },
    # === 諸子百家・古典文人 ===
    {
        'canonical': '荘子', 'aliases': ['荘周'],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代の道家。『荘子』の著者。',
    },
    {
        'canonical': '老子', 'aliases': ['李耳'],
        'subcategory': 'chinese_classical',
        'definition': '道家の祖。『老子（道徳経）』の著者と伝承される。',
    },
    {
        'canonical': '孔子', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '儒家の祖。春秋時代魯国。',
    },
    {
        'canonical': '孟子', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代の儒家。性善説。',
    },
    {
        'canonical': '荀子', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代の儒家。性悪説。',
    },
    {
        'canonical': '韓非', 'aliases': ['韓非子'],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代の法家。',
    },
    {
        'canonical': '列子', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代の道家。『列子』の伝承的著者。',
    },
    {
        'canonical': '揚雄', 'aliases': ['楊雄'],
        'subcategory': 'chinese_classical',
        'definition': '前漢末の文人・思想家。『太玄経』『法言』。',
    },
    {
        'canonical': '宋玉', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代楚の文人。屈原の弟子と伝承。',
    },
    {
        'canonical': '屈原', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '戦国時代楚の詩人。『離騒』作者。',
    },
    {
        'canonical': '司馬遷', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '前漢の史官。『史記』の著者。',
    },
    {
        'canonical': '司馬相如', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '前漢の文人。賦の名手。',
    },
    {
        'canonical': '陶淵明', 'aliases': ['陶潜'],
        'subcategory': 'chinese_classical',
        'definition': '東晋の隠逸詩人。',
    },
    {
        'canonical': '王羲之', 'aliases': ['王逸少'],
        'subcategory': 'chinese_classical',
        'definition': '東晋の書家。書聖。',
    },
    {
        'canonical': '張旭', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '唐代の草書家。草聖。',
    },
    {
        'canonical': '懐素', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '唐代の草書家。',
    },
    {
        'canonical': '郭璞', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '東晋の文人・卜筮家。『遊仙詩』。',
    },
    {
        'canonical': '阮籍', 'aliases': [],
        'subcategory': 'chinese_classical',
        'definition': '魏晋の竹林七賢。',
    },
    {
        'canonical': '嵆康', 'aliases': ['稽康'],
        'subcategory': 'chinese_classical',
        'definition': '魏晋の竹林七賢。',
    },
    # === 神話・伝説人物 ===
    {
        'canonical': '黄帝', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '三皇五帝の一。中華文明の祖と伝承される。',
    },
    {
        'canonical': '堯', 'aliases': ['尭', '帝堯'], 'is_single_kanji': True,
        'subcategory': 'chinese_legend',
        'definition': '五帝の一。聖王の代表。',
    },
    {
        'canonical': '舜', 'aliases': ['帝舜'], 'is_single_kanji': True,
        'subcategory': 'chinese_legend',
        'definition': '五帝の一。聖王の代表。',
    },
    {
        'canonical': '禹', 'aliases': ['夏禹'], 'is_single_kanji': True,
        'subcategory': 'chinese_legend',
        'definition': '夏の始祖。治水の聖王。',
    },
    {
        'canonical': '湯王', 'aliases': ['成湯'],
        'subcategory': 'chinese_legend',
        'definition': '殷の始祖。',
    },
    {
        'canonical': '文王', 'aliases': ['周文王'],
        'subcategory': 'chinese_legend',
        'definition': '周の始祖（武王の父）。',
    },
    {
        'canonical': '武王', 'aliases': ['周武王'],
        'subcategory': 'chinese_legend',
        'definition': '周王朝建国者。',
    },
    {
        'canonical': '周公', 'aliases': ['周公旦'],
        'subcategory': 'chinese_legend',
        'definition': '周王朝の摂政。礼制の整備者。',
    },
    {
        'canonical': '太公望', 'aliases': ['呂尚', '姜尚'],
        'subcategory': 'chinese_legend',
        'definition': '周文王・武王の軍師。',
    },
    {
        'canonical': '許由', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '上古の隠者。堯の譲位を辞退。',
    },
    {
        'canonical': '巣父', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '上古の隠者。許由と並ぶ高士。',
    },
    {
        'canonical': '伯夷', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '殷末の高士。叔斉とともに首陽山で餓死。',
    },
    {
        'canonical': '叔斉', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '殷末の高士。伯夷の弟。',
    },
    {
        'canonical': '葉公', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '葉公好龍の故事の主人公。',
    },
    {
        'canonical': '伯牙', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '伯牙絶弦の故事。鍾子期と知音。',
    },
    {
        'canonical': '鍾子期', 'aliases': [],
        'subcategory': 'chinese_legend',
        'definition': '伯牙の知音。',
    },
    # === 日本の天皇 ===
    {
        'canonical': '嵯峨天皇', 'aliases': ['嵯峨帝'],
        'subcategory': 'japanese_emperor',
        'definition': '空海の主たる帰依者。',
    },
    {
        'canonical': '桓武天皇', 'aliases': ['桓武帝'],
        'subcategory': 'japanese_emperor',
        'definition': '平安遷都の天皇。空海・最澄入唐の発令者。',
    },
    {
        'canonical': '淳和天皇', 'aliases': ['淳和帝'],
        'subcategory': 'japanese_emperor',
        'definition': '嵯峨天皇の弟。空海の支援者。',
    },
    {
        'canonical': '光仁天皇', 'aliases': [],
        'subcategory': 'japanese_emperor',
        'definition': '桓武天皇の父。',
    },
    {
        'canonical': '平城天皇', 'aliases': [],
        'subcategory': 'japanese_emperor',
        'definition': '桓武天皇の長男。',
    },
    # === 日本の貴族・文人 ===
    {
        'canonical': '橘逸勢', 'aliases': [],
        'subcategory': 'japanese_aristocrat',
        'definition': '空海とともに入唐。三筆の一人。',
    },
]


SINGLE_KANJI_PERSONS = {p['canonical'] for p in PERSONS if p.get('is_single_kanji')}
