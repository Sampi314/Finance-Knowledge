# Merge Data Using CONCATENATE or TEXTJOIN (Downloadable Template)

**Source:** https://macabacus.com/blog/merge-data-using-concatenate-textjoin

---

Merge Data Using CONCATENATE or TEXTJOIN
========================================

![Merge Data Using CONCATENATE or TEXTJOIN](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin.jpg)

Efficiently merging and manipulating data is a critical skill in finance. Combining information from various sources is a constant challenge for professionals who generate reports and conduct analyses. 

Fortunately, Microsoft Excel offers two functions to merge data: **CONCATENATE** and **TEXTJOIN**. Below, we will explore their utility in financial data management. You can also find an investment banking dataset to help you practice and apply the concepts discussed here.

**TABLE OF CONTENTS**

1.  [Understanding CONCATENATE](https://macabacus.com/blog/merge-data-using-concatenate-textjoin#understanding)
    
2.  [Exploring TEXTJOIN](https://macabacus.com/blog/merge-data-using-concatenate-textjoin#exploring)
    
3.  [Download Excel Template](https://macabacus.com/blog/merge-data-using-concatenate-textjoin#download)
    
4.  [Comparison Between CONCATENATE and TEXTJOIN](https://macabacus.com/blog/merge-data-using-concatenate-textjoin#comparison)
    
5.  [Advanced Usage Tips](https://macabacus.com/blog/merge-data-using-concatenate-textjoin#advanced)
    
6.  [Troubleshooting Common Issues](https://macabacus.com/blog/merge-data-using-concatenate-textjoin#troubleshooting)
    

**Understanding CONCATENATE**
-----------------------------

The CONCATENATE function in Excel is a tool for combining texts from multiple cells into a single cell. The function is essential for creating unique identifiers, merging client data, or generating comprehensive reports.

The syntax for CONCATENATE is:

**\=CONCATENATE(text1, \[text2\], …)**

Here, “**text1**” represents the first item to be merged, while “**\[text2\]**” and any subsequent arguments are optional additional items. 

Let’s consider a practical example using our investment banking dataset. Suppose you combine investors’ first and last names for more transparent financial documentation. 

You can do so by using the following formula:

**\=CONCATENATE(A2, ” “, B2)**

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-1.jpg)

In the above example, A2 contains the first name, B2 contains the last name, and the space in quotes (” “) adds a separator between the two. By dragging the formula down the column, you can quickly merge the names of all investors in your dataset.

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-2.jpg)

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-3.jpg)

Another everyday use case in finance is merging city and country information to view client locations comprehensively. Assuming the city is in column D and the country in column E, you can use CONCATENATE as follows:

**\=CONCATENATE(D2, “, “, E2)**

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-4.jpg)

The above formula combines the city and country with a comma and space separator, resulting in a merged location format such as “**New York, USA**.”

**Exploring TEXTJOIN**
----------------------

Although **CONCATENATE** is a valuable function, it may come with limitations when working with complex merging scenarios. Luckily, Excel 2019 introduced the **TEXTJOIN** function, which allows for concatenating text strings with a specified delimiter and the option to ignore empty cells. 

The syntax for TEXTJOIN is as follows:

**\=TEXTJOIN(delimiter, ignore\_empty, text1, \[text2\], …)**

**Where**:

*   The ‘**delimiter**‘ argument specifies the character or string between each merged item. For example, a comma as the delimiter will separate each item with a comma.
*   The ‘**ignore\_empty**‘ argument decides if empty cells should be included in the merged result (TRUE/FALSE). 
*   If set to **TRUE**, empty cells will be skipped. 

Let’s explore a practical example using our investment banking dataset. Create a formatted list of investment types for a client using columns F-J; some cells may be empty.

You can use TEXTJOIN to create a consolidated list as follows:

**\=TEXTJOIN(“, “, TRUE, F2:H2)**

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-5.jpg)

The formula sets the delimiter to comma and space and skips empty cells to display a formatted list of investment types.

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-6.jpg)

Combining investment amounts with their corresponding types can be quickly done using the **TEXTJOIN** function. Assuming the investment amounts are in columns H through K, you can use the following formula:

**\=TEXTJOIN(“, “, TRUE, “Amount Invested: $” & SUM(H:H), “Stocks: $” & SUM(I:I), “Bonds: $” & SUM(J:J), “Mutual Funds: $” & SUM(K:K))**

![merge data using concatenate textjoin](https://macabacus.com/assets/2024/05/merge-data-using-concatenate-textjoin-7.jpg)

The above formula concatenates each investment type with its corresponding amount, separated by a colon and a dollar sign. The result will provide a clear overview of the client’s investment allocations:

*   Amount Invested: $410
*   Stocks: $100
*   Bonds: $72
*   Mutual Funds: $160

**Download Excel Template**
---------------------------

![Download Template](https://macabacus.com/assets/macabacus-tables-template.svg)

Download Template
-----------------

[Merge Data Using CONCATENATE or TEXTJOIN](https://macabacus.com/assets/2024/05/Merge-Data-Using-CONCATENATE-or-TEXTJOIN-in-Excel_Dataset.xlsx)

**[Try Macabacus for free](https://macabacus.com/start-trial)
** to accelerate financial modeling in Excel.

**Comparison Between CONCATENATE and TEXTJOIN**
-----------------------------------------------

CONCATENATE and TEXTJOIN are Excel functions used to merge data. The difference is that CONCATENATE requires the delimiter to be manually included between items. Meanwhile, TEXTJOIN allows you to specify the delimiter once and apply it automatically. It makes TEXTJOIN more efficient for handling large amounts of data.

Use TEXTJOIN to merge cells without unwanted spaces. The ‘ignore\_empty’ argument lets you include or exclude empty cells from the merged output. Such a feature is helpful for financial datasets.

Finance professionals can improve efficiency and readability by switching from CONCATENATE to TEXTJOIN. TEXTJOIN is available in Excel 2019 and Excel for Microsoft 365. For earlier versions of Excel, use other functions like IF and ISBLANK.

**Advanced Usage Tips**
-----------------------

Mastering the use of CONCATENATE and TEXTJOIN with finance functions like XLOOKUP can significantly enhance your data merging capabilities. XLOOKUP is a powerful tool for locating and retrieving data from a table or range. Combined with CONCATENATE or TEXTJOIN, it becomes a dynamic data-merging solution based on your specific criteria.

To create dynamic reports from a table of client information with columns for client ID, name, and investment type, you can use XLOOKUP to find the investment type for a specific client ID and merge it with other relevant data using CONCATENATE or TEXTJOIN. It enables your reports to update automatically based on the selected client.

Combine TEXTJOIN with SUMIF/SUMIFS for efficient and readable complex data aggregation in Excel.

Optimizing performance is crucial when working with large financial datasets. Use helper columns, break down data into smaller chunks, and use named ranges or tables for easier reference and maintenance.

**Troubleshooting Common Issues**
---------------------------------

Even with the power of CONCATENATE and TEXTJOIN, there are common pitfalls that finance professionals may encounter when merging data. One issue is ensuring data accuracy and consistency. Before merging financial records, it’s crucial to validate and clean your data to avoid propagating errors or inconsistencies. It may involve using data validation techniques, removing duplicates, or standardizing formats.

Another challenge is maintaining scalable and readable financial models in Excel. As your data merging tasks become more complex, it’s essential to structure your workbook in a way that promotes clarity and ease of use. It can include using named ranges for frequently referenced data, organizing your worksheets logically, and providing clear documentation or comments for complex formulas.

If you encounter unexpected results or errors when using CONCATENATE or TEXTJOIN, there are a few troubleshooting steps you can take. First, double-check your syntax and ensure that you already included all the necessary arguments. Pay close attention to the placement of commas, quotation marks, and parentheses. If you’re working with text that contains special characters or delimiters, make sure to use appropriate text qualifiers or escape characters to avoid conflicts.

Another common issue is dealing with leading or trailing spaces in merged data. To remove unwanted spaces, you can wrap your CONCATENATE or TEXTJOIN formulas with the TRIM function, which eliminates any extra spaces from the beginning and end of the merged result.

**Conclusion**
--------------

In conclusion, CONCATENATE and TEXTJOIN are indispensable tools for finance professionals looking to streamline their data merging tasks in Excel. By mastering the said functions, you can efficiently combine information from various sources, generate comprehensive reports, and perform in-depth analyses. The real-world case studies presented above demonstrate the versatility and power of both functions in the context of portfolio management, client reporting, and risk analysis.

To further enhance your skills and accelerate your professional growth, we encourage you to use the provided investment banking dataset and practice applying the concepts discussed above. Experiment with various merging scenarios, integrate CONCATENATE and TEXTJOIN with other essential Excel functions, and explore methods to optimize your financial models for both performance and readability.

As you incorporate the above techniques into your daily workflow, consider exploring Macabacus to further elevate your productivity. **[Macabacus](https://macabacus.com/start-trial)
** offers specialized tools that enhance Excel capabilities and ensure seamless integration with PowerPoint and Word, making them ideal for finance and banking professionals committed to precision and efficiency. Discover how Macabacus can help you save time, maintain document consistency, and meet high brand compliance standards!

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