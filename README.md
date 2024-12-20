# Uncommon Python Error: Relying on Exceptions for Logic

This repository demonstrates a subtle and less common coding error in Python: using exception handling (try-except) to control program flow instead of proper conditional checks. This can lead to unexpected behavior, reduced code readability, and potential performance issues.  The provided solution shows how to rewrite the code for improved clarity, maintainability, and robustness.

**Bug:** The initial `bug.py` script utilizes a try-except block to handle a potential `ZeroDivisionError`.  However, this is an error prone approach, as the primary issue is the reliance on exception handling for standard program flow, rather than the potential `ZeroDivisionError` itself.

**Solution:** The `bugSolution.py` file demonstrates a cleaner and more effective solution: using an `if` statement to explicitly check for a zero value before performing the division, preventing the exception from occurring in the first place.  This approach avoids unexpected behavior and enhances the code's overall quality.