# Income tax bracket calculation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/income-tax-bracket-calculation

---

[Skip to main content](https://exceljet.net/formulas/income-tax-bracket-calculation#main-content)

[](https://exceljet.net/formulas/income-tax-bracket-calculation#)

*   [Previous](https://exceljet.net/formulas/get-stock-price-on-specific-date)
    
*   [Next](https://exceljet.net/formulas/mortgage-payment-schedule)
    

[Financial](https://exceljet.net/formulas#Financial)

Income tax bracket calculation
==============================

by Dave Bruns · Updated 7 Mar 2026

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[LET](https://exceljet.net/functions/let-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

[DROP](https://exceljet.net/functions/drop-function)

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

[FILTER](https://exceljet.net/functions/filter-function)

[OFFSET](https://exceljet.net/functions/offset-function)

[CHOOSECOLS](https://exceljet.net/functions/choosecols-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9471/download?token=GeTjG4mn)
 (26.25 KB)

![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")

Summary
-------

To calculate the total income tax owed in a progressive tax system with multiple tax brackets, you can use a simple, elegant approach that leverages Excel's new [dynamic array engine](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. In the worksheet shown, the main challenge is to split the income in cell I6 into the correct tax brackets. This is done with a single formula like this in cell E7:

    =LET(
    income,I6,
    upper,C7:C13,
    lower,DROP(VSTACK(0,upper),-1),
    IF(income<=lower,0,
    IF(income>upper,upper-lower,income-lower))
    )
    

This formula splits the income into the seven brackets in column E in one step. After that, simple formulas can be used to compute the tax per bracket and total tax. As explained [below](https://exceljet.net/formulas/income-tax-bracket-calculation#single-formula-option)
, it is also possible to extend this formula to calculate all taxes in one step.

_Note: Because this formula uses new functions like LET, DROP, and VSTACK, it requires a current version of Excel. In older versions of Excel, you can use a more traditional formula approach. Both methods are explained below._

Explanation 
------------

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two different methods:

1.  A [modern approach](https://exceljet.net/formulas/income-tax-bracket-calculation#method-1---a-modern-and-elegant-approach)
     that leverages the latest Excel formulas and functions
2.  A [traditional approach](https://exceljet.net/formulas/income-tax-bracket-calculation#method-2---a-traditional-formula-approach)
     that works in older versions of Excel.

The main focus of this article is a method to split income out by tax bracket in column E so that taxes can easily be computed in column F. However, it also discusses a [single formula](https://exceljet.net/formulas/income-tax-bracket-calculation#single-formula-option)
 solution to calculate all taxes in one step in cell I7. The article also explains how to make the tax rates dynamic based on the taxpayer's status in cell C4 and the year selected in F4.

> New: I've updated the worksheet to include tax rates for the year 2025. I've also modified the worksheet to store tax rates for previous years and fetch the correct rates for a given year based on the user's year selection in F4.

Table of Contents
-----------------

*   [Instructions](https://exceljet.net/formulas/income-tax-bracket-calculation#instructions)
    
*   [About progressive tax brackets](https://exceljet.net/formulas/income-tax-bracket-calculation#about-progressive-tax-brackets)
    
*   [Tax calculation with multiple brackets](https://exceljet.net/formulas/income-tax-bracket-calculation#tax-calculation-with-multiple-brackets)
    
*   [Method 1 - A modern and elegant approach](https://exceljet.net/formulas/income-tax-bracket-calculation#method-1---a-modern-and-elegant-approach)
    
*   [Single formula option](https://exceljet.net/formulas/income-tax-bracket-calculation#single-formula-option)
    
*   [Marginal vs. Effective Tax Rates](https://exceljet.net/formulas/income-tax-bracket-calculation#marginal-vs.-effective-tax-rates)
    
*   [Method 2 - A traditional formula approach](https://exceljet.net/formulas/income-tax-bracket-calculation#method-2---a-traditional-formula-approach)
    
*   [Clever MIN and MAX alternative](https://exceljet.net/formulas/income-tax-bracket-calculation#clever-min-and-max-alternative)
    
*   [Dynamic tax brackets](https://exceljet.net/formulas/income-tax-bracket-calculation#dynamic-tax-brackets)
    
*   [How to update the worksheet with new tax rates](https://exceljet.net/formulas/income-tax-bracket-calculation#how-to-update-the-worksheet-with-new-tax-rates)
    

### Instructions

Download the attached Excel workbook. The formulas in Sheet1 require a current version of Excel (Excel 365 or Excel 2024). The formulas in Sheet2 should work in any version. The worksheets require only three inputs:

1.  Select your filing status using the dropdown in C4.
2.  Select the tax year using the dropdown in cell  F4.
3.  Enter your taxable income in cell I6. 

Sheet3 contains U.S. federal tax rates for the years 2023, 2024, and 2025. Sheet1 and Sheet2 calculate the taxes in different ways, but given the same inputs, the results should be the same.

### About progressive tax brackets

The U.S. has a progressive tax system, which means that as your income increases, so does the rate at which you're taxed. Instead of taxing all income at a single rate, income is split into different "brackets," with each portion taxed at a different rate. The more you earn, the more income falls into higher brackets, which have a progressively higher rate. The IRS [publishes brackets and tax rates](https://www.irs.gov/filing/federal-income-tax-rates-and-brackets)
 each year. For 2025, the tax rates for a single taxpayer look like this:

| Tax rate | on taxable income from... | up to... |
| --- | --- | --- |
| 10% | $0  | $11,925 |
| 12% | $11,926 | $48,475 |
| 22% | $48,476 | $103,350 |
| 24% | $103,351 | $197,300 |
| 32% | $197,301 | $250,525 |
| 35% | $250,526 | $626,350 |
| 37% | $626,351 | And up |

> _Note: I don't know why the IRS adds $1.00 to the "From" values. This may \*look\* correct, but it isn't mathematically correct and may cause you to "lose" 1 dollar of income in some brackets. To keep things simple and avoid confusion, I have removed the extra $1.00 in the worksheet example. For the same reason, the "modern" formulas below ignore the "From" values and generate their own lower thresholds directly using the "To" values._

### Tax calculation with multiple brackets

Taxes are calculated progressively through the brackets. For example, for a single filer with $100,000 of taxable income in 2025, the total tax owed is calculated as follows:

*   In the first bracket, from $0 to $11,925, $11,925 is taxed at 10% = $1,193.
*   In the second bracket, from $11,925 to $48,475, $36,550 is taxed at 12% = $4,386.
*   In the third bracket, from $48,475 to $103,350, $51,525 is taxed at 22% = $11,336.
*   Since $100,000 does not exceed $103,350, no portion is taxed at 24%.

The total tax is $16,915, with each portion of income taxed at progressively higher rates. The marginal tax rate is 22%, and the effective tax rate is 16.9%.

### Method 1 - A modern and elegant approach

First, let's solve this problem in a fun, modern way. The hard part of this problem is splitting the income by bracket. These are the numbers seen in the range E7:E13. To be clear, the math is simple, but implementing the math using cell references can be tricky. In the worksheet shown, the formula used in cell E7 is:

    =LET(
    income,I6,
    upper,C7:C13,
    lower,DROP(VSTACK(0,upper),-1),
    IF(income<=lower,0,
    IF(income>upper,upper-lower,income-lower))
    )
    

This formula returns the correct income per bracket for all seven brackets at once. Compared to traditional formulas, it has several notable advantages:

1.  Just one formula, so there is no need to copy and paste.
2.  Only two cell references are required.
3.  There is no need to lock references due to the magic of dynamic arrays.
4.  Only the upper limits are required. The lower limits are generated automatically.
5.  Variable names that make the formula easier to read and understand.

Let's walk through how the formula works step by step. First, to make the formula more readable and efficient by storing and reusing values, the [LET function](https://exceljet.net/functions/let-function)
 defines three variables:

    =LET(
    income,I6,
    upper,C7:C13,
    lower,DROP(VSTACK(0,upper),-1),
    

*   _income_: This is the income to be taxed, coming from cell I6.
*   _upper_: The "upper" limits of the tax brackets, from range C7:C13.
*   _lower_: This creates the "lower" limits of the tax brackets. (see below)

The lower limits are generated with the [VSTACK function](https://exceljet.net/functions/vstack-function)
 and the [DROP function](https://exceljet.net/functions/drop-function)
 like this:

    DROP(VSTACK(0,upper),-1)
    

The values in _upper_ are from the range C7:C13. In array form, they look like this:

    {11925;48475;103350;197300;250525;626350;"And up"}
    

Inside DROP, VSTACK is used to add a zero (0) as the first value:

    =VSTACK(0,upper)
    

The result is an array like this:

    {0;11925;48475;103350;197300;250525;626350;"And up"}
    

This array is returned directly to the DROP function, which is configured to remove the last row:

    =DROP({0;11925;48475;103350;197300;250525;626350;"And up"},-1)
    

The result is a new array without the "And up" value:

    {0;11925;48475;103350;197300;250525;626350}
    

At this point, we have the _upper_ and lower arrays _correctly_ aligned and are ready to implement the logic.

> _Note: I could have picked up the lower values directly from the range B7:B13. However, I wanted this formula to work when only the upper threshold brackets are available. Because the formula uses the upper values to derive the lower values, the values in B7:B13 can be removed, and the formula will continue to operate correctly._

Next, we get to the heart of the formula, which is based on a nested [IF function](https://exceljet.net/functions/if-function)
.

    IF(income<=lower,0,
    IF(income>upper,upper-lower,income-lower))
    

The key to understanding this code is to remember that we are processing an _array_ of values, not just a single value. Because the _upper_ and _lower_ arrays each contain seven values, the formula will return seven results that will "flow" through the nested IF according to the following logic:

*   If the income is less than or equal to the lower bound of a bracket, then no income falls within that bracket, so the tax contribution from this bracket is 0.
*   If the income is _greater_ than the upper limit of the current bracket, the result is the difference between the upper and lower limits (upper - lower), which represents the full taxable portion for that bracket.
*   Otherwise, the result is the difference between the income and the lower limit (income - lower), which is the portion of the income that falls within that bracket.

In summary, the formula uses the upper limits in C7:C13 to compute the correct lower limits. Then, it uses the IF function and the upper and lower limits to split the income in cell I6 into the correct brackets. Once the income is split by bracket, we can easily calculate the tax per bracket with a formula like this in cell F7:

    =D7:D13*E7:E13
    

This formula simply multiplies the tax rates in D7:D13 by the income splits in E7:E13. The result is an array of 7 values like this, which spill into F7:F13:

    {1193;4386;11336;0;0;0;0}
    

To compute the total taxes owed in F15, we use the SUM function:

    =SUM(F7:F13)
    

The formula in E15 serves as a sanity check to make sure that all income from I6 has been accounted for:

    =SUM(E7:E13)
    

### Single formula option

So far, we have calculated the tax per bracket and total tax with separate formulas that return "per bracket" results on the worksheet. This is a good approach because it makes it easy to validate results at any point. But what if you want to calculate the total taxes owed in a _single_ formula? In that case, we need to add a few more lines of code to our formula. Below is the formula in cell I7, which does everything in one step:

    =LET(
    income,I6,
    tax_rates, D7:D13,
    upper,C7:C13,
    lower,DROP(VSTACK(0,upper),-1),
    income_by_bracket,IF(income<=lower,0,
    IF(income>upper,upper-lower,income-lower)),
    tax_by_bracket,income_by_bracket*tax_rates,
    SUM(tax_by_bracket)
    )
    

This new formula extends the original formula by adding three new variables:

*   _tax\_rates_ - the range D7:D13
*   _income\_by\_bracket_ - defined by the nested IF code explained above
*   _tax\_by\_bracket_ - defined by _income\_by\_bracket_ \* _tax\_rates_

Then, on the last line, we use the SUM function to return a result by summing the amounts in _tax\_by\_bracket_:

    SUM(tax_by_bracket)
    

This result matches the value in cell F15. Next, let's look at how to calculate the marginal and effective tax rates.

### Marginal vs. Effective Tax Rates

When discussing income tax, there are two rates you are likely to encounter: the marginal tax rate and the effective tax rate. The _marginal tax_ is the tax rate applied to the last dollar earned. For $100,000 of income, the marginal tax rate is 22% since that's the rate applied to income in the third bracket. The _effective tax_ is the overall percentage of income paid in taxes. It's calculated by dividing the total tax ($16,915) by the total income ($100,000), which gives an effective tax rate of 16.9%. This demonstrates that while the highest rate paid on the last portion of income is 22%, the _average_ rate across all brackets is lower due to the progressive system. To compute the marginal tax rate in cell I8, we use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 like this:

    =XLOOKUP(I6,C7:C13,D7:D13,,1)
    

*   _lookup\_value_ - from I6
*   _lookup\_array_ - the upper values in C7:C13
*   _return\_array_ - the tax rates in D7:D13
*   _if\_not\_found_ - omitted
*   _match\_mode_ - 1, for an exact match or next largest

The key here is the setting for _match\_mode_ (1), which causes XLOOKUP to return the next largest tax rate when an exact match on income is not found. To compute the effective tax rate in I9, we divide the total computed tax in I7 by the taxable income in I6:

    =I7/I6
    

The results from both formulas are formatted using Excel's [percentage number format](https://exceljet.net/glossary/percentage-number-format)
.

### Method 2 - A traditional formula approach

In older versions of Excel that do not support dynamic array formulas, I think the easiest solution is to use the "From" values directly in your calculations, then use the same nested IF logic explained above to compute the income by bracket. You can see this approach in the worksheet below:

![Calculating income by bracket with a traditional formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/income_tax_bracket_calculation_traditional_formula_approach.png "Calculating income by bracket with a traditional formula")

As mentioned above, the main challenge is to split the income in cell I6 by bracket in a clean and simple way. This is done with the following formula in cell E7:

    =IF($I$6<=B7,0,IF($I$6>C7,C7-B7,$I$6-B7))
    

As the formula is copied down, the income in each bracket is calculated like this:

*   If the income in I6 is less than or equal to the lower bound in B7, then no income falls within that bracket, so the tax contribution from this bracket is 0.
*   If the income in I6 is _greater_ than the upper limit (C7), the result is the difference between the upper and lower limits (C7 - B7). This is the full taxable portion for that bracket.
*   Otherwise, the result is the difference between the income and the lower limit (I6 - B7), which is the remaining portion of the income that falls within that bracket.

Then, to calculate the tax in each bracket, multiply the tax rate by the income in cell F7:

    =D7*E7
    

As this formula is copied down column F, it returns the correct income tax in each bracket.

### Clever MIN and MAX alternative

If you like clever formulas, you can simplify the nested IF logic above by replacing it with a more compact alternative based on [MAX](https://exceljet.net/functions/max-function)
 and [MIN](https://exceljet.net/functions/min-function)
 like this:

    =MAX(0,MIN($I$6,C7)-B7)
    

Both formulas apply the same logic and return the same results.

### Dynamic tax brackets

> Retrieving the correct tax rates for a given filing status and year isn't the main focus of splitting income into tax brackets and calculating the tax in each bracket. However, it's an important part of this worksheet's design, so I want to explain how it's done. The lookup formulas below are advanced. They are built on the idea that you can use numeric indexes for lookup operations that need to change based on specific inputs. For example, "Married filing jointly" is item 2 in the list of status options. The main idea is that we can do something intelligent with the number 2, when the user has made that selection. Specifically, we want to retrieve columns 4 and 5 when the filing status is 2. The trick is working out the simple math operations needed to convert the 2 into a 4 and 5. If you haven't been exposed to this idea before, don't be discouraged. Learning how to design and implement formulas like this takes time and practice. See [this page](https://exceljet.net/formulas/step-based-lookup-example)
>  for a simplified example with a more detailed explanation.

The formulas explained above split income into brackets and apply the correct tax rates. However, we still need to adapt the worksheet to make the tax rates reflect user choices. This is an advanced lookup scenario, and it requires careful design. The goal is to dynamically retrieve the correct tax rate data based on the selected year and filing status. The screen below shows how this information is organized on Sheet3 of the workbook, and the orange numbers represent the numeric index values we can use:

![Master tax rate table for 2025](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/master_tax_rate_table_2025.png "Master tax rate table for 2025")

The tax rates for all years are stored in the range B5:K25. This table contains ten columns in total. The first column contains the tax rate brackets. The next eight columns contain the thresholds for each filing status. Notice each filing status has a pair of columns, one for "From" values and one for "To" values. The last column is Year, which contains the year the brackets were active. There are seven brackets, so seven rows for each year. For convenience, _tax\_table_ (B5:K25), _status\_list_ (M5:M9), and _year\_list_ (O5:O7) are [named ranges](https://exceljet.net/articles/named-ranges)
 used by the formulas that fetch rates.

Back on Sheet1, cell C4 contains a dropdown list that presents values from the _status\_list_. Cell F4 is a similar dropdown list that lets the user select the year from _year\_list_. Both dropdowns are created with [Data Validation](https://exceljet.net/articles/excel-data-validation-guide)
. The values selected in C4 and F4 drive the formulas that retrieve the correct tax rates for the selected year and filing status. On Sheet1, the formula in B7 retrieves all required data in one step like this:

    =CHOOSECOLS(
    FILTER(tax_table,CHOOSECOLS(tax_table,-1)=F4),
    XMATCH(C4,status_list)*2,
    XMATCH(C4,status_list)*2+1,1)
    

![Modern all-in-one formula to retrieve tax rate information](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/modern_formula_to_retrieve_tax_rate_data.png "Modern all-in-one formula to retrieve tax rate information")

At a high level, we are using the [CHOOSECOLS function](https://exceljet.net/functions/choosecols-function)
 to get the columns we need based on the filing status. However, before we get the columns, we use the [FILTER function](https://exceljet.net/functions/filter-function)
 to get tax rates for the selected year like this:

    FILTER(tax_table,CHOOSECOLS(tax_table,-1)=F4) // get rates for year
    

FILTER is configured to return tax rate data for a given year like this:

*   _array_ - the named range _tax\_table_ (B5:K18 on sheet3)
*   _include_ - CHOOSECOLS(tax\_table,-1)=F4

The tricky part is using CHOOSECOLS with a -1 to get the _last column_ of the tax table, which is compared to cell F4. The result from FILTER is the subset of the tax rates that correspond to the year in F4. This is delivered directly to the outer CHOOSECOLS function as the _array_ argument. We now have all tax rate data for a given year, but we still have three tricky steps remaining:

1.  Calculate a numeric index for the "From" and "To" columns for the selected filing status.
2.  Extract the two columns related to filing status plus the tax rates themselves.
3.  Reorder the extracted columns to match the order on Sheet1 (rates appear last).

For step 1, we can use the selected status value as a numeric index, but we must make adjustments to account for the fact that each status has two columns. To get an index for the "From" column, we use the [XMATCH function](https://exceljet.net/functions/xmatch-function)
 like this:

    XMATCH(C4,status_list)*2
    

We multiply the result by 2, since each tax status has two columns, starting with column 2. To get an index for the "To" column, we use XMATCH again in the same way:

    XMATCH(C4,status_list)*2+1
    

This time, we multiply the result from XMATCH by 2, and then we add 1 to account for the fact that the To" column is the "next" column in each category. To recap, the XMATCH formulas above give us the numeric index number for each of the two columns we need for filing status. When the status is "Single taxpayer", the first XMATCH returns 2 and the second returns 3. Then, to get the last column (tax rates), we simply hardcode the number 1 since this data is the first column of the tax table. Putting the 1 last also effectively reorders the columns as needed, knocking off Step 3 from above. The result inside CHOOSECOLS looks like this:

    =CHOOSECOLS(array,2,3,1)
    

When a user selects a different taxpayer status, XMATCH calculates new column indexes. For example, if we choose "Married filing jointly", the "From" column becomes 4, the "To" column becomes 5, and the tax rate remains unchanged as 1.

    =CHOOSECOLS(array,4,5,1)
    

### Traditional formula option

In older versions of Excel, we don't have functions like FILTER or CHOOSECOLS to use. One alternative is to use the [OFFSET function](https://exceljet.net/functions/offset-function)
 with the [MATCH function](https://exceljet.net/functions/match-function)
. In Sheet2, the formula in B7 retrieves the correct "From" and "To" columns in one step like this:

    =OFFSET(tax_table,7*(MATCH(F4,year_list,0)-1),MATCH(C4,status_list,0)*2-1,7,2)
    

_Note: This is a_ [_multi-cell array formula_](https://exceljet.net/glossary/multi-cell-array-formula)
 _entered in the range B5:C13 with control + shift + enter._

This formula extracts a 7-row by 2-column range from the _tax\_table_ based on the taxpayer status and year selected. The tricky part is calculating the right offsets for the selected year and status. The inputs to OFFSET look like this:

*   _reference_ - tax\_table (OFFSET will use the upper left cell)
*   _rows_ - 7\*(MATCH(F4,year\_list,0)-1)
*   _cols_ - MATCH(C4,status\_list,0)\*2-1
*   _height_ - 7 (hardcoded)
*   _width_ - 2 (hardcoded)

To calculate the rows offset, we use MATCH like this:

    7*(MATCH(F4,year_list,0)-1
    

If F4 = 2025, MATCH returns 1 (since 2025 is in the first row). If F4 = 2024, MATCH returns 2 (since 2024 is in the second row). Therefore:

*   For 2025 (MATCH result = 1) → 7 \* (1-1) = 0 → Stays in rows 5-11.
*   For 2024 (MATCH result = 2) → 7 \* (2-1) = 7 → Moves down 7 rows to rows 12-18.

To calculate the column offset, we use MATCH like this:

    MATCH(C4,status_list,0)*2-1
    

Here, we multiply the MATCH result by 2, then subtract 1 because we need to skip the first column and account for the fact that each status has two columns. The calculation works like this:

*   Single taxpayer (MATCH result = 1) → 1\*2 - 1 = 1 → Starts at column C.
*   Married filing jointly (MATCH result = 2) → 2\*2 - 1 = 3 → Starts at column E.
*   Married filing separately (MATCH result = 3) → 3\*2 - 1 = 5 → Starts at column G.
*   Head of household (MATCH result = 4) → 4\*2 - 1 = 9 → Starts at column I.

The formula in D7 works similarly and uses OFFSET to retrieve the tax rates like this:

    =OFFSET(tax_table,7*(MATCH(F4,year_list,0)-1),0,7,1)
    

This formula extracts a 7-row by 1-column range from the _tax\_table_ based on the year selected. We handle the rows offset in the same way as above. Then, we provide 0 for the column offset in order to get column 1. Together, the two formulas above retrieve the correct tax rates for the selected status in C4 and the selected year in F4.

### How to update the worksheet with new tax rates

Each year, the IRS publishes updated tax brackets and thresholds. To update the worksheet with new rates, follow these steps:

1.  **Go to Sheet3**, which contains the master tax rate table in the range B5:K25.
2.  **Add seven new rows** below the existing data, one for each tax bracket. Each row needs the following columns:  
    \- Column B: The tax rate (e.g., 10%, 12%, 22%, 24%, 32%, 35%, 37%). These are unlikely to change but should be confirmed.  
    \- Columns C-D: "From" and "To" thresholds for Single taxpayer.  
    \- Columns E-F: "From" and "To" thresholds for Married filing jointly.  
    \- Columns G-H: "From" and "To" thresholds for Married filing separately.  
    \- Columns I-J: "From" and "To" thresholds for Head of household.  
    \- Column K: The new tax year (e.g., 2026).
3.  **Update the named ranges.** After adding the new rows, you need to expand the _tax\_table_ named range to include the new rows. Go to Formulas > Name Manager, select _tax\_table_, and update the range to include the new rows (e.g., change B5:K25 to B5:K32). Also add the new year to the _year\_list_ named range.
4.  **Update the year dropdown.** The dropdown in cell F4 on Sheet1 and Sheet2 is driven by the _year\_list_ named range. Once you update _year\_list_ to include the new year, it will automatically appear in the dropdown.
5.  **Verify your results.** Select the new year from the dropdown in F4, enter a sample income, and confirm that the brackets, thresholds, and calculated taxes match the IRS-published values. You can cross-check against the IRS [tax brackets page](https://www.irs.gov/filing/federal-income-tax-rates-and-brackets)
     or a trusted tax calculator.

Because the formulas on Sheet1 and Sheet2 dynamically look up rates based on the year and filing status, no formula changes are needed -- only the data on Sheet3 and the named ranges need to be updated.

Related formulas
----------------

[![Excel formula: Step-based lookup example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/step-based_lookup_example.png "Excel formula: Step-based lookup example")](https://exceljet.net/formulas/step-based-lookup-example)

### [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)

This worksheet demonstrates a clever way to look up prices that change based on a selected tier. Imagine a pricing system where the cost of a product depends on both the product color and a tier (e.g., "Bronze," "Silver," or "Gold"). The challenge is to pull the correct price based on both inputs...

[![Excel formula: VLOOKUP calculate shipping cost](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_shipping_cost.png "Excel formula: VLOOKUP calculate shipping cost")](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

### [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

This example shows how to use the VLOOKUP function to calculate the total shipping cost for an item in one formula, where the cost per kilogram (kg) varies according to weight. This requires an "approximate match" since in most cases the actual weight will not appear in the shipping cost table. For...

[![Excel formula: Tax rate calculation with fixed base](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tax_rate_calculation_with_fixed_base.png "Excel formula: Tax rate calculation with fixed base")](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

### [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

The goal is to calculate a tax amount with both fixed and variable components according to the following logic: If the amount is less than $1000, only the base tax applies. If the amount is $1000 or greater, the result is the base tax + 15% \* the amount over $1000 This problem can be easily solved...

[![Excel formula: VLOOKUP tax rate calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_tax_rate_calculation.png "Excel formula: VLOOKUP tax rate calculation")](https://exceljet.net/formulas/vlookup-tax-rate-calculation)

### [VLOOKUP tax rate calculation](https://exceljet.net/formulas/vlookup-tax-rate-calculation)

In this example, the goal is to look up a given income value in a tax table and return the correct tax rate for that income. The tax rate is organized into 5 tiers in the range F5:F9 with the corresponding tax rate in the range G5:G9. For convenience, the range F5:G9 is named tax\_data . The...

[![Excel formula: Tiered discounts based on quantity](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tiered_discounts_based_on_quantity.png "Excel formula: Tiered discounts based on quantity")](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

### [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)

This example shows a workbook designed to apply discounts based on seven pricing tiers. The total quantity of items is entered as a variable in cell C4. The discount is applied via the unit costs in E7:E13, which decrease as the quantity increases. The first 200 items have an undiscounted price of...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel OFFSET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_offset.png "Excel OFFSET function")](https://exceljet.net/functions/offset-function)

### [OFFSET Function](https://exceljet.net/functions/offset-function)

The Excel OFFSET function returns a reference to a range constructed with five inputs: (1) a starting point, (2) a row offset, (3) a column offset, (4) a height in rows, (5) a width in columns. OFFSET is handy in formulas that require a dynamic range.

[![Excel CHOOSECOLS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20choosecols%20function.png "Excel CHOOSECOLS function")](https://exceljet.net/functions/choosecols-function)

### [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)

The Excel CHOOSECOLS function returns specific columns from an array or range. The columns to return are provided as numbers in separate arguments. Each number corresponds to the numeric index of a column in the given array.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20are%20dynamic%20array%20formulas-Play.png)](https://exceljet.net/videos/what-are-dynamic-array-formulas)

### [What are Dynamic Array formulas?](https://exceljet.net/videos/what-are-dynamic-array-formulas)

In this video, I'll explain the basic idea of dynamic array formulas. Dynamic Array formulas are the biggest change to the Excel formula engine in years. Maybe the biggest change ever. This is because Dynamic Arrays make it easy to work with many values at the same time. For many users, this will...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Dynamic%20arrays%20are%20native-PLay.png)](https://exceljet.net/videos/dynamic-arrays-are-native)

### [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)

In this video we'll look at how dynamic array behavior is native and deeply integrated in Excel. Although new dynamic array functions will get a lot of attention, it's important to understand that dynamic array behavior is native and deeply integrated. All formulas will now run on a new calculation...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Step-based lookup example](https://exceljet.net/formulas/step-based-lookup-example)
    
*   [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    
*   [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)
    
*   [VLOOKUP tax rate calculation](https://exceljet.net/formulas/vlookup-tax-rate-calculation)
    
*   [Tiered discounts based on quantity](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [OFFSET Function](https://exceljet.net/functions/offset-function)
    
*   [CHOOSECOLS Function](https://exceljet.net/functions/choosecols-function)
    

### Videos

*   [What are Dynamic Array formulas?](https://exceljet.net/videos/what-are-dynamic-array-formulas)
    
*   [Dynamic arrays are native](https://exceljet.net/videos/dynamic-arrays-are-native)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)