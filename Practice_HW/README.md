# Digital Avionics Practice Homework

範圍：Handouts 1–7，共 44 題、23 頁。這是自編練習題，非教師正式作業；保留作答空間，不含解答。

- `digitalAvionics_practice_hw.pdf`：可閱讀、列印的題本。
- `digitalAvionics_practice_hw.tex`：可編輯的 LaTeX 原始檔。
- 同名 `.aux`、`.log`、`.out`、`.synctex.gz`：編譯及編輯器同步定位檔案。

| 題號 | 範圍 |
| --- | --- |
| 1–20 | 原有 Handouts 1–4 練習，內容保留 |
| 21–28 | Handout 5：FBW 架構、閉迴路、操縱品質、備援與故障管理 |
| 29–36 | Handout 6：INS、慣性感測器、姿態、座標轉換、誤差與整合導航 |
| 37–44 | Handout 7：GPS 架構、偽距、時鐘與誤差、訊號、DGPS、導航性能、SBAS/GBAS |

新增題目的頁碼指根目錄原講義 PDF 的頁序。數值計算題採自編參數，簡化假設均於題內說明；GPS 接收機時鐘未知量列為延伸練習。原講義 PDF 保留於上一層資料夾。

在此資料夾編譯：

```powershell
xelatex -interaction=nonstopmode -halt-on-error -synctex=1 digitalAvionics_practice_hw.tex
```

需 XeLaTeX、xeCJK 與 Microsoft JhengHei（或 FandolSong-Regular）字型。
