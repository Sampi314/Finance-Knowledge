# Monday Morning Mulling: December 2023 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-december-2023-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: December 2023 Challenge

*   December 31, 2023

Monday Morning Mulling: December 2023 Challenge
===============================================

Monday Morning Mulling: December 2023 Challenge
===============================================

1 January 2024

_Happy New Year! On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the following Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you, but we do appreciate your enthusiasm!_

**_The Challenge_**

Last Friday, we presented a word puzzle challenge: imagine that you’re presented with an intriguing linguistic challenge: to craft a list of words from a specified set of letters. Manually filtering every single keyword and copying / pasting them to a new location can be a tedious and time-consuming process. We provided you with two Excel Tables: **List\_of\_Letters** and **List\_of\_Words**.

Your objective was to develop one \[1\] dynamic Excel formula which would look up words from **List\_of\_Words** that may be formed from letters of a single word in **List\_of\_Letters**, as shown in the picture below:

![](<Base64-Image-Removed>)

For example, if the word ‘Epiphany’ were included in the **List\_of\_Letters** and the word ‘Happy’ appeared in the **List\_of\_Words**, the formula would check if all letters of the word ‘Happy’ were present in at least one word from the **List\_of\_Letters**. Since the letters ‘H’, ‘A’, ‘P’, and ‘Y’ are all found in the word ‘Epiphany’, the word ‘Happy’ will be included in the filtered list. You may download the question file **[here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2023/Dec/sp-word-lists-challenge---challenge.xlsx)
**.

As always, there were some requirements:

*   no Power Query / Get & Transform or VBA was allowed
*   the formula(e) should be dynamic so that they should update when a new entry was added
*   the solution should be case-insensitive, _e.g._ ‘E’ and ‘e’ should be treated similarly.

**_Suggested Solution_**

You can find our Excel file **[here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2023/Dec/sp-word-lists-challenge---suggested-solution.xlsx)
**, which shows our suggested solution. The steps are detailed below.

**_The Formula_**

Here’s one way to approach this problem using Excel’s dynamic array functions and text functions.The solution provided is based upon the idea of checking whether all characters in each word from the **List\_of\_Words** exists in any one of the words from the **List\_of\_Letters**.

**\=FILTER(List\_of\_Words\[Words\],  
BYROW(List\_of\_Words\[Words\],  
LAMBDA(input,OR(BYROW(List\_of\_Letters\[Letters\],  
LAMBDA(r, AND(ISNUMBER(SEARCH(MID(input,SEQUENCE(LEN(input)),1),r)))))))))**

Don’t worry if you do not understand the formula above. Let’s go through it step-by-step:

**_Creating a Sequence of Numbers_**

To begin, we need to extract all characters from each word in **List\_of\_Words**. This may be constructed using a combination of the [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 and [**SEQUENCE**](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 functions:

**\=SEQUENCE(LEN(input))**

The formula generates a sequence of numbers from one \[1\] to the length of the input word, serving as the start number for the [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 function to extract each character. For instance, if the input word is ‘Happy’, this step would generate the sequence \[1, 2, 3, 4, 5\], if the input word is ‘Bright’ it generates the sequence \[1, 2, 3, 4, 5, 6\].

In the formula above, ‘input’ refers to the current word being processed from the **List\_of\_Words**. As the formula iterates through the **List\_of\_Words**, it assigns each word to the variable ‘input’ and uses it to evaluate the subsequent expressions.

![](<Base64-Image-Removed>)

Note that we will break down a complex formula into manageable steps. This is why in the highlighted cells in red we will refer to specific cells. This approach facilitates a clearer understanding of the calculation complexity.

**_Extracting Letters_**

The [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 function then extracts a single character from the current word at each position in the generated sequence. The one \[1\] at the end indicates that only a single character should be extracted.

**\=MID(input,SEQUENCE(LEN(input)),1)**

![](<Base64-Image-Removed>)

**_Searching for the Extracted Letter_**

The [**SEARCH**](https://sumproduct.com/thought/introducing-the-search-function/)
 function will return a position number if the keywords are found within the text string. Otherwise, it will return _#VALUE!_ error. Then, the [**ISNUMBER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-isnumber-function)
 function checks whether the output of the [**SEARCH**](https://sumproduct.com/thought/introducing-the-search-function/)
 function is a number or not and will return TRUE or FALSE accordingly.

**\=ISNUMBER(SEARCH(MID(input,SEQUENCE(LEN(input)),1),r))**

Here, ‘r’ represents the current word being compared from the **List\_of\_Letters**. The [**SEARCH**](https://sumproduct.com/thought/introducing-the-search-function/)
 function checks if the extracted character from the input word is present in the current word from the **List\_of\_Letters**.

Using the input word ‘Happy’, the function above compares with the word ‘Epiphany’ from the **List\_of\_Letters**, and you can see the result below:

![](<Base64-Image-Removed>)

**_Validating Letter Extraction Against List\_of\_Words_**

**\=AND(ISNUMBER(SEARCH(MID(input,SEQUENCE(LEN(input)),1),r))))**

Here, the [**AND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-and-function)
 function ensures all extracted characters from the current word are found in at least one word from the **List\_of\_Letters**. If all characters are found, the result will be TRUE. Otherwise, it will be FALSE. This is a “safe” use of **AND**, as this does not always play nicely with **multiple** vectors or arrays.

![](<Base64-Image-Removed>)

By utilising the input word ‘Bright’, the function mentioned above is employed to compare it with the word ‘Epiphany’ from the **List\_of\_Letters**. Since not all the letters are present, the returned result is FALSE.

![](<Base64-Image-Removed>)

**_Filtering Condition for Results_**

This part of the formula applies a function to each row (word) in the **List\_of\_Words**. The function is defined as follows:

**\=BYROW(List\_of\_Words\[Words\], LAMBDA(input, OR(BYROW(List\_of\_Letters\[Letters\],  
LAMBDA(r, AND(ISNUMBER(SEARCH(MID(input,SEQUENCE(LEN(input)),1),r))))))))**

Let’s break down the function further. This inner [**BYROW**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-byrow-function)
 function checks if the current character of ‘input’ in the **List\_of\_Words** is present in the current word ‘**r**‘ in the **List\_of\_Letters** as mentioned above. It uses a nested [**BYROW**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-byrow-function)
 to iterate through each word ‘r’ in **List\_of\_Letters**.

In addition, the [**OR**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-or-function)
 function checks if any iteration of the inner [**BYROW**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-byrow-function)
 returned TRUE (meaning all characters were found in any word from **List\_of\_Letters**).

This formula essentially acts as a filter condition that returns TRUE or FALSE for [**FILTER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-filter-function)
 function**.**

![](<Base64-Image-Removed>)

**_The Final Formula_**

Finally, after explaining how the functions nested in the formula work. The final formula is as follows:

**\=FILTER(List\_of\_Words\[Words\],  
BYROW(List\_of\_Words\[Words\],LAMBDA(input,OR(BYROW(List\_of\_Letters\[Letters\],LAMBDA(r,  
AND(ISNUMBER(SEARCH(MID(input,SEQUENCE(LEN(input)),1),r)))))))))**

The [**FILTER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-filter-function)
 function in the formula plays a crucial role in filtering the list of words based on a specific condition. The first argument passed to [**FILTER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-filter-function)
 is **List\_of\_Words**, which represents the original list of words you want to filter. The second argument is an expression that utilises nested [**BYROW**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-byrow-function)
 and [**LAMBDA**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-lambda-function)
 functions to check if each word in the original list meets the filtering criteria and determines which words to keep. This results in a new list containing only words satisfying the condition above, and in our example, the output has a seasonal message from SumProduct for you:

  “**Happy New Year**”

![](<Base64-Image-Removed>)

**_Word to the Wise_**

We appreciate there are many, many ways this could have been achieved. If you have come up with an alternative, radically different approach, congratulations – that’s half the fun of Excel!

_The Final Friday Fix will return on Friday 26 January 2024 with a new Excel challenge. In the meantime, keep honing your Excel skills with our Daily Excel Tip on our home page, and look out for more informative blogs every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-december-2023-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-december-2023-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-december-2023-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-december-2023-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-december-2023-challenge/#0 "close")

top