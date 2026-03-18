# Remove characters from right - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/remove-characters-from-right

---

[Skip to main content](https://exceljet.net/formulas/remove-characters-from-right#main-content)

[](https://exceljet.net/formulas/remove-characters-from-right#)

*   [Previous](https://exceljet.net/formulas/pad-text-to-equal-length)
    
*   [Next](https://exceljet.net/formulas/remove-file-extension-from-filename)
    

[Text](https://exceljet.net/formulas#Text)

Remove characters from right
============================

by Dave Bruns · Updated 16 May 2025

Related functions 
------------------

[LEFT](https://exceljet.net/functions/left-function)

[LEN](https://exceljet.net/functions/len-function)

[REGEXREPLACE](https://exceljet.net/functions/regexreplace-function)

[REPLACE](https://exceljet.net/functions/replace-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/9123/download?token=GD7lC9NT)
 (27.03 KB)

![Excel formula: Remove characters from right](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/remove_characters_from_right.png "Excel formula: Remove characters from right")

Summary
-------

To remove the last character(s) from a text string, you can use a formula based on the [LEFT](https://exceljet.net/functions/left-function)
 and [LEN](https://exceljet.net/functions/len-function)
 functions. In the worksheet shown above, each city and country in column B ends with an asterisk (\*) that we would like to remove. We do it with a formula like this in cell D5:

    =LEFT(B5,LEN(B5)-1)
    

As the formula is copied down, it uses the LEFT function to remove the last character in each text string. The values in column D show the result.

> This formula will work in all versions of Excel. The article below also explains a fancy new way to do the same thing with the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
> , which requires the latest version of Excel.

Generic formula
---------------

    =LEFT(text,LEN(text)-n)

Explanation 
------------

In this example, the goal is to remove the asterisk (\*) at the end of each text city/country name in column B. As usual, there are many ways to solve a problem like this in Excel. In the article below, we'll look at two good options. The first is a traditional formula based on the LEFT function and the LEN function. This formula will work in any version of Excel. The second option is a formula based on the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
, which was [recently introduced to Excel](https://exceljet.net/articles/regular-expressions-in-excel)
. The REGEXREPLACE approach is more powerful and flexible, but it is only available in the latest version of Excel.

> If you only want to remove trailing spaces from a text string, the [TRIM function](https://exceljet.net/functions/trim-function)
>  is faster and easier. In one step, it can remove leading and trailing spaces and normalize the space between words.

### Table of Contents

*   [Remove the last character](https://exceljet.net/formulas/remove-characters-from-right#remove_last_character)
    
*   [Remove the last 3 characters](https://exceljet.net/formulas/remove-characters-from-right#remove_last_3_characters)
    
*   [REPLACE function alternative](https://exceljet.net/formulas/remove-characters-from-right#replace_function_alternative)
    
*   [Remove the last character with REGEXREPLACE](https://exceljet.net/formulas/remove-characters-from-right#remove_last_character_regexreplace)
    
*   [Remove the last 3 characters with REGEXREPLACE](https://exceljet.net/formulas/remove-characters-from-right#remove_last_3_characters_regexreplace)
    
*   [Making the formulas conditional](https://exceljet.net/formulas/remove-characters-from-right#conditional_formulas)
    

> Note, the formulas on this page are configured to remove asterisks (\*) because they are easy to see and understand. However, these formulas can be adapted to remove specific characters or a specific number of characters, as explained below. I realize you could use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
>  to remove specific text _anywhere_ in a text string. 🙂

### Remove the last character

The traditional way to solve this problem in Excel is to combine the LEFT and LEN functions. The [LEFT function](https://exceljet.net/functions/left-function)
 returns characters starting at the left side of a text string:

    =LEFT("apple",3) // returns "app"

The [LEN function](https://exceljet.net/functions/len-function)
 returns the length of a text string:

    =LEN("apple") // returns 5

To solve this problem, we want to get all of the characters starting at the left and ending at the character before the asterisk (\*) at the end. To do this, we can nest the LEN function inside the LEFT function to return the length of the string and then subtract one to remove the last character, like this:

    =LEFT(B5,LEN(B5)-1)

![Removing the last character with LEFT and LEN](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/remove_last_character_with_LEFT_and_LEN.png "Removing the last character with LEFT and LEN")

This is how the formula works:

    =LEFT(B5,LEN(B5)-1)
    =LEFT(B5,14-1)
    =LEFT(B5,13)
    ="Paris, France"
    

*   The LEN function returns 14 because "Paris, France\*" contains 14 characters.
*   We subtract 1, and the result (13) is passed to LEFT as _num\_chars_.
*   The LEFT function returns the first 13 characters of the text, skipping the last character.
*   The final result is "Paris, France", without the asterisk.
*   As the formula is copied down, the process repeats for each city in the list.

### Remove the last 3 characters

What if you want to remove more than one character from the end of a text string? The general form of the formula looks like this, where n represents the number of characters to remove:

    =LEFT(A1,LEN(A1)-n)

This means we just need to change n to the number of characters we'd like to remove. For example, in the worksheet below, we have the same city and country names, but now each one is followed by three asterisks. The formula in cell D5 now looks like this:

    =LEFT(B5,LEN(B5)-3)

![Removing the last 3 characters with LEFT and LEN](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/remove_last_3_characters_with_LEFT_and_LEN.png "Removing the last 3 characters with LEFT and LEN")

The formula works the same way as the example above, but now, because we are subtracting 3 from the length of the text string, the result is that we removed the last three characters from the right side. It's always a little confusing that we use the LEFT function to remove characters from the right side of the text string, but that's just the way this works 🙃.

### REPLACE function alternative

Although the formula based on the LEFT and LEN functions works fine, I should mention that you can write a similar formula based on the [REPLACE function](https://exceljet.net/functions/replace-function)
. The generic formula to remove the last n characters looks like this:

    =REPLACE(A1,LEN(A1)-n+1,n,"")

This formula will replace n characters in A1 with an empty string (""), starting at the position calculated with `LEN(A1)-n+1`. Both options are solid and will work in any version of Excel. 

### Remove the last character with REGEXREPLACE

The formula based on LEFT and LEN explained above is a traditional formula that will work in all versions of Excel. If you have the latest version of Excel, which includes [three new regex functions](https://exceljet.net/articles/regular-expressions-in-excel)
, you have a more powerful tool at your disposal. In the worksheet below, I have converted the formula to use the [REGEXREPLACE function](https://exceljet.net/functions/regexreplace-function)
 to remove the last character. The formula in D5 now looks like this:

    =REGEXREPLACE(B5,".$","")

![Removing the last character with REGEXREPLACE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/remove_last_character_with_REGEXREPLACE.png "Removing the last character with REGEXREPLACE")

Notice that we only have a single function call for this solution. The inputs to REGEXREPLACE are as follows:

*   _text_ - `B5`
*   _pattern_ - `".$"`
*   _replacement_ - `""`

At a high level, we are replacing the last character in B5 with an empty string (""). The trick is in how we match the last character, which is done with the pattern `".$"`. In regex, a single dot (.) will match any character. The dollar sign ($) is a special anchor character that matches the end of a text string. The result is a pattern that matches the last character at the end of the text string. See a related example [here](https://exceljet.net/formulas/remove-trailing-slash-from-url)
.

### Remove the last 3 characters with REGEXREPLACE

How do we use regex to target the last three characters? This is an example that shows off the flexibility of regex patterns. Regex has something called _quantifiers_ that you can use to specify how many instances of a character you want to match. In this case, we can use a form like `{n}` to specify `n` characters, so `{3}` to match 3 characters. You can see this in the worksheet below, where the formula in D5 now looks like this:

    =REGEXREPLACE(B5,".{3}$","")

![Removing the last 3 characters with REGEXREPLACE](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/remove_last_3_characters_with_REGEXREPLACE.png "Removing the last 3 characters with REGEXREPLACE")

As before, we are using REGEXREPLACE to replace text that matches a specific pattern with an empty string. The pattern in this case is `".{3}$"`, which breaks down as follows:

*   The `.` matches any single character.
*   The `{3}` means “exactly three”.
*   The `$` anchors the match to the end of the string.

### Making the formulas conditional

In this kind of problem, one challenge that comes up often is that you only want to remove certain characters at the end of a text string if they exist. Otherwise, you might chop off characters you want to keep. In other words, we want to make the formulas _conditional_. Let's look at how to do that with both the traditional LEFT + LEN formula and the newer formula based on regex replace. For the first formula, I think the simplest way to do this is to test the string directly with the IF function and the RIGHT function like this:

    =IF(RIGHT(B5,1)="*",LEFT(B5,LEN(B5)-1),B5)

Here we use the RIGHT function to extract the last character and check if it is an asterisk (\*). If so, we run the original formula that removes the last character. If not, we would return the original value unchanged. To make the regex replace formula conditional, we could use the IF function as above to check for the asterisk (\*) in the same way:

    =IF(RIGHT(B5,1)="*",REGEXREPLACE(B5,".$",""),B5)

However, a simpler option is to adjust the pattern to match a literal asterisk (\*) at the end of the text:

    =REGEXREPLACE(B5,"\*$","")

The pattern `"\*$"` works like this:

*   The `\*` matches a literal asterisk (\*)
*   The `$` anchors the match to the end of the string.

What's the backslash `\` doing in there? There are certain characters in regex (like `*`) that need to be _escaped_. This is because these characters have other meanings. For example, the asterisk (\*) by itself means "match zero or more times" when it appears as a quantifier in a pattern. The backslash is a way to specify these characters literally. So, `"\*$"` matches a literal asterisk that appears at the end of a text string. This means the match will fail if the `*` is not at the end of a text string, or if it appears anywhere else in the text. And, if the match fails, REGEXREPLACE returns the original value unchanged.

> Tip: Escape other regex metacharacters the same way, for example `\+$` for a trailing plus sign. 

In the worksheet below, notice that only some cities in column B are followed by an asterisk (\*). To avoid removing characters from cities that do not have an asterisk, we need conditional formulas. In cell D5, we use the traditional formula wrapped in IF to check for the asterisk before processing:

    =IF(RIGHT(B5,1)="*",LEFT(B5,LEN(B5)-1),B5)

In cell F5, we have the REGEXREPLACE alternative:

    =REGEXREPLACE(B5,"\*$","")

![Making these formulas conditional](https://exceljet.net/sites/default/files/images/formulas/inline/remove_characters_from_right_conditionally.png "Making these formulas conditional")

You can see that both formulas correctly remove the last character from cities that end in an asterisk. Cities that do not end in an asterisk are returned unchanged. 

> I should also mention that you could use the pattern `\*+$` to remove _any number_ of trailing asterisks. Regex has a huge number of special symbols that can be adapted in many ways for very specific matching. See our [quick reference table](https://exceljet.net/articles/regular-expressions-in-excel#regex-quick-reference)
>  for examples. 

I think this is a good example of how regex patterns are a much more powerful way to target specific text. In the traditional formula, the LEFT and LEN functions have no idea what they're doing. They're simply chopping off characters. Any control over which characters are being removed needs to be added to the formula in the form of other functions. By contrast, the REGEXREPLACE function can use regular expressions to target specific text precisely, with built-in tools to make the match conditional. The trade-off is that Excel's regex functions require at least some familiarity with regular expressions.

Related formulas
----------------

[![Excel formula: Remove trailing slash from url](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove_trailing_slash_from_URL.png "Excel formula: Remove trailing slash from url")](https://exceljet.net/formulas/remove-trailing-slash-from-url)

### [Remove trailing slash from url](https://exceljet.net/formulas/remove-trailing-slash-from-url)

The goal is to remove the forward-slash ("/") from the URLs in column B when it is present as the last character. When a URL does not end with a forward slash ("/") the original URL should be returned without modification. Despite the fact that Excel offers many functions designed to work with text...

[![Excel formula: Remove first character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20first%20character.png "Excel formula: Remove first character")](https://exceljet.net/formulas/remove-first-character)

### [Remove first character](https://exceljet.net/formulas/remove-first-character)

This formula uses the REPLACE function to replace the first character in a cell with an empty string (""). The arguments for REPLACE are configured as follows: old\_text is the original value from column B start\_num is hardcoded as the number 1 num\_chars comes from column C new\_text is entered as an...

[![Excel formula: Remove last word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20last%20word.png "Excel formula: Remove last word")](https://exceljet.net/formulas/remove-last-word)

### [Remove last word](https://exceljet.net/formulas/remove-last-word)

In this example, the goal is to remove the last word from the text strings in column B. This article explains two approaches: A modern formula based on the TEXTBEFORE function. A more traditional formula for older versions in Excel. The first option is much simpler, and you should use it if you...

[![Excel formula: Remove file extension from filename](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/remove%20file%20extension%20from%20filename.png "Excel formula: Remove file extension from filename")](https://exceljet.net/formulas/remove-file-extension-from-filename)

### [Remove file extension from filename](https://exceljet.net/formulas/remove-file-extension-from-filename)

The core of this formula is the LEFT function which simply extracts text from the file name, starting at the left, and ending at the character before the first period ("."). =LEFT(filename,characters) The FIND function is used to figure out how many characters to extract: FIND(".",B5)-1 Find...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

### [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text, and you won't be able to perform math operations on such values. To split a number from a unit value, you need to determine the position...

Related functions
-----------------

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel REGEXREPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_regexreplace_function.png "Excel REGEXREPLACE function")](https://exceljet.net/functions/regexreplace-function)

### [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)

The Excel REGEXREPLACE function replaces text matching a specific regex pattern in a given text string. Regex patterns are very flexible and can be configured to match numbers, email addresses, dates, and other values that have an identifiable structure. By default, REGEXREPLACE will...

[![Excel REPLACE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20replace%20function.png "Excel REPLACE function")](https://exceljet.net/functions/replace-function)

### [REPLACE Function](https://exceljet.net/functions/replace-function)

The Excel REPLACE function replaces characters at a specified position in a given text string with another text string. REPLACE a good solution when the text to replace can't easily be matched, but the location is predictable.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Remove trailing slash from url](https://exceljet.net/formulas/remove-trailing-slash-from-url)
    
*   [Remove first character](https://exceljet.net/formulas/remove-first-character)
    
*   [Remove last word](https://exceljet.net/formulas/remove-last-word)
    
*   [Remove file extension from filename](https://exceljet.net/formulas/remove-file-extension-from-filename)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split numbers from units of measure](https://exceljet.net/formulas/split-numbers-from-units-of-measure)
    

### Functions

*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [REGEXREPLACE Function](https://exceljet.net/functions/regexreplace-function)
    
*   [REPLACE Function](https://exceljet.net/functions/replace-function)
    

### Articles

*   [Regular Expressions in Excel](https://exceljet.net/articles/regular-expressions-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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