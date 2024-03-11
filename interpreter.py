import openai

class TarotInterpreter:
    def __init__(self, api_key):
        self.api_key = api_key

    def interpret_results(self, cards, question_type, custom_question=None):
        # カードの意味と質問から解釈を作成するための基本情報を組み立てます
        card_descriptions = '. '.join([f"{card['name']}のカードは{card['meaning']}を象徴しています" for card in cards])
        question_text = custom_question if question_type == 'custom' and custom_question else question_type

        # 解釈の生成に必要なプロンプトを作成します
        prompt = f"以下のタロットカードの組み合わせに基づいて、{question_text}についての解釈を生成してください: {card_descriptions}."
        
        # OpenAI APIを使用して解釈を生成します
        return self.generate_explanation(prompt)

    def generate_explanation(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",  # 適切なエンジンを選択
            prompt=prompt,
            max_tokens=150,  # 必要な応答の長さに応じて調整
            n=1,
            stop=None,
            temperature=0.7  # 創造性の度合いを調整
        )
        return response.choices[0].text.strip()

# 使用例
with open("api_key.txt", "r") as f:
    api_key = f.read().strip() # ここにOpenAIのAPIキーを設定
tarot_interpreter = TarotInterpreter(api_key)

# 選択されたカードと質問タイプを例として
selected_cards = [
    {"name": "愚者", "meaning": "新しい始まり、無知、自由"},
    # 他のカードも同様に追加可能
]
question_type = "love"
custom_question = "今後の恋愛運は？"

# 解釈を生成
interpretation = tarot_interpreter.interpret_results(selected_cards, question_type, custom_question)
print(interpretation)
