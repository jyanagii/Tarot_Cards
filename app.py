from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__, static_folder='static', template_folder='static/templates')
Bootstrap(app)

# タロットカードのデータ
tarot_cards = [
    {"name": "愚者", "meaning": "新しい始まり、無知、自由", "image": "fool"},
    {"name": "魔術師", "meaning": "創造性、自己表現、技術", "image": "magician"},
    {"name": "女教皇", "meaning": "知恵、直感、神秘", "image": "high_priestess"},
    {"name": "女帝", "meaning": "豊かさ、母性、自然", "image": "empress"},
    {"name": "皇帝", "meaning": "権威、父性、リーダーシップ", "image": "emperor"},
    {"name": "法王", "meaning": "伝統、信仰、教育", "image": "hierophant"},
    {"name": "恋人", "meaning": "愛、調和、選択", "image": "lovers"},
    {"name": "戦車", "meaning": "勝利、意志力、自己コントロール", "image": "chariot"},
    {"name": "力", "meaning": "勇気、強さ、説得力", "image": "strength"},
    {"name": "隠者", "meaning": "内省、探求、孤独", "image": "hermit"},
    {"name": "運命の輪", "meaning": "運命の変化、循環、機会", "image": "wheel_of_fortune"},
    {"name": "正義", "meaning": "公平、真実、因果応報", "image": "justice"},
    {"name": "吊るされた男", "meaning": "犠牲、受容、逆転", "image": "hanged_man"},
    {"name": "死神", "meaning": "終わり、変容、再生", "image": "death"},
    {"name": "節制", "meaning": "バランス、調和、自制", "image": "temperance"},
    {"name": "悪魔", "meaning": "誘惑、束縛、欲望", "image": "devil"},
    {"name": "塔", "meaning": "破壊、解放、衝撃", "image": "tower"},
    {"name": "星", "meaning": "希望、導き、平和", "image": "star"},
    {"name": "月", "meaning": "不安、幻想、潜在意識", "image": "moon"},
    {"name": "太陽", "meaning": "喜び、成功、活力", "image": "sun"},
    {"name": "審判", "meaning": "復活、覚醒、決断", "image": "judgement"},
    {"name": "世界", "meaning": "完成、統合、達成", "image": "world"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_cards = int(request.form['num_cards'])
        selected_cards = random.sample(tarot_cards, num_cards)
        return render_template('result.html', cards=selected_cards)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    # pass