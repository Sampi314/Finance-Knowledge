# Creating Dynamic Charts with Non-Contiguous Data

**Source:** https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data

---

Formula Forensics No. 032 – Creating Dynamic Charts with Non-Contiguous Data
============================================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Posts by Sajan](https://chandoo.org/wp/category/posts-by-sajan/)
 - 19 comments

  

I have lost count of the number of articles that discuss Excel charts.

There are also quite a few that discuss creation of dynamic charts (where the data to be plotted is determined dynamically).

However, most of the articles assume that the data to be plotted is organized neatly in adjacent cells. But what if you wanted to plot data that is not contiguous?

In this article, we will learn how to plot non-contiguous data. If you can identify an algorithm to locate your relevant data, we should be able to plot it, regardless of where the data is located!

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure1-Overview.png "Figure1-Overview")](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure1-Overview.png)

Background Information
----------------------

The following articles provide good background information on dynamic charts:

**Jon Peltier’s** article: [http://peltiertech.com/Excel/Charts/DynamicCharts.html](http://peltiertech.com/Excel/Charts/DynamicCharts.html "http://peltiertech.com/Excel/Charts/DynamicCharts.html")

**Debra Dalgleish’s** (Contextures) article: [http://www.contextures.com/xlNames02.html](http://www.contextures.com/xlNames02.html "http://www.contextures.com/xlNames02.html")

**Chandoo’s** article on this site: [http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/](http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/ "http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/")

This article assumes that you are already familiar with how to create an Excel Name, and how to assign a Name to a dynamic chart. If you need a refresher, please read the above referenced articles.

As with all Formula Forensic posts you can follow along using the sample files: [Excel 2007+](https://chandoo.org/wp/wp-content/uploads/2012/12/DynamicCharts.xlsx "https://chandoo.org/wp/wp-content/uploads/2012/12/DynamicCharts.xlsx")
; [Excel 97-2003](https://chandoo.org/wp/wp-content/uploads/2012/12/DynamicCharts.xls "https://chandoo.org/wp/wp-content/uploads/2012/12/DynamicCharts.xls")

Data Setup
----------

For the purposes of illustrating the dynamic chart, I have setup the data as follows:

Column A contains some date values

Column B determines the weekday (Sun, Mon, Tue, etc.) for the dates in Column A

Column C, D, E, F are data values corresponding to the dates in Column A. These will be the four data series that we will plot.

Column G contains text values that will be used as x-axis labels for the chart

A basic chart displaying this data is shown:

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip1.png "Snip1")](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip1.png)

Obviously we cannot see which Data is from Monday (Day 1)

To make the chart dynamic, we will plot the four data series only when the weekday value = 1 (denoting Sundays).

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure2-DataOverview.png "Figure2-DataOverview")](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure2-DataOverview.png)

(The rows where weekday=1 have been highlighted for ease of reference.)

The formulas that make the chart dynamic
----------------------------------------

Create the following Names to make references simple:

**WeekDayList** refers to the range B2:B23

**Series1FullList** refers to the range C2:C23

**Series2FullList** refers to the range D2:D23

**Series3FullList** refers to the range E2:E23

**Series4FullList** refers to the range F2:F23

**LabelsFullList** refers to the range G2:G23

If we needed to get the sum of all values in Series1 where WeekDay=1, we would use a formula similar to the following:

\=SUMPRODUCT((WeekDayList=1)\*Series1FullList)

The argument to the SUMPRODUCT formula resolves to the following array:

\={10;0;4;0;0;0;8;0;0;0;0;0;0;5;0;0;0;0;0;3;0;0}

As you can see, there are a lot of zeros for those data points where the WeekDay was not equal to 1.

If we were to plot this array, Excel would faithfully plot the zero values also.

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip4.png "Snip4")](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip4.png)

or hiding the Zeroes as:

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip2.png "Snip2")](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip2.png)

These charts show the Values but are not ideal.

Some of you might be thinking that you can just substitute zero values with #NA, and Excel will not plot the #NA values.

You are correct. That is one approach to not plotting the zero values.

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip3.png "Snip3")](https://chandoo.org/wp/wp-content/uploads/2012/12/Snip3.png)

However, since that is just tricking Excel into ignoring some values (even though the #NA values still exist), we will look at a different approach that truly condenses the array to the non-zero values.

### The Technique

First, let us build a helper formula that provides the position of the data where **WeekDay=1**

**SubsetIndex:** =SMALL(IF(WeekDayList=1, ROW(WeekDayList)-ROW(INDEX(WeekDayList,1))+1), ROW ($A$1 : INDEX ($A:$A, COUNTIF (WeekDayList, 1))))

Looking at the parts of this formula

ROW(WeekDayList)-ROW(INDEX(WeekDayList,1))+1 creates a sequential array from 1 to the number of rows in WeekDayList:

\={1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22}

IF(WeekDayList=1,…) produces an array with the sequential values above when WeekDay=1, and FALSE otherwise:

\={1;FALSE;3;FALSE;FALSE;FALSE;7;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;14;FALSE;FALSE;FALSE;FALSE;FALSE;20;FALSE;FALSE}

COUNTIF(WeekDayList,1) returns 5 in the above sample data, indicating that we have five rows where WeekDay=1

ROW($A$1:INDEX($A:$A,COUNTIF(WeekDayList,1))) produces a sequential array from 1 to the number of rows where WeekDay=1:

\={1;2;3;4;5}

SMALL(…) extracts the 5 smallest values from the IF(…) array:

\={1;3;7;14;20}.

Please note that these values indicate the position in the WeekDay list. i.e. the relevant positions are rows 2, 4, 8, 15 and 21 (to account for the headers in row 1).

Now use the SubsetIndex to extract the subset of relevant values in Series1FullList:

\=N(OFFSET(Series1FullList,SubsetIndex-1,0,1,1))

We will give it the name Series1SubsetData

Use SubsetIndex-1 because the first row for the OFFSET function is row zero.

The OFFSET function resolves to OFFSET(Series1FullList,{0;2;6;13;19},0,1,1).

i.e. we are asking the OFFSET function to extract the rows indicated by {0;2;6;13;19} in the same column (zero) as Series1FullList, that is 1 row high and 1 column wide.

The OFFSET(…) function returns the array

\={10;4;8;5;3}

It would have been straightforward if this returned array was usable as is. However, unless you array-enter this formula over 5 rows, you would not be able to use it anywhere else. (For example, if you check ROWS(OFFSET(…)), you would get the value 1 indicating that Excel is hiding the rest!

That is where the N() function comes in handy.

While the common use for this function is to convert text values into numbers, it also has a hidden talent for converting the references returned by OFFSET into an array.

The N(…) formula returns the following for our data set: {10;4;8;5;3}.

Even though it looks just like the output from OFFSET function alone, it has now become usable for our purposes!

For example, if you use ROWS(N(…)) you will get 5 as expected!

### Hint:

Please note that there are other ways to eliminate the zero values from an array. For example, please see the following recent post and responses:

[http://chandoo.org/forums/topic/dynamically-generate-contiguous-data-in-array-for-chart-from-non-contiguos-range](https://chandoo.org/forum/threads/dynamically-generate-contiguous-data-in-array-for-chart-from-non-contiguos-range.7683/ "http://chandoo.org/forums/topic/dynamically-generate-contiguous-data-in-array-for-chart-from-non-contiguos-range")

We will setup the following Names and formulas for the rest of the data series:

**Series2SubsetData** \=N(OFFSET(Series2FullList,SubsetIndex-1,0,1,1))

**Series3SubsetData** \=N(OFFSET(Series3FullList,SubsetIndex-1,0,1,1))

**Series4SubsetData** \=N(OFFSET(Series4FullList,SubsetIndex-1,0,1,1))

### Labels

While the trick with the N() function works with numeric data, it does not work with string data. Since we would like to use the text from LabelsFullList, we will need to use a helper column to extract just the text strings that correspond to the condition WeekDay=1.

There are many ways to extract a text subset, but I have used the following formula in cell J2 and copied down to J23.

\=INDEX(LabelsFullList, INDEX(SubsetIndex,ROW(1:1)))

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure4-DataWithHelperCol.png "Figure4-DataWithHelperCol")](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure4-DataWithHelperCol.png)

We can ignore the error values since we will only be using the subset that returned text values. We will use the Name HelperColForLabels to refer to cells J2:J23

To refer to just the text values, we will use the following formula, and give it the name XAxisLabels

\=INDEX(HelperColForLabels,1):INDEX(HelperColForLabels,ROWS(SubsetIndex))

The above formula resolves to \={“Dynamic”;”labels”;”are”;”really”;”easy”}

Creating the Dynamic Chart
--------------------------

Now that the formulas are in place, all we have to do is reference them in an Excel chart!

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure5-ChartSetup.png "Figure5-ChartSetup")](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure5-ChartSetup.png)

For the Chart,

**Series1** values refer to \=DynamicCharts.xlsx!Series1SubsetData  
**Series2** values refer to \=DynamicCharts.xlsx!Series2SubsetData  
**Series3** values refer to \=DynamicCharts.xlsx!Series3SubsetData  
**Series4** values refer to \=DynamicCharts.xlsx!Series4SubsetData  
**Horizontal (Category) Axis Labels** refer to \=DynamicCharts.xlsx!XAxisLabels

The end result looks as follows:

[![](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure3-FinishedChart.png "Figure3-FinishedChart")](https://chandoo.org/wp/wp-content/uploads/2012/12/Figure3-FinishedChart.png)

The chart and axis labels adjusts to changes in values in the underlying data, as expected.

Final Thoughts
--------------

We have used an innocuous looking function N() to make the chart dynamically adjust to non-contiguous data. (There are other ways to handle dynamic data… but that is for another article!)

Do you know of any other Excel functions with hidden talents?

Please write and let us know in the comments below:

In the meantime, I wish you continued EXCELlence!

**_Sajan._**

Thank You
---------

This was Sajan’s third post at Chandoo.org and so a special thank you again to **Sajan** for putting pen to paper to describe this great technique here.

If you like this technique, you may want to thank Sajan in the comments below:

[Formula Forensics “The Series”](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics Series")

---------------------------------------------------------------------------------------------------------------

This is the 32nd post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts: [Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share like above, try putting pen to paper and draft up a Post like Sajan has done above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "Contact Chandoo")
.

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Hui...  <br>Tags: [countif()](https://chandoo.org/wp/tag/countif/)<br>, [if()](https://chandoo.org/wp/tag/if/)<br>, [INDEX()](https://chandoo.org/wp/tag/index/)<br>, [N()](https://chandoo.org/wp/tag/n/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [small](https://chandoo.org/wp/tag/small/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 19 Responses to “Formula Forensics No. 032 – Creating Dynamic Charts with Non-Contiguous Data”

1.  ![](https://secure.gravatar.com/avatar/7af54b77735cab88c720cd0e915c1b05175573e2e0bb817804e65fe659426086?s=64&d=mm&r=g) [Jane Barry](http://www.lsbf.org.uk/)
     says:
    
    [December 4, 2012 at 10:19 am](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331445)
    
    Great thanks. I had some ideas on how to generate such charts. However, your idea with the SubsetIndex formula was really helpful. Waiting for the next article.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331445)
    
2.  ![](https://secure.gravatar.com/avatar/dbdeacf82c07fa366963e900968af334d09a06ba6f779d325c4639fc1c342958?s=64&d=mm&r=g) [Pavi](http://www.chandoo.org/)
     says:
    
    [December 4, 2012 at 11:29 am](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331513)
    
    Thanks Sajan really nice post... waitting to see more post from you...
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331513)
    
3.  ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/forums/profile/sthomas)
     says:
    
    [December 4, 2012 at 3:44 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331767)
    
    Thank you Jane Barry and Pavi.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331767)
    
4.  ![](https://secure.gravatar.com/avatar/3634835f6131806698500bc26a0b020b97d2a7c6249d5be11db4920ba639ed2d?s=64&d=mm&r=g) Paul says:
    
    [December 4, 2012 at 7:42 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331998)
    
    Great post!  I was able to modify it to dynamically change the chart for the day of the week.  Is there a way to dynamically chart the number of the series.  e.g. In your example you had 4 series, could one set up a chart to dynamically have only 2 series or 5 series based on the data that one dynamically selects?  Thanks!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-331998)
    
5.  ![](https://secure.gravatar.com/avatar/05f3fdcff01e92d7cc22de3c93d0d3bc7bf18196cfc63480641430070d98d667?s=64&d=mm&r=g) Kevin says:
    
    [December 4, 2012 at 8:22 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-332028)
    
    Great post!  I enjoyed seeing each array explained and results illustrated.  I appreciate your time well-spent.  I am looking forward to more posts from you as well.  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-332028)
    
6.  ![](https://secure.gravatar.com/avatar/586aa5f4d031191b4717c72c526863bf332fcf0059d9abac1d4a6153e4e9c4fe?s=64&d=mm&r=g) Andrew says:
    
    [December 4, 2012 at 9:43 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-332085)
    
    Thank you!  
    I was wondering how to do this last month - was even going to ask the question here.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-332085)
    
7.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [December 4, 2012 at 11:55 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-332203)
    
    Excellent post Sajan... Thanks for sharing the N()'s secret abilities with us.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-332203)
    
8.  ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/forums/profile/sthomas)
     says:
    
    [December 5, 2012 at 11:06 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-333570)
    
    **Paul, Kevin, Andrew, Chandoo:**  
    Thanks for the feedback.  Glad to hear you liked the article. 
    
    **Paul**, regarding your question about dynamically changing the number of series plotted...  
    Without resorting to VBA, I am not aware of a way to add/remove a series to a chart.  
    However, you could employ the following approach to making a series disappear from view.  (You would still need to setup the series in the chart.)  
    In the formula for a given series, you could substitute it with something like "={1} \* NA()" when you want that series to be invisible.   
    For example, the following is a modification for the formula for Series1 in the article:   
    \=IF(Criteria="ShowSeries1", N(OFFSET(Series1FullList,SubsetIndex-1,0,1,1)), {1}\*NA())  
    The above formula will cause the Series1 to become invisible if Criteria is not set to "ShowSeries1".
    
    Please note that the chart's legend will still show the name of that "invisible" series.
    
    Cheers,  
    Sajan.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-333570)
    
9.  ![](https://secure.gravatar.com/avatar/2ce0b6860ea486b9f91f5ba8422b861e6ce4439b6e01aa261df22a30301fec8f?s=64&d=mm&r=g) juanito says:
    
    [December 7, 2012 at 10:33 am](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-335810)
    
    Sajan - Thanks for this great teaching.
    
    Question on the N() function (and how arrays work).
    
    Say I have values in A1:A2 of 1 and 2. If I select the cells and insert column chart then I get the two values.
    
    If I go to B1 and array-enter =A1:A2 and insert chart I only get the first value. I still don't understand why.
    
    Now after reading your post I thought eureka! I could go to C1 and array-enter =N(A1:A2) and then if I inserted chart I'd get the two values.
    
    But I don't. Did I misunderstand  something?
    
    \- Juanito 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-335810)
    
10.  ![](https://secure.gravatar.com/avatar/27cde7a44cbe4067f41943198576f83f97e23475619fd24c23e0fc53029e2b49?s=64&d=mm&r=g) [Sajan](http://chandoo.org/forums/profile/sthomas)
     says:
    
    [December 7, 2012 at 3:45 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-336120)
    
    Hi Juanito,  
    Thanks for the feedback. 
    
    Since A1:A2 consists of two values, you would need to array-enter it over two cells (e.g. B1:B2) to see both of the results.
    
    I think you would find the following article of interest.  It explains the concept of a "multi-cell" array formula.  
    [http://office.microsoft.com/en-us/excel-help/introducing-array-formulas-in-excel-HA001087290.aspx](http://office.microsoft.com/en-us/excel-help/introducing-array-formulas-in-excel-HA001087290.aspx)
    
    Regards,  
    Sajan.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-336120)
    
11.  ![](https://secure.gravatar.com/avatar/2ce0b6860ea486b9f91f5ba8422b861e6ce4439b6e01aa261df22a30301fec8f?s=64&d=mm&r=g) juanito says:
    
    [December 7, 2012 at 8:50 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-336463)
    
    Sajan -  
    I believed that an single-cell array (such as the example in cell B1 above) should pass an array of various values to, say, a chart. It clearly doesn't, as per my trivial example. There are plenty of workarounds but I'm struggling with this very primitive question!  
    I was thinking that N() added something here... it clearly serves a function but not the one I understood from your post.
    
    Best,   Juanito      
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-336463)
    
12.  ![](https://secure.gravatar.com/avatar/d7f1121d456047bebb45ac34203b594880c18b3caf7e1546c41c5cebecade052?s=64&d=mm&r=g) Tim says:
    
    [April 25, 2014 at 10:36 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-491088)
    
    Is there a way to adapt this for sparklines? I was able to get it to work with a chart object, but when I tried to input Series1SubsetData as the data range for a sparkline, it returned an error. By the way - thanks so much for your very informative posts!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-491088)
    
13.  ![](https://secure.gravatar.com/avatar/b96164f14d3797ebfc8879436a51ea9533dd26ec261aa74ab9c61c7038c07a87?s=64&d=mm&r=g) Anders Carlsson says:
    
    [January 28, 2016 at 10:12 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1127928)
    
    Many thanks for this post - it helped me out!  
    Regarding the legend - I have found a away similar to the N() method for text.  
    It worked for me - but I wouldn't have found it out without the N()...  
    \=N(OFFSET(Series4FullList,SubsetIndex-1,0,1,1)) =>
    
    \=T(OFFSET(LabelsFullList,SubsetIndex-1,0,1,1))
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1127928)
    
14.  ![](https://secure.gravatar.com/avatar/3634835f6131806698500bc26a0b020b97d2a7c6249d5be11db4920ba639ed2d?s=64&d=mm&r=g) Paul S. says:
    
    [January 29, 2016 at 2:48 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1128419)
    
    Paul, Kevin, Andrew, Chandoo, Sajan
    
    Without using VBA, here is a way I do it to try to show the least amount of clutter.
    
    I have the original data. I then build a separate table to house only the data that will be in the chart (my “chart table”).  
    1\. I build the chart table to show the maximum amount of items in the series (2, 4, 6, or whatever the maximum is).  
    2\. My chart table is built using vlookup, index, or whatever you choose to dynamically get the data into your chart table.  
    3\. Choose whatever method you want to interact with your chart table as far as determining what items will be in your series – via drop down list box, directly in the chart table or whatever.  
    4\. Build the data lookup formulas in the chart table so that if you would choose to only show 3 items out of maximum of 4, then in the chart table  
    a. Where the legend shows, be sure to show a blank cell (“” being the result of the formula if you are doing it by formula).  
    b. Build the data portion of that row so that it will show #N/A if there is nothing in the legend cell.
    
    This will show only the number of series you want in the chart. The only thing “extra” in the chart will be in the legend, the legend will show the type of marker/line for the “missing” series. However, there will be no label beside the marker in the legend, thus cutting down on clutter.
    
    This reduces the clutter to a minimum (if you don’t want to do it via VBA) while allowing a lot of flexibility in what you chart for the series and the number of series you chart.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1128419)
    
15.  ![](https://secure.gravatar.com/avatar/f18cf577c2aae86c394895623f12db9362c7599fc300894160e29c73e69366ff?s=64&d=mm&r=g) John Focht says:
    
    [July 12, 2016 at 7:34 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1231068)
    
    This seemed to be an answer to my prayers for creating a dynamic graph with discontinuous values, but has become a personal nightmare. An observation, assumption, and a question:
    
    In Excel 2013, the SUMPRODUCT returns a single value of 30, not an array. (I know that the array is how the value of 30 was determined.) And I assume SubsetIndex: refers to a cell.
    
    The equation:
    
    \=SMALL(IF(WeekDayList=1, ROW(WeekDayList)-ROW(INDEX(WeekDayList,1))+1), ROW ($A$1 : INDEX ($A:$A, COUNTIF (WeekDayList, 1))))
    
    returns the error
    
    Microsoft Excel: We found a typo in your formula and tried to correct it to:
    
    \=SMALL(IF(WeekDayList=1,ROW(WeekDayList)-ROW(INDEX(WeekDayList,1))+1),ROW($A$1:INDEX($A:$A,COUNTIF(WeekDayList,1))))
    
    which doesn't look materially different to me.
    
    And the 'corrected' formula yields,
    
    #VALUE!
    
    I am working on the example dataset, created from scratch. What am I doing wrong?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1231068)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 13, 2016 at 3:25 am](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1231340)
        
        @John
        
        SubsetIndex is a Named Formula  
        and All Named Formula are Array Formula, that are entered using Ctrl+Shift+Enter key combination, not simply Enter  
        So the value 30 you are seeing is the first value in the array
        
        If you select the Top line in the chart you will see in the Formula Bar that it has an equation:  
        \=SERIES(DynamicCharts!$F$1,DynamicCharts.xlsx!**XAxisLabels**,DynamicCharts.xlsx!**Series4SubsetData**,4)
        
        The X Axis Labels are a named Formula called XAxisLabels  
        The Series Values are a named Formula called Series4SubsetData
        
        The Name Manager is accessible by going to the Formula, Name Manager Tab
        
        For further help I'd suggest posting a question in the Chandoo.org Forums and attach a sample file  
        Goto: [http://forum.chandoo.org/](http://forum.chandoo.org/)
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1231340)
        
16.  ![](https://secure.gravatar.com/avatar/f18cf577c2aae86c394895623f12db9362c7599fc300894160e29c73e69366ff?s=64&d=mm&r=g) John Focht says:
    
    [July 13, 2016 at 8:42 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1231751)
    
    Hui...
    
    Thanks. I stumbled upon the CSE issue after posting in this thread. Honestly, I haven't done much with these kinds of formulas, so it wasn't obvious problem to me.
    
    I will post my (abbreviated) spreadsheet shortly. I have strong working knowledge of VLOOKUP, HLOOKUP, and scientific and text manipulation functions, but indexing has me flummoxed.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-1231751)
    
17.  ![](https://secure.gravatar.com/avatar/78875c170319c84c1af3399aa07a88a3e9eef1f1bbff9e111ac297b5221eeb18?s=64&d=mm&r=g) Kaz Kowalski says:
    
    [June 9, 2022 at 5:14 pm](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-2079142)
    
    This is excellent.. although I have got things wrong!!  
    I have a slightly different where I have for ever month actuals and forecasts. Trying to draw the graph with the distribution of both. I can create all the lists and can create the rows, then i can reference the whole series to create the chart. The series ought to be dynamic - ok so if i have 10 columns or 12 columns it should work. But I can not get it to work by using the subset list name, have to select the whole range...
    
    Very confused, any ideas?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-2079142)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 12, 2022 at 3:17 am](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-2079282)
        
        @Kaz  
        Glad you like the post  
        Can I please ask that you post a new Thread in the Chandoo,.org Forums:  
        [https://chandoo.org/forum/](https://chandoo.org/forum/)
        
        Please attach a sample file and I will review from there
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#comment-2079282)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-032-creating-dynamic-charts-with-non-contiguous-data/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Become Awesome in Excel while saving money](https://chandoo.org/wp/holiday-sale-is-here/) | [How the tax burden has changed over the years – Excellent chart by NYTimes & Redoing it in Excel](https://chandoo.org/wp/tax-burden-chart-excel/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)