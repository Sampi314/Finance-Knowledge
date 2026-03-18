# Multiple Check Boxes

**Source:** https://edbodmer.com/multiple-check-boxes-for-creating-graphs

---

If you want multiple series options to put on a graph, you can add check boxes instead of using the list box. This page demonstrates how you can copy a whole bunch of check boxes and attach each check box to a TRUE/FALSE switch.  With the multiple check box macros you can create graphs that find only the check boxes that have an associated with TRUE.

The most difficult thing about this is copying the check boxes when you may have more than 100 different possible selections. To do this I have make a macro in the file available for downloading below. It is not perfect and you have to be careful when operating it. The first step is to copy the check boxes and make sure that you have new numbers for the check box (that you can find with looking at a macro as demonstrated below). You cannot do this with manual calculation. After copying the checkbox you can run the macro with SHIFT, CNTL, E. As with other macros, save your file before running the macro.

**[Excel File with Macro that Allows you to Attach Many Check Boxes to Adjacent TRUE/FALSE Inputs (Shift, CNTL, E)](https://edbodmer.com/wp-content/uploads/2018/05/Attach-Multiple-Checkboxes.xlsm)
**

Using the Attach Check Box Macro
--------------------------------

To attach a whole bunch of check boxes, you can copy a lot of check boxes and then use the TRUE or FALSE created by the check boxes to count the number of selections. This process of attaching the TRUE/FALSE is illustrated in the screen shots below.  When you open the file, the following appears and the SHIFT, CNLT, E macro that attaches TRUE/FALSE is implemented.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-1.jpg)

Now say that you have  list of stock prices, countries, accounts or anything else that you want to graph in a flexible manner with check boxes. I have used the Sun Edison (bankruptcy) example as illustrated in the screen shot below.  In this example we will make a graph of any of the items in the income statement with multiple check boxes.  Using the SHIFT, CNTL, E, the process should just take minutes.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-2.jpg)

The file with the completed example is available for download by pressing the button below.  The completed file has a number of check boxes whereby you can graph any of the items.

**[Sun Edison Bankruptcy Case Study with Example of how to Use Multiple Check Boxes and Flexible Graphs](https://edbodmer.com/wp-content/uploads/2018/05/Sun-Edison-Case-Study.xlsm)
**

With the attach check boxes file open, the next step is to make one check box and one TRUE false that can be copied downward.  This is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-3.jpg)

You can then copy the TRUE and the check box down.  Then find the number of the check box by right clicking and assigning a macro (do not attach a macro unless you want to; this is just to find the check box number that will be incremented. Note that in the example, the number of the check box is 1.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-5.jpg)

Once you have copied the check boxes and found the number, you can run the SHIFT, CNTL, E function. This function needs the start row and the end row as well as the check box number and the row for the TRUE/FALSE.  The screenshot below shows what will come up after you run the macro. When you get the screen, fill in the row start and row end as well as the check box number.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-6.jpg)

After you have run the macro, the check boxes should be each attached to a separate TRUE/FALSE. You should try to press different check boxes and see if the process really works.  After you have the check boxes you can move to the next step and make the graphs.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-7.jpg)

Process of Using Multiple Check Boxes to Create a Flexible Graph
----------------------------------------------------------------

Since you know that TRUE is 1 and FALSE is zero, you can create a column that counts the trues by adding the check boxes that are counted. This counter can then be matched against a counter variable to find the items that have been checked. You add a separate counter (you can use ALT, E, I, S) and then apply the MATCH function to find the number of the selection. Finally, use the INDEX function to put the items that are checked at the top. This process is illustrated below from the comprehensive stock price file.  This process is illustrated in the series of screen shots below.  The first screen shot simply shows how to accumulate the number of TRUES by making a cumulative counter.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-8.jpg)

The next screen shot demonstrates how to use the accumulation counter and the MATCH function to find the appropriate row with the first and second and third TRUE etc. This is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-9.jpg)

As usual, after the MATCH you can use the INDEX function.  The MATCH and INDEX functions can then be copied and used to make the graph.  The INDEX function is illustrated in the final screen shot below.

![](https://edbodmer.com/wp-content/uploads/2018/05/Attach-10.jpg)

Assuring that NA and Blanks are not on the Legend of the Graph
--------------------------------------------------------------

It is tricky to put a legend without #NA in the graphs after you have made the flexible graphs with the multiple check boxes.  You can make a dynamic range with the OFFSET function (by putting in the number of rows and columns in the height and width option).  To make the range name stay in the graph, or more precisely, change the graph when the listbox changes, you can make a little VBA code.  This re-does the data source when you change the list box.

![](https://edbodmer.com/wp-content/uploads/2018/05/Listbox-5.jpg)

A file that includes the VBA code to create flexible charts with legends that change is available for download by clicking on the button below. In this file you can press the CNTL and F3 sequence to see the dynamic range name.  This range name (graph\_data) changes when the list box changes and different numbers of graphs are selected. When you click the box named “adjust legend”, the legend should change.

**[Excel File with List Box and VBA Code that Allows you to Adjust the Legend when the Number of Series Changes](https://edbodmer.com/wp-content/uploads/2018/05/Exercise-without-NA-on-Graph.xlsm)
**

The VBA code that allows you to remove the blanks or the #NA’s from the legend is shown below.  You can either code into the macro for the listbox or you can include a separate macro. Of course, you need to find the name of your chart and adjust the macro accordingly.

Sub Adjust\_legend()
'
'
 current\_cell = ActiveCell.Address
 
 ActiveSheet.ChartObjects("Chart 8").Activate

ActiveChart.SetSourceData Source:=Range("graph\_data")
 
 Range(current\_cell).Activate
 
End Sub

Video Explanation of Multiple Check-Boxes to Make Flexible Graphs
-----------------------------------------------------------------

The process for creating check boxes is illustrated below from the template file named “Attach Multiple Check boxes.”   The file associated with this video is the file that you can download above.  There may have been a couple of improvements in the file since I first made the video.

VBA Code for Attaching Check Boxes
----------------------------------

The VBA code that attached the list boxes is presented below.

.

Public Sub Auto\_Open()
'
' Make a menu with an add-in
'
 Application.OnKey "^E", "attach\_check"

Application.StatusBar = "SHIFT,CNTL,E --> Create Check Box Links "

start\_row = 4
end\_row = 33
start\_box = 1
col\_link\_letter = "F"

End Sub

Sub auto\_close()
 
 Application.OnKey "^E"
End Sub


Sub attach\_check()

UserForm1.TextBox1 = start\_row
UserForm1.TextBox2 = end\_row
UserForm1.TextBox3 = start\_box
UserForm1.TextBox4 = col\_link\_letter

UserForm1.Show

start\_row = Val(UserForm1.TextBox1)
end\_row = Val(UserForm1.TextBox2)
start\_box = Val(UserForm1.TextBox3)
col\_link\_letter = UserForm1.TextBox4

current\_sheet\_name = ActiveSheet.Name
sheet\_name = "'" & current\_sheet\_name & "'!"
Count = 0

start\_box = start\_box
range\_box = "Check Box " & start\_box
For Row = start\_row To end\_row
   range\_box = "Check Box " & start\_box + Count
   range\_name = col\_check\_letter & Row
   On Error GoTo make\_sure\_copy:
   ActiveSheet.Shapes.Range(Array(range\_box)).Select
   On Error GoTo 0
   link\_name = sheet\_name & col\_link\_letter & Row
   Application.CutCopyMode = False
   With Selection
     .Value = xlOn
     .LinkedCell = link\_name
     .Display3DShading = False
   End With
 Count = Count + 1
Next Row

Exit Sub
exitsub:
MsgBox " make sure you have the correct checkbox number:"
Exit Sub
make\_sure\_copy:
MsgBox " Make Sure you Copy and Calculation is on when you copy "
End Sub

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3577&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=14560&rand=0.14127616352338812)