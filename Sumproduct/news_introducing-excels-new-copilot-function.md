# Introducing Excel’s New COPILOT Function

**Source:** https://sumproduct.com/news/introducing-excels-new-copilot-function/

---

[Home](https://sumproduct.com/)

\> Introducing Excel’s New COPILOT Function

*   August 20, 2025

Introducing Excel’s New COPILOT Function
========================================

![](https://sumproduct.com/wp-content/uploads/2025/08/image-88.png)

Today sees the launch of Excel’s “latest and greatest” function, **COPILOT**.  This function is currently in Beta and only available to users on the Beta Channel, which is available through the Microsoft Insider Program.

You will need to be on one of the following versions of Excel:

*   Windows: Version 2509 (Build 19212.20000) or later.
*   Mac: Version 16.101 (Build 25081334) or later.

It will be rolling out to Excel for the web users soon through the Frontier program, which offers you a similar “Insider” experience with the ability to access the latest features and provide feedback before experiences are made Generally Available.

The **COPILOT** function allows you to leverage artificial intelligence (AI) by providing a prompt and references from the Excel worksheet (what Microsoft has recently started calling “the grid”) to generate responses based upon an AI language model.  You will need a Copilot license for this function.

Its syntax is as follows:

**\=COPILOT(prompt\_part1, \[context1\], \[prompt\_part2\], \[context2\], …)**

Its arguments are as follows:

*   **prompt\_part:** this is required and represents the text that describes the task or question for the AI model.  You may combine each **prompt\_part** in sequence with its respective **context** to make a single prompt – a “call”
*   **context:** this argument is optional and denotes a reference from the Excel worksheet that provides context or data for the AI model.  This can be a single cell or a range.

The “complete” prompt is sent to the AI model.  As an example:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-89.png)

Here, in cell **J4**, it contains the formula:

**\=COPILOT(“Summarise the following data”,F13:G24,”into a PivotTable reporting quarterly”)**

This has two **prompt\_part**s and one \[1\] **context**.  You can see I have deliberately missed off the headings from the cell reference.  Therefore, the PivotTable uses the headers **Quarter** (presumably from the context of summarising quarterly) and **Sum of Values** even though it is clearly marked **Sales** in the source table. 

This is because the **COPILOT** function only has access to the prompt and **context** provided to or referenced by the function.  It does not have access to other data from your workbook no matter how close the proximity, data from other files or enterprise information.

In the next example, the headers are more meaningful as the headings have been included in the **context**:

![](<Base64-Image-Removed>)

But **COPILOT** is still lying to me – albeit with little white lies.  The output is not a PivotTable.  It has produced a dynamic array formula.  And what is the formula?  I have no idea – it has just provided the summary result as the response to the prompt.

**\=COPILOT(“Summarise the following data”,F33:G45,”into a PivotTable reporting quarterly”)**

has been sent to the AI model as

_Summarise the values in cells **F33:G45**_ _into quarterly Sales Totals._

It is not a teaching tool, but it does appear to get the results required.

And maybe, don’t be fooled by the similarity between the output presented and the output requested.  The following prompt did not go so well:

**\=COPILOT(“Summarise the following data”,F33:G45,”into a Bar Chart reporting quarterly”)**

![](<Base64-Image-Removed>)

Erm, that’s not quite a Bar Chart.  But let’s be fair here: this is only early days and no one stated it would provide graphical results (yet).

So what is going on?  The **COPILOT** function calls an AI model hosted on Azure directly from a cell formula.  It returns a response based upon your prompt and any referenced data, enabling dynamic outputs on the spreadsheet.

Microsoft states that the **COPILOT** function is designed for semantic, generative and exploratory tasks.  It is best suited for scenarios where deterministic accuracy is not required (just about any calculation in Excel then!), and where natural language understanding can provide value. 

![](<Base64-Image-Removed>)

It was successful in listing the 27 current countries in the European Union.  This could be readily tabulated using the **WRAPROWS** function, for instance.

**COPILOT** uses data available within the large language model itself, meaning it cannot directly access live web data or internal business documents.  If you need **COPILOT** to analyse current or internal data, you will first need to import that data into your workbook and then reference it directly within the **COPILOT** function.  Its output should be reviewed and validated for accuracy, especially for critical business decisions or reports. 

Having said this, Microsoft has advised that support for live web data and internal business documents will be added in the future although when this will be has not been made clear.

It seems a little “buggy” presently.  I modified the prompt for a different region and obtained the following results:

![](<Base64-Image-Removed>)

Perhaps there is debate as to how many states there are presently, given some of the political rhetoric!

Perhaps this a good time to highlight the various error messages Microsoft states you might get:

![](<Base64-Image-Removed>)

Can I get any more errors?  Let’s see.  Returning to listing states, closer to home, let’s try Australia:

![](<Base64-Image-Removed>)

This is not quite right: the Australia Capital Territory and Northern Territory are not states.  It is important to note that the **COPILOT** function relies on the underlying AI model and inaccurate, incorrect and erroneous results do occur.  You should **always** check your results!

The marketing literature supplementing the announcement provides recommended use cases such as:

*   summarising text
*   generating sample data
*   classifying or tagging content
*   generating text.

Do you see what is missing presently?  Numerical calculations are very conspicuous by their absence – and there is a very good reason for this, even though I did start with an illustration that worked.  Consider the following example:

![](<Base64-Image-Removed>)

Here, I have used the prompt:

**\=COPILOT(“Plot the 5 products over five years from 2025 onwards (years displayed horizontally).  The products are given by the following:”,F13:F17,”Initial sales for the first year are given by the following:”,G13:G17,”Annual growth rates are given by the following:”,H13:H17)**

It appears to be pretty impressive.  Only one problem: it’s **wrong**.

Unfortunately, this falls for the same problems models built time and time again with Large Language Models (LLMs) suffer from – computational errors.

Cell **O14** should be 22,497, not 22,517, and all numbers in the final year have errors, some minor, some more noticeable.  This the danger with LLM-led modelling: the errors are hard to spot.  The Excel calculation engine somehow needs to be combined with the LLM, because somewhere, somehow, they are not talking to each other.  The fact the calculations are not shown – only the COPILOT syntax – does not help. 

The problem is the numbers _almost_ look right.  That is the worst part.  They are going to be tricky to spot and unsuspecting analysts make erroneous computations – and hence conclusions – regardless of the warnings Microsoft give them about checking results. 

People talk about AI building models for them.  I am not so sure that will be happening in the very near future.  Computational results are sometimes wrong and because the errors tend to be small, they can be difficult to identify.  We are going to spend all our time saved on building models checking them!

A new study by METR, published in July (source: Time magazine), set out to measure the degree to which AI speeds up the work of experienced software developers.  The results were “very unexpected”.  METR measured the speed of 16 developers working on complex software projects, both with and without AI assistance.  After finishing their tasks, the developers estimated that access to AI had accelerated their work by 20% on average.  In fact, the measurements showed that AI had slowed them down by about 20%, due to modifying prompts, checking work and fine-tuning results.

Microsoft states that “to ensure reliability and to use it responsibly”, you should avoid using **COPILOT** (presumably for the time being) for:

*   **numerical calculations:** they suggest using native Excel formulae instead for any task requiring accuracy or reproducibility (er, any task then)
*   **responses that require context other than the ranges provided:** the **COPILOT** function only has access to the prompt and context provided to or referenced by the function.  As stated above, it does not have access to other data from your workbook, data from other files or enterprise information
*   **lookups based on data in your workbook:** use lookup functions such as **INDEX MATCH** and **XLOOKUP** to look up data based upon a table or range
*   **tasks with legal, regulatory or compliance implications:** avoid using AI-generated outputs for financial reporting, legal documents or other high-stakes scenarios.  Just four days before writing this article, a senior lawyer in Australia has been forced to apologise to a judge in the Supreme Court of Victoria for filing submissions in a murder case that included fake quotes and non-existent case judgments generated by AI.  This not the only such instance!
*   **recent or real-time data:** the function is non-deterministic and may return different results on recalculation.  Currently, the model’s knowledge is limited to information before June 2024.

It is worth playing with **COPILOT** but copious feedback should be provided to Microsoft.  This is clearly a function that is not fully cooked.  I don’t want to say it’s half-baked, because it is better than that.

AI is here to stay.  It needs to be embraced, but it cannot be relied upon – yet.  There is an AI arms race in progress – we are all scared of being left behind – but the bigger worry is we accept erroneous results and make wrong decisions.

By its nature, AI is continuously improving, and the **COPILOT** function is no different. We are considering many improvements – some of these improvements will be available through the beta phase, and others will come in the future based on your feedback or be areas of continued enhancement.

Microsoft has noted that they are presently working on and / or investigating various areas including:

*   **better large array support:** rows can be omitted when returning arrays.  To work around this, restructure your queries to return smaller array results
*   **best-in-class models:** Microsoft is actively testing and benchmarking models for the best blend of performance and capabilities.  The underlying model will evolve and get more capable over time
*   **better guidance:** they are investigating providing user guidance when the **COPILOT** function is used for tasks not suitable for LLMs, _e.g._ **\=COPILOT(“Sum these values”,A1:A10)**
*   **enhanced knowledge:** the **COPILOT** function is model grounded, with no access to web and enterprise data.  Microsoft is investigating adding support for expanding these capabilities
*   **better date support:** currently, the **COPILOT** function returns dates as text rather than Excel’s date serial format.

For those wanting to test **COPILOT**, do take into account the following:

*   the **COPILOT** function is only available to users with a Copilot subscription and an active internet connection to access the AI models, hosted on Azure
*   you can calculate up to 100 **COPILOT** functions every 10 minutes and up to 300 calls per hour.  If you need additional calls, consider using arrays instead.  A call occurs each time a **COPILOT** function calculates, regardless of the input or output size.  For formulae such as **\=COPILOT(…)&COPILOT(…)** or **\=COPILOT(COPILOT(…))**, they both would count as two calls
*   the **COPILOT** function cannot calculate in workbooks labelled Confidential or Highly Confidential

*   currently, the **COPILOT** function uses gpt-4.1-mini (although this is noted from 14 April 2025 and may have been updated subsequently)
*   the **COPILOT** function’s model will evolve and improve in the future and formula results may change over time, even with the same arguments.  If you don’t want results to recalculate, consider converting them into values with Copy and Paste Values
*   your prompts and data supplied as context will not be used to train AI models.

Furthermore, to get the most out of the **COPILOT** function, consider:

*   how you write your prompt: clearer, longer, more explicit prompts are more likely to provide what you require.  Consider the **context** arguments carefully and specify how you want outputs to be arranged / summarised
*   verbs such as “summarise”, “categorise” and “highlight” will help produce the outputs in a certain style or format
*   **COPILOT** uses data available within the large language model only.

The **COPILOT** function is formally recognised as the successor to the **LABS.GENERATIVEAI** function that debuted as an experiment in the Excel Labs add-in.

**_Word to the Wise_**

Whilst I could lament it was interesting how many times Excel crashed producing the examples above, I think Copilot’s own take on **COPILOT** is a better footnote!  Given the news only broke recently, I decided it might be worth asking Copilot how this new function worked.  Not only did it state it should be used for formulae and had no usage limits (both points are incorrect), but it also got the syntax wrong too:

**\=COPILOT(“prompt”, \[data\_range\], \[options\])**

Interestingly, the **options** argument imagined could prove useful, as Copilot stated this defines how output is presented (_e.g_. numerically, in a PivotTable, in a chart).  Maybe it knows something the rest of us don’t.

To be continued…

*   [Log in](https://sumproduct.com/news/introducing-excels-new-copilot-function/#0)
    
*   [Register](https://sumproduct.com/news/introducing-excels-new-copilot-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/introducing-excels-new-copilot-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/introducing-excels-new-copilot-function/#0)

[](https://sumproduct.com/news/introducing-excels-new-copilot-function/#0 "close")

top