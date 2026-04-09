# VBA Blogs: The Value of Declaring Variables

**Source:** https://sumproduct.com/blog/vba-blogs-the-value-of-declaring-variables/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: The Value of Declaring Variables

*   October 12, 2017

VBA Blogs: The Value of Declaring Variables
===========================================

VBA Blogs: The Value of Declaring Variables
===========================================

13 October 2017

We first looked at declaring variables [here](https://www.sumproduct.com/blog/article/vba-blogs/declaring-variables)
 and though it takes a lot more effort to remember to declare all variables used, let’s take an in depth look as it is good coding practice to and how it helps write better VBA code.

**Efficiency**

VBA data types determine the way in which data is stored in the computer’s memory. It allocates the memory before the procedure is run instead of generating it on the fly. By default when an undeclared variable is called upon, VBA assigns it as the Variant, which is the largest of the data types stored as 16 bytes. This can accumulate and take up a lot of memory and cause the execution to become sluggish.

**Robustness**

The problem with allowing the variable to be a Variant is that as the compiler tries to figure out what action you perform on it. It can cause unexpected results if you are not careful.

Let’s look at the following example:

![](https://sumproduct.com/wp-content/uploads/2025/05/acea85b433b085c90870ffb6a73a07b4.jpg)

The variable “One” in the first instance is used as a number and in the second instance as a string. But as the type was not explicitly declared, VBA allowed it to be transformed mid routine. As a result, when it was called upon the second time, it was converted to string operation resulting in “111” instead of adding to 3. By declaring the variable as an Integer or Long (Numeric data types), VBA would have recognised the correct expected result using addition as a summing operator or alerted us upon compiling that there was a mistake in the code.

![](https://sumproduct.com/wp-content/uploads/2025/05/19dc307b19e98bc78e932cc2921b000f.jpg)

When the variable is explicitly declared to be an Integer, the compiler recognises that the quotation marks are superfluous and converts our number string to an actual number, which is what was actually expected and vice versa if declared as String:

![](https://sumproduct.com/wp-content/uploads/2025/05/63a8d81275fbcb3ce89d004b4e7602f3.jpg)

Now if it had been declared as a Boolean for an example, the compiler would give an error alert saying that the incorrect type has been used.

![](https://sumproduct.com/wp-content/uploads/2025/05/c217a484562d50134669569057caed4a.jpg)

**Consistency**

Now the VBA editor does some weird things when variable is not declared.

Let’s reuse the variable whilst typing:

![](https://sumproduct.com/wp-content/uploads/2025/05/e317aa114248ec8a9352a67845426a84.jpg)

However when Enter is pressed right after, this happens:

![](https://sumproduct.com/wp-content/uploads/2025/05/f2b74d92caaec6f3ca3fefc001352b09.jpg)

The capitalisation of the variable has changed! If the variable is not declared, then it will take the capitalisation properties of your **_most recent entry_** as opposed to the original. By declaring the variable with the capitalisation structure to be maintained, the editor autocorrects each instance to capitalisation to the declaration style, not the most recent.

After typing the declaration string changes all the code from this:

![](https://sumproduct.com/wp-content/uploads/2025/05/02b9eab60fe7cfe18fd808b8933219ee.jpg)

To this:

![](https://sumproduct.com/wp-content/uploads/2025/05/6c21c087142af6202824bdd59e2e1299.jpg)

A nice thing about declaring a variable is that VBA editor’s auto complete function can be utilised.

By typing the first three characters (“myV”) and then pressing <Ctrl> + <Space> it will autocomplete to the variable matching those letters (“myVariable”).

However if two similarly named variables are available, a handy dialogue will pop up allowing the coder to see what names are available for use.

![](<Base64-Image-Removed>)

Declaring variables in VBA is always good coding practice. Not only is the code more efficient to run, it allows the programmer to use consistent form, check against errors and mitigate potentially rogue operations.

So declare everything! Tune in next week to see options on how to help manage declarations and their scope.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-the-value-of-declaring-variables/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-the-value-of-declaring-variables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-the-value-of-declaring-variables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-the-value-of-declaring-variables/#0)

[](https://sumproduct.com/blog/vba-blogs-the-value-of-declaring-variables/#0 "close")

top