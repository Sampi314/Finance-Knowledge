# Errors with Data Analysis Course » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/errors-with-data-analysis-course

---

Thanks for watching the “**[Beginner to PRO Data Analysis Course](https://www.youtube.com/watch?v=v2oNWja7M2E)
**” video.

If you are having troubles with the course work, here is some help.

Can’t change part of array ERROR
--------------------------------

![](https://chandoo.org/wp/wp-content/uploads/2022/01/cant-change-part-of-array-error.png)

FIX for the ERROR
-----------------

You have two options.

**Option 1:** Instead of using UNIQUE() for country names, just have the values typed in the cell (you can copy paste the formula as value). Then you can sort the table normally.

**Option 2:** Change all formulas to **_array version_** so the table is _automatically sorted._

To do this, you need to update the formulas like this.

*   **Country column** =SORTBY(UNIQUE(data\[Geography\]), SUMIFS(data\[Amount\], data\[Geography\], UNIQUE(data\[Geography\])),-1)
*   **Amount** =SUMIFS(data\[Amount\], data\[Geography\],C6#)
*   **Bar** =D6#
*   **Units** \=SUMIFS(data\[Units\], data\[Geography\],C6#)

See this illustration:

![](https://chandoo.org/wp/wp-content/uploads/2022/01/fix-for-the-error.png)