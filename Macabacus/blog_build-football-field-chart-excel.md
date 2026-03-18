# Building a Football Field Chart in Excel

**Source:** https://macabacus.com/blog/build-football-field-chart-excel

---

Building a Football Field Chart in Excel
========================================

![Football Field Demo](https://macabacus.com/assets/2023/09/football-field-hero.png)

Investment bankers often need to present a range of valuations for a company based on different methodologies like comparable companies analysis, precedent transactions analysis, DCF analysis, and LBO analysis.

One effective way to visually present these valuation ranges is through a football field chart (also known as a floating bar or column chart). This chart allows you to easily compare multiple valuation ranges in a clean graphical format.

In this post, I’ll walk you through step-by-step how to build a football field chart in Excel to showcase valuation ranges in investment banking.

### **Key Sections**

*   [Why Use a Football Chart](https://macabacus.com/blog/build-football-field-chart-excel#why-use)
    
*   [How to Build Your Football Field Chart in Excel](https://macabacus.com/blog/build-football-field-chart-excel#excel)
    
*   [Building a Football Field Chart Faster with Macabacus](https://macabacus.com/blog/build-football-field-chart-excel#macabacus)
    

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

**What is a Football Field Chart?**
-----------------------------------

A football field chart is a type of bar or column chart that shows different valuation ranges for a company. Each valuation methodology forms its own “field” going vertically, like the yards on a football field.

The chart typically displays:

*   The low and high ends of each valuation range
*   The midpoints of each range
*   The average of the different valuations

This allows readers to quickly visualize the full spectrum of valuations and identify outliers.

**Why Use a Football Field Chart?**
-----------------------------------

There are several benefits to using a football field chart for investment banking valuation analysis.

*   **Visually compares valuation ranges** – Rather than a table of numbers, the football field chart allows readers to quickly compare the valuation ranges visually in a graphical format.
*   **Identifies outliers** – It’s easy to see when one valuation range stands out from the others as an outlier. This allows you to dig deeper into the assumptions behind that methodology.
*   **Shows summary statistics** – The chart visually highlights the average and midpoints of the ranges, providing useful summary statistics at a glance.
*   **Clean format** – The football field chart presents the data in a clean, uncluttered way without excessive numbers or text.
*   **Flexibility** – You can include as many or as few valuation methodologies as you want. The chart works for 2-3 ranges or 10+ ranges.

For these reasons, the football field chart has become a popular way for investment bankers to communicate valuations visually in presentations and models.

**How to Build Your Football Field Chart in Excel**
---------------------------------------------------

### **1\. Organize Your Data**

Start by setting up your data. Create three columns:

*   Valuation Method
*   Minimum (or Low) Value
*   Maximum (or High) Value

For instance, your data could look something like:

![Organize Your Data](https://macabacus.com/assets/2023/09/building-a-football-chart-in-excel1.png)

### **2\. Prepare Your Data for Charting**

To make the data ready for a stacked column chart, create another column titled ‘Difference’ which calculates the difference between Maximum and Minimum values. The formula is =C2-B2 for the first row.

Your data should now look like this:

![Prepare Your Data for Charting](https://macabacus.com/assets/2023/09/building-a-football-chart-in-excel2.png)

### **3\. Create a Stacked Column Chart**

*   Highlight your data (excluding the ‘Valuation Method’ column).
*   Navigate to Insert > Column or Bar Chart > Stacked Column.

This will create a basic stacked column chart.

### **4\. Format the Chart**

*   Click on the chart. In the chart design options, select the data series which represents the ‘Minimum’ value.
*   Right-click and choose ‘Format Data Series.’
*   Under the ‘Fill’ option, choose ‘No Fill.’ This will make the ‘Minimum’ value invisible, leaving just the ‘Difference’ visible, thus creating the look of a football field chart.

### **5\. Finalize the Look and Feel**

*   Delete any legends, gridlines, or unnecessary labels.
*   Add data labels to show the exact range of each valuation method. You can add both minimum and maximum labels to give a clearer picture.
*   Adjust column width, colors, and fonts to match your desired aesthetics.

### **6\. Adjust Axes**

*   Make sure the vertical axis (Valuation Methods) lists the methods in the order you desire.
*   Adjust the horizontal axis to ensure it covers the full range of values you’re representing.

Creating a football field chart in Excel without external tools like Macabacus might take a bit more manual work, but the result is a clean, professional chart that clearly visualizes valuation ranges. With practice, this process becomes swift and intuitive, making it a key skill for anyone in finance to hone.

To create a football field chart the easy way, and with more formatting options, try using Macabacus.

**Building a Football Field Chart in Macabacus**
------------------------------------------------

Macabacus contains a built-in template to easily create football field charts for valuation ranges. Here’s how to use it:

1.  **Input your valuation data** – Set up your data with columns for valuation methodology, minimum value, and maximum value.
2.  **Select your data** – Highlight your input data to feed the football field chart.
3.  **Insert Football Field chart** – Go to CHARTS > Quick Charts > Football Field.
4.  **Configure settings** – Select your data in the dialog box. Adjust size, colors, data labels.
5.  **Refine formatting** – Tweak fonts, number formats, column widths to polish the look and feel.

Check out these video tutorials showing the process.

**Plotting the Chart**
----------------------

Excel does offer some native solutions, but they can be tedious. Using plugins like Macabacus can simplify the process:

*   Start by selecting your data range.
*   Navigate to the charts section and look for the football field chart option.
*   Once you’ve made your selection, a dialog box will appear. Set your preferred dimensions and orientation.
*   If you’d like to add a statistical line, such as an average or median line, you can choose to do so.
*   Once done, a new tab with the chart appears.

**Refining and Customizing the Chart**
--------------------------------------

The initial output may not be entirely aligned with your branding or desired aesthetic. You can:

*   Adjust data labels for clarity.
*   Modify the Y-axis and gridlines for a cleaner look.
*   Adjust font, size, and colors as per your brand.

*   For a more precise presentation, you can add lines indicating the average, median, or a targeted share price.

[**Try Macabacus for free**](https://macabacus.com/start-trial)
 and see for yourself how easy it is to create football field charts in Excel and create links to PowerPoint.

Discover more topics
--------------------

[Webinar: The AI Edge in Investment Banking](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Join experts from Macabacus & LSEG to learn practical insights about AI’s influence on the future of banking.

[Read more](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

[DCF Excel Template](https://macabacus.com/excel/templates/discounted-cash-flow)

Elevate your investment analysis with our free DCF model template. Understand discounted cash flow principles and perform accurate valuations in Excel.

[Read more](https://macabacus.com/excel/templates/discounted-cash-flow)

[Operating Model Excel Template](https://macabacus.com/excel/templates/operating-model)

Download our free operating model Excel template. Forecast revenue, expenses, and key financial metrics for better decision-making.

[Read more](https://macabacus.com/excel/templates/operating-model)

[LBO Excel Model](https://macabacus.com/excel/templates/lbo-model-short)

Try LBO modeling with our comprehensive Excel template. Understand key concepts, calculate returns, and gain actionable insights.

[Read more](https://macabacus.com/excel/templates/lbo-model-short)