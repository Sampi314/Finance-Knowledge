# Monday Morning Mulling: February 2023 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-february-2023-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: February 2023 Challenge

*   February 26, 2023

Monday Morning Mulling: February 2023 Challenge
===============================================

Monday Morning Mulling: February 2023 Challenge
===============================================

27 February 2023

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_The Challenge_**

Have you ever thought of putting an interactive picture within Excel that changes with just a simple press of the **F9** key on your keyboard? This month, we challenged you to do that. You could download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2023/Jan/sp-alternating-switch---challenge.xlsm)
.

This month’s challenge was to build a cell that could alternate between at least three \[3\] different values each time Excel recalculates (by pressing **F9**) and use these values in conditional formatting to make the traffic light flash as shown below:

![](https://sumproduct.com/wp-content/uploads/2025/05/image1-1675310333.gif)

As always, there were some requirements:

*   no Power Query / Get & Transform, VBA or circular reference(s) was allowed
*   the traffic light should always alternate in a loop from red to yellow to green and then red again, _etc_.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2023/Jan/sp-alternating-switch---suggested-solution.xlsm)
, which shows our suggested solution.

To begin with, we have an input cell to enter the number of values in one alternating loop. In this case, we will enter three \[3\] as we want the traffic light to switch between three \[3\] colours which are red, yellow (amber) and green:

![](https://sumproduct.com/wp-content/uploads/2025/05/96563215713d7f2d03626195d9434f55.jpg)

We have named this assumption cell **Number\_in\_Loop**. Then, we have another cell for the outputs with the name **Result**:

![](https://sumproduct.com/wp-content/uploads/2025/05/56cd38c82975b551059974484899b209.jpg)

We will leave the **Result** cell empty for now. Next, we will prepare a Data Table. In the column input of the Data Table (_i.e._cell **H13**), we let this cell equal **Result**:

**\=Result**

In the row input of the Data Table (_i.e._ cell **G14**), we enter the following formula:

**\=MOD(Result,Numbers\_in\_Loop)+1**

This formula calculates the next number in a loop when the **Result** is changed. The final step is to create the Data Table. We will select the whole range **G13:H14**, go to the **Data** tab, select **What-If Analysis** and then **Data Table** (or **ALT + D + T**):

![](https://sumproduct.com/wp-content/uploads/2025/05/be383b6bf199ebf242bcaa913e1b0ca6.jpg)

In the ‘Row input cell’ box, we select the **Result** cell, cell **G10**.

The finishing touch for this alternating switch is that in the **Result** cell, we set this equal to the output of the Data Table which is located in cell **H14**:

![](https://sumproduct.com/wp-content/uploads/2025/05/356d2c33801b11d043b46bf4e6fb7e8b.jpg)

After clicking OK, the row input of the data within the Data Table will calculate once and then stop. Then, the Data Table’s output will go to the **Result** cell which makes the ‘Row input’ and ‘Column input’ of the Data Table change. However, the Data Table will not update until we press the **F9** key to force Excel to recalculate. This way we can avoid the circular reference within the model:

![](https://sumproduct.com/wp-content/uploads/2025/05/ca2e021ed707e63be33c3e682d7fccf3.jpg)

At this point, we are partially done with the challenge. As we can see that every time the **F9** key on the keyboard is pressed the number in **Result** will increase by one \[1\] and loop back to one \[1\] after reaching three \[3\].

![](https://sumproduct.com/wp-content/uploads/2025/05/image7-1675310343.gif)

The final step we need to implement here is to use conditional formatting to add the fading colour to the traffic light. To begin, select the red light region and go to **Home** -> **Styles** -> **Conditional Formatting** \->**New Rule** (or _**ALT + O + D**__)._ We select the last ‘Rule Type’ which is ‘Use a formula to determine which cells to format’ and in the formula box below we enter the following formula and apply a light background colour format:

![](<Base64-Image-Removed>)

If the **Result** is different from one \[1\], the red light will have a grey colour. We can repeat the same process for the yellow and green lights, using the numbers two \[2\] and three \[3\] respectively. Finally, we have our interactive traffic light, shown below:

![](<Base64-Image-Removed>)

**_Word to the Wise_**

We appreciate there are many, many ways this could have been achieved. If you have come up with an alternative, radically different approach, congratulations – that’s half the fun of Excel!

_The Final Friday Fix will return on Friday 24 March 2023 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-february-2023-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-february-2023-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-february-2023-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-february-2023-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-february-2023-challenge/#0 "close")

top