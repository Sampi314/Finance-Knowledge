# Charts and Dashboards: Dynamic Chart Labels

**Source:** https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Dynamic Chart Labels

*   December 17, 2020

Charts and Dashboards: Dynamic Chart Labels
===========================================

Charts and Dashboards: Dynamic Chart Labels
===========================================

18 December 2020

_Welcome back to this week’s Charts and Dashboards blog series. This week, we show you how to create dynamic chart labels._

I have created a straightforward line chart in Excel and want to show both the data values and label the chart so that the label attaches itself to the position of the final data point rather than in a legend somewhere.

In this example, the aim is to attach the label for the chart series to the series itself, _e.g._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-87-1.jpg)

As you can see from the above figure, the line chart’s label appears on the right hand side next to the final data point in the series. If the values were to change, the label would move too:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-75-1.jpg)

You may note that the final period is earlier and that the values for the final point differ – yet the labels hang on steadfastly.

So how do we do this?

First of all, make sure your chart data is collated in a Table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-68-1.jpg)

The benefit is that if charts are linked to a Table range and the range is contracted or extended, the dependent chart will update automatically without having to use the ‘Select Data…’ functionality.

Creating a line chart from this Table is trivial. Simply highlight the Table and click on the Quick Analysis tool in the bottom right hand corner (**CTRL + Q**):

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-60-1.jpg)

Following the resultant prompts leads to a line chart in all of about two seconds. Right-clicking on one of the data series then allows you to add data labels:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-50-1.jpg)

By default, Excel adds the values. Right-clicking on these values and selecting ‘Format Data Labels…’ from the pop-up context menu triggers the ‘Format Data Labels’ task pane and allows you to choose **what** should be displayed (_e.g._ value, series name, category name), **where** it should be displayed (_e.g._ left of the data point, above it, below it) and **how** it should be displayed (format to use):

![](<Base64-Image-Removed>)

Selecting ‘Series Name’ in ‘Label Options’ _almost_ provides what is required:

![](<Base64-Image-Removed>)

The problem here is that we only require the series name against the final data point. If we need this to be flexible, manual adjustment is insufficient: we need to cheat.

‘Cheating’ requires us to add two more columns to the underlying data Table:

![](<Base64-Image-Removed>)

Assuming the first three columns have been labelled **Date**, **Sales Input** and **Costs Input** as in the example illustration above, we add two more columns **Sales** and **Costs** (_N.B._ in a Table, the same column heading may not be used more than once). The formulae in the two columns would be as follows:

**\=IF(OFFSET(\[@Date\],1,)=””,\[@\[Sales Input\]\],NA())**

_and_

**\=IF(OFFSET(\[@Date\],1,)=””,\[@\[Costs Input\]\],NA())**

The **@** symbol for Tables in Excel 2010 onwards signifies that the formula is referring to the data point for that field in that row, _e.g._ the formula highlighted in cell **I35** in the image is essentially

**\=IF(OFFSET(F35,1,)=””,G35,NA())**

which is effectively

**\=IF(F36=””,G35,NA())**

This is necessary as Table formulae do not like calculations linking to other rows.

These formulae cause the corresponding **Sales** and **Costs** values only to appear in the final row of the table, with _#N/A_ elsewhere. Normally, I would strongly recommend against having _prima facie_ errors in an Excel file, but here they are useful – this is the syntax required for these data points to be ignored by the chart engine.

You are almost done. All that is left is to highlight the revised Table and recreate the line chart from earlier. After selecting the Data Labels for the **Sales Input** and **Costs Input** series (just as previously), you simply add Data Labels for the two new “series” **Sales** and **Costs** even though they are singleton points:

![](<Base64-Image-Removed>)

_Et voila!_ You have created the chart required:

![](<Base64-Image-Removed>)

That’s it for this week. Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/#0 "close")

top