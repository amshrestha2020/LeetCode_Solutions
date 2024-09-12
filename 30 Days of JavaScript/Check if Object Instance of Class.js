Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods.

There are no constraints on the data types that can be passed to the function. For example, the value or the class could be undefined.

 

Example 1:

Input: func = () => checkIfInstanceOf(new Date(), Date)
Output: true
Explanation: The object returned by the Date constructor is, by definition, an instance of Date.
Example 2:

Input: func = () => { class Animal {}; class Dog extends Animal {}; return checkIfInstanceOf(new Dog(), Animal); }
Output: true
Explanation:
class Animal {};
class Dog extends Animal {};
checkIfInstanceOf(new Dog(), Animal); // true

Dog is a subclass of Animal. Therefore, a Dog object is an instance of both Dog and Animal.
Example 3:

Input: func = () => checkIfInstanceOf(Date, Date)
Output: false
Explanation: A date constructor cannot logically be an instance of itself.
Example 4:

Input: func = () => checkIfInstanceOf(5, Number)
Output: true
Explanation: 5 is a Number. Note that the "instanceof" keyword would return false. However, it is still considered an instance of Number because it accesses the Number methods. For example "toFixed()".



/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    // Ensure classFunction is a function (i.e., a constructor function or class)
    if (typeof classFunction !== 'function') {
        return false;
    }
    
    // Use try-catch to handle cases where obj might not be an object (e.g., undefined, null)
    try {
        // If obj is null or undefined, it can't be an instance of any class
        if (obj == null) {
            return false;
        }

        // Check if obj is an instance of classFunction
        return Object(obj) instanceof classFunction;
    } catch (e) {
        // If there is any error during the check, return false
        return false;
    }
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */