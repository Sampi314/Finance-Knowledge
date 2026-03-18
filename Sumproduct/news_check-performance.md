# Check Performance

**Source:** https://sumproduct.com/news/check-performance/

---

[Home](https://sumproduct.com/)

\> Check Performance

*   April 18, 2023

Check Performance
=================

Check Performance
=================

18 April 2023

Originally added to Excel for the web back in October last year, ‘Check Performance’ has been improved for Excel for the web, although precisely what these improvements are we aren’t clear. Anyone who uses Excel regularly will be familiar with the dreaded file bloating phenomenon, where file sizes suddenly increase drastically and / or unexpectedly. At long last, the Excel Performance team has created a new capability to detect and remove unwanted size bloat and speed up such workbooks.

Often, a workbook can collect cells that have no data but still contain hidden information of little or no use anymore. These cells may have had data and formatting to start with, however now they do not have any data, but still take up space because they contain formatting. Consequently, too many of these cells can cause your workbook to slow down or become unresponsive. As a consequence, this update enables you to detect and remove these cells slowing down your workbooks, with ‘Check Performance’ – albeit presently available only in Excel for the Web.

When you open your workbook, Excel now detects whether your workbook contains too many of these unwanted formatted cells. If it does, Excel shows a “Business bar” to launch the ‘Check Performance’ feature. This may be launched manually from **Review -> Check Performance** too.

Once launched, there are two ways to remove these cells:

1.  by navigating to a sheet in the task pane to review each range of these cells to optimise, and then pressing the ‘Optimize Sheet’ button; _or_
2.  by pressing the ‘Optimize All’ button to remove all unwanted cells from all sheets in the workbook.

Consider the following example. Here, we have a file that has a current size of 3.14MB – not too large, but as it turns out, much larger than it _should_ be.

![](https://sumproduct.com/wp-content/uploads/2025/05/d1dd45ae969ecdef2c084ad60af569c5.jpg)

Upon opening, the Business bar (yellow bar) highlights the slow workbook and prompts you to ‘Check Performance’. This may also be accessed from the Review tab, as displayed below:

![](https://sumproduct.com/wp-content/uploads/2025/05/572943eb06e3b42030d0b9b68544dc98.jpg)

The ‘Workbook Performance’ pane appears and highlights two of the three worksheets may require review, citing a total of four ranges, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/cd9a1fb8655d86b00d11e145689f3735.jpg)

Clicking on the ‘Inventory’ box in the ‘Workbook Performance’ pane yields information on three empty cell ranges that may be optimised and prompts with an ‘Optimize sheet’ button (bottom right):

![](https://sumproduct.com/wp-content/uploads/2025/05/2f4f597cf31d557451b0a606bf394da4.jpg)

Similarly, the ‘Supplier’ sheet details one range to consider:

![](https://sumproduct.com/wp-content/uploads/2025/05/0e0f54af1a2d2aeaebcef255132a3e95.jpg)

Following the prompts and optimising both sheets generates considerable savings in file size:

![](https://sumproduct.com/wp-content/uploads/2025/05/67a92d858af7086cfda855442871af75.jpg)

Here, ‘Check Performance’ has reduced a 3.14 MB file down to 17.5 KB, by detecting and removing more than a million unwanted formatted cells. Bearing this in mind, you might think, why doesn’t Excel remove these cells in the background without alerting me? This is because, even though the cell has no data, removing its formatting may result in visible changes. For example, removing yellow fill from a cell may reset its fill to ‘No Color’, which might not be what you want. Microsoft does not want any Excel users to be surprised by visual changes by doing this in the background without alerting hence the manual interaction.

You should note that this new feature will be enabled gradually to more and more users over time as Microsoft rolls out the update and ensures it is working correctly. Therefore, if you do not see the ‘Check Performance’ button in the Review menu tab, then the feature may not be enabled for you yet.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/check-performance/#0)
    
*   [Register](https://sumproduct.com/news/check-performance/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/check-performance/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/check-performance/#0)

[](https://sumproduct.com/news/check-performance/#0 "close")

top