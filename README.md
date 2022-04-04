# Intermediate_Python_NanoDegree
---
## Course 1 : 
===
## `Lesson 2`=> combine what you've learned about data types to build a predictive text algorithm.This exercise comes in three levels of difficulty. Everyone should aim   to complete the first function - parse_content. It's worthwhile to attempt the make_tree function. Lastly, the predict function is the hardest and most complex, but the most rewarding. Finishing the predict function is evidence that you solidly understand the contents of this lesson.


* `parse_content` : simply read raw txt file and parse every word to it's t9 frequency. 
* `make_trie` : Trie is a very useful data structure. It is commonly used to represent a dictionary for looking up words in a vocabulary. To implement such a function, we need several things at the backend. The first, obviously, is a list of common queries. Or it can be a list of proper English words for the purpose of auto-completion). Secondly, we will need to have an algorithm to quickly look up words starting with the characters input by the user, and this is where we need to use the trie data structure.
* `predict` : 

## `Lesson 3` 
New Terms In This Lesson
Term	Definition
Argument	An object (or a name referring to an object) that is supplied to a function when the function is invoked.
Decorator	A high-level function that traditionally transforms an input function into a slightly-modified output function with desired decorated behavior.
@decorator	Special syntax to apply a decorator to an immediately-subsequent function definition.
filter	A built-in function that filters an iterable by keeping only elements that successfully pass a predicate function.
The fn.__code__ attribute	An attribute of function objects that represents the function's code object.
The fn.__doc__ attribute	An attribute of function objects that represents the function's documentation string.
The fn.__name__ attribute	An attribute of function objects that represents the function's name.
Function Objects	A type of object in Python representing a callable function.
Functional Implementation	The details of how a function transforms its inputs to outputs
Functional Interface	A function's inputs and outputs, viewed collectively as a contract between the function and the outside world
Functional Programming	A programming paradigm focusing on higher-order functions and composition as fundamental tools for solving problems.
Generator Expression	A syntactical shortcut to create on-the-fly iterators with simple implementations.
Generator Function	A special type of function containing the keyword yield that can produce a stream of values when called.
globals()	A Python builtin function call that returns a dictionary representation of the global namespace.
Iterable	An object that can be iterated over.
Iterator	An object representing a stream of data that can yield successive values.
Keyword Argument	An argument that is supplied to a function call by keyword, not by position.
Keyword-Only Parameters	A subcategory of optional parameters defined by a function signature that can only be overridden by an argument supplied by keyword.
lambda	An anonymous function used to define simple callables.
locals()	A Python builtin function call that returns a dictionary representation of the local namespace.
map	A built-in function that applies a function to every element of an iterable.
Name Resolution	The process by which Python determines the value associated with a name, by searching outwards through nested namespaces.
The operator module	A built-in module that provides standard operators as functions.
Optional Parameter	A category of parameters defined by a function signature that provides a default value for a parameter name.
Parameter	A name defined in a function signature that will be bound to a value when the function is invoked.
Pass-By-Object-Reference	The mechanism by which Python supplies arguments a function's local symbol table - variables (i.e. references to objects) are copied, but the referred objects are themselves accessible through the reference.
PEP 257	Docstring Conventions
PEP 8	Style Guide for Python Code
Positional-Only Arguments	A subcategory of required parameters defined by a function signature that can only be supplied by a positional argument.
Positionally-Supplied Argument	An argument that is supplied to a function call by position, not by keyword.
Required Parameter	A category of parameters defined by a function signature that does not provide any default value and must receive a value from a corresponding supplied argument.
Scope	The range within which a variable name is accessible.
str.format	A method to format a string by substituting values passed by position or by keyword.
Variadic Keyword Argument Unpacking	A mechanism to unpack a mapping with the syntax **mapping into keyword arguments supplied when a function is invoked.
Variadic Keyword Parameter Collection	A category of parameters like **kwargs that captures a variable number of excess keyword arguments in a dictionary.
Variadic Positional Argument Unpacking	A mechanism to unpack an iterable with the syntax *iterable into positional arguments supplied when a function is invoked.
Variadic Positional Parameter Collection	A category of parameters like *args that captures a variable number of excess positional arguments in a tuple.