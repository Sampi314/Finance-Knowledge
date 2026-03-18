# Power BI Blog: Highlight Event Periods – Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Highlight Event Periods – Part 2

*   January 31, 2024

Power BI Blog: Highlight Event Periods – Part 2
===============================================

Power BI Blog: Highlight Event Periods – Part 2
===============================================

1 February 2024

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/highlight-event-periods-part-1)
, we introduced to you our combination (“combo”) visual that highlights event periods and displays the events’ names.

![](<Base64-Image-Removed>)

The visual is built upon a simulated sales dataset for 2020 and detailed events in the year. We went through data preparation and the first chart measure last week. This week, we will go through the other measures and complete the combo visual. You can download our [data workbook](https://sumproduct.com/assets/blog-pictures/2022/pbi/311/financial-sample.xlsx)
 and [sample file](https://sumproduct.com/assets/blog-pictures/2022/pbi/311/sp-event-highlights.pbix)
 to follow along.

**_Error Bar Measures_**

The first measure for the labelling error bar is **Event Marker Bottom**, height of the bottom of the error bar, which is also the top of the column.

**Event Marker  
Bottom = CALCULATE(\[Sales value\], ‘Calendar'\[Date\] = MAX(Events\[Start\]))**

Here, we use the function **CALCULATE** with a filter that the current date equals the start date of an event. The next measure **Event Marker Top** is height of the top of the labelling error bar. We find out the maximum sales of the month and multiply a factor to set the height.

**Event Marker Top =  
VAR Height = MAXX(ALLSELECTED(‘Calendar’), \[Sales value\]) \* 1.3  
RETURN IF(SELECTEDVALUE(‘Calendar'\[Date\]) in VALUES(Events\[Start\]), Height)**

Here, the function **ALLSELECTED** returns all dates of the selected month, and **MAXX** function calculates the maximum sales in the month. We multiply a factor bigger than one \[1\] to define the variable **Height** (_e.g._ 1.3 here), and we output the variable only when the current date is the start date of an event.

Now we can choose **Event Market Top** as the chart’s Line **y**\-axis, and in **Format -> Visual -> Error bars** we enable error bars for **Event Marker Top** and select **Event Market Bottom** as its **Lower bound**.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Now comes the key to labelling names of the events on chart. First, in **Format -> Visual -> Data labels**, we turn on data labels for **Event Market Top** and off for **Sales values**.

![](<Base64-Image-Removed>)

The Data label is still a numerical value on top of the label stick. We need to go to **Table view**, select the measure **Event Marker Top** and in **Measure tools** select **Dynamic** format.

![](<Base64-Image-Removed>)

On the left-hand side of the Formula bar, we select **Format** from the drop-down and then type in (without the equal sign ‘**\=**‘)

**MAX(Events\[Title\])**

![](<Base64-Image-Removed>)

That way, the measure **Event Marker Top** uses the current event’s title as its format, and we will also see the event title on the Data label. Lastly, we make sure the **Secondary y-axis** option is turned off in **Format -> Visual**.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

**_Adjust Y-Axis_**

Since we are labelling names of events on top of the columns, we need to extend the maximum of the **y**\-axis for presentation. Here, we use a similar idea as for **Event Marker Top** to define a measure for setting the **y**\-axis maximum:

**Y Axis Max =  
VAR EventInMonth\_Flag = INT(COUNTROWS(Events) > 0)  
VAR Month\_Max = MAXX(ALLSELECTED(‘Calendar’), \[Sales value\])  
RETURN IF(EventInMonth\_Flag, Month\_Max \* 1.9, Month\_Max \* 1.2)**

The variable **Month\_Max** calculates the maximum sales of the selected month. We return 1.9 times **Month\_Max** to present the labelling sticks if that month has events, and only return 1.2 times **Month\_Max** otherwise. Here, the factors only need to be large enough for presentation and you can try and choose your own factors.

The way we decide whether a month has events is by using the variable **EventInMonth\_Flag**. The **COUNTROWS** function will count how many events there are in the current month, and the **INT** function converts Boolean outputs (TRUE or FALSE) of the logical comparison to one \[1\] or zero \[0\].

Now we can set this measure as the **y**\-axis maximum. We go to the Format pane for the chart, and in **Visual -> Y-axis -> Range** we click the **Conditional formatting** button (**_fx_**) for **Maximum**.

![](<Base64-Image-Removed>)

We use the measure **Y Axis Max** as the maximum.

![](<Base64-Image-Removed>)

Now the visual has more top space to display the event names. Turning off the legend we finally have the combo visual as desired:

![](<Base64-Image-Removed>)

That’s it for this week’s Power BI blog. Hope you’ve enjoyed our article, and please stay tuned for more thoughts and insights from [https://www.sumproduct.com](https://www.sumproduct.com/)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-2/#0 "close")

top