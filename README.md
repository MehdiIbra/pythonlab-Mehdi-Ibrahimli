This project covers three different programming approaches in Python to perform mathematical calculations.

The imperative approach uses loops and if/elif statements to iterate through data, handling division by zero with error messages so the program keeps running.

The functional approach avoids loops and if/elif statements completely, using filter to drop division by zero entries and map with a dictionary of lambda functions to calculate results.

The higher-order function approach uses a custom calculate function that accepts callback functions and safely catches ZeroDivisionError by returning None.
