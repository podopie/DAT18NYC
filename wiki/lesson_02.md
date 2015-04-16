# Practice Goals
* Build some basic linear algebra functions
* Improve comfort with flow patterns
* Explore list comprehensions

## Practice: Python Control flow

Here is the common if/else example from lecture. Notice each x and y are False, and the lone "if x/y" statements check to see if they are true.

    x,y = False, False
    if x:
        print 'apple'
    elif y:
        print 'banana'
    else:
        print 'sandwich'


While loops allow iteration until some event happens:

    x = 0
    while True:
        print 'HELLO!'
        x += 1
        if x >= 3:
            break

For loops are more useful going through a predetermined range of things, particularly lists:

    for k in range(4):
        print k

These are all most useful as we combine these things to help filter out information.

    a = [10, 20, 25, 35, 45]
    for value in a:
        if value >= 30:
            print value

(This should all be relatively familiar already given some of the extra work we had done last class)
    

## Practice: Linear Algebra
Primarily let's focus on some of the concrete components we talked about in class

### Matrices and Vectors

For the most part, we can consider using lists to create matrices and vectors (especially given that a Python list is, essentially, a vector)

    vector = [1, 2, 3]
    matrix = [ [1, 2, 3, 4], 
      [5, 6, 7, 8],
      [9, 10, 11, 12] ]


We'll learn more about numpy next week, but numpy makes it incredibly easy to auto generate both of these!

    import numpy as np
    npMatrix = np.matrix('1 2 3; 4 5 6; 7 8 9')

### Math

    vector * 3
    
Note that "common sense" here won't work: we're looking for a way to multiply each value within a vector by a value, not no repeat the vector 3 times. Here, we can use _list comprehensions_ instead:

    [x*3 for x in vector]

And easier, we can write this as a function.

    def vectorMultiply(vector, value):
        return [x*value for x in vector]

(Granted, we could extend the list class… but let's not and say we did)

Can also use list comprehensions to transpose a matrix, which should turn the matrix, essentially, "90 degrees."

    def matrixTranspose(matrix):
         return [ [row[i] for row in matrix] for i in range(len(matrix[0]))]

## Classwork
1. Write two more functions: vectorMatrix multiplication and matrix multiplication. No numpy/scipy! Do this with pure python. Use triple quotes/doc quotes:

        """
        Documentation in Python
        """
    To explain the properties expected for a matrix in these functions.
    Submit this code on Schoology. Check your answers using the logic we went over from lecture. PROGRAMMER GOAL: Write test cases and use try/catch in your functions for when matrices are not defined correctly (ie: [ [1,2,3], [4,5] ] is not a matrix.) Or, create a matrix class that also follows these rules.

2. Write a function that creates an identity matrix. An identity matrix is a matrix where value = 1 if the row and column index are the same, and 0 otherwise. It should build any size identity matrix you want.

        Example: iMatrix(4) should be:
        [ [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1] ]
 
   Post your scripts on Schoology under Classwork 02.

## Homework

Let's revise the original script we wrote on Class01 to now return a new csv file that summarizes the data in such a way:

HEADERS:

    "age", "gender", "signed_in", "avg_click", "avg_impressions", "max_click", "max_impressions"
    
This means that we are now aggregating data by age, gender, and signed_in to get these new data features: avg_click, avg_impressions, max_click, max_impressions.
Let's include Age = 0 (null age) as a possible groupable.

Submit on Schoology using Homework02.

## Extra Links

[Great review on Linear Algebra](http://cs229.stanford.edu/section/cs229-linalg.pdf)

[Early learning on its application to linear models](http://dept.stat.lsa.umich.edu/~kshedden/Courses/Stat401/Notes/401-multreg.pdf)