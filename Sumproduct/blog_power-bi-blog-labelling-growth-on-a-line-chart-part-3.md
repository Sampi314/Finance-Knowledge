# Power BI Blog: Labelling Growth on a Line Chart – Part 3

**Source:** https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-3/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Labelling Growth on a Line Chart – Part 3

*   November 1, 2023

Power BI Blog: Labelling Growth on a Line Chart – Part 3
========================================================

Power BI Blog: Labelling Growth on a Line Chart – Part 3
========================================================

2 November 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we complete our custom visual by creating the label measures, and constructing the chart ._

Power BI visuals are an excellent tool when it comes to telling stories with our data.When we are analysing quantitative data, we often need to compare percentage differences.The most common example of this would probably be, “How much did the stock change today?”.However, how do we highlight that percentage change on a Power BI visual, _e.g._ on a stock price Line chart?

![](https://sumproduct.com/wp-content/uploads/2025/05/b1f0cb7202bfc54c20bff898308b74e5.jpg)

Above, we have created a custom visual to show cumulative profit, focussing on a specified interval. We have created a label to display the growth of cumulative profit and the current selection is from April to July. We can change the interval shown, by choosing an end month, and then specifying how many months to look back. The visual will not only display a label showing the growth, but it will also change colour automatically depending on whether the growth is positive or negative!

We will be using the **Financials** sample dataset in Power BI Desktop, and you can download our demonstration file with this [link](https://www.sumproduct.com/assets/blog-pictures/2022/PBI/298/sp-growth-label.pbix)
.

In [Part 1](https://www.sumproduct.com/blog/article/power-bi-tips/labelling-growth-on-a-line-chart-part-1)
 we prepared to create our visual by making a copy of the **Calendar** table.

![](https://sumproduct.com/wp-content/uploads/2025/05/e319e651a9de02b77a0d575bbdb570fa.jpg)

[Last time](https://www.sumproduct.com/blog/article/power-bi-tips/labelling-growth-on-a-line-chart-part-2)
, we create the chart measures that we need to construct the custom visual.

This week, we will create the measures we need to create the label, and complete our visual.

To create the dynamic growth label above the line, we define another two \[2\] measures. The first one calculates the growth (or decline) percentage and produces a text label, and it has the name **Labels**:

![](<Base64-Image-Removed>)

Here, for the first month and the last month, we calculate the cumulative profits in variables **First\_Month\_Profit** and **Last\_Month\_Profit**. Then in the variable **Perc\_Change** we calculate the percentage of change. The variable **Label\_Position** outputs the dates in the second last month of the selected period, which is where we would like to position out text label. Then we create the variable **Flag** using **Label\_Position** as filter. In the outputting **IF** function, we use the flag to output at the second last month and specify different labels for positive and negative values.

The second measure **Label Colour** changes colour for the label, and it uses a very similar formula:

![](<Base64-Image-Removed>)

It calculates the percentage change and outputs at the same position. The only difference is that we specify the colours red or green in the output **IF** function.

**_Construct the Chart_**

Now we are ready to build the Line chart and create our dynamic growth label. To build the background chart, we create a Line chart and choose our cumulative profit measure as the **y**\-axis. Since we are comparing monthly figures in this example, we choose **Year** and **Month Name** for the **x**\-axis.

Then we create two \[2\] Slicers, one \[1\] for the column **Period** from Table **Period Selection**, and the other for the column **Year Month** from Table **YearMonth Copy**. We suggest turning on **Single select** for the Slicers (in **Format -> Visual -> Slicer settings**) so there are always values selected for the measures.

Next, besides the cumulative profit we choose measures **Line** and **Markers** as **y**\-axis fields for the Line chart:

![](<Base64-Image-Removed>)

Then, we create the vertical lines by using the measure **End Points** as Error bars for the measure **Markers**. To do that, we go to **Format -> Visual -> Error bars**, choose the measure **Markers** in **Apply settings to**, and in **Options** we turn on **Enabled**, choose **By field** in **Type** and use the measure **End Points** as the **Upper bound**.

![](<Base64-Image-Removed>)

We can further format the Error bars in **Format -> Visual -> Error bars -> Bar**. For example, it’s a good idea to choose ‘None’ for **Marker shape**. So far, the visual will look something like the following if one selects ‘Jul-2014’ and three \[3\] months:

![](<Base64-Image-Removed>)

To build the dynamic text label we use measures in Data labels. The options for Data labels are located at **Format -> Visual -> Data labels**. We first turn off Data labels for the main field **Cum Profit**, and we keep the option on for the **Markers** field. For the field **Line**, we go into **Data labels -> Values**, turn on **Custom label** and select the measure **Labels**.

![](<Base64-Image-Removed>)

Still in **Data labels -> Values**, we click the conditional formatting button (**_fx_**) of **Color**, and use the measure **Label Colour**:

![](<Base64-Image-Removed>)

At this point, we have created all the wonderful elements of our custom visual. Our dynamic text label tells the percentage growth or decline, and it even changes colour!

We can complete it with a bit of final formatting:

![](<Base64-Image-Removed>)

Our visual is complete!

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-3/#0)

[](https://sumproduct.com/blog/power-bi-blog-labelling-growth-on-a-line-chart-part-3/#0 "close")

top