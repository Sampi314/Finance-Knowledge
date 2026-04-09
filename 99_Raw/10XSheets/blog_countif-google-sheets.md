# How to Use COUNTIF in Google Sheets (With Multiple Criteria) - 10XSheets

**Source:** https://www.10xsheets.com/blog/countif-google-sheets

---

[Skip to content](https://www.10xsheets.com/blog/countif-google-sheets/#content)

[![10XSheets Logo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%2080'%3E%3C/svg%3E)![10XSheets Logo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%2080'%3E%3C/svg%3E)](https://www.10xsheets.com/)

[Get Started](https://www.10xsheets.com/templates)

![How to Use COUNTIF in Google Sheets With Multiple Criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

[Google Sheets](https://www.10xsheets.com/blog/category/google-sheets/ "Google Sheets")

How to Use COUNTIF in Google Sheets (With Multiple Criteria)
============================================================

By Hady ElHady

—

February 11, 2024

Share It!

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.10xsheets.com%2Fblog%2Fcountif-google-sheets%2F&t=How%20to%20Use%20COUNTIF%20in%20Google%20Sheets%20%28With%20Multiple%20Criteria%29 "Facebook")
[](https://x.com/intent/post?text=How%20to%20Use%20COUNTIF%20in%20Google%20Sheets%20%28With%20Multiple%20Criteria%29&url=https%3A%2F%2Fwww.10xsheets.com%2Fblog%2Fcountif-google-sheets%2F "X")
[](https://reddit.com/submit?url=https%3A%2F%2Fwww.10xsheets.com%2Fblog%2Fcountif-google-sheets%2F&title=How%20to%20Use%20COUNTIF%20in%20Google%20Sheets%20%28With%20Multiple%20Criteria%29 "Reddit")
[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.10xsheets.com%2Fblog%2Fcountif-google-sheets%2F&title=How%20to%20Use%20COUNTIF%20in%20Google%20Sheets%20%28With%20Multiple%20Criteria%29&summary=Ever%20wondered%20how%20to%20efficiently%20count%20and%20analyze%20data%20in%20Google%20Sheets%3F%20With%20COUNTIF%2C%20you%20can%20unlock%20the%20power%20of%20... "LinkedIn")
[](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.10xsheets.com%2Fblog%2Fcountif-google-sheets%2F&description=Ever%20wondered%20how%20to%20efficiently%20count%20and%20analyze%20data%20in%20Google%20Sheets%3F%20With%20COUNTIF%2C%20you%20can%20unlock%20the%20power%20of%20...&media= "Pinterest")

##### Get Started With a Prebuilt Model

Start with a free template and upgrade when needed.

[Explore Templates](https://www.10xsheets.com/templates)

*   [What is COUNTIF in Google Sheets?](https://www.10xsheets.com/blog/countif-google-sheets/#toc_What_is_COUNTIF_in_Google_Sheets)
    
*   [How to Use COUNTIF in Google Sheets?](https://www.10xsheets.com/blog/countif-google-sheets/#toc_How_to_Use_COUNTIF_in_Google_Sheets)
    
*   [Advanced Techniques with COUNTIF in Google Sheets](https://www.10xsheets.com/blog/countif-google-sheets/#toc_Advanced_Techniques_with_COUNTIF_in_Google_Sheets)
    
*   [Google Sheets COUNTIF Examples and Scenarios](https://www.10xsheets.com/blog/countif-google-sheets/#toc_Google_Sheets_COUNTIF_Examples_and_Scenarios)
    
*   [COUNTIF Google Sheets Tips and Best Practices](https://www.10xsheets.com/blog/countif-google-sheets/#toc_COUNTIF_Google_Sheets_Tips_and_Best_Practices)
    
*   [Conclusion](https://www.10xsheets.com/blog/countif-google-sheets/#toc_Conclusion)
    

Ever wondered how to efficiently count and analyze data in [Google Sheets](https://www.10xsheets.com/blog/how-to-use-google-sheets/)
? With COUNTIF, you can unlock the power of [data analysis](https://www.10xsheets.com/blog/data-analysis-software/)
 by effortlessly tallying occurrences based on specific criteria. Whether you’re tracking [sales](https://www.10xsheets.com/terms/budget-variance-analysis/)
 figures, monitoring [inventory](https://www.10xsheets.com/terms/inventory/ "Inventory is the collection of goods and materials a business holds for production, sale, or use.")
 levels, or analyzing survey responses, COUNTIF empowers you to extract valuable insights and make informed decisions. In this guide, we’ll explore the ins and outs of using COUNTIF in [Google Sheets](https://www.10xsheets.com/blog/how-to-use-google-sheets/)
, from its basic syntax to advanced techniques and practical examples. Let’s dive in and harness the full potential of COUNTIF for your [data analysis](https://www.10xsheets.com/blog/data-analysis-software/)
 needs.

What is COUNTIF in Google Sheets?
---------------------------------

The COUNTIF function in Google Sheets is a powerful tool designed to count the number of cells within a specified range that meet a given condition or criteria. Its primary purpose is to provide a quick and efficient way to perform counting operations based on specific criteria, allowing users to analyze data and extract valuable insights.

The function’s syntax is straightforward: `COUNTIF(range, criterion)`. The `range` parameter refers to the range of cells to be evaluated, while the `criterion` parameter specifies the condition that must be met for a cell to be counted.

COUNTIF is particularly valuable in scenarios where users need to quantify the occurrence of certain data points, such as counting the number of [sales](https://www.10xsheets.com/terms/budget-variance-analysis/)
 exceeding a certain threshold, tallying the frequency of specific keywords in a text corpus, or identifying missing or incomplete data entries in a dataset.

### Importance of COUNTIF in Data Analysis

The COUNTIF function plays a crucial role in data analysis by enabling users to:

*   **Quantify Data**: By counting occurrences based on specific criteria, COUNTIF allows users to quantify data points, providing valuable insights into patterns, trends, and distributions within their datasets.
*   **Filter Data**: COUNTIF can be used to filter data based on specific conditions, allowing users to focus on subsets of data that meet predefined criteria. This filtering capability is essential for conducting targeted analyses and drawing meaningful conclusions.
*   **Detect Patterns**: COUNTIF facilitates the detection of patterns and anomalies within datasets by identifying recurring occurrences or deviations from expected norms. This helps users identify areas of interest or concern that may require further investigation.
*   **Make Informed Decisions**: By providing quantitative metrics on data distributions, COUNTIF empowers users to make informed decisions based on objective evidence. Whether assessing [performance metrics](https://www.10xsheets.com/terms/performance-metrics/ "Performance metrics are quantifiable measures used to assess and evaluate the effectiveness of business operations.")
    , monitoring trends, or evaluating the effectiveness of strategies, COUNTIF supports data-driven decision-making processes.

The COUNTIF function is an indispensable tool for data analysts, researchers, and professionals across various industries. Its ability to efficiently count occurrences based on user-defined criteria makes it an invaluable asset for extracting insights, identifying patterns, and making informed decisions in data analysis workflows.

How to Use COUNTIF in Google Sheets?
------------------------------------

Understanding the basic usage of the COUNTIF function is crucial for efficiently analyzing data in Google Sheets.

### Counting Occurrences of a Specific Value

Counting occurrences of a specific value is a fundamental operation in data analysis. With COUNTIF, you can easily determine how many times a particular value appears within a given range.

Consider a scenario where you have a list of product names in column A, representing sales transactions. You want to know the number of times the product “Apple” was sold. To achieve this, you can [use](https://www.10xsheets.com/blog/best-online-form-builder-software/)
 the COUNTIF formula:

`=COUNTIF(A:A, "Apple")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Counting Occurrences of a Specific Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Counting-Occurrences-of-a-Specific-Value.png)

This formula counts all instances of “Apple” within column A and returns the total count.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Counting Occurrences of a Specific Value Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Counting-Occurrences-of-a-Specific-Value-Formula.png)

### Counting Occurrences Based on Criteria

The flexibility of COUNTIF extends beyond simple value matching. You can [use](https://www.10xsheets.com/blog/best-online-form-builder-software/)
 it to count cells based on various criteria, such as numerical comparisons, text patterns, or logical conditions.

Imagine you have a dataset of sales amounts in column B, and you’re interested in counting the number of sales exceeding $100. The COUNTIF formula for this scenario would be:

`=COUNTIF(B:B, ">100")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Counting Occurrences Based on Criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Counting-Occurrences-Based-on-Criteria.png)

This formula evaluates each cell in column B and counts those that are greater than $100.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Counting Occurrences Based on Criteria Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Counting-Occurrences-Based-on-Criteria-Formula.png)

### Google Sheets COUNTIF Blank

Dealing with blank cells is common when working with datasets. COUNTIF provides a convenient way to handle such scenarios by allowing you to count the number of blank cells within a range.

Suppose you have data in column C, and you need to determine how many cells are empty. You can use the following COUNTIF formula:

`=COUNTIF(C2:C21, "")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Blank.png)

This formula counts all blank cells within column C, providing insights into data completeness.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Blank Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Blank-Formula.png)

### Google Sheets COUNTIF Not Blank

Similarly, counting non-blank cells is often necessary for [data validation](https://www.10xsheets.com/blog/data-validation/)
 or analysis purposes. COUNTIF enables you to count cells that contain data, excluding empty cells.

For example, if you want to know how many cells in column D are populated with values, you can use the following formula:

`=COUNTIF(D2:D21, "<>")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Not Blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Not-Blank.png)

This formula counts all non-blank cells in column D, aiding in understanding data density.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Not Blank Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Not-Blank-Formula.png)

### Google Sheets COUNTIF Cell Contains Text

Counting cells containing specific text is a common requirement in data analysis. Whether you’re dealing with product descriptions, customer feedback, or transaction details, you can use COUNTIF to tally instances where cells contain particular text.

For example, suppose you have a list of customer comments in column B, and you want to count the number of comments containing the exact word “satisfied”. You can use the following COUNTIF formula:

`=COUNTIF(B:B, "satisfied")   `

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Cell-Contains-Text.png)

This formula counts all cells in column B that contain the word “satisfied”, regardless of its position within the cell.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Cell Contains Text Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Cell-Contains-Text-Formula.png)

### Google Sheets COUNTIF Contains Partial Text

In some cases, you may need to count cells containing partial text matches. This can be useful when dealing with variations or substrings of a word or phrase.

For instance, let’s say you have a list of product names in column A, and you want to count how many product names contain the word “apple” (e.g., “Apple”, “ApplePie”, “Pineapple”). You can use the following COUNTIF formula:

`=COUNTIF(A:A, "*apple*")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Contains Partial Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Contains-Partial-Text.png)

This formula counts all cells in column A that contain the substring “apple”.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Contains Partial Text Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Contains-Partial-Text-Formula.png)

### Google Sheets COUNTIF Greater Than

Counting cells with values greater than a specified threshold is a common [task](https://www.10xsheets.com/terms/erp-enterprise-resource-planning/)
 in data analysis. Whether you’re analyzing sales figures, exam scores, or [inventory](https://www.10xsheets.com/terms/inventory/)
 levels, COUNTIF can help you identify instances where values exceed a certain threshold.

For example, let’s assume you have a list of sales amounts in column C, and you want to count the ones greater than 100. You can use the following COUNTIF formula:

`=COUNTIF(C:C, ">100")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Greater Than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Greater-Than.png)

This formula counts all cells in column C with scores higher than 80.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Greater Than Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Greater-Than-Formula.png)

### Google Sheets COUNTIF Between Two Numbers

Counting cells falling within a range of numbers allows you to segment data and gain deeper insights into your dataset. Whether you’re analyzing sales [revenue](https://www.10xsheets.com/terms/revenue/ "Revenue is the income generated from the sale of goods or services.")
, age demographics, or temperature readings, COUNTIF can assist you in tallying cells within a specific numerical range.

Suppose you have a list of product prices in column C, and you want to count the number of products priced between $50 and $100. You can use the following COUNTIF formula:

`=COUNTIF(C:C, ">=50") - COUNTIF(C:C, ">100")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Between Two Numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Between-Two-Numbers.png)

This formula calculates the difference between the count of cells with prices greater than or equal to $50 and the count of cells with prices greater than $100, effectively giving you the count of cells within the specified range.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Google Sheets COUNTIF Between Two Numbers Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Google-Sheets-COUNTIF-Between-Two-Numbers-Formula.png)

By leveraging these basic functionalities of the COUNTIF function, you can perform a wide range of counting tasks in Google Sheets, empowering you to extract valuable insights from your data. Now, let’s delve into more advanced techniques and practical examples to further enhance your data analysis skills.

Advanced Techniques with COUNTIF in Google Sheets
-------------------------------------------------

Now, let’s explore advanced techniques that take your usage of the COUNTIF function in Google Sheets to the next level. These techniques include utilizing wildcards for flexible matching, combining COUNTIF with other functions for complex analysis, and effectively utilizing cell references.

### Using Wildcards for Flexible Matching

Wildcards in COUNTIF allow for versatile pattern matching within cells, enabling you to perform more flexible searches and counts. This feature is particularly useful when dealing with text data that may have variations or unknown characters.

For example, suppose you have a list of product codes in column A, where each code starts with “PROD-” followed by a unique identifier. You want to count all products that start with “PROD-“. You can use the following COUNTIF formula:

`=COUNTIF(A:A, "PROD-*")   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Using Wildcards for Flexible Matching](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Using-Wildcards-for-Flexible-Matching.png)

This formula counts all cells in column A that begin with “PROD-“.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Using Wildcards for Flexible Matching Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Using-Wildcards-for-Flexible-Matching-Formula.png)

### Wildcards in Google Sheets

Google Sheets provides several wildcards that you can use with functions like COUNTIF to perform flexible matching within cells. These wildcards allow for versatile pattern matching, making it easier to search for specific patterns or text fragments within your data.

#### Asterisk (\*) Wildcard

The asterisk wildcard represents zero or more characters in a search pattern. It can be used to match any sequence of characters in a cell.

Suppose you have a list of product codes in column A, where each code starts with “PROD-” followed by a unique identifier. You want to count all products that start with “PROD-“. You can use the following COUNTIF formula:

`=COUNTIF(A:A, "PROD-*")   `

This formula counts all cells in column A that begin with “PROD-“.

#### Question Mark (?) Wildcard

The question mark wildcard represents a single character in a search pattern. It can be used to match any single character in a cell.

Suppose you have a list of file names in column B, and you want to count all files with a three-letter extension. You can use the following COUNTIF formula:

`=COUNTIF(B:B, "*.???")   `

This formula counts all cells in column B that have a file name with a three-letter extension.

#### Tilde (~) Escape Character

The tilde wildcard is used as an escape character to match the actual wildcard characters (\*, ?, ~) in a cell. When you want to search for cells containing an asterisk, question mark, or tilde, you need to precede these characters with a tilde in your search pattern.

Suppose you have a list of email addresses in column C, and you want to count all addresses containing the “@” symbol. You can use the following COUNTIF formula:

`=COUNTIF(C:C, "*~@*")   `

This formula counts all cells in column C that contain the “@” symbol.

By leveraging these wildcards, you can perform more precise and flexible searches within your Google Sheets data, allowing for advanced analysis and insights.

### Combining COUNTIF with Other Functions for Complex Analysis

Combining COUNTIF with other functions in Google Sheets can enhance the depth of your data analysis and streamline complex calculations.

For instance, consider a scenario where you have a sales dataset with product categories in column A, sales quantities in column B, and [profit](https://www.10xsheets.com/terms/profit/ "Profit is the financial gain earned by a company after deducting all expenses from the revenue.")
 margins in column C. You want to determine the total number of sales for products with a [profit margin](https://www.10xsheets.com/terms/net-profit-margin/)
 above 20%. To achieve this, you can use the SUM function in conjunction with COUNTIF. Here’s how you can set up the formula:

`=SUM(COUNTIF(C:C, ">0.2") * (B:B))   `

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Combining COUNTIF with Other Functions for Complex Analysis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Combining-COUNTIF-with-Other-Functions-for-Complex-Analysis.png)

This formula first counts all cells in column C with [profit](https://www.10xsheets.com/terms/profit/)
 margins greater than 20% using COUNTIF. Then, it multiplies the count by the corresponding sales quantities from column B. The SUM function adds up the results, giving you the total number of sales for products with a [profit](https://www.10xsheets.com/terms/profit/ "Profit is the financial gain earned by a company after deducting all expenses from the revenue.")
 margin above 20%.

 [![How to Use COUNTIF in Google Sheets With Multiple Criteria Combining COUNTIF with Other Functions for Complex Analysis Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-With-Multiple-Criteria-Combining-COUNTIF-with-Other-Functions-for-Complex-Analysis-Formula.png)

This example demonstrates how combining COUNTIF with other functions allows for comprehensive analysis and actionable insights into your data.

### Utilizing Cell References Effectively

Instead of hardcoding values or criteria directly into your COUNTIF formulas, you can enhance flexibility and maintainability by referencing cells containing your criteria. This approach allows you to dynamically adjust criteria without modifying the formula itself, making your analysis more adaptable to changing data.

For example, suppose you have a threshold value stored in cell F2, and you want to count the number of sales exceeding this threshold in column C. You can use the following formula:

`=COUNTIF(C:C, ">" & F2)   `

 [![How to Use COUNTIF in Google Sheets Utilizing Cell References Effectively](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-Utilizing-Cell-References-Effectively.png)

This formula counts all cells in column C with values greater than the threshold specified in cell F2.

 [![How to Use COUNTIF in Google Sheets Utilizing Cell References Effectively Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%203360%202100'%3E%3C/svg%3E)](https://www.10xsheets.com/wp-content/uploads/How-to-Use-COUNTIF-in-Google-Sheets-Utilizing-Cell-References-Effectively-Formula.png)

By mastering these advanced techniques, you can elevate your data analysis capabilities in Google Sheets and tackle even the most complex counting tasks with ease. Now, let’s put these techniques into practice with practical examples and scenarios.

Google Sheets COUNTIF Examples and Scenarios
--------------------------------------------

Let’s explore practical examples and scenarios where you can apply the COUNTIF function in Google Sheets to solve real-world data analysis challenges. We’ll cover counting occurrences in a single column, counting occurrences in multiple columns, and conditional counting based on multiple criteria.

### Counting Occurrences in a Single Column

Counting occurrences in a single column is a common [task](https://www.10xsheets.com/terms/erp-enterprise-resource-planning/)
 when analyzing categorical data, such as product names, customer types, or service categories. You can use the COUNTIF function to quickly tally the frequency of each category.

For example, suppose you have a dataset with product names in column A, and you want to count the number of times each product appears. You can create a summary table by listing unique product names in one column and using the COUNTIF function in the adjacent column to count occurrences:

`=COUNTIF(A:A, "Product1")   `

This formula counts the occurrences of “Product1” in column A. Repeat this formula for each unique product name to generate a comprehensive summary of product frequencies.

### Counting Occurrences in Multiple Columns

Sometimes, you may need to count occurrences across multiple columns, especially when dealing with datasets with categorized information spread across different fields. In such cases, you can use a combination of COUNTIF and other functions to consolidate counts from multiple columns.

For instance, consider a dataset with customer feedback responses categorized into “Positive”, “Neutral”, and “Negative” across columns B, C, and D, respectively. You can calculate the total count of positive feedback using the following formula:

`=COUNTIF(B:D, "Positive")   `

This formula counts all occurrences of “Positive” across columns B, C, and D.

### Conditional Counting Based on Multiple Criteria

Conditional counting based on multiple criteria allows you to extract specific subsets of data from your dataset. You can use logical operators (AND, OR) along with COUNTIF to count cells that meet multiple conditions simultaneously.

For example, suppose you have a dataset with sales transactions, and you want to count the number of transactions where the product is “Product1” and the sales amount exceeds $100. You can use the following formula:

`=COUNTIFS(A:A, "Product1", B:B, ">100")   `

This formula counts all occurrences where the product is “Product1” in column A and the sales amount exceeds $100 in column B.

By applying the COUNTIF function in these practical examples and scenarios, you can efficiently analyze your data and extract valuable insights to inform decision-making processes. Now, let’s explore tips and best practices for optimizing your COUNTIF usage.

COUNTIF Google Sheets Tips and Best Practices
---------------------------------------------

To make the most out of the COUNTIF function in Google Sheets and ensure efficient data analysis, it’s essential to follow certain tips and best practices. By avoiding common pitfalls, optimizing formulas for performance, and organizing your data effectively, you can streamline your COUNTIF usage and enhance your productivity.

### Avoiding Common Pitfalls

1.  **Incorrect Range Selection**: Ensure that you select the correct range when using COUNTIF. Failing to do so can lead to inaccurate results.
2.  **Case [Sensitivity](https://www.10xsheets.com/terms/sensitivity-analysis/)
    **: Note that COUNTIF is case-sensitive when counting text values. Make sure your criteria match the case of the data.
3.  **Numeric Criteria**: When using numeric criteria, ensure they are formatted correctly. Mismatched formats can result in unexpected outcomes.
4.  **Mixed Data Types**: Be cautious when counting cells with mixed data types (e.g., numbers and text). COUNTIF may not function as expected in such cases.

### Optimizing Formulas for Performance

1.  **Minimize Volatile Functions**: Reduce the use of volatile functions (e.g., NOW, RAND) within COUNTIF formulas to improve performance. Volatile functions recalculate every time a change is made to the spreadsheet, impacting efficiency.
2.  **Limit Range Size**: Avoid using excessively large ranges in COUNTIF formulas. Restricting the range to only the necessary cells can speed up calculations.
3.  **Use Cell References**: Instead of hardcoding criteria directly into formulas, reference cells containing criteria. This makes formulas more dynamic and easier to adjust.
4.  **Use Helper Columns**: Consider using helper columns to preprocess data or simplify complex criteria. This can make COUNTIF formulas more manageable and efficient.

### Organizing Data for Better Analysis

1.  **Structured Data**: Organize your data in a structured format with clear headers and consistent formatting. This makes it easier to identify and select ranges for COUNTIF formulas.
2.  **Named Ranges**: Use named ranges to refer to specific data ranges in your formulas. Named ranges improve formula readability and make it easier to maintain and update your spreadsheet.
3.  **Regular Data Cleaning**: Regularly clean and update your data to remove duplicates, errors, or inconsistencies. Clean data ensures accurate results when using COUNTIF.
4.  **[Data Validation](https://www.10xsheets.com/blog/data-validation/)
    **: Implement data validation rules to enforce consistency and prevent data entry errors. This helps maintain data integrity and improves the reliability of COUNTIF calculations.

By adhering to these tips and best practices, you can maximize the effectiveness of the COUNTIF function in Google Sheets and streamline your data analysis workflows. Now, armed with these insights, you’re well-equipped to tackle a wide range of counting tasks with confidence and efficiency.

Conclusion
----------

Mastering the COUNTIF function in Google Sheets opens up a world of possibilities for data analysis and decision-making. By understanding its syntax, parameters, and various applications, you can efficiently count and analyze data based on specific criteria. Whether you’re a beginner or an experienced user, COUNTIF offers a user-friendly yet powerful tool for extracting valuable insights from your spreadsheets.

Furthermore, with the advanced techniques and practical examples covered in this guide, you’re equipped to tackle a wide range of data analysis tasks with confidence. From counting occurrences of specific values to conditional counting based on multiple criteria, COUNTIF empowers you to efficiently analyze your data and derive meaningful conclusions. So, next time you’re faced with a data analysis challenge in Google Sheets, remember the versatility and efficiency of the COUNTIF function, and let it guide you towards informed decision-making and actionable insights.

Get Started With a Prebuilt Template!
-------------------------------------

Looking to streamline your business financial modeling process with a prebuilt customizable template? Say goodbye to the hassle of building a [financial model](https://www.10xsheets.com/terms/financial-model/ "Financial Model is a quantitative representation of a company's financial situation and projections, used for analysis, planning, and decision-making.")
 from scratch and get started right away with one of our premium templates.

*   Save time with no need to create a financial model from scratch.
*   Reduce errors with prebuilt formulas and calculations.
*   Customize to your needs by adding/deleting sections and adjusting formulas.
*   Automatically calculate key metrics for valuable insights.
*   Make informed decisions about your strategy and goals with a clear picture of your business performance and [financial health](https://www.10xsheets.com/terms/financial-health/ "Financial Health is the measure of a company's fiscal well-being, encompassing liquidity, solvency, and profitability.")
    .

*   [Sale!\
    \
      ![Marketplace Financial Model Template - Contents and Instructions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![Marketplace Financial Model Template - Key Metrics (MoM)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/marketplace-financial-model/)
       
    
    ### [Marketplace Financial Model Template](https://www.10xsheets.com/templates/marketplace-financial-model/)
    
    ~184,03 €~ Original price was: 184,03 €.125,21 €Current price is: 125,21 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/marketplace-financial-model/)
     [Details](https://www.10xsheets.com/templates/marketplace-financial-model/)
    
*   [Sale!\
    \
      ![E-Commerce Financial Model Template - Getting Started and Instructions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![E-Commerce Financial Model Template - Key Metrics](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/ecommerce-financial-model/)
       
    
    ### [E-Commerce Financial Model Template](https://www.10xsheets.com/templates/ecommerce-financial-model/)
    
    ~184,03 €~ Original price was: 184,03 €.125,21 €Current price is: 125,21 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/ecommerce-financial-model/)
     [Details](https://www.10xsheets.com/templates/ecommerce-financial-model/)
    
*   [Sale!\
    \
      ![SaaS Financial Model Template - About](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![SaaS Financial Model Template - Financial Statements](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20320'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/saas-financial-model/)
       
    
    ### [SaaS Financial Model Template](https://www.10xsheets.com/templates/saas-financial-model/)
    
    ~184,03 €~ Original price was: 184,03 €.125,21 €Current price is: 125,21 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/saas-financial-model/)
     [Details](https://www.10xsheets.com/templates/saas-financial-model/)
    
*   [Sale!\
    \
      ![Standard Financial Model Template - Getting Started and Instructions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![Standard Financial Model Template - Income Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/standard-financial-model/)
       
    
    ### [Standard Financial Model Template](https://www.10xsheets.com/templates/standard-financial-model/)
    
    ~184,03 €~ Original price was: 184,03 €.125,21 €Current price is: 125,21 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/standard-financial-model/)
     [Details](https://www.10xsheets.com/templates/standard-financial-model/)
    
*   [Sale!\
    \
      ![E-Commerce Profit and Loss P&L Statement Template - Actuals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![E-Commerce Profit and Loss Statement - P&L Statement Template](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/ecommerce-profit-and-loss-statement/)
       
    
    ### [E-Commerce Profit and Loss Statement](https://www.10xsheets.com/templates/ecommerce-profit-and-loss-statement/)
    
    ~100,00 €~ Original price was: 100,00 €.66,39 €Current price is: 66,39 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/ecommerce-profit-and-loss-statement/)
     [Details](https://www.10xsheets.com/templates/ecommerce-profit-and-loss-statement/)
    
*   [Sale!\
    \
      ![SaaS Profit and Loss Statement P&L Template - Actuals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![SaaS Profit and Loss Statement P&L Template - P&L Statement](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/saas-profit-and-loss-statement/)
       
    
    ### [SaaS Profit and Loss Statement](https://www.10xsheets.com/templates/saas-profit-and-loss-statement/)
    
    ~100,00 €~ Original price was: 100,00 €.66,39 €Current price is: 66,39 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/saas-profit-and-loss-statement/)
     [Details](https://www.10xsheets.com/templates/saas-profit-and-loss-statement/)
    
*   [Sale!\
    \
      ![Marketplace Profit and Loss Statement P&L Template - Contents and Instructions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![Marketplace Profit and Loss Statement - P&L Statement Template](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/marketplace-profit-and-loss-statement/)
       
    
    ### [Marketplace Profit and Loss Statement](https://www.10xsheets.com/templates/marketplace-profit-and-loss-statement/)
    
    ~100,00 €~ Original price was: 100,00 €.66,39 €Current price is: 66,39 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/marketplace-profit-and-loss-statement/)
     [Details](https://www.10xsheets.com/templates/marketplace-profit-and-loss-statement/)
    
*   [Sale!\
    \
      ![Startup Profit and Loss Statement P&L Template - Contents and Instructions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E) ![Startup Profit and Loss Statement - P&L Template](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20318'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/startup-profit-and-loss-statement/)
       
    
    ### [Startup Profit and Loss Statement](https://www.10xsheets.com/templates/startup-profit-and-loss-statement/)
    
    ~100,00 €~ Original price was: 100,00 €.66,39 €Current price is: 66,39 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/startup-profit-and-loss-statement/)
     [Details](https://www.10xsheets.com/templates/startup-profit-and-loss-statement/)
    
*   [Sale!\
    \
      ![Startup Financial Model Template - Content and Instructions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20320'%3E%3C/svg%3E) ![Startup Financial Model Template - Profit and Loss](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20320'%3E%3C/svg%3E)](https://www.10xsheets.com/templates/startup-financial-model/)
       
    
    ### [Startup Financial Model Template](https://www.10xsheets.com/templates/startup-financial-model/)
    
    ~100,00 €~ Original price was: 100,00 €.66,39 €Current price is: 66,39 €.
    
    Value added tax is not collected, as small businesses according to §19 (1) UStG.
    
    [Add to Cart](https://www.10xsheets.com/templates/startup-financial-model/)
     [Details](https://www.10xsheets.com/templates/startup-financial-model/)
    

[More Templates](https://www.10xsheets.com/templates)

![Excel and Google Sheets Templates and Financial Models](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20584%20584'%3E%3C/svg%3E "Excel and Google Sheets Templates and Financial Models")

Expert Templates For You
------------------------

Don’t settle for mediocre templates. Get started with **premium spreadsheets and financial models** customizable to your unique business needs to help you save time and streamline your processes.

[Explore Templates](https://www.10xsheets.com/templates)

[![10XSheets Logo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%2080'%3E%3C/svg%3E)![10XSheets Logo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%2080'%3E%3C/svg%3E)](https://www.10xsheets.com/)

Receive Exclusive Updates
-------------------------

Get notified of **new templates and business resources** to help grow your business. Join our community of forward-thinking entrepreneurs and stay ahead of the game!

Submit

Thank you for your message. It has been sent.

×

There was an error trying to send your message. Please try again later.

×

[hello@10xsheets.com](mailto:hello@10xsheets.com)

[](https://www.youtube.com/@10XSheets)

© Copyright 2026 | 10XSheets | All Rights Reserved

[Page load link](https://www.10xsheets.com/blog/countif-google-sheets/#)

![You were not leaving your cart just like that, right?](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20600'%3E%3C/svg%3E "You were not leaving your cart just like that, right?")

Want a secret deal? 🚨
----------------------

💰 Get 10% off – but only if you act now!

 Save

![](https://www.10xsheets.com/blog/countif-google-sheets/)

🚨 Oops! You Forgot Something!
------------------------------

We saved your cart! Your templates are still waiting—grab them before they’re gone. 🛒 Tap to check out!

Continue [Maybe later](https://www.10xsheets.com/blog/countif-google-sheets/# "Maybe later")

[Go to Top](https://www.10xsheets.com/blog/countif-google-sheets/#)