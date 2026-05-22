# ZRM Changelog

## 2026-05-21
- Text creation and proofreading were carried out by IKEDA Shoju and Shin Woongchul.
- Published `ZRM.tsv` in the HDIC directory as the full text version of the Zushoryōbon *Ruiju Myōgishō* dataset.
- Updated the file name from the working draft style to the public release name `ZRM.tsv`.
- Standardized the metadata header in `ZRM.tsv`:
    - `Version: 1.1.1`
    - `Date: 21 May 2026`
    - `Last update : 21 May 2026`
- Rebuilt the TSV from `zrm_processed_elements_v3.xlsx` (`zrm_main_shin` sheet).
- Mapped the following columns into the release TSV:
    - `entry_id`
    - `radical_index`
    - `radical_name`
    - `page`
    - `entry`
    - `definition`
    - `url`
    - `remarks`
- Converted multi-line definition text into single-line TSV values.
- Generated `url` values from page numbers using the Imperial Household Agency viewer URL with `page + 1`.
- Added `remarks` values from `ZRM20190225.xlsx` (`ZR_remarks`) when available.
- Preserved parenthetical `（ ）` notes and square-bracket `【 】` notes in the `definition` field for the current release.
- Added explanatory notes in the TSV header describing the current treatment of these annotations.

## Notes
- This changelog records public-facing updates to the HDIC release file `ZRM.tsv`.
- When a release changes file naming, metadata headers, column meanings, or public usage notes, related documentation such as `README.md` should be reviewed and updated as needed.
- Working notes, exploratory scripts, and temporary files in the `zrm` workspace are not necessarily listed here unless they directly affect the released dataset.
