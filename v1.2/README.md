# Overview of Public Data

Ikeda Shoju

28 March, 2025

This document provides an overview of the data from the Kanchi-in manuscript of the Ruiju Myogisho, which is publicly available at [https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC).

- krm_main
- krm_notes
- krm_wakun
- krm_definitions
- krm_pronunciations
- krm_ndl

A significant specification change was implemented in March 2025. Previously, the published files were prefixed with "KRM," but the files following this specification change will be prefixed with "krm."

The files incorporating the specification changes have been placed in the "v2" folder. Please note that this is a temporary arrangement.

# krm_main

This document explains the core file of the Kanchi-in manuscript of the Ruiju Myogisho (hereinafter referred to as "Myogisho") database. The file previously made public was a TSV file named KRM.tsv.

It includes information regarding head characters, definitions, volumes, radicals, and the locations in the Kazama Shobo edition and the Tenri Zenpon Sosho edition.

In March 2025, the specifications for column names and the display method of tone marks were changed. To clearly indicate that it is the file after the specification change, it was named krm_main.tsv. A JSON format is also available for this file.

The comparison of the new and old column names is as follows:

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

Remarks have been omitted and will be summarized in the following krm_notes file.


Next, the content of the column names will be explained.

| New Column Name (v1.2.0)|Explanation|
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F', followed by '_00'.                                                                                                                                                                                                                                                                         |
| hanzi_id                 | A heading Hanzi ID consisting of a 5-digit numeric ID starting with 'S'.                                                                                                                                                                                                                                                                                       |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number.                                                              |
| kazama_hanzi_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 0 for single-character headwords, and 1, 2, ..., n for multiple-character headwords or entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. |
| tenri_location           | Location information from the Tenri edition (T, volume(volume letters), page(xxx), line(y), column(zz)). Where volume(volume letters) represents the volume letters, page(xxx) the page number, line(y) the line number, and column(zz) the column number.                                                                                                     |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.                                                                                                                                                                                                                                                                    |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.                                                                                                                                                                                                                                                  |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.                                                                                                                                                                                                                                                 |
| hanzi_entry              | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.                                                                                                                                                                                                                                          |
| original_entry           | Original Hanzi character representations, retaining errors from the original text, with non-Unicode variants expressed using IDS or 〓.                                                                                                                                                                                                                         |
| definition               | Includes glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and other relevant notes, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.  |


## krm_notes

A new file, krm_notes.tsv, has been created, containing detailed annotation information added to the KRM_def.tsv file.

This is available in both TSV and JSON formats. To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names krm_notes.tsv and krm_notes.json.

Considering krm_notes.tsv as the new file and KRM_definitions.tsv as the old file, the comparison of their column names is as follows:

| New Column Name (v1.2.0) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_entry_location    | KR2ID                      |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks_definition       | Remarks                    |

Next, the content of the column names will be explained.

| New Column Name (v1.2.0) | Explanation              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| definition_seq_id        | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. |
| hanzi_entry              | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.                                                                                                                                                                             |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per entry.                                                                                   |
| definition_type_code     | 3-digit numeric code representing the definition type.       |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, wakun, and others.                                                                                                                               |
| remarks_definition       | Editor's notes providing additional context or information.       |

## krm_wakun
This data is derived by extracting wakun from the KRM.tsv file of the Myogisho database, organizing variant forms of the wakun, and adjusting their correspondence with variant characters (itai-ji).

Collation and textual research related to wakun are documented in krm_notes, so they are omitted here.

In wakun, different readings may be written alongside the main reading as annotations.

For example, the wakun "マサル" (masaru) is assigned to the character "倍" (bai), but "su" is written in small katakana to the right of "ル" (ru) as an annotation. This indicates that the wakun "マス" (masu) is annotated in addition to "マサル" (masaru).

Since information from the JapanKnowledge version of the Nihon Kokugo Daijiten (Second Edition) will be added to the wakun, it is necessary to accommodate cases where variant forms of wakun are written together.

The handling of variant characters involves cases where variant forms are indicated for the head character, and this data has been adjusted to account for them.

For example, the wakun "yatsukare" appears in the definition for the head characters "㒒/僕". The wakun "yatsukare" is a wakun for "僕" (boku) and is simultaneously a wakun for "㒒". The relationship between standard and variant forms such as "爲" and "為", or "來" and "来" is similar.

The JapanKnowledge version of the Nihon Kokugo Daijiten (Second Edition) has a "Notation" field that includes the kanji notations from the Myogisho, so this adjustment is a measure to ensure correspondence with it.

To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names krm_wakun.tsv and krm_wakun.json."

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


Remarks have been omitted and will be summarized in the following krm_notes file.

Next, the content of the column names will be explained.

| New Column Name (v1.2.0)      | Explanation        |
|-------------------------|------------------|
| wakun_id                | Wakun ID, extracted from kr_definition_sequence_id, containing only entries where the type of order is Japanese reading (wakun). Variant forms are appended with 'b', 'c', 'd'.          |
| definition_seq_id       | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      |
| kazama_entry_location   | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. |
| hanzi_entry             | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.         |
| wakun_elements          | Extracted Japanese reading (wakun) components from the full definition, one component per entry.  |
| wakun_form              | Form of the Japanese reading (wakun). Inflected words are in dictionary form, excluding particles. The particles 'no' and 'to' from 文選 readings are omitted. |
| wakun_standard_hanzi    | Standard wakun notation using standard kanji.      |
| wakun_variant_in_hanzi  | Variant form of wakun notation using standard Hanzi characters.      |
| variant_hanzi_for_wakun | Wakun notation using variant Hanzi characters (itai-ji).           |
| japan_knowledge_id      | The alphanumeric part of the JapanKnowledge URL, from 20020 to the end.    |

## krm_definitions

The definitions in the Myogisho include not only wakun but also elements such as glyph annotations, pronunciation annotations, and meaning annotations.

This file contains records created by categorizing each element of the definitions according to their order of appearance, assigning them numbers based on this order, and classifying the types of definitions. This was done for the purpose of collation and textual research.

The file previously made public was KRM_definitions.tsv.

After the specification change in March 2025, this information has been integrated into krm_notes, so a separate explanation will be omitted here.

## krm_pronunciations

The pronunciation annotations (on-chū) in the Myogisho include fanqie, similar-sound annotations, and kana annotations, and these often have tone marks applied to them.

As a database of Japanese kanji pronunciations, the "Database of Historical Sino-Japanese Readings" (abbreviated DHSJR), created by Professor Daikaku Kato and others, boasts very comprehensive content. Furthermore, its specifications are also published in detail.

We are currently considering publishing our data in accordance with the DHSJR specifications.


## krm_ndl

This file compiles links to the images of the Kanchi-in manuscript of the Ruiju Myogisho that are publicly available in the National Diet Library Digital Collections.

This data cross-references the locations within the Kanchi-in manuscript of the Ruiju Myogisho with their corresponding URLs in the National Diet Library Digital Collections. The file name is KRM_ndl.tsv.

The KRM_ndl.tsv file was largely unaffected by the specification changes in March 2025, so a detailed explanation will be omitted here.