Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().
Modify the given program to output "foobar" n times.

 

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
 

Constraints:

1 <= n <= 1000





import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_condition = threading.Condition()
        self.bar_condition = threading.Condition()
        self.foo_turn = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.foo_condition:
                while not self.foo_turn:
                    self.foo_condition.wait()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.foo_turn = False
                with self.bar_condition:
                    self.bar_condition.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.bar_condition:
                while self.foo_turn:
                    self.bar_condition.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.foo_turn = True
                with self.foo_condition:
                    self.foo_condition.notify()

