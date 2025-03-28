# 公開データの概要

池田　証寿
Ikeda Shoju
2025年3月28日

[https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC)
で公開している観智院本類聚名義抄のデータについて、その概要を
解説する。

- krm_main
- krm_notes
- krm_wakun　
- krm_definitions　
- krm_pronunciations
- krm_ndl

2025年3月に大幅な仕様変更を行った。従来の公開ファイルは、
KRMを付していたが、仕様変更後のファイルは、krmを付すことに
した。

仕様変更後のファイルはv2のフォルダーに置いた。これは一時的なものである。

## krm_main


観智院本類聚名義抄（以下、名義抄）デーベースの中核となるファイルを解説する。
従来公開していたのは、KRM.tsvという名称のTSVファイルである。

掲出字、注文、巻、部首、風間書房版と天理善本叢書版の所在などに関する情報を
収録する。

2025年3月に、カラム名、声点の表示法の仕様を変更した。仕様変更後の
ファイルであることを明示するために、krm_main.tsvという名称にした。
これにはJSON形式も用意した。

新旧のカラム名を対照すれば次のようになる。


| New Column Name (v1.2.0) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| hanzi_id                 | KRID_sn                    |
| kazama_entry_location    | KR2ID                      |
| kazama_hanzi_location    | KRID                       |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| hanzi_entry              | Entry                      |
| original_entry           | Entry_original             |
| definition               | Def                        |
| -                        | Remarks                    |

Remarksは次のkrm_notesにまとめることとして、省略した。

次に、カラム名の内容を英語と日本語で説明する。

| New Column Name (v1.2.0) | English explanation           | Japanese explanation                    |
|--------------------------|-----------------------------|-------------------------------------------|
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F', followed by '_00'.               | Fで始まる5桁の数値に_00を加えた見出し項目ID。     |
| hanzi_id                 | A heading Hanzi ID consisting of a 5-digit numeric ID starting with 'S'.           | Sで始まる5桁の数値からなる見出し漢字ID。         |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number.                                                              | 位置情報（風間版：K、冊子（巻）、ページ（xxx）、行（y）、列（zz））を含むID。列に複数のエントリがある場合は、1、2、...、n の順位になる。                 |
| kazama_hanzi_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 0 for single-character headwords, and 1, 2, ..., n for multiple-character headwords or entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. | K・巻数(2桁)・風間書房版ページ数(3桁)・行数(1桁)・段数(1桁)・字順(1桁)を示すID。掲出字が単字なら字順は0、複字なら1, 2, ..., n。一段に複数項目あれば単字でも1, 2, ..., n。            |
| tenri_location           | Location information from the Tenri edition (T, volume(volume letters), page(xxx), line(y), column(zz)). Where volume(volume letters) represents the volume letters, page(xxx) the page number, line(y) the line number, and column(zz) the column number.   | 八木書店版の掲出字ID。T・巻数（a/b/c）・ページ数（3桁数）・行数（1桁）・段数（1桁）・字順（1桁）を示す。最後の字順の示し方は掲出字IDの場合に同じとする。八木書店『天理図書館善本叢書』に基づく。        |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.            | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す。                              |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.                   | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す。       |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.           | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。            |
| hanzi_entry              | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.        | 原文の漢字を校訂したもの。康熙字典体とするのを原則としたが、Unicodeで入力できる新字体（通用字体、俗字体）を残すこともある。複数の漢字からなる見出し項目の場合は、／（全角スラッシュ）で区切り、省略符号「｜」がある場合、ー（長音符）を用いて、その後の（）（全角括弧）内に該当字を入力する。 |
| original_entry           | Original Hanzi character representations, retaining errors from the original text, with non-Unicode variants expressed using IDS or 〓.      | 原字形に近い見出し文字。池田が必要と判断したものは「原字形に近い掲出字」として入力し、不要な場合は「〇」を入力。                                                                                           |
| definition               | Includes glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and other relevant notes, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.    | 注文は、字体注、音注、義注、和訓、その他からなる。これらをスペース区切りで入力。原則として「康熙字典体」に含まれる字形を入力。                 |




## krm_notes



KRM_def.tsvファイルに詳細な注釈情報を追加したファイルkrm_notes.tsvを作成した。
これは、TSV形式とJSON形式で用意した。
2025年3月の仕様変更後のファイル名であることを明示的に示すため、
大文字のKRMではなく小文字のkrmを用いて
krm_notes.tsvとkrm_notes.jsonという名称とした。

krm_notes.tsvを新とし、KRM_definitions.tsvを旧として、両者のカラム名を対照すれば次のようになる。



| New Column Name (v1.2.0) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_entry_location    | KR2ID                      |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks_definition       | Remarks                    |


次に、カラム名の内容を英語と日本語で説明する。

| New Column Name (v1.2.0) | English explanation          | Japanese explanation             |
|--------------------------|-----------------------------------|----------------|
| definition_seq_id        | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。 |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. | 位置情報（風間版：K、冊子（巻）、ページ（xxx）、行（y）、列（zz））を含むID。列に複数のエントリがある場合は、1、2、...、n の順位になる。                 |
| hanzi_entry              | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.                | 原文の漢字を校訂したもの。康熙字典体とするのを原則としたが、Unicodeで入力できる新字体（通用字体、俗字体）を残すこともある。                            |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per entry.                 | 注文の全文から、字体注、音注、意義注、和訓、その他の５種に区分し、それぞれの要素を一つずつ抜き出したもの。         |
| definition_type_code     | 3-digit numeric code representing the definition type.         | 注文の種類を分類した3桁の数値。               |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, wakun, and others.                                                                                                                               | 注文の種類を字体注、音注、意義注、和訓、その他の５種に区分して、そのいずれに該当するかをしめしたもの。                                          |
| remarks_definition       | Editor's notes providing additional context or information.           | 編集者による追加の文脈や情報を提供する注記。 |

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

| New Column Name (v1.2.0)            | English explanation                                                                                                                                                                                                                                                                               | Japanese explanation                                                                         |
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
| japan_knowledge_id      | The alphanumeric part of the JapanKnowledge URL, from 20020 to the end.       | ジャパンナレッジのURLの後半、20020から末尾までの英数字。                   |

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
