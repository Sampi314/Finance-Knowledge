# Charts and Dashboards: Dynamic Simulation Charts

**Source:** https://sumproduct.com/blog/charts-and-dashboards-dynamic-simulation-charts/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Dynamic Simulation Charts

*   December 31, 2020

Charts and Dashboards: Dynamic Simulation Charts
================================================

Charts and Dashboards: Dynamic Simulation Charts
================================================

1 January 2021

_Happy New Year!_

_Welcome back to this week’s Charts and Dashboards blog series. As the first blog of the year, we will create a dynamic simulation chart._

A while ago, on SumProduct’s [Thought](https://www.sumproduct.com/thought)
 page, we discussed [simulations](https://www.sumproduct.com/thought/simulation-stimulation)
, where we applied simulation analysis in Excel and created several charts, _e.g._

![](<Base64-Image-Removed>)

This time, we will go through the steps of creating one. The [attached Excel file](https://sumproduct.com/assets/blog-pictures/2020/charts-and-dashboards/048/simulation-example.xlsm)
 can be used in practice.

The above column chart has dynamic series and axes defined as ‘**Chart\_Stratification**‘ and ‘**Chart\_Count’**, which change by the choice from the drop-down list. It only requires a quick collation step to summarise the outputs graphically.

First, in the **Lookups** sheet, define the ‘**LU\_Simulation\_Outputs**‘ range (cell **G11:G14**).

![](<Base64-Image-Removed>)

Now, to create the drop-down list, navigate to the Developer tab on the Ribbon, from Insert, choose ‘Combo Box (Form Control)’ and draw a drop-down list box.

![](<Base64-Image-Removed>)

Then, right-click on the drop-down list box and choose ‘Format Control’. Link the ‘Input range’ and ‘Cell link’. The number of ‘Drop down lines’ should be eight (8).

![](<Base64-Image-Removed>)

The cell **P1044** is named ‘**DD\_Simulations\_Outputs**‘, which is the indication of the drop-down choice.

The formula in cell **P1046** is

**\=INDEX(LU\_Simulation\_Outputs,DD\_Simulations\_Outputs)**

The **[OFFSET](https://www.sumproduct.com/thought/onset-of-offset)** function is used to get the **Stratification** and **Count**, respectively:

**\=OFFSET(E1048,,2\*DD\_Simulations\_Outputs)**

and

**\=OFFSET(F1048,,2\*DD\_Simulations\_Outputs)**

![](<Base64-Image-Removed>)

Next, define the [dynamic range name](https://www.sumproduct.com/thought/dynamic-range-names)
 using the **OFFSET** function:

**Chart\_Stratification = OFFSET(‘Simulation Example’!$P$1048,,,OFFSET(‘Simulation Example’!$F$1043,,’Simulation Example’!$P$1044),1)**

**Chart\_Count = OFFSET(‘Simulation Example’!$Q$1048,,,OFFSET(‘Simulation Example’!$F$1043,,’Simulation Example’!$P$1044),1)**

Select the value in the **Stratification** and **Count** columns to create a Column chart, then right-click on the chart and choose ‘Select Data…’.

![](<Base64-Image-Removed>)

Let the ‘Series values’ take the dynamic ‘**Chart\_Count**‘ range

![](<Base64-Image-Removed>)

and ‘Axis label range’ be the ‘**Chart\_Stratification’** range. Please note that the sheet name should also be included.

![](<Base64-Image-Removed>)

Last but not least, make the axis label dynamic by point it to the cell **‘Simulation Example’!$P$1046.**

![](<Base64-Image-Removed>)

That’s it for this week. Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-dynamic-simulation-charts/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-dynamic-simulation-charts/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-dynamic-simulation-charts/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-dynamic-simulation-charts/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-dynamic-simulation-charts/#0 "close")

top