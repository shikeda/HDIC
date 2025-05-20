# Kanchi-in Manuscript of the *Ruiju Myōgishō* Database

## Overview

This database is a full-text digitization of the Kanchi-in manuscript of the *Ruiju Myōgishō* (abbreviated as KRM), incorporating location information, textual collation, source studies, and more. It is one of the **Hanzi** dictionary databases comprising the **Integrated Database of Hanzi Dictionaries in Early Japan** (abbreviated as HDIC). **The terms 'kanji' and 'hanzi' are explained later.**

The Kanchi-in manuscript of the *Ruiju Myōgishō* is a **Hanzi** dictionary compiled in the twelfth century by a Shingon Buddhist monk. It has been regarded as an important resource for Japanese historical linguistics research due to its extensive collection of *wakun* indicating accent, detailed annotations on **Hanzi** pronunciations, and annotations on variant characters. Furthermore, its Chinese annotations on **fanqie**, meanings, and glyph forms have also garnered attention as materials for Chinese linguistics.

It was first published in March 2022, and in March 2025, a revised edition with specification changes and detailed explanations will be released.


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

Date published: March 30, 2025  
Last modified: May 13, 2025

### Version History

#### krm_main 
- Version: 1.2.6 (latest)  
    Date published: March 28, 2025  
    Last modified: May 11, 2025
- Version: 1.1.347  
    Date: March 11, 2022  
    Last modified : March 17, 2025

### krm_notes
- Version: 1.2.7 (latest, Newly released after the specification change)  
    Date published: March 28, 2025  
    Last modified: May 11, 2025

### krm_headword_chars
- Version: 1.2.1 (latest, Newly released after the specification change)  
    Date published: May 11, 2025  
    Last modified: May 11, 2025

### krm_pronounciations
- Version: 1.2.1 (latest, DHSJR format)  
    Date published: May 20, 2025  
    Last modified: May 20, 2025


### krm_wakun
- Version: 1.2.2 (latest)  
    Date published: March 28, 2025  
    Last modified: May 12, 2025

- Version: 1.1.97  
    Date published: June 11, 2024  
    Last modified: March 17, 2025

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

### Overview and file formats


This section describes the core files of the database for the Kanchi-in manuscript of the *Ruiju Myōgishō* (hereinafter "*Myōgishō*").

Previously, the released file was a TSV file named `KRM.tsv`.

It contains information regarding **`Headwords`**, the full content of the **`Definition (Original Glosses)`**, volume, radical, and the locations in the Kazama Shobō edition and the Tenri Central Library/Yōtokusha (Tenri Zenhon Sōsho) edition.

In March 2025, the specifications for column names and the display method for **`Tone marks (*shōten*)`** were updated. To clearly indicate that it is the file with these updated specifications, it was renamed `krm_main.tsv`. A JSON version of this file has also been made available.

### Column name comparison

The correspondence between the old and new column names is as follows:

| New Column Name (v1.2.5) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| hanzi_id                 | KRID_sn                    |
| -                        | KR2ID                      |
| kazama_location          | KRID                       |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| hanzi_entry              | Entry                      |
| original_entry           | Entry_original             |
| definition               | Def                        |
| -                        | Remarks                    |

The `KR2ID` column was omitted, and the `kazama_location` column was aligned with the `KRID` column.

The `Remarks` column was omitted; this information is now consolidated in the `krm_notes` file (which contains data for the **`Compiler's Remarks`**).

### Description of each column

The content of each column (v1.2.5) is explained below.

| New Column Name (v1.2.5) | Explanation     |
| :----------------------- | :------------------------- |
| entry_id                 | A heading **`Entry`** ID consisting of a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.       |
| hanzi_id                 | A heading **`Hanzi (Chinese character)`** ID consisting of a 5-digit numeric ID starting with 'S'. For some added entry items, a 'b' suffix is appended.        |
| kazama_location          | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.       |
| tenri_location           | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.     |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏下本, 仏下末, 法上, 法中, 法下, 僧上, 僧中, and 僧下.      |
| radical_name             | Name of the radical, consisting of 120 radicals ranging from 人 to 雑, used to classify **`Hanzi (Chinese characters)`**.   |
| volume_radical_index     | Volume and radical number, ranging from v1#1 (Volume 1, Radical 1) to v10#120 (Volume 10, Radical 120), indicating the location of the **`Entry`** within the text. (Corresponds to 第1帖仏上 to 第10帖僧下).     |
| hanzi_entry              | The collated **`Headword`** (校訂漢字) principally uses Kangxi Dictionary form, including Unicode simplified **Chinese characters** (common-use forms, popular variants). For **Chinese characters** not included in Unicode, they are represented by the following methods: If representable by combining **Chinese character** components, input using IDS (Ideographic Description Sequence). For specific **Chinese characters** or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). **Chinese characters** not representable by any of the above methods, or characters unreadable in the original text (due to damage such as wormholes, etc.), are input as '■' (black square). **`Headwords`** consisting of multiple **Chinese characters** are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). |
| original_entry           | **`Headword`** based on the original character form. Typographical errors in the original are preserved. The representation of **Chinese characters** outside Unicode follows the rules for `hanzi_entry`. If the original-form **`Headword`** is not needed, '〇' is used.  |
| definition               | The content of this `definition` column represents the **`Definition (Original Glosses)`**. It includes **`Notes on Character Form`**, **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, **`Japanese Native Readings (*wakun*)`**, and **Other** relevant information, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.       |


## krm_notes

### Overview and file formats

A new file, `krm_notes.tsv`, has been created, containing detailed annotation information added to the `KRM_definitions.tsv` file.

This is available in both TSV and JSON formats. To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_notes.tsv` and `krm_notes.json`.

### Column name comparison

This section compares the column names in the new `krm_notes.tsv` (v1.2.6) with those in the previous files it replaces or incorporates data from.

#### Comparison with KRM_definitions.tsv (v1.1.55)

The following table shows the correspondence between columns primarily related to definition details derived from the previous definitions file:

| New Column Name (krm_notes v1.2.6) | Old Column Name (KRM_definitions v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_location          | KRID                       |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks                  | Remarks                    |

#### Incorporation of KRM.tsv (v1.1.347) content

The new `krm_notes.tsv` also incorporates information previously stored in `KRM.tsv`. The corresponding column names are compared below:

| New Column Name (krm_notes v1.2.6) | Old Column Name (KRM v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| original_entry           | Entry_original             |


### Data Structure: ER Diagram and JSON Implementation



The JSON representation of `krm_notes` utilizes a nested format, as detailed below.

![ER_notes diagram](/images/krm_notes_er.drawio.png)


In the **ER diagram**, the `krm_notes` table is shown as a child table linked to `krm_main` (as detailed in the [krm_main section](./02-01-main)) by `entry_id`. However, in the **actual JSON data**, the equivalent of the `krm_notes` table is not flat: instead, it is implemented as a **nested array of objects** under the key `"definitions"` within each top-level record (referred to as a `krm_main` conceptual record).

Each object inside the `definitions` array corresponds to a definition note and contains the following fields:

* `definition_seq_id`
* `definition_elements`
* `definition_type_code`
* `definition_type_name`
* `remarks`

This structure can be conceptually represented in the ER diagram as follows:

* The **`krm_main` table** has a **one-to-many relationship** with a conceptual `definitions` or `notes` table.
* In the JSON representation, the **definitions are embedded as an array of objects** within each `krm_main` object, rather than being stored in a separate flat table.

**Example JSON:**

```
{
  "entry_id": "F00001",
  ...
  "definitions": [
    {
      "definition_seq_id": "F00001_01",
      "definition_elements": "音仁（LV）「ニン」",
      "definition_type_code": 215,
      "definition_type_name": "音注声点有_類音注等",
      "remarks": "広韻「如鄰切」..."
    },
    ...
  ]
}
```
### Description of each column

Next, the content of the column names will be explained.


| New Column Name (v1.2.6) | English Explanation (Further Revised)      |
| :----------------------- | :------------------------------------------------------------ |
| entry_id                 | A heading **`Entry`** ID consisting of a 5-digit numeric ID starting with 'F'. For some newly added **`Entries`**, a 'b' suffix is appended.    |
| definition_seq_id        | An identifier for each component of the **`Definition (Original Glosses)`** or for the **`Headword`** itself within an **`Entry`**. It is formed by appending a sequential suffix (e.g., "_00" for the **`Headword`** or overall **`Entry`** note, "_01", "_02" for subsequent elements of the **`Definition (Original Glosses)`** in order of appearance) to the 5-digit numeric part of the corresponding `entry_id`.                                          |
| kazama_location          | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.       |
| tenri_location           | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.              |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏下本, 仏下末, 法上, 法中, 法下, 僧上, 僧中, and 僧下.     |
| radical_name             | Name of the radical, consisting of 120 radicals ranging from 人 to 雑, used to classify **`Hanzi (Chinese characters)`**. |
| volume_radical_index     | Volume and radical number, ranging from v1#1 (Volume 1, Radical 1) to v10#120 (Volume 10, Radical 120), indicating the location of the **`Entry`** within the text. (Corresponds to 第1帖仏上 to 第10帖僧下).       |
| hanzi_entry              | The collated **`Headword`** (校訂漢字) principally uses Kangxi Dictionary form, including Unicode simplified **Chinese characters** (common-use forms, popular variants). For **Chinese characters** not included in Unicode, they are represented by the following methods: If representable by combining **Chinese character** components, input using IDS (Ideographic Description Sequence). For specific **Chinese characters** or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). **Chinese characters** not representable by any of the above methods, or characters unreadable in the original text (due to damage such as wormholes, etc.), are input as '■' (black square). **`Headwords`** consisting of multiple **Chinese characters** are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). |
| original_entry           | **`Headword`** based on the original character form. Typographical errors in the original are preserved. The representation of **Chinese characters** outside Unicode follows the rules for `hanzi_entry`. If the original-form **`Headword`** is not needed, '〇' is used.     |
| definition_elements      | Extracted individual elements from the full **`Definition (Original Glosses)`**, classified into five types: **`Notes on Character Form`**, **`Phonetic Gloss`**, **`Semantic Gloss in Chinese`**, **`Japanese Native Reading (*wakun*)`**, and **`Other`** information. Each record in `krm_notes` typically corresponds to one such extracted element.     |
| definition_type_code     | A 3-digit numeric code representing the type of element from the **`Definition (Original Glosses)`**.     |
| definition_type_name     | Indicates which of the five following categories the element from the **`Definition (Original Glosses)`** belongs to: **`Notes on Character Form`**, **`Phonetic Gloss`**, **`Semantic Gloss in Chinese`**, **`Japanese Native Reading (*wakun*)`**, or **`Other`** information.    |
| remarks                  | **`Compiler's Remarks`**: Notes by the database compilers providing additional context, scholarly observations, results of textual collation, or source investigations related to the specific `definition_element` or `Headword`.    |


### Content and Significance of Compiler's Remarks (the remarks Column)

Please note that this `remarks` column stores the **`Compiler's Remarks`** (annotations by the database creators).

The `remarks` column provides the following types of information:

* **Additional context**: Supplementary background or related information that aids in understanding the *Myōgishō*'s entries.
* **Scholarly observations**: Philological, linguistic, or other expert perspectives on specific descriptions, including references to previous research.
* **Results of textual collation**: Findings from comparisons with variant manuscripts or related materials, and textual interpretations based on these collations.
* **Source investigations**: Results and considerations regarding the textual sources of the *Myōgishō*'s entries, including references to findings from previous studies.

These remarks are each associated with one of the following specific parts of a *Myōgishō* **`Entry`**:

* A specific `definition_element` (an individual component of the **`Definition (Original Glosses)`**): This refers to a distinct element within the *Myōgishō*'s original annotation for an **`Entry`** (such as a particular **`Note on Character Form`**, **`Phonetic Gloss`**, **`Semantic Gloss in Chinese`**, or **`Japanese Native Reading (*wakun*)`**), as itemized in the `krm_notes` file.
* Or the **`Headword`**: The main character(s) of the **`Entry`**.

In essence, the `remarks` column serves to provide specialized, supplementary information from the database compilers, enabling a deeper understanding and facilitating further research that goes beyond what can be gleaned from the *Myōgishō*'s main text and original glosses alone.


## krm_headword_chars

### Overview and file formats

**`Headwords`** in the *Myōgishō* can consist of single **Chinese characters** or multiple **Chinese characters** (multi-character compounds). The `krm_headword_chars` data file provides a list of all **constituent characters that form these `Headwords`** from the *Myōgishō*. The characters are ordered according to the sequence of **`Entries`** (items) in the *Myōgishō* and then by the order of appearance of characters within each **`Headword`**.

In the *Myōgishō* database, the primary data file `krm_main`, the `krm_notes` file (containing data for **`Compiler's Remarks`**), and the `krm_wakun` file (**`Japanese Native Reading (*wakun*)`** data) are all structured on an **`Entry`**-by-**`Entry`** basis. Consequently, for **`Headwords`** composed of multiple **Chinese characters**, any character subsequent to the first cannot be directly referenced from these particular data files.

To search for **`Headwords`** from the *Myōgishō* character by character, display their original manuscript images, or perform analyses at the individual **Chinese character** level, a complete list of all constituent characters of the **`Headwords`**, including those from the second character onwards in multi-character compounds, is necessary.

The `krm_headword_chars` data file was created for this purpose. This data is provided in TSV and JSON formats. Each row (or record) corresponds to a single constituent character of a **`Headword`** and includes information such as: the sequential ID of the **`Headword`** (single or multi-character) in the *Myōgishō* to which the constituent character belongs (`hanzi_id`); the ID of the *Myōgishō* **`Entry`** to which this character's **`Headword`** belongs (`entry_id`); the order of the character within its **`Headword`** (`character_order`); the character itself (`constituent_char`); the file name of the individually cropped image for the character (`img_file_name`); and location information for that character in both the Kazama and Tenri editions (`kazama_location_id`, `tenri_location_id`). This enables information access at the individual character level while allowing linkage with **`Entry`**-based data files such as `krm_main`.

## Description of each column

The column names and their descriptions for `krm_headword_chars` are as follows:

| Column Name          | English Explanation      |
| :------------------- | :------------------------------------------------------ |
| hanzi_id             | A sequential ID assigned to each **`Headword`** (whether single or multi-character) in the order of its appearance in the *Myōgishō*. It consists of a 5-digit numeric ID starting with 'S'.   |
| entry_id             | The ID of the **`Entry`** (from `krm_main`) to which the **`Headword`** (containing this constituent character) belongs. This ID is a 5-digit numeric value starting with 'F'. For some newly added **`Entries`**, a 'b' suffix is appended.      |
| constituent_char     | The constituent **Chinese character** itself. Abbreviation marks (ー) and iteration marks (〻) are converted to the actual characters they represent. Collated **Chinese characters** are, in principle, Kangxi Dictionary forms; the handling of Unicode new character forms (common-use forms, popular variants) is specified separately. For detailed collation notes, refer to `krm_notes` (for **`Compiler's Remarks`** on collation).       |
| character_order      | Indicates the numerical order of appearance of the character within its **`Headword`**.     |
| kazama_location_id   | An ID indicating the location of this constituent character in the Kazama Edition: K + Volume (2 digits) + Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character Order in Segment (1 digit).  |
| tenri_location_id    | An ID indicating the location of this constituent character in the Tenri Edition: T + Volume (a/b/c) + Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character Order in Segment (1 digit).   |
| img_file_name        | File name of the image for the constituent **`Headword`** character (including the .jpg extension). The main part of the file name consists of a 7-digit number for images from Volume 1 to Volume 9, and an 8-digit number for images from Volume 10. For 7-digit numbers, the first digit indicates the volume number; for 8-digit numbers, the first two digits indicate Volume 10. The last 6 digits are based on the order of appearance, assigned according to a unique internal rule. Detailed documentation for this naming convention is not available as the work was completed over two decades ago. Null if no image is available. |


## krm_wakun

### Overview and file formats

This data file is derived by extracting **`Japanese Native Readings (*wakun*)`** from the `KRM.tsv` file (an older version of `krm_main`) of the *Myōgishō* database, organizing variant forms of these **`wakun`**, and adjusting their correspondence with **`variant characters (*itaiji*)`**.

Collation notes and source investigations related to **`wakun`** are documented in the `krm_notes` file (which contains data for **`Compiler's Remarks`**), so they are omitted here.

In some **`wakun`** entries, different phonetic readings are presented side-by-side as annotations.
For example, the **`wakun`** "マサル" (masaru) is assigned to the **`Hanzi (Chinese character)`** "倍" (bai), but "ス" (su) is written in small katakana to the right of "ル" (ru) as an additional note. This indicates that the **`wakun`** "マス" (masu) is also noted in addition to "マサル" (masaru).

Since information from the JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) will be added to the **`wakun`** data, it is necessary to accommodate cases where variant forms of **`wakun`** are presented together.

The correspondence with **`variant characters (*itaiji*)`** has been adjusted because **`Headwords`** in the *Myōgishō* sometimes indicate such variants.
For example, the **`wakun`** "ヤツカレ" (yatsukare) appears in the **`Definition (Original Glosses)`** for the **`Headword(s)`** "㒒／僕". The **`wakun`** "ヤツカレ" is a **`Japanese Native Reading`** for "僕" (boku) and simultaneously for "㒒". The relationship between standard and variant forms such as "爲" and "為", or "來" and "来" is handled similarly.

The JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) has a "Notation" (表記) field that includes **`Hanzi (Chinese character)`** notations from the *Myōgishō*; this adjustment is a measure to ensure correspondence with that resource.

To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_wakun.tsv` and `krm_wakun.json`.


### Column name comparison

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
| -                       | Remarks       |

`Remarks` have been omitted as this type of information is now consolidated in the `krm_notes` file (data for **`Compiler's Remarks`**).


### Description of each column


Next, the content of the column names will be explained.

| New Column Name (v1.2.0)   | English Explanation (Final Revised)                                                                                                                                                                                                                                                           |
| :------------------------- | :-------------------------------------------------- |
| wakun_id                   | An ID for each **`Japanese Native Reading (*wakun*)`**. This is derived from `definition_seq_id` by extracting only those elements where the type (from `definition_type_name` in `krm_notes`) is **`Japanese Native Reading (*wakun*)`**. Suffixes 'b', 'c', 'd' are appended for variant forms. |
| definition_seq_id        | An identifier for each component of the **`Definition (Original Glosses)`** or for the **`Headword`** itself within an **`Entry`**. It is formed by appending a sequential suffix (e.g., "_00" for the **`Headword`** or overall **`Entry`** note, "_01", "_02" for subsequent elements of the **`Definition (Original Glosses)`** in order of appearance) to the 5-digit numeric part of the `entry_id`. (This ID links to records in `krm_notes`). |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book/volume, page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple **`Entries`** in a column. "Book(volume)" represents the volume number, "page(xxx)" the page number, "line(y)" the line number, and "column(zz)" the column number. |
| hanzi_entry              | The collated **`Headword`** (using **`Hanzi (Chinese characters)`**) to which this **`Japanese Native Reading (*wakun*)`** pertains. Principally Kangxi Dictionary forms, though Unicode-representable new forms (common-use, popular variants) may be retained.                                |
| wakun_elements           | Extracted elements of **`Japanese Native Readings (*wakun*)`** from the full **`Definition (Original Glosses)`**. Each record typically corresponds to one such element.                                                                                                            |
| wakun_form               | The lexical form of the **`Japanese Native Reading (*wakun*)`**. Inflected words are generally given in their dictionary (citation) form, excluding grammatical particles. The particles 'no' and 'to' from *Monzen* (文選) style readings are omitted.                                     |
| wakun_standard_hanzi     | Notation of the **`Japanese Native Reading (*wakun*)`** using standard **`Hanzi (Chinese characters)`**.        |
| wakun_variant_in_hanzi   | Notation of a variant form of the **`Japanese Native Reading (*wakun*)`** using standard **`Hanzi (Chinese characters)`**.    |
| variant_hanzi_for_wakun  | Notation of the **`Japanese Native Reading (*wakun*)`** using **`variant characters (*itaiji*)`** of **`Hanzi (Chinese characters)`**.     |
| japan_knowledge_id       | If this **`Japanese Native Reading (*wakun*)`** exists as a headword in the JapanKnowledge version of the *Nihon Kokugo Daijiten* (2nd Ed.), the alphanumeric part of its URL (from "20020" to the end) is recorded here. If it does not exist as a headword, "null" is entered.           |


## krm_definitions

The **`Definition (Original Glosses)`** in the *Myōgishō* is composed not only of **`Japanese Native Readings (*wakun*)`** but also other elements such as **`Notes on Character Form`**, **`Phonetic Glosses`**, and **`Semantic Glosses in Chinese`**.

The `KRM_definitions.tsv` file, which was previously released, provided these elements of the **`Definition (Original Glosses)`** categorized by type and ordered by their appearance. This dataset was created to facilitate collation and source investigation.

Following the specification changes implemented in March 2025, the data and functionalities previously found in `KRM_definitions.tsv` have been integrated into the `krm_notes` file (which contains data for **`Compiler's Remarks`** and detailed analyses of these original gloss elements). Consequently, a separate detailed explanation for `krm_definitions` is omitted here.


## krm_pronunciations

### Overview and file formats

The **`Phonetic Glosses`** in the Kanchi-in manuscript of the *Ruiju Myōgishō* (hereafter *Myōgishō*) include **`Fanqie spellings`** (反切), **`Similar sound notes`** (類音注, *ruion-chū*), and **`Kana glosses`** (仮名注, *kana-chū*). These are often accompanied by **`Tone marks (*shōten*)`**.
As a database for Sino-Japanese character pronunciations, the **"Database of Historical Sino-Japanese Readings"** (abbreviated as DHSJR), developed by Professor Katō Taitsuru and others, offers exceptionally rich content. Its specifications are also publicly available in detail. We are currently considering releasing data aligned with the DHSJR specifications.

The DHSJR defines a data structure with 23 column names.

To facilitate linkage with the *Myōgishō* data included in HDIC, it is necessary for HDIC to assign unique column names to its own data files and to establish Primary Keys and Foreign Keys for interoperability between HDIC's internal data files.

For this purpose, `pronunciation_id` (音注ID) has been set as the Primary Key, and `definition_seq_id` (注文ID) as the Foreign Key.

Since the *Myōgishō* features diverse formats for its **`Phonetic Glosses`**, a classification field named `annotation_format` (音注型) has been established to categorize them.

While DHSJR uses Japanese column names, HDIC employs English ones. Therefore, for data processing convenience within HDIC, English column names have been adopted.

### Column name comparison

The current draft, with English and Japanese explanations side-by-side, is as follows. The Japanese explanations are those stipulated by DHSJR. The English explanations are formulated to facilitate correspondence with HDIC. This is a provisional measure until official English explanations are released by DHSJR.

HDIC's original column names are indicated in **bold**.

| DHSJR (Japanese) | HDIC (English)            | Key         | English Explanation                                                                 | Japanese Explanation (from DHSJR)                     |
| :--------------- | :------------------------ | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| ID               | dhsjr\_id                  |             | DHSJR unique ID for each single **`Hanzi (Chinese character)`** (integrated data only)                                                                                                                                                                                                            | 単字ごとのユニークID（統合データのみ）                            |
| **音注ID** | **`pronunciation_id`** | Primary Key | ID for each **`Phonetic Gloss`**. This is derived from `definition_seq_id` by extracting only those elements where the type (from `definition_type_name` in `krm_notes`) is **`Phonetic Gloss`**. Suffixes 'b', 'c', 'd' are appended for variant forms.                                           | 音注ID。kr\_definition\_sequence\_idから、注文の種類が音注のものだけを取り出したもの。変異形を追加したものには末尾にxを付した。 *(User indicates 'x' is incorrect, and 'b,c,d' is correct for variants)* |
| **注文ID** | **`definition_seq_id`** | Foreign Key | An identifier for each component of the **`Definition (Original Glosses)`** or for the **`Headword`** itself within an **`Entry`**. It is formed by appending a sequential suffix (e.g., "\_00" for the **`Headword`**, "\_01", "\_02" for subsequent elements) to the corresponding `entry_id`. | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に\_01、\_02のように追加したもの。見出しには\_00を追加する。 |
| 資料番号         | material\_id               |             | Material ID                                                                                                                                                                                                                                                                                     | 資料ID                                                |
| 資料名           | material\_name             |             | Name of the material                                                                                                                                                                                                                                                                            | 資料の名称                                            |
| 資料内漢字番号   | material\_character\_index  |             | Sequential number of a **`Hanzi (Chinese character)`**'s appearance in the material                                                                                                                                                                                                            | 漢字の資料内出現順の通し番号                                |
| 資料内漢語番号   | material\_word\_index       |             | Sequential number of a Chinese word's appearance in the material                                                                                                                                                                                                                              | 漢語の資料内出現順の通し番号                                |
| 単字\_見出し      | character\_headword        |             | **`Headword`** column for **`Hanzi (Chinese characters)`** with **`Phonetic Glosses`** | 音注が付された漢字の見出し列                                  |
| 単字\_出現形      | character\_form            |             | **`Hanzi (Chinese characters)`** that have **`Phonetic Glosses`** | 音注が付された漢字                                        |
| 漢語\_見出し      | word\_headword             |             | **`Headword`** column of Chinese words containing **`Hanzi (Chinese characters)`** with **`Phonetic Glosses`** | 音注が付された漢字を含む漢語の見出し列                              |
| 漢語\_出現形      | word\_form                 |             | Chinese words containing **`Hanzi (Chinese characters)`** with **`Phonetic Glosses`** | 音注が付された漢字を含む漢語                                  |
| 漢語\_alphabet  | word\_alpha                |             | Entered when there is an alphabetic representation of the Chinese word                                                                                                                                                                                                                          | 欧文による漢語の表記がある場合に入力されている。                                |
| 語種             | word\_type                 |             | Indicates the word type when there are mixed-language words (e.g., hybrid Sino-Japanese words)                                                                                                                                                                                              | 混種語がある場合に、語種を示す。                                  |
| 漢語内位置       | word\_position             |             | Position of the single **`Hanzi (Chinese character)`** within the Chinese word                                                                                                                                                                                                                  | 漢語内での単字の位置                                      |
| 単字長           | character\_mora\_count      |             | Number of morae for the single **`Hanzi (Chinese character)`** | 単字の拍数                                            |
| 声点             | tone\_marks                |             | **`Tone marks`** for single **`Hanzi (Chinese characters)`**, indicating Four Tones (平上去入), Six Tones (平平軽上去入軽入), and voicing (清濁).                                                                                                                                                     | 単字に対する四声（平上去入）、六声（平平軽上去入軽入）及び清濁。                    |
| 声点型           | tone\_pattern              |             | Combination of **`Tone marks`** for Chinese words. **`Hanzi (Chinese characters)`** without **`Tone marks`** are represented by a full-width asterisk (＊).                                                                                                                                      | 漢語に対する声点の組合せ。声点がない単字については＊で表す。                        |
| 仮名注           | kana\_notes                |             | **`Kana glosses`** (仮名注) for **`Hanzi (Chinese characters)`**, including kana-based *fanqie*.                                                                                                                                                                                             | 仮名表記による字音注（仮名反切を含む）                                |
| 仮名型           | kana\_pattern              |             | Combination of **`Kana glosses`** for Chinese words. **`Hanzi (Chinese characters)`** without **`Kana glosses`** are represented by a full-width asterisk (＊).                                                                                                                                    | 漢語に対する仮名注の組合せ。仮名注がない単字については＊で表す。                      |
| 反切             | fanqie                    |             | **`Fanqie spellings`** (反切) for single **`Hanzi (Chinese characters)`**.                                                                                                                                                                                                                   | 単字に対する反切注                                        |
| 類音             | similar\_sound             |             | **`Similar sound notes`** (類音注) for single **`Hanzi (Chinese characters)`**.                                                                                                                                                                                                                | 単字に対する類音注                                        |
| **音注型** | **`annotation_format`** |             | Pattern of combined phonetic information (e.g., **`Kana glosses`**, **`Fanqie spellings`**, **`Similar sound notes`**, **`Tone marks`**).                                                                                                                                                         | 仮名注、反切、類音、声点などの複数の音注が組み合わさった形式のパターン。                  |
| 節博士           | fushi\_hakase              |             | **`Fushi-hakase notations`** (melodic or intonational markings) attached to musical materials such as *Shōmyō* (Buddhist chant).                                                                                                                                                              | 声明等音楽資料に付される博士譜など                                |
| その他           | other\_phonetic\_annotations|             | Other types of **`Phonetic Glosses`**.                                                                                                                                                                                                                                                           | その他の音注                                            |
| 出現位置         | material\_location         |             | Location of single **`Hanzi (Chinese characters)`** and Chinese words within the material.                                                                                                                                                                                                      | 資料内の単字・漢語の所在                                    |
| 備考             | remarks\_pronunciation     |             | Matters to be noted regarding these phonetic elements.                                                                                                                                                                                                                                          | 注記すべき事柄                                            |

The `material_location` is indicated in the format: K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit). For example, `K0201474` indicates an appearance in Volume 2, Page 14, Line 7, Segment 4.

Currently, this is under consideration in the case study "[Linkage with DHSJR](/docs/krm/08-case-studies/5-dhsjr/)," which should also be consulted.



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



