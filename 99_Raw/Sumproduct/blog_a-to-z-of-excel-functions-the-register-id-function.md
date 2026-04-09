# A to Z of Excel Functions: The REGISTER.ID Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-register-id-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The REGISTER.ID Function

*   October 6, 2024

A to Z of Excel Functions: The REGISTER.ID Function
===================================================

A to Z of Excel Functions: The REGISTER.ID Function
===================================================

7 October 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **REGISTER.ID** function._

**The REGISTER.ID function**

![](https://sumproduct.com/wp-content/uploads/2025/05/d8ae3e376a3ff36cf4fde78f3ee6cc6d-1.jpg)

**REGISTER.ID** is anotherfunction that Microsoft refuses to register. The software company has one of its longest Help pages on this function and it makes as much sense as trying to determine what the colour 17 smells like.

This function can be used on worksheets (unlike **[REGISTER](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-register-function)
**), but we are stumped as to precisely how it works. It appears to rely upon Operating Systems before Windows 7 (we love to bring you all the latest technology here!).

It allegedly returns the registry ID for a specific DLL (Dynamic Linked Library), which is a shared library in the Microsoft Windows or OS/2 operating system. A DLL can contain executable code, data and resources in various combinations, and are designed to allow other programs to use them.

Amongst other utilities, this information may be used for registry modification (the registry is a centralised, hierarchical database that manages resources and stores configuration settings typically for applications on the Windows operating system). Incorrectly editing said registry may severely damage your operating system, requiring you to reinstall it. That’s not a good idea, especially as Microsoft will not guarantee that problems resulting from editing the registry incorrectly may even be resolved. Before editing the registry, back up any valuable data.

In summary, it should only be used if you _don’t_ need to read this article.

The **REGISTER.ID** function cannot be used in Excel for the web at all and is associated with the **[CALL](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-call-function)
** function.

The syntax is not straightforward.You cannot specify function or argument names, and its syntax differs depending upon your operating environment, but includes a **type\_text** argument

**\=REGISTER.ID(module\_text,  
procedure, \[type\_text\])**

It has the following arguments:

*   **module\_text:** this is required and represents the text specifying the name of the DLL that contains the function in Excel
*   **procedure:** this is also required. This is the text specifying the name of the function in the DLL in Excel
*   **type\_text:** this argument is optional and denotes the data type of the return value and the data types of all arguments to the DLL. If the function or code resource is already registered, you may omit this argument.

The **procedure** argument may also use the ordinal value of the function from the EXPORTS statement in the module-definition file (**.DEF**). The ordinal value or resource ID number must not be in text form.

The **type\_text** argument specifies the data type of the return value and the data types of all arguments to the DLL function or code resource. The first character of **type\_text** specifies the data type of the return value. The remaining characters indicate the data types of all the arguments. For example, a DLL function that returns a floating-point number and takes an integer and a floating-point number as arguments would require “BIB” for the **type\_text** argument.

The following table contains a complete list of the data type codes that Microsoft Excel recognises, a description of each data type, how the argument or return value is passed, and a typical declaration for the data type in the C programming language. Enjoy.

![](<Base64-Image-Removed>)

It should be noted that:

*   the C language declarations are based on the assumption that your compiler defaults to 8-byte doubles, 2-byte short integers and 4-byte long integers
*   in the Microsoft Windows programming environment, all pointers are far pointers. For example, you must declare the D data type code as unsigned char far \* in Microsoft Windows
*   all functions in DLLs and code resources are called using the Pascal calling convention. Most C compilers allow you to use the Pascal calling convention by adding the Pascal keyword to the function declaration, as shown in the following example: pascal void main (rows,columns,a)
*   if a function uses a pass-by-reference data type for its return value, you can pass a null pointer as the return value. Microsoft Excel will interpret the null pointer as the _#NUM!_ error value.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-register-id-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-register-id-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-register-id-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-register-id-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-register-id-function/#0 "close")

top