from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random
import logging
from interpreter import TarotInterpreter


app = Flask(__name__, static_folder='static', template_folder='static/templates')
Bootstrap(app)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

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
        spread_type = request.form['spread_type']
        question_type = request.form['question_type']
        custom_question = ""
        
        # 自由記述欄が表示され、何らかの値が入力されている場合その値を取得
        if question_type == 'custom' and "question" in request.form:
            custom_question = request.form['custom_question']

        if spread_type == 'one_card':
            num_cards = 1
        elif spread_type == 'three_cards':
            num_cards = 3
        else:
            num_cards = 10
    
        selected_cards = random.sample(tarot_cards, num_cards)

        for card in selected_cards:
            card['reversed'] = random.randint(0, 1)

        # logging
        user_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')

        # device type
        if 'Mobile' in user_agent:
            device = 'Mobile'
        elif 'Tablet' in user_agent:
            device = 'Tablet'
        else:
            device = 'PC'
        logging.info(f"User with IP {user_ip}, Device: {device}, Selected {num_cards} cards")

        return render_template('result.html', cards=selected_cards, spread_type=spread_type, question_type=question_type, custom_question=custom_question)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    # pass