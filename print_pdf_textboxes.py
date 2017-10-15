import sys
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def find_textboxes_recursively(layout_obj):
    '''
    再帰的にテキストボックス(LTTextBox)を探して、テキストボックスのリストを取得する。
    '''
    # LTTextBoxを継承するオブジェクトの場合は1要素のリストを返す。
    if isinstance(layout_obj, LTTextBox):
        return [layout_obj]
    # LTContainerを継承するオブジェクトは子要素を含むので、再帰的に探す。
    if isinstance(layout_obj, LTContainer):
        boxes = []
        for child in layout_obj:
            boxes.extend(find_textboxes_recursively(child))
        return boxes
    return []

# layout Analysisのパラメーターを設定。縦書きの検出を有効にする。
laparams = LAParams(detect_vertical=True)
# 共有のリソースを管理するリソースマネージャーを作成
resource_manager = PDFResourceManager()
# ページを集めるPageAggregatorオブジェクトを作成
device = PDFPageAggregator(resource_manager, laparams=laparams)
# Interpreterオブジェクト作成
interpreter = PDFPageInterpreter(resource_manager, device)

# ファイルをバイナリ形式で開く
with open(sys.argv[1], 'rb') as f:
    # PDFPage.get_pages()にファイルオブジェクトを指定して、PDFPageオブジェクトを順に取得する。
    # 時間がかかるファイルは、キーワード引数pagenosで処理するページ番号(0始まり)のリストを指定すると良い。
    for page in PDFPage.get_pages(f):
        interpreter.process_page(page)
        layout = device.get_result()
        boxes = find_textboxes_recursively(layout)
        # y1(Y座標の位置)は上に行くほど大きくなるので、正負を反転させる。
        boxes.sort(key=lambda b: (-b.y1, b.x0))
        # 読みやすいよう区切り線を表示する。
        for box in boxes:
            print('-' * 10)
            print(box.get_text().strip())
=
