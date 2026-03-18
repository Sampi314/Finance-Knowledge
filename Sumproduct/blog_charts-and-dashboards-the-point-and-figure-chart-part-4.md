# Charts and Dashboards: The Point and Figure Chart – Part 4

**Source:** https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-4/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: The Point and Figure Chart – Part 4

*   August 10, 2023

Charts and Dashboards: The Point and Figure Chart – Part 4
==========================================================

Charts and Dashboards: The Point and Figure Chart – Part 4
==========================================================

11 August 2023

_Welcome back to our Charts and Dashboards blog series. This week, we continue to explain how to create a bespoke Point and Figure chart by looking at how we use all the data we have summary, prepare and transform to plot the chart._

_**Plotting Data**_

Next, we head to the ‘**PnF-CSE**‘ sheet. In the **Lower Bin** column, we will implement the following formula for the column:

**\=Max-Width\*ROW(INDIRECT(“A1:A”&Number\_of\_Bins))**

Let’s recall that we have **Max** as the maximum value in the **Adj Close** column, **Width** is the distance between two \[2\] bins of number and **Number\_of\_Bins** is the number of number bins we have. The **ROW(INDIRECT(“A1:A”&Number\_of\_Bins))** will generate an array of numbers from one \[1\] to the number of bins we enter in **Number\_of\_Bins** cells. (You can also use the **SEQUENCE** function here to achieve the same thing. What we are doing here is building this model in the Legacy Excel version for most of the users)

In Legacy Excel for the above formula to work we need to select a range that is equal to the **Number\_of\_Bins** (in our case here is 30) then enter the formula and press **Ctrl + Shift + Enter**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1085f52690d9b55e115a4d7ade4fdc5.jpg)

If there is a curly bracket around the formula afterward then we are heading in the right direction:

**{=Max-Width\*ROW(INDIRECT(“A1:A”&Number\_of\_Bins))}**

We do a similar thing for the **Upper Bin** column with the following formula:

**\=Max-Width\*(ROW(INDIRECT(“A1:A”&Number\_of\_Bins))-1)**

With that we have finished our vertical axis:

![](<Base64-Image-Removed>)

We will name the data in the Lower Bin column as **Lower\_Bin\_Column** and Upper Bin column as **Upper\_Bin\_Column**

Next, we will create the horizontal Axis. In the sheet we prepare for you, we will select **E9:EF10** and enter the following formula:

**\=TRANSPOSE(Transform\_Data\[\[Unique Index\]:\[Date\]\])**

This formula will flip the row we have for the **Unique Index** column and **Date** column in the **Transform\_Data** table to the right. As this is a legacy array, we need to press **Ctrl + Shift + Enter** to complete the formula and with that our axes are completed. We will name the numbering row as **Index\_Row** and we will have the following visual:

![](<Base64-Image-Removed>)

The final step is to plot the chart. We select the chart area from **G11:EF40**. Then we enter the following formula:

**\=IF((Upper\_Bin\_Column>=TRANSPOSE(Transform\_Data\[Min\]))**

       **\*(Lower\_Bin\_Column<=TRANSPOSE(Transform\_Data\[Max\])),**

  **IFS(Starting\_Symbol=Up\_Symbol,IF(MOD(Index\_Row,2)=1,Up\_Symbol,Down\_Symbol),                   Starting\_Symbol=Down\_Symbol,IF(MOD(Index\_Row,2)=1,Down\_Symbol,Up\_Symbol)),””)**

Let’s break down the meaning of each component in this formula:

**(Upper\_Bin\_Column>=TRANSPOSE(Transform\_Data\[Min\]))**: The **Upper\_Bin\_Column** is an array that looks like a column vector and the output of this formula **TRANSPOSE(Transform\_Data\[Min\]))** is an array that looks like a row vector. The logical formula between these two arrays will generate a matrix of TRUE or FALSE with the width of the matrix is the maximum number of the **Unique Index** column in the **Transform\_Data** Table and the height of the matrix is the **Number\_of\_Bins**. This matrix will have TRUE on top and FALSE on the bottom like the following image:

![](<Base64-Image-Removed>)

**(Lower\_Bin\_Column<=TRANSPOSE(Transform\_Data\[Max\]))**: The **Lower\_Bin\_Column** is an array that looks like a column vector and the output of this formula **TRANSPOSE(Transform\_Data\[Max\]))** is an array that looks like a row vector. The logical formula between these two arrays will generate a matrix of TRUE or FALSE with the width of the matrix is the maximum number of the **Unique Index** column in the **Transform\_Data** Table and the height of the matrix is the **Number\_of\_Bins**. This matrix will have FALSE on top and TRUE on the bottom like the following image:

![](<Base64-Image-Removed>)

**(Upper\_Bin\_Column>=TRANSPOSE(Transform\_Data\[Min\]))\*(Lower\_Bin\_Column<=TRANSPOSE(Transform\_Data\[Max\]))**

When we multiply these two matrices, we will generate a matrix of one \[1\] and zero \[0\] where the overlapping TRUE components are one \[1\] and the rest is zero \[0\] which will look like the following matrix:

![](<Base64-Image-Removed>)

We have overlapping points; we will need to determine which symbol goes into the cells. That is when the latter components come in handy:

**IFS(Starting\_Symbol=Up\_Symbol,IF(MOD(Index\_Row,2)=1,Up\_Symbol,Down\_Symbol),**

 **Starting\_Symbol=Down\_Symbol,IF(MOD(Index\_Row,2)=1,Down\_Symbol,Up\_Symbol))**

The first thing we check is if our **Starting\_Symbol** is **Up\_Symbol**, then every odd index number will possess the **Up\_Symbol** and every even index number will possess the **Down\_Symbol**. This is why we use the **MOD** function like this **MOD(Index\_Row,2)=1** to detect the even and odd number here. We repeat the same process if our **Starting\_Symbol** is **Down\_Symbol**.

**“”**: the last component of the big **IF** function here is the blank space which will keep the chart clean.

Finally, after entering the formula and pressing **Ctrl + Shift + Enter** we will have the chart we want:

![](<Base64-Image-Removed>)

Now you might want to colour the ‘X’ symbol green and the ‘O’ symbol red. We can employ **Conditional Formatting** to do our bidding. We go to **Home -> Styles -> Conditional Formatting -> New Rules** (or **Alt + O + D** for short). We add these rules for the colour scheme of the graph:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Congratulations we make the Point and Figure Chart.

You can download the complete file [here](https://sumproduct.com/assets/blog-pictures/2022/cd/145/sp-point-and-figure-chart---complete.xlsm)
, where it contains the chart make from CSE array, dynamic array and a dynamic array version that have Bollinger Bands.

**_Word to the Wise_**

This chart would be more useful if adding Bollinger Bands for our chart here and the chart will look like this with some tweaks in the formula and data transformation:

![](<Base64-Image-Removed>)

This can be in other Charts and Dashboards for some other day.

That’s it for this week, come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-4/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-the-point-and-figure-chart-part-4/#0 "close")

top