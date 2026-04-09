# Power BI Blog: Highlight Event Periods – Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Highlight Event Periods – Part 1

*   January 24, 2024

Power BI Blog: Highlight Event Periods – Part 1
===============================================

Power BI Blog: Highlight Event Periods – Part 1
===============================================

25 January 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we will show you how to label periods on a visual._

Different things may affect sales and revenue. Holidays generally lead to higher consumption, businesses themselves can host sales campaigns to boost the figures, and unfortunate events can also happen to hurt businesses, such as COVID-19. So, when creating sales visuals in Power BI, how do we highlight such events?

![](https://sumproduct.com/wp-content/uploads/2025/05/d11ea51cbcf71f50d6c96dab7152d119-4.jpg)

We simulated a sales dataset for 2020 and selected a few events for the year. With that, we built the above visual which highlights the duration of an event and displays the event’s name in a label.

We will go through detailed steps to build this visual, and you can download our [data workbook](https://sumproduct.com/assets/blog-pictures/2022/pbi/310/financial-sample.xlsx)
 and [sample file](https://sumproduct.com/assets/blog-pictures/2022/pbi/310/sp-event-highlights.pbix)
 to follow along.

**_Chart Data_**

Besides the main dataset, we need details of the events to build the visual. In our [workbook](https://sumproduct.com/assets/blog-pictures/2022/pbi/310/financial-sample.xlsx)
 we included the Table **Events**:

![](https://sumproduct.com/wp-content/uploads/2025/05/a290a339c965c6d55e67b5fbc6e363f1-5.jpg)

You need to load both the main Table **Financials** and the Table **Events** into Power BI. We created a parameter **File\_Path** in Power Query. After downloading our data workbook, please change the parameter to your local file path of the workbook.

![](https://sumproduct.com/wp-content/uploads/2025/05/8442614c4f37f49db019b5fcb94f3a04-6.jpg)

We also need two \[2\] copies of the Table **Events**, one unconnected and one connected to **Calendar**. To make a duplicate of the Table **Events**, we right click on it and choose **Duplicate**.

![](https://sumproduct.com/wp-content/uploads/2025/05/5d143e89f1ed36467a475af7d4bfd0de-2.jpg)

Finally, we build a **Many to one** relationship between **‘Financials'\[Date\]** and **‘Calendar'\[Date\]**, and another **Many to one** relationship between **‘Events'\[Start\]** and **‘Calendar'\[Date\]**.

![](https://sumproduct.com/wp-content/uploads/2025/05/7e80bcfa618b223856fe7be0a117e62f-5.jpg)

**_The ‘Event flag’ Measure_**

Now let’s create the first chart measure that can be used to change colours to highlight a period. The measure is a flag checking whether the current date is related to any events, and we will use the unconnected copy of the Table **Events**.

**Event flag =  
SUMX(Events\_Copy,  
INT(MAX(‘Calendar'\[Date\]) IN CALENDAR(Events\_Copy\[Start\], Events\_Copy\[End\])))**

The function **SUMX** executes on each row of the Table **Events\_Copy**, where the **CALENDAR** function creates a single-column Table containing the dates between **Start** and **End** of an event.

The **MAX** function returns the current date of **Calendar**. The logical operator **IN** checks whether the current date is within duration of the event and returns TRUE or FALSE.

Lastly, the **INT** function converts the Boolean values (TRUE or FALSE) to one \[1\] or zero \[0\]. Then, **SUMX** sums up all rows of events in **Events\_Copy**. That means the measure equals to zero \[0\] if the current date is not contained in any events, and it equals to one \[1\] if the current date is contained in one \[1\] and only one \[1\] event. The measure can be greater than one \[1\] if multiple events are overlapping, but we will only be using it as a zero/non-zero flag.

To build the combo visual, we first create a Line and Stacked Column chart, use **Month Name** and **Day** as **x**\-axis fields, and use **Sales** as the column **y**\-axis field. Here, we have created a simple measure for the sales values:

**Sales value =  
SUM(Financials\[Sales\])**

![](<Base64-Image-Removed>)

Then, we insert a Slicer on **Month Name**.

![](<Base64-Image-Removed>)

Now, we can use the measure **Event flag** that we just defined to highlight the event periods. Inside the Format pane for the chart, we go to **Visual -> Columns -> Colors** and click the **Conditional formatting** button (**_fx_**).

![](<Base64-Image-Removed>)

Here, we choose the **Gradient** style and select the measure **Event flag**. For Minimum and Maximum, we choose the colours that we want for ordinary periods and periods with events. Also, we set the **Custom** values to zero \[0\] and one \[1\]. That way, non-zero values equal or larger than one \[1\] will all be treated as one \[1\].

![](<Base64-Image-Removed>)

Now the Christmas sales campaign from 5th to 28th December has been highlighted, so are other events in the year.

That’s it for this week’s Power BI blog. We will go through the other chart measures and how to complete the visual next week. Hope you’ve enjoyed our article, and please stay tuned for more thoughts and insights from [https://www.sumproduct.com](https://www.sumproduct.com/)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-highlight-event-periods-part-1/#0 "close")

top