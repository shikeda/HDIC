# Kanchi-in Manuscript of the *Ruiju Myōgishō* Database

## Overview

This database is a full-text digitization of the Kanchi-in manuscript of the *Ruiju Myōgishō* (abbreviated as KRM), incorporating location information, textual collation, source studies, and more. It is one of the **Hanzi** dictionary databases comprising the **Integrated Database of Hanzi Dictionaries in Early Japan** (abbreviated as HDIC). **The terms 'kanji' and 'hanzi' are explained later.**

The Kanchi-in manuscript of the *Ruiju Myōgishō* is a **Hanzi** dictionary compiled in the twelfth century by a Shingon Buddhist monk. It has been regarded as an important resource for Japanese historical linguistics research due to its extensive collection of *wakun* indicating accent, detailed annotations on **Hanzi** pronunciations, and annotations on variant characters. Furthermore, its Chinese annotations on **fanqie**, meanings, and glyph forms have also garnered attention as materials for Chinese linguistics.

It was first published in March 2022, and in March 2025, a revised edition with specification changes and detailed explanations will be released.

The link to the GitHub repository is as follows:

[https://github.com/shikeda/HDIC/tree/master/v1.2/README_jp.md](https://github.com/shikeda/HDIC/tree/master/v1.2/README_jp.md)

## Kanji and Hanzi

To bridge the gap between 'Kanji' and 'Hanzi,' and to facilitate international academic discourse, the following supplementary explanation may be useful:

Dictionaries of Chinese characters compiled in Japan during the Heian period are invaluable resources not only for the study of Japanese linguistics but also for the study of Chinese linguistics. To promote international accessibility, we propose using the term 'Hanzi.' Researchers specializing in Japanese studies may, without any issue, read this term as 'Kanji.' This approach aims to respect the linguistic diversity and academic traditions of both fields, while encouraging broader scholarly exchange.

This explanation aims to provide clarity and respect for both terminologies, ensuring that researchers from different backgrounds can engage with the material without linguistic barriers.


## Data Files

### List and Brief Description

The data from the Kanchi-in manuscript of the *Ruiju Myōgishō*, published at [https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2), is as follows. This includes some files that are currently being prepared for public release.

- [krm_main](#krm_main): Basic data. Includes information about head characters, full definitions, locations, etc. TSV and JSON files are available.
- [krm_notes](#krm_notes): Annotation data. Categorized into head characters, glyph annotations, pronunciation annotations, meaning annotations, *wakun*, and others, with collation and source studies. TSV and JSON files are available.
- [krm_headword_chars]: Detailed information about all head characters. Includes location in the Kazama edition, location in the Tenri edition, image file names, etc. Currently under preparation for release.
- [krm_wakun](#krm_wakun): *Wakun* data. Includes information about variant forms of *wakun*, variant forms of hanzi (*itai-ji*), and correspondence with the "Notation" field of the *Nihon Kokugo Daijiten* (Second Edition). TSV and JSON files are available.
- [krm_definitions](#krm_definitions): Definitions categorized into glyph annotations, pronunciation annotations, meaning annotations, *wakun*, and others. TSV file available. Same as the already published [KRM_definitions.tsv](https://github.com/shikeda/HDIC/KRM_definitions.tsv).
- [krm_pronunciations](#krm_pronuncitaions): Data for linking with DHSJR regarding pronunciation annotations (under preparation).
- [krm_ndl](#krm_ndl): Links to the National Diet Library Digital Collections. TSV file available. Same as the already published [KRM_ndl.tsv](https://github.com/shikeda/HDIC/KRM_ndl.tsv).


### Specification Change

A significant specification change was implemented in March 2025. Previously, the published files were prefixed with "KRM," but the files following this specification change will be prefixed with "krm."

The files incorporating the specification changes have been placed in the "v1.2" folder. Please note that this is a temporary arrangement.

Here are the key points of the specification change:

- The at mark "@", which indicates that kana wakun does not have tone marks, has been changed to an underscore "_".
- The double quotation mark """, which indicates that voiced sound wakun has tone marks, has been changed to a half-width English letter "V".
- The half-width parentheses "()", which indicate the presence of tone marks, have been changed to full-width parentheses "（）".
- The half-width parentheses "()" indicating a correction proposal for a typo have been changed to full-width square brackets "〔〕".
- The half-width square brackets "[]", which indicate missing characters, have been changed to full-width square brackets "［］".

### ER Diagram

The following ER diagram shows the relationship between the three tables: `krm_main`, `krm_notes`, and `krm_wakun`.

![ER diagram.](/images/krmer.drawio.png)

Moreover, `krm_notes.json` has a nested structure as shown in the following diagram.

![ER_notes diagram](/images/krm_notes_er.drawio.png)

## Common Information

This section describes information common to all data files published here.

### Last Updated Date

Date published: 30 March 30 2025  
Last modified: 11 May 2025

### Version History

#### krm_main 
- Version: 1.2.6 (latest)  
    Date published: 28 March 2025  
    Last modified: 11 May 2025
- Version: 1.1.347  
    Date: 11 March 2022  
    Last modified : 17 March 2025

### krm_notes
- Version: 1.2.7 (latest, Newly released after the specification change)  
    Date published: 28 March  2025  
    Last modified: 11 May  2025

### krm_headword_chars
- Version: 1.2.1 (latest, Newly released after the specification change)  
    Date published: 11 May  2025  
    Last modified: 11 May  2025

### krm_wakun
- Version: 1.2.1 (latest)  
    Date published: 28 March 2025  
    Last modified: 2 May 2025

- Version: 1.1.97  
    Date published: 11 June 2024  
    Last modified: 17 March 2025

### Author and Copyright Information

HDIC Project
Representative: Shoju Ikeda (Professor Emeritus, Hokkaido University)
Copyright (c) 2022-2025 HDIC project, IKEDA Shoju (Chair, Professor Emeritus, Hokkaido University)

Contact:
ikeda.shoju@gmail.com, liyuansapporo@yahoo.co.jp, toyjack@gmail.com, kleinekuma@gmail.com

### License Information

The contents of this site are provided under the CC BY-NC-SA 4.0 license.  
This is open access data.

### List of Abbreviations of Cited Works

For each cited reference, the original notation is given first, followed by the English translation. The Romanized notation is provided in parentheses where necessary.

- 正宗索引: 正宗敦夫編, 類聚名義抄 仮名索引, 日本古典全集刊行会, 1939-1940  
  Masamune Index: Edited by Masamune Atsuo, *Kana Index to the Ruiju Myogisho*, Nihon Koten Zenshu Kankokai, 1939-1940  
  (Romanization: Masamune Sakuin: Masamune Atsuo hen, *Ruiju Myōgishō Kana Sakuin*, Nihon Koten Zenshū Kankōkai, 1939-1940)
- 岡田研究: 岡田希雄, 類聚名義抄の研究, 一条書房, 1944  
    Okada Research: Okada Mareo, *Research on the Ruiju Myogisho*, Ichijo Shobo, 1944  
    (Romanization: Okada Kenkyū: Okada Mareo, *Ruiju Myōgishō no Kenkyū*, Ichijō Shobō, 1944)
- 望月和訓集成: 望月郁子編, 類聚名義抄: 四種声点付和訓集成, 笠間書院, 1974  
    Mochizuki Wakun Collection: Edited by Mochizuki Ikuko, *Ruiju Myogisho: Collection of Four Types of Wakun with Tone Marks*, Kasama Shoin, 1974  
    (Romanization: Mochizuki Wakun Shūsei: Mochizuki Ikuko hen, *Ruiju Myōgishō: Shishu Shōten-tsuki Wakun Shūsei*, Kasama Shoin, 1974)
- 中村文選: 中村宗彦, 九条本文選古訓集, 風間書房, 1983  
    Nakamura Monzen: Nakamura Munehiko, *Old Japanese Readings of the Kujo Text of the Wen Xuan*, Kazama Shobo, 1983  
    (Romanization: Nakamura Monzen: Nakamura Munehiko, *Kujō-bon Monzen Kokunshū*, Kazama Shobō, 1983)
- 草川和訓集成: 草川昇編, 五本対照類聚名義抄和訓集成, 汲古書院, 2000  
    Kusakawa Wakun Collection: Edited by Kusakawa Noboru, *Comparative Collection of Wakun from Five Texts of the Ruiju Myogisho*, Kyuko Shoin, 2000  
    (Romanization: Kusakawa Wakun Shūsei: Kusakawa Noboru hen, *Gohon Taishō Ruiju Myōgishō Wakun Shūsei*, Kyūko Shoin, 2000) 
- 西端誤写考察: 西端幸雄, 類聚名義抄における誤写の考察, 訓点語と訓点資料45, 1971  
    Nishihata Miscopy Study: Nishihata Yukio, A Study on Miscopies in the *Ruiju Myogisho*, Kunten-go to Kunten Shiryo 45, 1971  
    (Romanization: Nishihata Gosha Kōsatsu: Nishihata Yukio, *Ruiju Myōgishō* ni okeru Gosha no Kōsatsu, Kunten-go to Kunten Shiryō 45, 1971)
- 西端誤写諸例: 西端幸雄, 類聚名義抄における誤写の諸例, 訓点語と訓点資料52，1973  
    Nishihata Miscopy Examples: Nishihata Yukio, Examples of Miscopies in the *Ruiju Myogisho*, Kunten-go to Kunten Shiryo 52, 1973  
    (Romanization: Nishihata Gosha Shorei: Nishihata Yukio, *Ruiju Myōgishō* ni okeru Gosha no Shorei, Kunten-go to Kunten Shiryō 52, 1973)
- 略注: 佐藤喜代治，色葉字類抄略注，明治書院，1995  
    Brief Notes: Sato Kiyoji, *Brief Notes on the Iroha Jirui Sho*, Meiji Shoin, 1995  
    (Romanization: Ryakuchū: Satō Kiyoji, *Iroha Jirui Shō Ryakuchū*, Meiji Shoin, 1995)
- 群書治要: 小林芳規・原卓志・山本秀人・山本真吾・佐々木勇編, 宮内庁書陵部蔵本群書治要経部語彙索引, 汲古書院, 1996  
    Gunsho Chiyo: Edited by Kobayashi Yoshinori, Hara Takushi, Yamamoto Hideto, Yamamoto Shingo, Sasaki Isamu, *Index to the Vocabulary of the Classics Section of the Gunsho Chiyo*, Imperial Household Agency Archives Collection, Kyuko Shoin, 1996
- 毛詩鄭箋: 毛詩鄭箋（一）（二）（三）, 古典研究会叢書漢籍之部１～３, 原本所蔵静嘉堂文庫, 汲古書院, 1992  
    Mao Shi Zheng Jian: Mao Shi Zheng Jian (1) (2) (3), Series of the Classical Studies Association, Chinese Classics Section 1-3, Original Texts in the Seikado Bunko, Kyuko Shoin, 1992

### Acknowledgments

We would like to express our gratitude to Tenri Central Library and Yagi Bookstore for granting permission to publish the decipherment text of the Kanchi-in manuscript of the *Ruiju Myōgishō*.  

This research is partly supported by JSPS KAKENHI Grant Numbers 16H03422, 19H00526, 23K17500 and 25K00466. We gratefully acknowledge this support.

## krm_main

This section explains the core file of the Kanchi-in manuscript of the *Ruiju Myōgishō* (hereinafter referred to as "*Myōgishō*") database. The file previously made public was a TSV file named `KRM.tsv`.

It includes information regarding head characters, definitions, volumes, radicals, and the locations in the Kazama Shobo edition and the Tenri Zenpon Sosho edition.

In March 2025, the specifications for column names and the display method of tone marks were changed. To clearly indicate that it is the file after the specification change, it was named `krm_main.tsv`. A JSON format is also available for this file.

The comparison of the new and old column names is as follows:

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

The `KR2ID` column was omitted, and the `kazama_location` column was aligned with the `KRID` column.
The `Remarks` column was omitted and will be summarized in the following `krm_notes` file.


Next, the content of the column names will be explained.

| New Column Name (v1.2.5)|Explanation|
|--------------------------|----------------------|
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.     |
| hanzi_id                 | A heading Hanzi ID consisting of a 5-digit numeric ID starting with 'S'. For some added entry items, a 'b' suffix is appended.   |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  |
| tenri_location           | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.   |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.      |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.   |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text. |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used. |
| definition               | Includes glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and other relevant notes, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.  |


## krm_notes

A new file, krm_notes.tsv, has been created, containing detailed annotation information added to the `KRM_def.tsv` file.

This is available in both TSV and JSON formats. To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_notes.tsv` and `krm_notes.json`.

Considering `krm_notes.tsv` as the new file and `KRM_definitions.tsv` as the old file, the comparison of their column names is as follows:

| New Column Name (v1.2.6) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_location          | KRID                      |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks_definition       | Remarks                    |

Furthermore, we decided to incorporate the contents of `KRM.tsv` into `krm_notes`. Comparing the column names of both will result in the following.

| New Column Name (v1.2.6) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id        | KRID_n                    |
| tenri_location    | KR_Tenri_p                      |
| volume_name            | KR_vol_name                      |
| radical_name      | KR_radical                        |
| volume_radical_index     | KR_vol_radical                |
| original_entry     | Entry_original                   |


As mentioned earlier, the internal structure of `krm_notes` has the following nested format.


![ER_notes diagram](/images/krm_notes_er.drawio.png)

Next, the content of the column names will be explained.


| New Column Name (v1.2.6) | English Explanation              |
|--------------------------|---------------------------|
| entry_id                 |A heading item ID formed by a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.  |
| definition_seq_id        | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.|
| tenri_location           |An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.   |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.          |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.         |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used.  |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per entry.           |
| definition_type_code     | 3-digit numeric code representing the definition type.   |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, wakun, and others.  |
| remarks                  | Editor's notes providing additional context or information.      |



## krm_wakun

This data is derived by extracting wakun from the `KRM.tsv` file of the *Myōgishō* database, organizing variant forms of the wakun, and adjusting their correspondence with variant characters (itai-ji).

Collation and textual research related to wakun are documented in `krm_notes`, so they are omitted here.

In wakun, different readings may be written alongside the main reading as annotations.

For example, the wakun "マサル" (masaru) is assigned to the character "倍" (bai), but "su" is written in small katakana to the right of "ル" (ru) as an annotation. This indicates that the wakun "マス" (masu) is annotated in addition to "マサル" (masaru).

Since information from the JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) will be added to the wakun, it is necessary to accommodate cases where variant forms of wakun are written together.

The handling of variant characters involves cases where variant forms are indicated for the head character, and this data has been adjusted to account for them.

For example, the wakun "yatsukare" appears in the definition for the head characters "㒒/僕". The wakun "yatsukare" is a wakun for "僕" (boku) and is simultaneously a wakun for "㒒". The relationship between standard and variant forms such as "爲" and "為", or "來" and "来" is similar.

The JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) has a "Notation" field that includes the kanji notations from the Myōgishō, so this adjustment is a measure to ensure correspondence with it.

To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_wakun.tsv` and `krm_wakun.json`."

The comparison of the new and old column names is as follows:

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


`Remarks` have been omitted and will be summarized in the following `krm_notes` file.

Next, the content of the column names will be explained.

| New Column Name (v1.2.0)      | Explanation        |
|-------------------------|------------------|
| wakun_id                | Wakun ID, extracted from kr_definition_sequence_id, containing only entries where the type of order is Japanese reading (wakun). Variant forms are appended with 'b', 'c', 'd'.  |
| definition_seq_id       | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.    |
| kazama_entry_location   | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. |
| hanzi_entry             | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.         |
| wakun_elements          | Extracted Japanese reading (wakun) components from the full definition, one component per entry.  |
| wakun_form        | Form of the Japanese reading (wakun). Inflected words are in dictionary form, excluding particles. The particles 'no' and 'to' from 文選 readings are omitted. |
| wakun_standard_hanzi    | Standard wakun notation using standard kanji.      |
| wakun_variant_in_hanzi  | Variant form of wakun notation using standard Hanzi characters.      |
| variant_hanzi_for_wakun | Wakun notation using variant Hanzi characters (itai-ji).    |
| japan_knowledge_id      | The alphanumeric part of the JapanKnowledge URL for the corresponding entry in the *Nihon Kokugo Daijiten* 2nd Ed., starting from "20020" to the end, is recorded here if the wakun exists as a headword. If the wakun does not exist as a headword in the JapanKnowledge edition, null is entered.    |

## krm_definitions

The definitions in the *Myōgishō* include not only wakun but also elements such as glyph annotations, pronunciation annotations, and meaning annotations.

This file contains records created by categorizing each element of the definitions according to their order of appearance, assigning them numbers based on this order, and classifying the types of definitions. This was done for the purpose of collation and textual research.

The file previously made public was `KRM_definitions.tsv`.

After the specification change in March 2025, this information has been integrated into `krm_notes`, so a separate explanation will be omitted here.

## krm_pronunciations

The pronunciation annotations (on-chū) in the *Myōgishō* include fanqie, similar-sound annotations, and kana annotations, and these often have tone marks applied to them.

As a database of Japanese kanji pronunciations, the "Database of Historical Sino-Japanese Readings" (abbreviated DHSJR), created by Professor Daikaku Kato and others, boasts very comprehensive content. Furthermore, its specifications are also published in detail.

We are currently considering publishing our data in accordance with the DHSJR specifications.


## krm_ndl

This file compiles links to the images of the Kanchi-in manuscript of the *Ruiju Myōgishō* that are publicly available in the National Diet Library Digital Collections.

This data cross-references the locations within the Kanchi-in manuscript of the *Ruiju Myōgishō* with their corresponding URLs in the National Diet Library Digital Collections. The file name is `KRM_ndl.tsv`.


This data indicates the volume name, radical character, Kazama edition page number, Tenri edition page number, and the URL for the National Diet Library Digital Collections.

Next, a sample of the beginning of the data is shown below.


| Book | Radical | Kazama | Tenri | NDL_url                                       |
|------|---------|--------|-------|-----------------------------------------------|
| 仏上   | 人       | 1      | 23    | https://dl.ndl.go.jp/info:ndljp/pid/2586891/6 |
| 仏上   | 人       | 2      | 24    | https://dl.ndl.go.jp/info:ndljp/pid/2586891/7 |


We plan to make improvements to facilitate easier integration with `krm_main`.
