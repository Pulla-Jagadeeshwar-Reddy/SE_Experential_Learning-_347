# Reflection

1. **What is static code analysis, and how did the tools differ?**  
   Static analysis examines source code without running it. Pylint checks code quality and likely errors, Bandit checks common security risks, and Flake8 checks Python style and formatting.

2. **What issues did you identify?**  
   The program had a mutable default argument, broad exception handling, a weak MD5 digest, shell execution with an interpolated folder value, an unused hard-coded password, and style problems.

3. **Which fixes were most important?**  
   Replacing the shell backup command removed a command-injection risk. Changing the shared list default prevented data from leaking between calls. The demo continued to produce the expected totals and vehicle count.

4. **What are the limitations of static analysis?**  
   Clean reports cannot prove code is correct or secure in every situation. Tools can miss context-dependent problems, so their results should be combined with running the program, tests, and human review.