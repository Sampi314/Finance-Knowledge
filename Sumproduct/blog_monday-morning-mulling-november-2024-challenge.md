# Monday Morning Mulling: November 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-november-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: November 2024 Challenge

*   December 1, 2024

Monday Morning Mulling: November 2024 Challenge
===============================================

Monday Morning Mulling: November 2024 Challenge
===============================================

2 December 2024

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution. This past Friday, we presented you with the Staircase Challenge._

**_The Challenge_**

In this challenge, we asked you to calculate the number of distinct ways to climb a staircase with **n** steps, where each step can be climbed by taking either a single step or a double step at a time. For example, for a staircase with 3 steps, the possible ways to climb it would be:

*   taking three single steps: 1 – 1 – 1
*   one single step followed by a double step: 1 – 2
*   one double step followed by a single step: 2 – 1.

![](https://sumproduct.com/wp-content/uploads/2025/05/9fd5c3f32b694326d7f670dea6148c42-1.jpg)

This results in three \[3\] unique ways to climb three \[3\] steps. But as the number of steps of the stair increases, so do the possible combinations, making it an interesting puzzle. You could download the original question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/November/sp-staircase-problem---starter-file.xlsm)
.

As always, there were some requirements:

*   the formula needs to be within just one \[1\] cell (no “helper” cells).

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/November/sp-staircase-problem---suggested-solutions.xlsm)
, which shows our suggested solution. The steps are detailed below.

**_The Fibonacci Connection_**

This challenge has a surprising link to the Fibonacci sequence! Here’s how the connection works:

To determine the number of ways to reach the **n**th step, you could:

*   arrive from the (**n**\-1)th step by taking one \[1\] step
*   arrive from the (**n**\-2)th step by taking a two-step at once.

This means the total number of ways to reach the **n**th step, **F(n)**, can be defined as:

**F(n) = F(n-1) + F(n-2)**

This is precisely the recurrence relation that defines the Fibonacci sequence, where each number is the sum of the two preceding ones. If we start with **F(1) = 1** (only one way to reach the first step) and **F(2) = 2** (two ways to reach the second step: either two single steps or one double step), the number of ways to reach each subsequent step aligns with the Fibonacci numbers.

**_Solution 1: Binet’s Formula: A Closed Form for Fibonacci Numbers_**

Using the recurrence relation **F(n) = F(n−1) + F(n−2)** yields the Fibonacci sequence, but we can also use **Binet’s formula** to calculate the **n**th Fibonacci number directly. Binet’s formula expresses Fibonacci numbers as:

![](<Base64-Image-Removed>)

You can model Binet’s formula directly in Excel using **LET**, which simplifies complex formulas by defining variables for easy reference:

**\=ROUND(LET(Golden\_Ratio,(1+SQRT(5))/2,**

**Conjugate\_of\_Golden\_Ratio,(1-SQRT(5))/2,**

**(Golden\_Ratio^(H10+1)+Conjugate\_of\_Golden\_Ratio^(H10+1))/SQRT(5)),0)**

where **H10** is the number of step count if a stair and here’s what each part does:

*   **LET** allows us to define **Golden\_Ratio** and **Conjugate\_of\_Golden\_Ratio** as intermediate variables for readability
*   then in the fifth argument of **LET** we write the Binet’s formula for calculating the Fibonacci and then the **ROUND** function will round them up correctly.

**_Solution 2: Using REDUCE and LAMBDA for an Iterative Approach_**

Another way to solve this problem in Excel is using **REDUCE** and **LAMBDA** functions to iteratively generate Fibonacci numbers up to **n.**

1.  **the number of steps (n)**: in cell **H10** we will put in the number of steps
2.  **the maximum number of steps (k)**: in cell **H11** we will put the maximum number of steps which is two \[2\] in this case.

![](<Base64-Image-Removed>)

In the output cell we will put this formula:

**\=TAKE(REDUCE(1, SEQUENCE(H10),  
LAMBDA(x, y, VSTACK(x, SUM(TAKE(x, -H11)))), -1)**

Here’s a breakdown:

*   **REDUCE(1, SEQUENCE(H10), LAMBDA(x, y, …))**:

*   **1** is the initial value (the start of the sequence).
*   **SEQUENCE(H10)** generates a sequence up to **n** to control the number of iterations.
*   **LAMBDA(x, y, …)** defines an iterative function that stacks (using **VSTACK**) the next Fibonacci number based on the last two values in the sequence

*   **SUM(TAKE(x, -H11))**: adds the last **k**\=2 values in the sequence to generate the next Fibonacci number.
*   **REDUCE(1, SEQUENCE(H10), LAMBDA(x, y, VSTACK(x, SUM(TAKE(x, -H11)))), -1)**:this part of the formula will generate the Fibonacci sequence from 1 to **n**:

![](<Base64-Image-Removed>)

*   **TAKE(…, -1)**: retrieves the last value from the sequence, which is the **n**th Fibonacci number.

**_Word to the Wise_**

If a person can take more than two \[2\] steps at a time (_e.g_. three \[3\] or four \[4\] or even more than that), the number of possible combinations increases significantly. While Binet’s formula applies strictly to the Fibonacci sequence (when the allowed steps are exactly one \[1\] or two \[2\]), the second solution using **REDUCE** and **LAMBDA** is highly flexible and can handle scenarios where any number of steps, up to a defined maximum of **n**, can be taken at once. Simply update the value in **H11** to reflect the maximum number of steps, and the formula will adjust dynamically.

This dynamic capability makes the second solution particularly versatile for solving more complex variations of the Staircase Challenge.

Interestingly, this challenge happens to be on the eighth anniversary of a previous challenge regarding Fibonacci sequences. You can check it out here: [https://www.sumproduct.com/blog/article/monday-morning-mulling-november-challenge](https://www.sumproduct.com/blog/article/monday-morning-mulling-november-challenge)
.

_The Final Friday Fix will return on Friday 27 December 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-november-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-november-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-november-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-november-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-november-2024-challenge/#0 "close")

top