# #N/A Fix for Multiple Series

**Source:** https://edbodmer.com/making-the-na-not-appear-on-graphs-with-multiple-series

---

This webpage explains how to make a graph really flexible where you can a different number of series on a graph. For example when you have list boxes that allow you select different numbers of series, you do not want the irritating #N/A’s to appear.  To fix this you can create a flexible range name using the OFFSET function. You will have to make a little macro to re-set the graph area and find the name of the graph. When you create a graph with the list box and use the MATCH and INDEX process, the graph will have #N/A’s for potential series that are not selected. This has been an irritation for me for years. It is tricky to put a legend without #NA in the graphs after you have made the flexible graphs, but it can be done. The screenshot below illustrates the problem where series that are not graphed have the #N/A.

The Problem
-----------

If you have a potential area that is large and you do not use all of the area that is covered, the reserved series will not be used and you will see the #N/A function.  The lines that are not graphed are shown on the line on the bottom. The area that is selected is large enough to cover four additional lines.

![](https://edbodmer.com/wp-content/uploads/2018/07/Flexible-Graphs-NA.jpg)

The reason the #N/A’s appear is that the area of the graph must be large enough to capture the maximum amount of series that you would like to appear on the graph.  The graph area that is larger than the amount of actual series that are graphed is illustrated on the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/07/Flexible-Graph-Area.jpg)

### Fixing the Problem Step 1: Create Flexible Range Name with Offset

To fix the problem, one way is to make the area more flexible. I thought you could use the OFFSET function with a dynamic range name and then put this into the chart data range as illustrated in the screenshot below.  This does not work without a little macro.  When you make the dynamic range with the OFFSET function (by putting in the number of rows and columns in the height and width option), the range name does not stay in the graph.

To fix the problem, you still have to make a flexible range name with different number of columns.  The number of series to graph and the length of the graph should be defined somewhere.  These are the parameters for the height and width of the dynamic range as illustrated below.  The start row and the start column should generally be zero.  A dynamic range name created with the OFFSET function that uses length and width is illustrated below.  Note that the number of rows and the number of columns must include space for the x-axis and the y-axis.  Note that there are two zeros in the offset function.  You can press the CNTL and F3 to find this.

![](https://edbodmer.com/wp-content/uploads/2018/07/Graph-with-NA-1.jpg)

### Fixing the Problem Step 2: Create VBA Code to Define Graph Range

You may think all you have to do is to put the flexible range name in the data range part of the graph. This unfortunately does not work as the range name is not maintained when you change the number of series.  The screen shot below was taken after I put a range name called graph\_data into the chart data range.  After clicking again on the chart, the range name goes away.

![](https://edbodmer.com/wp-content/uploads/2018/05/Listbox-5.jpg)

To make the range name stay in the graph, or more precisely, change the graph when the listbox changes, you can make a little VBA code.  You need to first activate the chart name.  You can find the chart name by right clicking on the chart name and then going to assign macro. You do not have to assign a macro, just do this to find the chart name. In the screenshot below, the chart name is chart1.

![](https://edbodmer.com/wp-content/uploads/2018/07/Flexible-Graph-Chart-Name.jpg)

After you find the chart name, copy the VBA code at the end of this webpage into your file. You can press the ALT, F8 key sequence and then edit any macro.  Just copy the macro and modify the chart name and, if necessary, the range name.

Finally, create a button with something like “update chart” as the name.  Then assign the macro you just copied to that range name. The final chart should look something like below.  Now, when you change the number of series on the graph, you should hit the update button. (Note, you may have to work with the x-scale a bit).

![](https://edbodmer.com/wp-content/uploads/2018/07/Flexible-Graph-Finished.jpg)

File that Includes Example of Adjusting the #N/A Legend Problem
---------------------------------------------------------------

A file that includes the VBA code to create flexible charts with legends that change is available for download by clicking on the button below. In this file you can press the CNTL and F3 sequence to see the dynamic range name.  This range name (graph\_data) changes when the list box changes and different numbers of graphs are selected. When you click the box named “adjust legend”, the legend should change.

**[Excel File with List Box and VBA Code that Allows you to Adjust the Legend when the Number of Series Changes](https://edbodmer.com/wp-content/uploads/2018/05/Exercise-without-NA-on-Graph.xlsm)
**

The VBA code that allows you to remove the blanks or the #NA’s from the legend is shown below.  You can either code into the macro for the listbox or you can include a separate macro.

Sub Adjust\_legend()
'
'
   current\_cell = ActiveCell.Address
 
   ActiveSheet.ChartObjects("Chart 8").Activate

   ActiveChart.SetSourceData Source:=Range("graph\_data")
 
   Range(current\_cell).Activate
 
End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9071&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11768&rand=0.7494136066988328)