# Randomly assign people to groups - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/randomly-assign-people-to-groups

---

[Skip to main content](https://exceljet.net/formulas/randomly-assign-people-to-groups#main-content)

[](https://exceljet.net/formulas/randomly-assign-people-to-groups#)

*   [Previous](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    
*   [Next](https://exceljet.net/formulas/add-row-numbers-and-skip-blanks)
    

[Random](https://exceljet.net/formulas#Random)

Randomly assign people to groups
================================

by Dave Bruns · Updated 11 Apr 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[RAND](https://exceljet.net/functions/rand-function)

[RANK](https://exceljet.net/functions/rank-function)

[ROUNDUP](https://exceljet.net/functions/roundup-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[RANDARRAY](https://exceljet.net/functions/randarray-function)

[SORTBY](https://exceljet.net/functions/sortby-function)

[LET](https://exceljet.net/functions/let-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8264/download?token=tOW3ZlyF)
 (19.53 KB)

![Excel formula: Randomly assign people to groups](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/randomly_assign_people_to_groups.png "Excel formula: Randomly assign people to groups")

Summary
-------

To randomly assign people to groups or teams of equal size, you can use a formula based on the [RANK](https://exceljet.net/functions/rank-function)
 and [ROUNDUP](https://exceljet.net/functions/roundup-function)
 functions. In the example shown, the formula in D5 is:

    =INDEX(groups,ROUNDUP(RANK(C5,randoms)/(ROWS(randoms)/COUNTA(groups)),0))
    

where **groups** (F5:F7) and **randoms** (C5:C22) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, it returns a random group of "A", "B", or "C" on each row. In addition, the formula is configured to create groups of equal size.

_Note: this problem can also be solved with a single Dynamic Array formula and no helper column. See below for details._

Generic formula
---------------

    =INDEX(groups,ROUNDUP(RANK(C5,randoms)/(ROWS(randoms)/COUNTA(groups)),0))

Explanation 
------------

In this example, the goal is to randomly assign the names in column B to three groups of equal size. The group names are "A", "B", and "C", and these values appear in the named range **groups** (F5:F7). The solution should automatically count the number of groups to assign and attempt to generate the same count for each group. The worksheet shown contains 18 names, the final result should be that each group includes 6 random names from the list. The article below explains two approaches: (1) a traditional formula that depends on random values in a helper column, which will work in any version of Excel, and (2) a [Dynamic Array](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 formula that will return all random groups in one step without a helper column.

> The solutions explained here are more complex because we are taking care to place the same number of people in each group when possible. To simply assign random groups without regard to size, [see this page](https://exceljet.net/formulas/randomly-assign-data-to-groups)
> .

Basic approach
--------------

For both formulas explained below, the basic approach is the same and looks like this:

1.  Generate random numbers for each row
2.  Rank the random numbers
3.  Count groups and calculate the ideal group size
4.  Divide each rank by the group size
5.  Round the results up to the nearest whole number
6.  Use the whole number to fetch a group name with INDEX

The difference below is in the implementation. In older versions of Excel, we need to add a helper column that contains random numbers to the data, then use a formula that ranks each row according to the helper column. In the current version of Excel, we can use a single formula that generates all random numbers at once, and there is no need for a helper column.

Traditional formula
-------------------

The traditional way to solve this problem in an older version of Excel is to use a helper column populated with random numbers with the [RAND function](https://exceljet.net/functions/rand-function)
, as seen in the worksheet above. In the worksheet shown, the random numbers appear in the range C5:C22 which is named "randoms" for convenience. To generate a full set of random values in one step, select the range C5:C22 and type =RAND() in the formula bar. Then use the [shortcut](https://exceljet.net/shortcuts)
 control + enter to enter the formula in all cells at once.

_Note: the RAND function will keep generating random values every time a change is made to the worksheet, so typically you will want to replace the results in column C with actual values using [paste special](https://exceljet.net/videos/shortcuts-for-paste-special)
 to prevent changes after random values are assigned._

### Assigning groups with INDEX

The formula used to assign random groups looks like this:

    =INDEX(groups,ROUNDUP(RANK(C5,randoms)/(ROWS(randoms)/COUNTA(groups)),0))
    

At a high level, this formula uses the [INDEX function](https://exceljet.net/functions/index-function)
 to assign a group of "A", "B", or "C" to each name in the list. The generic pattern looks like this, where n is a number that corresponds to a group:

    =INDEX(groups,n)
    

Because there are three groups total, the value for n needs to be between 1 and 3:

    =INDEX(groups,1) // returns "A"
    =INDEX(groups,2) // returns "B"
    =INDEX(groups,3) // returns "C"

The hard part of the formula is generating a random number (n) for each row that will result in three groups of equal size. This is done in the snippet below, which makes up the bulk of the formula:

    ROUNDUP(RANK(C5,randoms)/(ROWS(randoms)/COUNTA(groups)),0)
    

Working from the inside out, the first step is to assign a numeric rank to each random number with the [RANK function](https://exceljet.net/functions/rank-function)
:

    RANK(C5,randoms)
    

RANK compares the number in cell C5 to all values in C5:C22 and returns its position relative to the other numbers in the range. The smallest number gets rank 1, the next smallest rank 2, and so on. Because there are 18 numbers in the list, RANK will generate a rank of 1-18. The next part of the formula calculates the optimal size for each group by dividing the total number of rows in the data by the number of groups to assign:

    ROWS(randoms)/COUNTA(groups)

The [ROWS function](https://exceljet.net/functions/rows-function)
 returns a count of rows (18), and the [COUNTA function](https://exceljet.net/functions/counta-function)
 returns a count of groups (3). Simplifying, we have:

    =ROWS(randoms)/COUNTA(groups)
    =18/3
    =6

The result is 6, which is the number of names that should be in each of the three groups. Next, the rank of each random number is divided by the number of names per group (6):

    rank/6
    

For example, when a row is ranked 1st, the formula would return a value of 1/6, or 0.1667, when a row has a rank of 6, the formula returns 1/1, or 1, and so on. This is the mechanism by which the formula generates groups of equal size. The final step is to use the  [ROUNDUP function](https://exceljet.net/functions/roundup-function)
 to _round each number up to the next whole number,_ effectively dividing the ranked individuals into three equally sized groups based on their rank. The result from ROUNDUP is a random number between 1-3 (n) which is then used by INDEX to assign a group.

Dynamic Array formula
---------------------

In Excel 2021 or later, dynamic array formulas allow a more sophisticated solution with an all-in-one formula that requires no helper columns. In the screen below, the formula in cell C5 is:

    =LET(
    ct,ROWS(B5:B22),
    groups,E5:E7,
    size,ct/COUNTA(groups),
    randoms,SORTBY(SEQUENCE(ct),RANDARRAY(ct)),
    INDEX(groups,ROUNDUP(randoms/size,0)))

![An all-in-one dynamic array formula to assign people to equal-sized groups](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/randomly_assign_people_to_groups_dynamic_array_formula.png "An all-in-one dynamic array formula to assign people to equal-sized groups")

This formula uses the LET function to create named variables within the formula, which reduces complexity and improves readability. In the first part of the formula, four variables are defined as follows:

*   **ct**: The count of names, determined by **ROWS(B5:B22)**.
*   **groups**: The groups to be assigned in the range **E5:E7**.
*   **size**: The size of each group, determined with **ct/COUNTA(groups)**
*   **randoms**: A sorted list of random numbers created with **SORTBY(SEQUENCE(ct), RANDARRAY(ct))**.

The definition of **randoms** is the most interesting bit:

    SORTBY(SEQUENCE(ct),RANDARRAY(ct))

Since **ct** has been previously defined as 18, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 creates an array of sequential numbers between 1 and 18. The [RANDARRAY function](https://exceljet.net/functions/randarray-function)
 creates an array of random numbers of the same size. Next, the [SORTBY function](https://exceljet.net/functions/sortby-function)
 sorts the sequence in the order of the random numbers, effectively shuffling the sequence. The result is the numbers 1 to 18 in a random order.

With the variables above in place, the last line in the formula generates the random groups like this:

    INDEX(groups,ROUNDUP(randoms/size,0))

Like the original formula above, the basic pattern of this formula is:

    =INDEX(groups,n)
    

where **n** is a random number between 1 and 3, corresponding to the three groups. The 18 individual values for **n** are calculated in one step like this:

    ROUNDUP(randoms/size,0)

First, the numbers in **randoms** are divided by **size** to get a decimal number corresponding to a group. Then they handed off to the ROUNDUP function which rounds the numbers up to the nearest whole number. The result from ROUNDUP is an array that contains 18 numbers between 1 and 3. This array is returned directly to INDEX as the _row\_num_ argument, and INDEX returns the corresponding 18 groups in one step. The final result is that each group contains 6 random names from the list.

### Conclusion

Although both formulas explained above work well, the dynamic array formula keeps all operations in a single cell. There is no need for a helper column. In addition, the LET function allows us to define variables that can be reused in the formula without recalculation, which makes the formula easier to read and more efficient. The result is a dynamic and efficient way to assign individuals to random groups of equal size with a single formula.

Related formulas
----------------

[![Excel formula: Randomly assign data to groups](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/randomly_assign_data_to_groups.png "Excel formula: Randomly assign data to groups")](https://exceljet.net/formulas/randomly-assign-data-to-groups)

### [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)

In this example, the goal is to return a random group ("A", "B", or "C") at each new row. The simplest way to do this is to use the RANDBETWEEN function with the CHOOSE function. In the current version of Excel, it is also possible to generate all random groups in one step with the RANDARRAY...

[![Excel formula: Random text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20text%20values.png "Excel formula: Random text values")](https://exceljet.net/formulas/random-text-values)

### [Random text values](https://exceljet.net/formulas/random-text-values)

The CHOOSE function provides the framework for this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are using four values:...

[![Excel formula: Random number from fixed set of options](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20number%20from%20fixed%20set%20of%20options.png "Excel formula: Random number from fixed set of options")](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

### [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)

The CHOOSE function does most of the work in this formula. Choose takes a single numeric value as its first argument (index\_number), and uses this number to select and return one of the values provides as subsequent arguments, based on their numeric index. In this case, we are providing four...

[![Excel formula: Random numbers without duplicates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random%20numbers%20without%20duplicates.png "Excel formula: Random numbers without duplicates")](https://exceljet.net/formulas/random-numbers-without-duplicates)

### [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)

In this example, the goal is to generate a list of random numbers without duplicates. This involves jumping through a few hoops because although the RANDARRAY function can easily generate a list of random integers, there is no guarantee that the numbers will be unique. In the explanation below, we'...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel RAND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rand%20function.png "Excel RAND function")](https://exceljet.net/functions/rand-function)

### [RAND Function](https://exceljet.net/functions/rand-function)

The Excel RAND function returns a random number between 0 and 1. For example, =RAND() will generate a number like 0.422245717. RAND recalculates when a worksheet is opened or changed.

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel ROUNDUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20roundup%20function.png "Excel ROUNDUP function")](https://exceljet.net/functions/roundup-function)

### [ROUNDUP Function](https://exceljet.net/functions/roundup-function)

The Excel ROUNDUP function returns a number rounded up to a given number of decimal places. Unlike standard rounding, where only numbers less than 5 are rounded down, ROUNDUP rounds _all numbers up_....

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel RANDARRAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_randarray_function.png "Excel RANDARRAY function")](https://exceljet.net/functions/randarray-function)

### [RANDARRAY Function](https://exceljet.net/functions/randarray-function)

The Excel RANDARRAY function generates an array of random numbers between two values. The size or the array is specified by _rows_ and _columns_ arguments. The generated values can be either decimals or whole numbers.

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20randomly%20assign%20people%20to%20teams-Play.png)](https://exceljet.net/videos/how-to-randomly-assign-people-to-teams)

### [How to randomly assign people to teams](https://exceljet.net/videos/how-to-randomly-assign-people-to-teams)

In this video, we'll look at a way to use basic formulas to randomly assign people to teams. Here we have a list of 36 people. Let's say we want to randomly assign each person to a team of 4 people so that we have a total of 9 teams with 4 people in each. I'm going to solve this problem in small...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Randomly assign data to groups](https://exceljet.net/formulas/randomly-assign-data-to-groups)
    
*   [Random text values](https://exceljet.net/formulas/random-text-values)
    
*   [Random number from fixed set of options](https://exceljet.net/formulas/random-number-from-fixed-set-of-options)
    
*   [Random numbers without duplicates](https://exceljet.net/formulas/random-numbers-without-duplicates)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [RAND Function](https://exceljet.net/functions/rand-function)
    
*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [ROUNDUP Function](https://exceljet.net/functions/roundup-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [RANDARRAY Function](https://exceljet.net/functions/randarray-function)
    
*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

### Videos

*   [How to randomly assign people to teams](https://exceljet.net/videos/how-to-randomly-assign-people-to-teams)
    

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