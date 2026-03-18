# Step-by-Step: Format Excel Chart Data Labels as Thousands or Millions

**Source:** https://macabacus.com/blog/format-excel-chart-millions-thousands

---

Step-by-Step: Format Excel Chart Data Labels as Thousands or Millions
=====================================================================

When creating Excel charts, it’s easy to encounter issues during the display of large numbers on the value axis. Typically, Excel defaults to a full number format, showcasing all zeros (example: 1,500,000), which can lead to complications. Optimizing the axis for readability by cleanly formatting Excel chart data to millions or thousands can prevent it from appearing crowded and difficult to read.

Turn 1,600,000 -> 1.6M

And 900,000 -> 900K

We’ll dig into how to do this in Excel natively, but if you want a [**shortcut to handle this formatting in seconds**, skip ahead](https://macabacus.com/blog/format-excel-chart-millions-thousands#with-macabacus)
.

### [Format Excel Charts with Ease Using Macabacus](https://macabacus.com/start-trial)

**1,600,000 -> 1.6M is just a click away with Macabacus, [try for yourself](https://macabacus.com/start-trial)
**. Create professional, visually compelling charts in just a few clicks with Macabacus’ powerful charting tools. Customize data labels, formatting, and styling options to make your charts exceptionally clear.

[Start your Free Trial](https://macabacus.com/start-trial)

**The Problem with Large Numbers on Excel Charts**
--------------------------------------------------

Let’s look at an example. Here’s a column chart showing revenue by year. The amounts range from 0 to 1.6 million.

![Unformatted Chart in Millions and Thousands](https://macabacus.com/assets/2023/08/unformatted-chart-in-millions-thousands.png)

You can see that the y-axis feels cluttered with all those zeros. It’s not very readable or aesthetically pleasing. The core issue is that Excel displays the full unformatted number on charts by default. This works fine for smaller data sets, but isn’t ideal for larger numbers.

**Built-In Options to Format the Value Axis**
---------------------------------------------

Luckily, Excel provides a few built-in options to format the value axis units

*   **Thousands –** Displays numbers in thousands (example: 1.6K for 1,600)
*   **Millions –** Displays numbers in millions (example: 1.5M for 1,500,000)
*   **Billions –** Displays numbers in billions (example: 1.5B for 1,500,000,000)

**To access these options**

1.  Select the chart and go to Chart Design > Add Chart Elements > Axes > Primary Vertical
2.  In the Format Axis pane, go to Axis Options > Units
3.  Choose the desired units: Thousands, Millions, or Billions
4.  Go to the “Number” dropdown and insert: **$\* #,##0.#\_**

![Instructions in Formatting Excel Chart](https://macabacus.com/assets/2023/08/instructions-formatting-excel-chart.png)

![Numbers Format](https://macabacus.com/assets/2023/08/numbers-format.png)

This will automatically scale the units on the axis and add the appropriate abbreviation (K, M, B) after the numbers.

Here’s how the chart looks after formatting to millions:

![Chart Excel Reformatted in Millions](https://macabacus.com/assets/2023/08/chart-excel-reformatted-in-millions.png)

Much cleaner and easier to read! The axis only displays the necessary units without cluttering it up with extra zeros.

**Limitations of Built-In Formatting**
--------------------------------------

The built-in options work well, but you do have a few limitations.

*   You will have to manually update the chart if the data changes substantially. Excel doesn’t dynamically recalculate the best scale.
*   You can only show units in thousands, millions, or billions. There’s no other way to customize other formats like hundred thousands.
*   Custom number formatting can be difficult to figure out and, as you can see, sometimes it adds a “1.”. It’s not a huge deal, but is a bit inconsistent with what we’d like to see.

**Alternatives for More Customization**
---------------------------------------

To overcome these limitations, you can create custom number formats for the axis:

Millions and Thousands

$\* #,##0.#\_, “M”;($\* #,##0.#\_, “K”)

This displays large numbers in millions and smaller numbers in thousands. No abbreviation is shown if not needed.

This lets you fully customize the units, text, separators, decimals, and more. The advantage of creating custom formats is you get complete control. You can tweak it to fit your specific data and preferences. The only caveat is that you’ll need to manually update it if your data changes drastically. There’s no automatic scaling like the built-in options.

**Formatting Excel Chart Axis in a Few Clicks with Macabacus**
--------------------------------------------------------------

Manually updating axis formats can be tedious, especially with multiple charts. You see this a lot in finance and banking and it’s where Macabacus can help. Macabacus has a simple option to format your Excel charts to millions or thousands with one click. 

**Here’s how it works:**

1.  [Download your Macabacus Free Trial](https://macabacus.com/start-trial)
    
2.  Select your chart and go to Macabacus > Charts
3.  Scroll to Other Formats > Y-Axis Formats
4.  Choose Format for Millions or Format for Thousands

[![format axis with macabacus](https://macabacus.com/assets/2023/09/format-axis-with-macabacus.png)](https://macabacus.com/assets/2023/09/format-axis-with-macabacus.png)

That’s it! Macabacus instantly applies the appropriate formatting across all your selected charts. It also does the work of updating the format dynamically if your data changes substantially. No more manual tweaking needed.

**[Sign up for a free trial of Macabacus](https://macabacus.com/start-trial)
** to format charts and speed up your Microsoft Office workflows.

Macabacus makes it easy to optimize large numbers on your Excel charts. Whether you have a few charts or hundreds, it helps apply and update value axis formats.

**Key Takeaways**
-----------------

Large, unformatted numbers can clutter Excel chart axes. Use these approaches to cleanly format the values in millions, thousands, or custom units.

*   Leverage Excel’s built-in options of Thousands, Millions, Billions
*   Create custom number formatting for advanced customization
*   Use Macabacus to automate formatting across charts, with dynamic updates when data changes

Proper number formats help create more readable, professional charts. Try out these options next time you build charts with large data sets in Excel.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

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