from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkTextbox
from googletrans import Translator

class MainFrame:
    def __init__(self, master, *args, **kwargs):
        self.frame = CTkFrame(master, *args, **kwargs)
        self.frame.pack(side="top", fill="both", expand=True, padx=7, pady=7)

class MainLabel:
    def __init__(self, master, *args, **kwargs):
        self.label = CTkLabel(master, *args, **kwargs)

class MainButton:
    def __init__(self, master, *args, **kwargs):
        kwargs.setdefault("command", None) 
        self.button = CTkButton(master, *args, **kwargs, corner_radius=32 ,fg_color="#010973", hover_color="#0813a3")
        self.button.grid(sticky="w", padx=5, pady=5)

class MainText:
    def __init__(self, master, *args, **kwargs):
        self.text = CTkTextbox(master, *args, **kwargs, text_color="white", font=("", 34))

class MainApp:
    def __init__(self):
        self.root = CTk()
        self.root.title("Kanji Filter")

        self.frame = MainFrame(self.root)
        self.frame.frame.pack(fill="x", expand=False)

        self.frame2 = MainFrame(self.root)
        self.frame2.frame.pack()
        self.frame2.frame.rowconfigure(1, weight=1)
        self.frame2.frame.columnconfigure(0, weight=1)
        self.frame2.frame.columnconfigure(1, weight=1)


        self.button_no_filter = MainButton(self.frame.frame, text="NO FILTER", command=self.no_filter)
        self.button_no_filter.button.grid(row=0, column=0)

        self.button_jlp5_n5 = MainButton(self.frame.frame, text="JLPT N5", command=self.jlpt_n5)
        self.button_jlp5_n5.button.grid(row=0, column=1)

        self.button_jlpt_n4 = MainButton(self.frame.frame, text="JLPT N4", command=self.jlpt_n4)
        self.button_jlpt_n4.button.grid(row=0, column=2)

        self.button_jlpt_n3 = MainButton(self.frame.frame, text="JLPT N3", command=self.jlpt_n3)
        self.button_jlpt_n3.button.grid(row=0, column=3)

        self.button_translate = MainButton(self.frame.frame, text="TRANSLATE", command=self.perform_translation)
        self.button_translate.button.grid(row=0, column=4)

        self.filter_label = MainLabel(self.frame.frame, text="Current filter: None")
        self.filter_label.label.grid(row=2, column=0, columnspan=3, padx=10, pady=3, sticky="w")

        self.input_label = MainLabel(self.frame2.frame, text="Input", font=("", 18))
        self.input_label.label.grid(row=0, column=0, padx=10, pady=3, sticky="w")

        self.output_label = MainLabel(self.frame2.frame, text="Output", font=("", 18))
        self.output_label.label.grid(row=0, column=1, padx=10, pady=3, sticky="w")

        self.input_text = MainText(self.frame2.frame)
        self.input_text.text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.output_text = MainText(self.frame2.frame)
        self.output_text.text.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        self.current_filter = None
        self.original_text = ""
        self.normal_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', ',', '.', '?', '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '<', '>', '/', '\ ', '"', "'", '`', '~', '。', '、']
        self.jlpt_kana_list = ['あ', 'い', 'う', 'え', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'や', 'いい', 'ゆ', 'いぇ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'ん', 'わ'] + ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ', 'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ゼ', 'ソ', 'ゾ', 'タ', 'ダ', 'チ', 'ヂ', 'ツ', 'ヅ', 'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ', 'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'ボ', 'ポ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'イイ', 'ユ', 'イェ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ン']
        #https://jlptsensei.com/jlpt-n5-kanji-list/
        self.jlpt_n5_list = ['日', '一', '国', '人', '年', '大', '十', '二', '本', '中', '長', '出', '三', '時', '行', '見', '月', '分', '後', '前', '生', '五', '間', '上', '東', '四', '今', '金', '九', '入', '学', '高', '円', '子', '外', '八', '六', '下', '来', '気', '小', '七', '山', '話', '女', '北', '午', '百', '書', '先', '名', '川', '千', '水', '半', '男', '西', '電', '校', '語', '土', '木', '聞', '食', '車', '何', '南', '万', '毎', '白', '天', '母', '火', '右', '読', '友', '左', '休', '父', '雨']
        self.jlpt_n4_list = ['会', '同', '事', '自', '社', '発', '者', '地', '業', '方', '新', '場', '員', '立', '開', '手', '力', '問', '代', '明', '動', '京', '目', '通', '言', '理', '体', '田', '主', '題', '意', '不', '作', '用', '度', '強', '公', '持', '野', '以', '思', '家', '世', '多', '正', '安', '院', '心', '界', '教', '文', '元', '重', '近', '考', '画', '海', '売', '知', '道', '集', '別', '物', '使', '品', '計', '死', '特', '私', '始', '朝', '運', '終', '台', '広', '住', '無', '真', '有', '口', '少', '町', '料', '工', '建', '空', '急', '止', '送', '切', '転', '研', '足', '究', '楽', '起', '着', '店', '病', '質', '待', '試', '族', '銀', '早', '映', '親', '験', '英', '医', '仕', '去', '味', '写', '字', '答', '夜', '音', '注', '帰', '古', '歌', '買', '悪', '図', '週', '室', '歩', '風', '紙', '黒', '花', '春', '赤', '青', '館', '屋', '色', '走', '秋', '夏', '習', '駅', '洋', '旅', '服', '夕', '借', '曜', '飲', '肉', '貸', '堂', '鳥', '飯', '勉', '冬', '昼', '茶', '弟', '牛', '魚', '兄', '犬', '妹', '姉', '漢']
        self.jlpt_n3_list = ['政', '議', '民', '連', '対', '部', '合', '市', '内', '相', '定', '回', '選', '米', '実', '関', '決', '全', '表', '戦', '経', '最', '現', '調', '化', '当', '約', '首', '法', '性', '的', '要', '制', '治', '務', '成', '期', '取', '都', '和', '機', '平', '加', '受', '続', '進', '数', '記', '初', '指', '権', '支', '産', '点', '報', '済', '活', '原', '共', '得', '解', '交', '資', '予', '向', '際', '勝', '面', '告', '反', '判', '認', '参', '利', '組', '信', '在', '件', '側', '任', '引', '求', '所', '次', '昨', '論', '官', '増', '係', '感', '情', '投', '示', '変', '打', '直', '両', '式', '確', '果', '容', '必', '演', '歳', '争', '談', '能', '位', '置', '流', '格', '疑', '過', '局', '放', '常', '状', '球', '職', '与', '供', '役', '構', '割', '身', '費', '付', '由', '説', '難', '優', '夫', '収', '断', '石', '違', '消', '神', '番', '規', '術', '備', '宅', '害', '配', '警', '育', '席', '訪', '乗', '残', '想', '声', '助', '労', '例', '然', '限', '追', '商', '葉', '伝', '働', '形', '景', '落', '好', '退', '頭', '負', '渡', '失', '差', '末', '守', '若', '種', '美', '命', '福', '望', '非', '観', '察', '段', '横', '深', '申', '様', '財', '港', '識', '呼', '達', '良', '阪', '候', '程', '満']

    def perform_translation(self):
        translator = Translator()
        self.filter_label.label.configure(text="Translated")
        text_to_translate = self.input_text.text.get("1.0", "end-1c")
        if text_to_translate:
            translated_text = translator.translate(text_to_translate)
            self.output_text.text.delete("1.0", "end")
            self.output_text.text.insert("1.0", translated_text.text)
        else:
            self.filter_label.label.configure(text="Type something...")

    def apply_filter(self):
        current_text = self.input_text.text.get("1.0", "end-1c")
        if self.current_filter:
            lines = current_text.split("\n")
            updated_lines = []

            for line in lines:
                updated_line = ''.join(['×' if char not in self.current_filter else char for char in line])
                updated_lines.append(updated_line)

            updated_text = '\n'.join(updated_lines)
        else:
            updated_text = current_text
            
        self.output_text.text.delete("1.0", "end")
        self.output_text.text.insert("1.0", updated_text)

    def no_filter(self):
        self.filter_label.label.configure(text="Current filter: None")
        self.current_filter = None
        self.apply_filter()

    def jlpt_n5(self):
        self.filter_label.label.configure(text="Current filter: JLPT N5")
        self.current_filter = self.normal_list + self.jlpt_kana_list + self.jlpt_n5_list
        self.apply_filter()

    def jlpt_n4(self):
        self.filter_label.label.configure(text="Current filter: JLPT N4")
        self.current_filter = self.normal_list + self.jlpt_kana_list + self.jlpt_n5_list + self.jlpt_n4_list
        self.apply_filter()

    def jlpt_n3(self):
        self.filter_label.label.configure(text="Current filter: JLPT N3")
        self.current_filter = self.normal_list + self.jlpt_kana_list + self.jlpt_n5_list + self.jlpt_n4_list + self.jlpt_n3_list
        self.apply_filter()


    def run(self):
        self.root.geometry("1200x700")
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()
