from pdfminer.high_level import extract_text
import re
import PyPDF2

# 入力フォーム付きのPDFファイルを開く
input_pdf_path = "契約書（入力フォーム有）.pdf"
output_pdf_path = "ドラフトoutput_filled.pdf"

# PDFリーダーオブジェクトを作成
pdf_reader = PyPDF2.PdfReader(input_pdf_path)
pdf_writer = PyPDF2.PdfWriter()


pdf_path = "pdf_data/（目標）謄本抽出データ.pdf"

text = extract_text(pdf_path)


# cleaned_text = re.sub(r"[┏━┃┠─┴┨┏┓│├┯┗┷┬┼┛　 ]", "", text)

# Extract required data
data = {
    "Textbox1": re.search(r"表題部（一棟の建物の表示）所在([^\n]+)", text).group(1).strip(),
    "Textbox2": re.search(r"表題部（一棟の建物の表示）建物の名称([^\n]+)", text).group(1).strip(),
    "Textbox3": re.search(r"表題部（一棟の建物の表示）構造([^\n]+)", text).group(1).strip(),
    "Textbox4": re.search(r"表題部（一棟の建物の表示）床面積([^\n]+)", text).group(1).strip(),
    "Textbox5": re.search(r"表題部（専有部分の建物の表示）家屋番号([^\n]+)", text).group(1).strip(),
    "Textbox6": re.search(r"表題部（専有部分の建物の表示）建物の名称([^\n]+)", text).group(1).strip(),
    "Textbox7": re.search(r"表題部（専有部分の建物の表示）①種類([^\n]+)", text).group(1).strip(),
    "Textbox8": re.search(r"表題部（専有部分の建物の表示）②構造([^\n]+)", text).group(1).strip(),
    "Textbox9": re.search(r"表題部（専有部分の建物の表示）床面積_階数([^\n]+)", text).group(1).strip(),
    "Textbox10": re.search(r"表題部（専有部分の建物の表示）床面積_面積([^\n]+)", text).group(1).strip(),
    "Textbox11": re.search(r"表題部（敷地権の目的である土地の表示）所在([^\n]+)", text).group(1).strip(),
    "Textbox12": re.search(r"表題部（敷地権の目的である土地の表示）地番([^\n]+)", text).group(1).strip(),
    "Textbox13": "",
    "Textbox14": re.search(r"表題部（敷地権の目的である土地の表示）地目([^\n]+)", text).group(1).strip(),
    "Textbox15": re.search(r"表題部（敷地権の目的である土地の表示）地積([^\n]+)", text).group(1).strip(),
    "Textbox16": re.search(r"表題部（敷地権の目的である土地の表示）敷地権の種類([^\n]+)", text)
    .group(1)
    .strip(),
    "Textbox17": re.search(r"表題部（敷地権の目的である土地の表示）敷地権の割合([^\n]+)", text)
    .group(1)
    .strip(),
    "Textbox18": re.search(r"表題部（敷地権の目的である土地の表示）筆数([^\n]+)", text).group(1).strip(),
    "Textbox19": re.search(r"表題部（敷地権の目的である土地の表示）地積([^\n]+)", text).group(1).strip(),
    "Textbox20": "",
}

# 各ページをPDFライターに追加
for page in pdf_reader.pages:
    pdf_writer.add_page(page)

# フォームデータを埋め込む
pdf_writer.update_page_form_field_values(pdf_writer.pages[0], data)

# 出力PDFファイルを保存
with open(output_pdf_path, "wb") as output_file:
    pdf_writer.write(output_file)

print("PDFフォームへの書き込みが完了しました！")
# Output the extracted data
# for key, value in data.items():
#     print(f"{key}: {value}")
