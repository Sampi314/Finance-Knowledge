# Charts and Dashboards: Interactive Charts – Part 2: Form Controls (Continued)

**Source:** https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-2-form-controls-continued/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Interactive Charts – Part 2: Form Controls (Continued)

*   August 6, 2020

Charts and Dashboards: Interactive Charts – Part 2: Form Controls (Continued)
=============================================================================

Charts and Dashboards: Interactive Charts – Part 2: Form Controls (Continued)
=============================================================================

7 August 2020

_Welcome back to this week’s Charts and Dashboards blog series. This week, let’s continue our consideration of Form Controls. Here, we look at how to create a Drop-down List using them._

To recap, with Form Controls, we can add a data selection option to charts, for example, through a Check box or a Drop-down List. In the [previous blog](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-1-form-controls/)
, we discussed how to create Check Boxes using Form Controls. Now, let’s see how we may create a Drop-down List.

First, in the chart data area, we will add a column, _e.g._ ‘**Sales by group**‘, with which we will later build our chart. We will also add a list of **Groups**, with a blank cell at the top (highlighted in green in the image below). Later, we will add a cell link to this.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-167-1.jpg)

We navigate to the Developer tab on the Ribbon. We choose **Insert -> Form Controls** and click the Combo Box (the second left icon on the top row):

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-155-1.jpg)

We need to make sure we choose the Combo Box from the ‘Form Controls’ group, not the ‘ActiveX Controls’ group – which is for VBA. If you inadvertently choose the wrong version, you will notice that there is no Control tab in the ‘Format Control’ dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-148-1.jpg)

Having selected the Form variant, by holding the **ALT** key and click on a cell in the worksheet, a box with an arrow icon will appear that may be snapped to grid:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-130-1.jpg)

Next, right-click on the icon on the work sheet and click ‘Format Control…’. In the Control tab, to define the ‘Input range’, we will select the list of groups in cell **K12:K16**, and refer the ‘Cell link’ to the blank green cell, which is cell **K11**.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-111-1.jpg)

Then, we will resize the arrow box (if necessary). As we choose one item from the list, note that the cell link will reflect its index number (_i.e._ position in the list):

![](<Base64-Image-Removed>)

Now, we need to match the sales figures corresponding to the group that we have chosen from the drop-down menu. This can be done easily using the **INDEX** function. The ‘**Sales by group**‘ cell will be the index result from the corresponding range chosen; the array in this example has only one row, so only one reference is required, whether the range were to consist of one row or one column. Here, if we choose **Biz Supplies** from the list, the cell link shows number one (1) – as this is the order of **Biz Supplies** item in the list, this will also be the column number to index.

The formula in cell **J11** is:

**\=INDEX($E11:$I11,$K$11)**

![](<Base64-Image-Removed>)

Then we can build a chart on the ‘**Sales by group**‘ column based on Quarters. We may also need to bring the drop-down box to front to insert to the chart. To insert the Drop-down List, just drag the icon to the chart:

![](<Base64-Image-Removed>)

This chart is now interacted accordingly to our group selection using the Drop-down List.

![](<Base64-Image-Removed>)

That’s it for this week, check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-2-form-controls-continued/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-2-form-controls-continued/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-2-form-controls-continued/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-2-form-controls-continued/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-interactive-charts-part-2-form-controls-continued/#0 "close")

top