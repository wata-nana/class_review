class Customer:

    # コンストラクタ(初期化メゾット) constructor...構築者(初期の設定を構築する)
    def __init__(self, first_name, family_name, age):
        # インスタンス変数
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # C-1.フルネームを返すメゾット
    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    # C-2.年齢はすでに設定済み

    # C-3.C-5.C-6.入場料を返すメゾット
    def entry_fee(self):
        # 料金設定欄
        age_range = [
            (0, 4, 0),  # 3歳以下0円
            (4, 20, 1000),  # 3歳超20歳未満1000円
            (20, 65, 1500),  # 20歳以上65歳未満1500円
            (65, 75, 1200),  # 65歳以上75歳未満1200円
            (75, 300, 500)  # 75歳以上500円
        ]

        # 年齢判定処理
        for min, max, fee in age_range:
            if min <= self.age < max:
                return fee
        raise ValueError(f"年齢が適切ではありません。{self.age}")

    # C-4.顧客情報をcsvで返すメゾット
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    #  C-7.C-8.顧客情報を任意の形式で返すメゾット
    def information(self):
        # 基本となる構文の設定
        template = f"{self.full_name()}{{}}{self.age}{{}}{self.entry_fee()}"

        # 出力フォーマットの選択
        format = input("形式を以下から選んでください(tab,pipe):")

        # タイプ別の文章処理
        if format == "tab":
            get_info = template.format(" ", " ")
        elif format == "pipe":
            get_info = template.format("|", "|")
        else:
            get_info = print("入力が正しくありません。")

        return get_info


# 直接実行時に基本課題の回答が出力されるよう実装
if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
    michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

    print(ken.full_name())  # "Ken Tanaka" という値を出力
    print(tom.full_name())  # "Tom Ford" という値を出力
    print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
    print(michelle.full_name())

    print(ken.age)  # 15 という値を出力
    print(tom.age)  # 57 という値を出力
    print(ieyasu.age)  # 75 という値を出力
    print(michelle.age)

    print(ken.entry_fee())  # 1000 という値を出力
    print(tom.entry_fee())  # 1500 という値を出力
    print(ieyasu.entry_fee())  # 1200 という値を出力
    print(michelle.entry_fee())

    print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
    print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
    print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
    print(michelle.info_csv())

    print(michelle.information())  # 形式を選んで値を出力
