What are the objects in this program?
- Message -> String ("Please enter some coordinates")
- Coordinate -> Float (10.1, 2.55)
- Rectangle -> ? (Not a built-in object, create new class for this)
- Point -> ? (Not a built-in objject, create a new class for this)

Development steps
1. Write down the objects on paper
2. Write a class for each object (ie. custom Point and Rectangle class)
3. Write methods for each class (Add method/function in the class, ie. what a Point/Rectangle can do?)
4. Calling the classes and their methods (Call/Instatiating the class to execute the program)

Creating a class
```python
class Point
    def __init__(self, x, y)
        self.x = x
        self.y = y
```
- It contains at least an init function as it hold the minimum parameter of the object we are creating
- Self in a class is the variable that holds the object instance that is being created by that class

Example of Object Instance
```python
point1 = Point(10,20)
```
- You instatiate the class, from the blueprint (class Point)
- 

Check the type of Object
```python
type(point1)
>> __main__.Point
```

Print the point and integer
```python
print(point1)
>> <__main__.Point object at 0x111c7bb70>
number1 = 1
print(number1)
>> 1
```

