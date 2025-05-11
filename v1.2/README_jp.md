# 観智院本類聚名義抄データベース

## 概要

このデータベースは、観智院本類聚名義抄（略称KRM）の全文をテキストデータベース化し、所在情報、本文校勘、出典考証などを行ったものであり、
平安時代漢字字書総合データベース（略称HDIC）を構成する漢字字書データベースのひとつである。

観智院本類聚名義抄は、十二世紀に成立した漢字の字書であり、真言宗の僧侶によって編纂された。
アクセントを示した和訓、詳細な漢字音の注記、異体字の注記を大量に収録することから、日本語史研究の
重要資料とされてきた。また、反切、意義注、字体注の漢文注記は、中国語学の資料としても注目されている。

2022年3月から公開していたが、2025年3月に、仕様の変更を行い、詳細な説明を施して改訂版を公開するものである。

このファイルのGitHubリポジトリへのリンクは次のとおりである。

[https://github.com/shikeda/HDIC/tree/master/v1.2/README_jp.md](https://github.com/shikeda/HDIC/tree/master/v1.2/README_jp.md)


## データファイル一覧

### 一覧と簡単な説明

[https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2)
で公開している観智院本類聚名義抄のデータは次のとおりである。
一部公開準備中のものを含む。

- [krm_main](#krm_main): 基本データ。掲出字、注文全文、所在などに関する情報を含む。TSVファイルとJSONファイルを公開。
- [krm_notes](#krm_notes): 注釈データ。掲出字、字体注、音注、意義注、和訓、その他に分類し、校勘と出典考証を行ったもの。TSVファイルとJSONファイルを公開。
- [krm_headword_chars](#krm_headword_chars): すべての掲出字に関する詳細情報。風間版所在、天理版所在、画像ファイル名など。公開準備中。
- [krm_wakun](#krm_wakun): 和訓データ。和訓の異形、漢字の異体字、『日本国語大辞典第二版』の表記欄との対応に関する情報を含む。TSVファイルとJSONファイルを公開。
- [krm_definitions](#krm_definitions): 注文を字体注、音注、意義注、和訓、その他に分類したもの。TSVファイルを公開。公開済みの[KRM_definitions.tsv](https://github.com/shikeda/HDIC/KRM_definitions.tsv)に同じ。
- [krm_pronunciations](#krm_pronunciations): 音注に関してDHSJRとの連携をとるためのデータ（準備中）。
- [krm_ndl](#krm_ndl): 国会図書館デジタルコレクションへのリンク。TSVファイルを公開。公開済みの[KRM_ndl.tsv](https://github.com/shikeda/HDIC/KRM_ndl.tsv)に同じ。

2025年3月に大幅な仕様変更を行った。従来の公開ファイルは、
KRMを付していたが、仕様変更後のファイルは、krmを付すことに
した。

## 仕様変更

仕様変更の要点は次のとおりである。

- 仮名和訓の無声点を示す“@”を“_”に変更
- 濁音の声点を示す“"”を半角英字“V”に変更
- 有声点を示す半角()を全角（）に変更
- 誤字の訂正案を示す半角()を全角〔〕に変更
- 脱字を示す半角[]を全角［］に変更

仕様変更後のファイルはv1.2のフォルダーに置いた。これは一時的なものである。

## ER図

krm_main、krm_notes、krm_wakunの三つのテーブルの関係を図示すれば 次のようになる。

![ER図](/images/krmer.drawio.png)

さらにkrm_notes.jsonは次に図示するような入れ子構造を持っている。

![ER_notes図](/images/krm_notes_er.drawio.png)


## 共通情報

ここに公開するデータファイルに共通する情報を記す。

### 最終更新日

初版公開日：2025年3月30日  
最終更新日：2025年5月11日

### バージョン履歴

#### krm_main 
- Version: 1.2.6 (最新)  
    初版公開日：2025年3月30日 
    最終更新日：2025年5月11日
- Version: 1.1.347  
    初版公開日：2022年3月1日 
    最終更新日：2025年3月17日

### krm_notes
- Version: 1.2.7 (最新, 仕様変更後に公開)  
    初版公開日：2025年3月28日 
    最終更新日：2025年5月11日

### krm_headword_chars
- Version: 1.2.1 (最新, 仕様変更後に公開) 
    初版公開日：2025年5月11日 
    最終更新日：2025年5月11日

### krm_wakun
- Version: 1.2.1  (最新)  
    初版公開日：2025年3月30日 
    最終更新日：2025年5月2日
- Version: 1.1.97  
    初版公開日：2024年6月11日 
    最終更新日：2025年3月17日


### 作成者および著作権情報

HDIC プロジェクト

代表者：池田　証寿（北海道大学名誉教授）

Copyright (c) 2022-2025 HDIC project, IKEDA Shoju (Chair, Professor Emeritus, Hokkaido University)

連絡先：
ikeda.shoju@gmail.com, liyuansapporo@yahoo.co.jp, toyjack@gmail.com, kleinekuma@gmail.com

### ライセンス情報

このサイトの内容はCC BY-NC-SA 4.0ライセンスのもとに提供される。

オープンアクセスデータです。

### 引用書の略称一覧

- 正宗索引: 正宗敦夫編, 類聚名義抄 仮名索引, 日本古典全集刊行会, 1939-1940
- 岡田研究: 岡田希雄, 類聚名義抄の研究, 一条書房, 1944
- 望月和訓集成: 望月郁子編, 類聚名義抄: 四種声点付和訓集成, 笠間書院, 1974
- 中村文選: 中村宗彦, 九条本文選古訓集, 風間書房, 1983
- 草川和訓集成: 草川昇編, 五本対照類聚名義抄和訓集成, 汲古書院, 2000
- 西端誤写考察: 西端幸雄, 類聚名義抄における誤写の考察, 訓点語と訓点資料45, 1971
- 西端誤写諸例: 西端幸雄, 類聚名義抄における誤写の諸例, 訓点語と訓点資料52，1973
- 略注: 佐藤喜代治，色葉字類抄略注，明治書院，1995
- 群書治要: 小林芳規・原卓志・山本秀人・山本真吾・佐々木勇編, 宮内庁書陵部蔵本群書治要経部語彙索引, 汲古書院, 1996
- 毛詩鄭箋: 毛詩鄭箋（一）（二）（三）, 古典研究会叢書漢籍之部１～３, 原本所蔵静嘉堂文庫, 汲古書院, 1992


### 謝辞

観智院本類聚名義抄の解読テキストの公開について、御許可を賜った
天理図書館ならびに八木書店に感謝申し上げる。


この研究は日本学術振興会科学研究費補助金（課題番号16H03422、 19H00526、23K17500、25K00466）の成果の一部である。記して感謝の意を表す。


## krm_main


観智院本類聚名義抄（以下、名義抄）データベースの中核となるファイルを解説する。
従来公開していたのは、KRM.tsvという名称のTSVファイルである。

掲出字、注文、巻、部首、風間書房版と天理善本叢書版の所在などに関する情報を
収録する。

2025年3月に、カラム名、声点の表示法の仕様を変更した。仕様変更後の
ファイルであることを明示するために、krm_main.tsvという名称にした。
これにはJSON形式も用意した。

新旧のカラム名を対照すれば次のようになる。


| New Column Name (v1.2.5) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| hanzi_id                 | KRID_sn                    |
| -     | KR2ID                      |
| kazama_location    | KRID                       |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| hanzi_entry              | Entry                      |
| original_entry           | Entry_original             |
| definition               | Def                        |
| -                        | Remarks                    |

KR2IDは省略し、kazama_locationをKRIDに対応させた。

Remarksは次のkrm_notesにまとめることとして、省略した。

次に、カラム名の内容を英語と日本語で説明する。

| New Column Name (v1.2.5) | English Explanation           | Japanese Explanation                    |
|--------------------------|-----------------------------|-------------------------------------------|
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F'.          | Fで始まる5桁の数値からなる見出し項目ID。     |
| hanzi_id                 | A heading Hanzi ID consisting of a 5-digit numeric ID starting with 'S'.           | Sで始まる5桁の数値からなる見出し漢字ID。         |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  | K・巻数（2桁）・風間版頁数（3桁）・行数（1桁）、段数（1桁）、字順（1桁）を示すID。字順付与のルールの詳細は別に定める。    |
| tenri_location           | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  |T・巻数（a/b/c）・天理版頁数（3桁）・行数（1桁）・段数（1桁）・字順（1桁）を示す。字順付与のルールの詳細は別に定める。     |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.            | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す。                              |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.                   | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す。       |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.           | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。            |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). | 校訂漢字は原則、康熙字典体（Unicodeの新字体（通用字体・俗字体）を含む）を用いる。Unicodeに収録されていない漢字については、以下の方法で表現する。漢字の部品の組み合わせで表現可能な場合は、IDS（漢字構成記述文字列）で入力する。特定の漢字やその部品で、IDSまたは標準Unicodeで表現が困難な場合は、CHISEおよびGlyphWikiの実体参照方式に基づいた簡略表記（例：CDP-8C55, koseki-00001）を用いる。上記のいずれの方法でも表現できない文字や、原典で判読不能な文字（虫損等）は、「■」（黒い四角）で入力する。複数漢字の見出しは「／」（全角スラッシュ）で区切る。省略符号「｜」は「ー」（長音符）で示し、全角括弧（）内に該当字を付記する。 |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used. | 原字形に準拠した見出し字。誤字はそのまま。Unicode外の漢字の表現はhanzi_entryに準じる。原字形の掲出字が不要なら「〇」。  |
| definition               | Includes glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and other relevant notes, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.    | 注文は、字体注、音注、義注、和訓、その他からなる。これらをスペース区切りで入力。原則として「康熙字典体」に含まれる字形を入力。                 |




## krm_notes



**KRM_definitions.tsv**ファイルに詳細な注釈情報を追加したファイル
**krm_notes.tsv**および**krm_json**を作成した。
これは、TSV形式とJSON形式で用意した。
2025年3月の仕様変更後のファイル名であることを明示的に示すため、
大文字のKRMではなく小文字のkrmを用いて
krm_notes.tsvとkrm_notes.jsonという名称とした。

krm_notesを新とし、KRM_definitionsを旧として、両者のカラム名を対照すれば次のようになる。


| New Column Name (v1.2.6) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_location          | KRID                      |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks       | Remarks                    |

さらに**KRM.tsv**の内容をkrm_notesに取り込むことにした。両者のカラム名を対照すれば次のようになる。

| New Column Name (v1.2.1) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id        | KRID_n                    |
| tenri_location    | KR_Tenri_p                      |
| volume_name            | KR_vol_name                      |
| radical_name      | KR_radical                        |
| volume_radical_index     | KR_vol_radical                |
| original_entry     | Entry_original                   |


前述したように、krm_notesの内部は次のような入れ子構造となっている。

![ER_notes図](/images/krm_notes_er.drawio.png)


次に、カラム名の内容を英語と日本語で説明する。



| New Column Name (v1.2.6) | English Explanation       | Japanese Explanation                                                                                    |
|--------------------------|--------------|------------------
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.  | Fで始まる5桁の数値に_00を加えた見出し項目ID。一部、追加した掲出項目にはb番号を付す。    |
| definition_seq_id        | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。            |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately. | K・巻数（2桁）・風間版頁数（3桁）・行数（1桁）、段数（1桁）、字順（1桁）を示すID。字順付与のルールの詳細は別に定める。  |
| tenri_location           | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately. | T・巻数（a/b/c）・天理版頁数（3桁）・行数（1桁）・段数（1桁）・字順（1桁）を示す。字順付与のルールの詳細は別に定める。 |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.    | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す                                                   |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.     | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す                                                                          |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.     | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。                            |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses ().  | 校訂漢字は原則、康熙字典体（Unicodeの新字体（通用字体・俗字体）を含む）を用いる。Unicodeに収録されていない漢字については、以下の方法で表現する。漢字の部品の組み合わせで表現可能な場合は、IDS（漢字構成記述文字列）で入力する。特定の漢字やその部品で、IDSまたは標準Unicodeで表現が困難な場合は、CHISEおよびGlyphWikiの実体参照方式に基づいた簡略表記（例：CDP-8C55, koseki-00001）を用いる。上記のいずれの方法でも表現できない文字や、原典で判読不能な文字（虫損等）は、「■」（黒い四角）で入力する。複数漢字の見出しは「／」（全角スラッシュ）で区切る。省略符号「｜」は「ー」（長音符）で示し、全角括弧（）内に該当字を付記する。  |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used.  | 原字形に準拠した見出し字。誤字はそのまま。Unicode外の漢字の表現はhanzi_entryに準じる。原字形の掲出字が不要なら「〇」。  |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per entry.     | 注文の全文から、字体注、音注、意義注、和訓、その他の５種に区分し、それぞれの要素を一つずつ抜き出したもの。    |
| definition_type_code     | 3-digit numeric code representing the definition type.     | 注文の種類を分類した3桁の数値。                                                                                        |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, wakun, and others.     | 注文の種類を字体注、音注、意義注、和訓、その他の５種に区分して、そのいずれに該当するかを示したもの。    |
| remarks                  | Editor's notes providing additional context or information.   | 編集者による追加の文脈や情報を提供する注記。    |

## krm_wakun

これは、名義抄デーベースのKRM.tsvから和訓を抜き出して、
和訓の異形を整理し、異体字との対応を調整したデータである。

和訓に関する校勘と出典考証はkrm_notesに記載したので省略している。

和訓には、異なる読み方を傍書して併記する場合がある。

たとえば「倍」に「マサル」という和訓を付すが、「ル」の右に小さい片仮名で「ス」を傍書する。
これは「マサル」に加えて「マス」という和訓を注記したものである。

和訓にはジャパンナレッジ版『日本国語大辞典第二版』の情報を追加するので、
和訓の異形を併記する場合に対応する必要がある。

異体字との対応は、掲出字に異体字を示すことがあり、これを調整したものである。

たとえば、「ヤツカレ」という和訓は、掲出字「㒒／僕」の注文に見える。
和訓「ヤツカレ」は、「僕」に対する和訓であると同時に「㒒」に対する和訓となっている。
「爲」と「為」、「來」と「来」との関係も同様である。

ジャパンナレッジ版『日本国語大辞典第二版』には「表記」欄があり、名義抄の
漢字表記を収録しているので、これとの対応をとるための措置である。

2025年3月の仕様変更後のファイル名であることを明示的に示すため、
大文字のKRMではなく小文字のkrmを用いて
krm_wakun.tsvとkrm_wakun.jsonという名称とした。

新旧のカラム名を対照すれば次のようになる。

| New Column Name (v1.2.0) | Old Column Name (v1.1.97) |
|-------------------------|---------------|
| wakun_id                | KRID_wakun_no |
| definition_seq_id       | KRID_no       |
| kazama_entry_location   | KR2ID         |
| hanzi_entry             | Entry         |
| wakun_elements          | Def           |
| wakun_form              | Word_form     |
| wakun_standard_hanzi    | Wakun_Hanzi   |
| wakun_variant_in_hanzi  | Wakun_variant |
| variant_hanzi_for_wakun | Hanzi_variant |
| japan_knowledge_id      | JK_URL        |
| -           | Remarks       |

Remarksはkrm_notesにまとめることとして、省略した。

次に、カラム名の内容を英語と日本語で説明する。

| New Column Name (v1.2.0)            | English Explanation               | Japanese Explanation                                                                         |
|-------------------------|-------------|--------------------|
| wakun_id                | Wakun ID, extracted from kr_definition_sequence_id, containing only entries where the type of order is Japanese reading (wakun). Variant forms are appended with 'b', 'c', 'd'.        | 和訓ID。kr_definition_sequence_idから、注文の種類が和訓のものだけを取り出したもの。変異形を追加したものには末尾にa, b, c, dを付した。        |
| definition_seq_id       | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。 |
| kazama_entry_location   | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. | 位置情報（風間版：K、冊子（巻）、ページ（xxx）、行（y）、列（zz））を含むID。列に複数のエントリがある場合は、1、2、...、n の順位になる。                 |
| hanzi_entry             | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.          | 原文の漢字を校訂したもの。康熙字典体とするのを原則としたが、Unicodeで入力できる新字体（通用字体、俗字体）を残すこともある。                            |
| wakun_elements          | Extracted Japanese reading (wakun) components from the full definition, one component per entry.   | 注文の全文から、和訓の要素を一つずつ抜き出したもの。             |
| wakun_form              | Form of the Japanese reading (wakun). Inflected words are in dictionary form, excluding particles. The particles 'no' and 'to' from 文選 readings are omitted.      | 和訓の語形。活用のあるものは、助詞助動詞を除いて終止形とする。文選読みの「の」「と」は省略する。            |
| wakun_standard_hanzi    | Standard wakun notation using standard kanji.             | 標準的な漢字による和訓表記。                            |
| wakun_variant_in_hanzi  | Variant form of wakun notation using standard Hanzi characters.                 | 標準的な漢字による和訓の異形の表記。                                                                           |
| variant_hanzi_for_wakun | Wakun notation using variant Hanzi characters (itai-ji).        | 異体字による和訓の表記。                           |
| japan_knowledge_id      | The alphanumeric part of the JapanKnowledge URL for the corresponding entry in the Nihon Kokugo Daijiten 2nd Ed., starting from "20020" to the end, is recorded here if the wakun exists as a headword. If the wakun does not exist as a headword in the JapanKnowledge edition, null is entered.       | ジャパンナレッジ版『日本国語大辞典第二版』にこの和訓が見出しとして存在する場合に、そのURLの後半、20020から末尾までの英数字を記載する。見出しとして存在しない場合は null と入力する。                   |

## krm_definitions


名義抄の注文には、和訓だけではなく、字体注、音注、意義注などの要素を含んでいる。
これらの校勘と出典考証を行うために、注文の各要素を出現順に区分し、出現の順番に
番号を与えたレコードを作成し、注文種類の分類を行ったファイルである。
従来公開していたのは、KRM_definitions.tsvである。
2025年3月の仕様変更後は、krm_notesに統合したので、
説明は省略する。


## krm_pronunciations


名義抄の音注は、反切、類音注、仮名注があり、それらに声点が施されることも多い。
日本漢字音のデータベースとしては、加藤大鶴氏らによる
「資料横断的な漢字音・漢語音データベース」（略称DHSJR）が非常に充実した
内容を持っている。またその仕様も詳細に公開されている。
DHSJRの仕様に合わせたデータ公開を検討中である。

## krm_ndl

国会図書館デジタルコレクションで公開している
観智院本類聚名義抄の画像へのリンクを整理したものである。
観智院本類聚名義抄の所在と国会図書館デジタルコレクションのURLとを対照させたデータである。
ファイル名は、KRM_ndl.tsvである。

KRM_ndl.tsvは2025年3月の仕様変更の影響がほとんどないので
説明は省略する。


巻名（帖名）、部首字、風間版頁数、天理版頁数、国会図書館デジタルコレクションのURL、を示すデータである。

次にサンプルとしてデータの冒頭部分を示す。

| Book | Radical | Kazama | Tenri | NDL_url                                       |
|------|---------|--------|-------|-----------------------------------------------|
| 仏上   | 人       | 1      | 23    | https://dl.ndl.go.jp/info:ndljp/pid/2586891/6 |
| 仏上   | 人       | 2      | 24    | https://dl.ndl.go.jp/info:ndljp/pid/2586891/7 |


`krm_main` との連携がとりやすいようするため、改良を加える予定である。
