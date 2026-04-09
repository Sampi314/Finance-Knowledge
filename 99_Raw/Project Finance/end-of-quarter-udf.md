# End of Quarter UDF

**Source:** https://edbodmer.com/end-of-quarter-udf

---

This sheet shows you how to create an end of quarter function and an end of half year function that can be useful in creating quarterly summaries from monthly data. The videos below explain how to roll-up data using the SUMIF or SUMIFS along with the end of quarter function.

.

Function eoqtr(date1)

month\_of\_date = Month(date1)

If month\_of\_date = 1 Or month\_of\_date = 4 Or month\_of\_date = 7 Or month\_of\_date = 10 \_
 Then eoqtr = WorksheetFunction.EoMonth(date1, 2)

If month\_of\_date = 2 Or month\_of\_date = 5 Or month\_of\_date = 8 Or month\_of\_date = 11 \_
 Then eoqtr = WorksheetFunction.EoMonth(date1, 1)

If month\_of\_date = 3 Or month\_of\_date = 6 Or month\_of\_date = 9 Or month\_of\_date = 12 \_
 Then eoqtr = WorksheetFunction.EoMonth(date1, 0)


End Function


.

Videos the Explain how and why to Use End of Quarter
----------------------------------------------------

The videos below describe how and why to use the end of quarter function.

.

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3696&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11048&rand=0.5912032409830594)