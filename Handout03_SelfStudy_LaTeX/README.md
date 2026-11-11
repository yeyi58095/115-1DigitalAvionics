# Handout 3：基礎氣動與縱向靜穩定

沿用 `Chapter03_SelfStudy_LaTeX` 的繁體中文 Beamer 版型與自讀方式。

已產生閱讀版：62 頁。

範圍：Handout 3 與既有 Chapter 3 的氣動、配平、穩定性自讀詳解。

- `handout03_slides.pdf`：閱讀版，含書籤。
- `handout03_slides.tex`：可修改的自讀詳解，含概念、原頁、算例、自我檢查及參考解答。
- `figures/`：本份需要的講義原頁與課本原圖。所有圖片都在此資料夾內，搬移時請一起保留。
- `FIGURE_INDEX.md`：主題、原講義頁序及原圖對照。
- `compile.ps1`：以 XeLaTeX 編譯兩次，將完成 PDF 放回本資料夾。
- `build/`：編譯紀錄、內容索引與預覽，均屬本份建置資料。

原始講義 `CA7528_Digital Avionics Handout #3_20260923_update.pdf` 保留於上一層，編譯不需要跨資料夾讀取該檔。

閱讀次序為概念、原圖、先自行作答、參考解答。講義 PDF 頁序與課本印刷頁碼會分別標明。
算例依題內假設使用，歷史表格與法規敘述不視為現行規範。核對說明是自讀整理，非正式勘誤。

## 編譯

在本資料夾執行：

```powershell
.\compile.ps1
```

使用本機 XeLaTeX、Beamer、ctex、pgfplots 與 Microsoft JhengHei 字型。
