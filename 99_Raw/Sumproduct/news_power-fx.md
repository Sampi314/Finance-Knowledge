# Power Fx

**Source:** https://sumproduct.com/news/power-fx/

---

[Home](https://sumproduct.com/)

\> Power Fx

*   March 3, 2021

Power Fx
========

Power Fx
========

3 March 2021

Microsoft Power Fx has been announced as “…the newest member of the Microsoft Power Platform family…”. It is the low code language for expressing logic across the Microsoft Power Platform. It is the same language that is at the heart of the so-called Microsoft Power Apps canvas apps today and is inspired by Microsoft Excel. It enables the full spectrum of development from “no code” to “pro code”.

Microsoft views this announcement as a statement of direction. There are no adverse implications for Power BI’s existing **M** and DAX languages. Power Fx is complementary to them: **M** and DAX focus on reading, shaping, joining and summarising large amounts of data, whilst Power Fx focuses on reading and writing smaller sets of relational data.

In particular:

*   **Power Fx is open source.** Microsoft has learned from the public’s adoption of languages like C# and Typescript. With Power Fx, we’re now bringing that same open approach to the low code world. Microsoft will open-source Power Fx, making the language available for open contribution by the broader community on GitHub
*   **Power Fx is based on Microsoft Excel.** Using formulae that are already familiar to hundreds of millions of users, Power Fx allows a broad range of people to bring skills they already know to low code solutionsz
*   **Power Fx is built for “low code”.** Already the foundation of the Microsoft Power Apps canvas, Power Fx will soon be extended for use across Power Platform to Microsoft Dataverse, Microsoft Power Automate, Microsoft Power Virtual Agents, and beyond.

This table shows all of Power Fx’s pure functions, the ones marked in green are identical or very close to Excel’s version:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-29.jpg)

Excel has many more functions than this and Microsoft will be adding more all the time to Power Fx.

**_Low Code_**

Power Fx describes business logic in concise, yet powerful, formulae, in a way that would make sense to your average Excel user.

In particular, there are many attributes worth noting for Power Fx:

*   **Asynchronous.** All data operations in Power Fx are asynchronous. The maker doesn’t need to specify this, nor does the maker need to synchronize after the call is over. Most importantly, the maker doesn’t need to be aware of this concept at all, they don’t need to know what a promise or lambda function is, which is just as well, as I have no idea what Microsoft is talking about!
*   **Local and remote.** Power Fx uses the same syntax and functions for data that is local in-memory and remote in a database or service. The user need not think about this distinction. Power Fx automatically delegates what it can to the server to process filters and sorts there more efficiently
*   **Relational data.** Database keys are another concept the maker doesn’t need to know about. The maker can use simple dot notation to access the entire graph of relationships from a record
*   **Projection.** When writing a query, many developers will naively write _“select \* from …”_ that brings back all the columns of data. Power Fx performs analysis of all the columns that are used through the entire app, even across formula dependencies. Projection is automatically optimised and again the maker need not even know what that word means
*   **Retrieve only what is needed.** The LookUp function implies that only one record should be retrieved and that is all that is brought back. If more records are requested by using the Filter function, for which thousands of records may qualify, only a single page of data is brought back at a time, on the order of a hundred records. The user must gesture through a gallery or data table to see the additional data, and it is automatically brought in for them. The maker can reason about large sets of data without needing to think about limiting data requests to reasonable amounts
*   **Runs only when it is needed.** Calculations may be deferred until required
*   **Excel syntax translation.** Excel is used by hundreds of millions of users. Microsoft wants to leveraging the knowledge users already have
*   **Display names and localisation.** In Dataverse and SharePoint, there is a display name for fields and tables as well as a unique logical name. The display names are often much more user friendly, as in this case, but they have another important quality: they can be localised. If you have a multi-lingual team, each team member can see table and field names in their own language. In all cases, Power Fx makes sure that the correct logical name is sent to the database automatically.

**_Always Live_**

Excel has no edit mode, compile step or run state. Youn simply open your spreadsheet, you edit formulae and values freely and work with the results. The spreadsheet is always live while in Excel and there is no distinction made between editing and running. Changes in any value or formula are immediate propagated throughout the spreadsheet and the maker can quickly check for the right answer. Any errors that Excel detects are surfaced immediately and don’t interfere with the rest of the spreadsheet.

Power Fx strives for this same live experience. It incorporates an incremental compiler to update formulas while the app is running and without disturbing state.

**_No Code_**

You don’t need to read and write Power Fx to start expressing logic. There are lots of customisations and logic that can be expressed through simple switches and UI builders. Microsoft has built these “no code” tools to read and write Power Fx to ensure there is plenty of headroom for someone to take it further, acknowledging that “no code” tools will never offer all the expressiveness of the full language.

**_Pro Code_**

Low code makers build things that sometimes require the help of an expert or are taken over by a professional to maintain and enhance. Professionals also appreciate that low code development can be easier, faster and less costly than building in a professional tool. Not every situation requires the full power of Visual Studio.

Professionals want to use professional tools to be the most productive. This is why language tooling has been introduced that unpacks a canvas app into constituent parts that can be edited with Visual Studio Code or Visual Studio:

![](<Base64-Image-Removed>)

**_In Summary_**

Power Fx is the new language for expressing logic across the Microsoft Power Platform. It’s not so much a new programming language as the “announced new name” for the formula language for the canvas apps. It is intended to be a general purpose, strong-typed, declarative and functional programming language, sharing many of the same syntax and functions as Excel.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/power-fx/#0)
    
*   [Register](https://sumproduct.com/news/power-fx/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/power-fx/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/power-fx/#0)

[](https://sumproduct.com/news/power-fx/#0 "close")

top