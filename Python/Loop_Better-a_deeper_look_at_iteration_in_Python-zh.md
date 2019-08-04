## 更好的循环：深入了解Python中的迭代

[英文版](<https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/>)

Python中的for循环不像其他语言中的for循环那样运行。在本文中，我们将深入研究Python中的for循环，了解它们是如何工作的，以及它们为什么这样工作。

[TOC]

### 1.循环的错误

让我们从一些错误开始我们的旅程。在了解了Python中的循环的工作方式后，我们将回过头来再看一次这些错误，并解释其中的原因。

#### 错误1: 两次循环

假设我们有一个由数组成的列表和一个生成器，这个生成器会生成数字列表中的数字的平方:

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> squares = (n**2 for n in numbers)
```

我们可以把得到的生成器对象传递给tuple构造函数，使它成为一个元组:

```python
>>> tuple(squares) 
(1, 4, 9, 25, 49) 
```

如果我们将同一个生成器对象传递给sum函数，我们可能会期望得到这些数字的和，即88。

```python
>>> sum(squares)
0
```

然而我们得到的是0.

#### 错误2: 包含检查

让我们采用相同的数字列表和相同的生成器对象：

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> squares = (n**2 for n in numbers) `
```

如果我们询问`9`是否在我们的`square`生成器中，Python会告诉我们9在square中。但是如果我们再次询问同样的问题，Python会告诉我们9不在square中。

```python
>>> 9 in squares True 
>>> 9 in squares False `
```

我们问了同一个问题两次，但是Python却给了我们不同的答案。

#### 错误3: 拆包

下面这个字典有两个键-值对：

```python
>>> counts = {'apples': 2, 'oranges': 1} 
```

让我们用多重赋值来对这个字典进行拆包：

```python
>>> x, y = counts 
```

在对这个字典进行拆包时，你可能期望获得键值对或者得到一个错误。但实际上拆包这个字典并不会报错，而且它并不返回键值对。实际上，对字典拆包只能得到键：

```python
>>> x 'apples' 
```

在我们了解了驱动这些Python代码片段如此运行的逻辑之后，我们将回到这些错误对其进行审视。

### 2.回顾：Python的for循环

Python的for循环和传统的不一样。为了解释这句话，让我们看看另一种编程语言中的for循环。

这是一个用JavaScript编写的传统C语言风格的for循环:

```javascript
let numbers = [1, 2, 3, 5, 7]; 
for (let i = 0; i < numbers.length; i += 1) {
	print(numbers[i]) 
}
```

JavaScript、C、C++、Java、PHP以及许多其他的编程语言都有这种“for”循环。但Python没有。

Python 没有传统的C语言风格的for循环。我们在Python中确实有一个“for”循环，但是它的工作方式类似于[foreach 循环](https://en.wikipedia.org/wiki/Foreach)。下面的才是Python风格的for循环：

```python
numbers = [1, 2, 3, 5, 7] 
for n in numbers:
	print(n) 
```

与传统C风格的for循环不同，Python中的for循环没有**索引变量**。**没有索引初始化、边界检查或索引递增**。在numbers列表循环中，Python的for循环为我们做了所有的工作。

所以虽然Python中有for循环，但我们没有传统的C风格的for循环。我们所谓的for循环的工作方式非常不同。

### 3.定义: 可迭代与序列

上面说明了Python中的“for”循环是无索引的，接下来来看看一些定义。

任何你可以用Python中的for循环来循环的东西都称为**可迭代**的。即可迭代的元素可以循环，任何可以循环的东西都是可迭代的。

```python
for item in some_iterable:     
	print(item) 
```

序列是一种非常常见的可迭代类型。列表、元组和字符串都是序列。

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> coordinates = (4, 5, 7) 
>>> words = "hello there" 
```

序列是具有一些特定特性的迭代器。它们可以从0开始被索引，以比序列长度小1的数结尾，它们有一个长度，并且可以被切片。列表、元组、字符串和所有其他的序列都是如此。

```python
>>> numbers[0]
1 
>>> coordinates[2]
7 
>>> words[4]
'o' `
```

Python中的很多东西都是可迭代的，但**并不是所有的可迭代元素都是序列**。集合、字典、文件和生成器也是可迭代的，但它们都不是序列。

```
>>> my_set = {1, 2, 3} 
>>> my_dict = {'k1': 'v1', 'k2': 'v2'} 
>>> my_file = open('some_file.txt') 
>>> squares = (n**2 for n in my_set) `
```

所以任何可以用for循环来循环的东西都是可迭代的，序列是可迭代的一种，但是Python也有很多其他类型的可迭代元素。

### 4.Python的for循环不使用索引

你可能认为Python的for循环底层还是使用索引来循环。这里我们使用一个while循环和索引来手动循环一个可迭代元素：

```python
numbers = [1, 2, 3, 5, 7] 
i = 0 
while i < len(numbers):
	print(numbers[i])    
	i += 1 
```

这个适用于列表，但并不能适用于所有。这种循环的方法只适用于序列。

如果我们试图使用索引来手动循环一个集合，我们会得到一个错误:

```python
>>> fruits = {'lemon', 'apple', 'orange', 'watermelon'} 
>>> i = 0 
>>> while i < len(fruits): 
...     print(fruits[i]) 
...     i += 1 
... 
Traceback (most recent call last): 
File "<stdin>", line 2, in <module> 
TypeError: 'set' object does not support indexing
```

集合不是序列，因此不支持索引。我们不能通过使用索引来手动循环Python中的所有迭代器。这对于非序列的迭代器根本不起作用。

### 5.迭代器给for循环提供动力

因此，我们已经看到Python的for 循环并非在底层使用索引。相反，Python的for循环使用**迭代器**。

迭代器是支持可迭代的东西。您可以从任意可迭代的东西中获得一个迭代器。你也可以使用一个迭代器来手动循环它所来自的可迭代元素。让我们看看它是如何工作的。这里有三个可迭代类:集合、元组和字符串。

```python
>>> numbers = {1, 2, 3, 5, 7} 
>>> coordinates = (4, 5, 7) 
>>> words = "hello there" 
```

将一个可迭代元素传递给Python中内置的iter函数，总会返回一个迭代器，不管我们使用的是哪种类型的可迭代元素。

```python
>>> iter(numbers) 
<set_iterator object at 0x7f2b9271c860> 
>>> iter(coordinates)
<tuple_iterator object at 0x7f2b9271ce80>
>>> iter(words) 
<str_iterator object at 0x7f2b9271c860> `
```

一旦我们有了一个迭代器，我们可以用它做的一件事就是将它传递给内置的next函数来获得它的下一项。

```python
>>> numbers = [1, 2, 3] 
>>> my_iterator = iter(numbers) 
>>> next(my_iterator)
1
>>> next(my_iterator) 
2
```

迭代器是有状态的，这意味着一旦你使用了其中的一个项，这个项就会消失。

如果你向迭代器请求“next”项，但是没有更多的项，就会得到一个`StopIteration`异常:

```python
>>> next(iterator) 
3 
>>> next(iterator) 
Traceback (most recent call last):   
File "<stdin>", line 1, in <module> StopIteration `
```

所以你可以从每个可迭代元素中得到一个迭代器。**使用迭代器唯一能做的就是使用“next”函数询问它们的下一项**。如果将迭代器传递给“next”，但迭代器没有下一项，则会引发一个`StopIteration`异常。

### 6.没有for循环的循环

既然我们已经了解了迭代器和“iter”、“next”函数，我们将尝试在一个迭代器上手动循环，而不使用“for”循环。

我们将尝试把下面这个for循环变成while循环:

```python
def funky_for_loop(iterable, action_to_do):     
	for item in iterable:         
		action_to_do(item) `
```

为此，我们将:

1. 从给定的可迭代元素中获取一个迭代器
2. 重复地从迭代器中获取下一项
3. 如果我们成功地获得下一项，则执行原先在for循环中的代码
4. 如果在获取下一项时出现了`StopIteration`异常，则停止循环

```Python
def funky_for_loop(iterable, action_to_do):     
	iterator = iter(iterable)     
	done_looping = False     
	while not done_looping:         
        try:             
            item = next(iterator)         
        except StopIteration:             
            done_looping = True         
        else:             
            action_to_do(item) `
```

我们刚刚通过使用while循环和迭代器重新实现了一个for循环。上面的代码基本上定义了Python中的循环底层的运行方式。如果你理解了内置的“iter”和“next”函数用于循环的方式，那么你就理解了Python的for循环是如何工作的。实际上，你将不仅仅理解Python中“for”循环是如何工作的。在可迭代元素上的所有的迭代都是这样工作的。

**迭代器协议**是“在Python中迭代器是如何工作的”的一种精致的说法。它本质上就是Python中“iter”和“next”函数工作方式的定义。Python中所有形式的迭代都由迭代器协议提供支持。

“for”循环使用迭代器协议(正如我们已经看到的):

```python
for n in numbers:     
	print(n) 
```

多重赋值也使用迭代器协议:

```python
x, y, z = coordinates
```

星型表达式使用迭代器协议:

```python
a, b, *rest = numbers 
print(*numbers)
```

许多内置函数都依赖于迭代器协议：

```python
unique_numbers = set(numbers)
```

在Python中，任何一个与可迭代元素一起工作的东西都可能以某种方式使用迭代器协议，任何时候循环一个可迭代元素也都依赖于迭代器协议。

### 7.生成器是迭代器

因此，你可能会想: 迭代器看起来很酷，但它们看起来也只是一个实现的细节，作为Python的用户，我们可能不需要关心它们。但实际上，在Python中直接使用迭代器是非常常见的。

下面的 `squares` 对象就是一个迭代器：

```python
>>> numbers = [1, 2, 3] 
>>> squares = (n**2 for n in numbers)
```

生成器是迭代器，这意味着你可以在生成器上调用“next”来获得它的下一项:

```python
>>> next(squares) 
1 
>>> next(squares) 
4 
```

但是如果你以前使用过生成器，你可能知道你也可以在生成器上进行循环:

```python
>>> squares = (n**2 for n in numbers) 
>>> for n in squares: 
...     print(n) 
... 
1 4 9
```

在Python中，如果你可以在某个东西上进行循环，那么它就是一个**可迭代的**元素。

所以**生成器是迭代器**，但是生成器也是可迭代的。这是怎么回事?

### 8.我骗了你

实际上，当我在前面解释迭代器如何工作时，我跳过了关于它们的一个重要细节，那就是：**迭代器也是可迭代的**。再重复一次：在Python中的任何一个迭代器也都是可迭代的，这意味着你可以在迭代器上进行循环。

因为迭代器也是可迭代的，所以可以使用内置的“iter”函数从一个迭代器中获得一个迭代器:

```python
>>> numbers = [1, 2, 3] 
>>> iterator1 = iter(numbers) 
>>> iterator2 = iter(iterator1) 
```

记住，当我们对可迭代元素调用iter函数时，可迭代元素会给我们一个迭代器。而当我们对迭代器调用iter函数时，会返回迭代器本身。

```python
>>> iterator1 is iterator2 
True
```

迭代器是可迭代的，所有迭代器都是它们自己的迭代器。

```python
def is_iterator(iterable):     
	return iter(iterable) is iterable `
```

困惑了吗?让我们重述一下这些术语。

1. 一个可迭代元素是你能够迭代的东西。
2. 一个迭代器是在可迭代元素上实际执行迭代的一个代理。
3. 此外，在Python中迭代器也是可迭代的，它们充当“自己的”迭代器。
4. 所以迭代器是可迭代的，但是它们没有一些在某些可迭代元素上所具有的特性。
5. 迭代器没有长度，不能被索引。

```python
>>> numbers = [1, 2, 3, 5, 7]
>>> iterator = iter(numbers) 
>>> len(iterator) 
TypeError: object of type 'list_iterator' has no len() 
>>> iterator[0] 
TypeError: 'list_iterator' object is not subscriptable `
```

从Python程序员的角度来看，你能用迭代器做的唯一有用的事情就是把它传递给内置的“next”函数，或者循环它:

```python
>>> next(iterator) 
1 
>>> list(iterator) 
[2, 3, 5, 7] `
```

如果我们对迭代器进行第二次循环，我们将一无所获:

```python
>>> list(iterator) 
[]
```

你可以认为迭代器是**惰性可迭代元素**，即它们是**单次使用的**，这意味着它们只能循环一次。

|  Object   | Iterable? | Iterator? |
| :-------: | :-------: | :-------: |
| Iterable  |     ✔️     |     ❓     |
| Iterator  |     ✔️     |     ✔️     |
| Generator |     ✔️     |     ✔️     |
|   List    |     ✔️     |     ❌     |

正如你在上面的真值表中所看到的，可迭代元素并不总是迭代器，但是迭代器总是可迭代元素。

### 9.完整的迭代器协议

让我们从Python的角度定义迭代器是如何工作的。

**可迭代元素**可以被传递给“iter”函数并从中获得一个迭代器。

**迭代器**:

1. 可以传递给next函数，该函数将给出它们的下一个项。如果下一个项不存在，将引发`StopIteration`异常。
2. 可以传递给iter函数并将自己返回。

这些说法反过来也成立:

1. 任何可以传递给“iter”而没有“TypeError”的东西都是可迭代的

2. 任何可以传递给“next”而没有“TypeError”的东西都是迭代器
3. 任何传递给“iter”时返回自身的东西都是迭代器

这就是Python中的迭代器协议。

### 10.迭代器使得惰性成为可能

迭代器允许我们使用和创建**惰性可迭代**元素，在我们向它们询问下一项之前，它们不做任何工作。因为我们可以创建惰性可迭代元素，所以我们可以创建一个无限长的可迭代器。同时我们可以创建对系统资源比较节约的可迭代元素，这样可以节省内存和CPU时间。

### 11.迭代器无处不在

你已经在Python中看到了很多迭代器。前面也已经提到生成器是迭代器。Python的许多内置类也是迭代器。例如，Python的' enumerate '和' reverse '对象是迭代器。

```python
>>> letters = ['a', 'b', 'c'] 
>>> e = enumerate(letters) 
>>> e 
<enumerate object at 0x7f112b0e6510>
>>> next(e)
(0, 'a') `
```

在Python 3中, `zip`, `map`, 和 `filter` 对象也都是迭代器。

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> letters = ['a', 'b', 'c'] 
>>> z = zip(numbers, letters) 
>>> z 
<zip object at 0x7f112cc6ce48> 
>>> next(z) 
(1, 'a') `
```

Python中的文件对象也是迭代器。

```python
>>> next(open('hello.txt')) 
'hello world\n' `
```

在标准库和第三方Python库中都有大量的迭代器。这些迭代器都像惰性可迭代元素一样，将工作延迟到你向它们询问下一个项的时候。

### 12.创建你自己的迭代器

了解迭代器是很有用的，但是还需要了解如何创建自己的迭代器和惰性可迭代元素。

下面这个类生成一个迭代器，该迭代器接受一个数字的可迭代元素，并在循环时产生每个数字的平方。

```python
class square_all:     
	def __init__(self, numbers):         
		self.numbers = iter(numbers)     
	def __next__(self):
    	return next(self.numbers) ** 2     
    def __iter__(self):         
    	return self
```

但是，在我们开始循环该类的实例之前，它不会做任何工作。

下面我们有一个无限长的可迭代元素' count '，你可以看到' square_all '可以接收' count '，而不需要完全循环这个无限长的可迭代元素:

```python
>>> from itertools import count 
>>> numbers = count(5) 
>>> squares = square_all(numbers) 
>>> next(squares) 
25 
>>> next(squares) 
36 
```

这个迭代器类可以工作，但是我们通常不这样设置迭代器。当我们想要一个自定义迭代器时，我们做一个生成器函数:

```python
def square_all(numbers):
	for n in numbers:
    	yield n**2 `
```

这个生成器函数等价于上面的类，两者的工作原理基本相同。“yield”语句可能看起来很神奇，但它非常强大: “yield”允许我们在两个“next”函数的调用之间暂停生成器函数。“yield”语句将生成器函数与常规函数分开。

另一种实现相同的迭代器的方法是使用生成器表达式。

```python
def square_all(numbers):     
	return (n**2 for n in numbers) `
```

它的作用与生成器函数的作用相同，但是它使用的语法看起来像列表推断。如果你需要在代码中实现一个延迟可迭代元素或者说惰性可迭代元素，可以考虑使用迭代器，并考虑创建生成器函数或生成器表达式。

### 13.迭代器如何改进代码

一旦你接受了在代码中使用惰性可迭代元素的想法，你就会发现有很多可能性来创建帮助函数，这些帮助函数可以帮助你遍历可迭代元素并处理数据。

#### 惰性与求和

这是一个for循环，它累加了在一个Django queryset中的所有需要计费的小时:

```python
hours_worked = 0 
for event in events:     
	if event.is_billable():         
		hours_worked += event.duration `
```

下面的代码使用生成器表达式来执行相同的操作，但是可以做到延迟计算:

```python
billable_times = (     
	event.duration     
	for event in events     
	if event.is_billable() 
)
hours_worked = sum(billable_times) `
```

注意，我们的代码的形状已经发生了巨大的变化。将我们的计费时间转换为一个惰性的可迭代元素，这允许我们命名一些之前未命名的东西(' billable_times ')，同时也允许我们使用“sum”函数。我们之前不能用sum因为我们甚至没有一个可迭代元素传递给它。迭代器允许你从根本上改变代码的结构。

#### 惰性和打破循环

下面这段代码打印日志文件的前十行:

```python
for i, line in enumerate(log_file):
	if i >= 10:
    	break
    print(line) 
```

这段代码做的是同一件事，但当我们循环时，使用了“itertools.islice”函数来惰性抓取文件的前10行:

```python
from itertools import islice  
first_ten_lines = islice(log_file, 10) 
for line in first_ten_lines:    
	print(line) `
```

我们创建的' first_ten_lines '变量是一个迭代器。再次使用迭代器允许我们为之前未命名的东西(前十行)命名。命名可以使我们的代码更具描述性和可读性。

另外，在新的循环中不需要“break”语句，因为“islice”函数为我们来处理breaking。你可以在标准库中的[itertools](https://docs.python.org/3/library/itertools.html)以及第三方库中找到更多的迭代助手函数。

#### 创建你自己的迭代助手

您可以在标准库和第三方库中找到用于循环的帮助函数，但是您也可以创建自己的帮助函数!

下面这段代码创建一个序列中连续值之间的差异的列表，。

```python
current = readings[0] 
for next_item in readings[1:]:     
	differences.append(next_item - current)     
	current = next_item
```

注意，这段代码有一个额外的变量，我们需要在每次循环时分配它。此外还要注意，这段代码只适用于可以进行切片的东西，比如序列。如果“readings”是一个生成器、一个zip对象或任何其他类型的迭代器，则此代码将失效。

让我们编写一个helper函数来完善代码。

下面的是一个生成器函数，它为我们提供了当前项，并在所给定的可迭代元素中的每个项提供了它们的下一个项:

```python
def with_next(iterable):
    """Yield (current, next_item) tuples for each item in iterable."""     
    iterator = iter(iterable)     
    current = next(iterator)     
    for next_item in iterator:         
        yield current, next_item         
        current = next_item `
```

我们从可迭代元素中手动获取一个迭代器，在其上调用' next '来获取第一项，然后在迭代器上循环以获取所有后续的项，同时一路跟踪后一个项。这个函数不仅适用于序列，而且适用于任何类型的可迭代元素。

下面的代码作用相同，但我们使用helper函数with_next，而不是手动跟踪' next_item ':

```python
differences = [] 
for current, next_item in with_next(readings):     
	differences.append(next_item - current) 
```

注意，这段代码并没有给循环中的“next_item”进行赋值。“with_next”生成器函数为我们处理跟踪“next_item”的工作。需要注意的是，这段代码已经足够紧凑，如果我们愿意，甚至可以放到一个列表推导式里面去：

```python
differences = [ 
    (next_item - current)     
    for current, next_item in with_next(readings) 
] 
```

### 14.循环中的错误：重新审视

现在回到第一节，看看这些错误里面发生了什么。

#### 错误1: 耗尽一个迭代器

这里我们有一个生成器对象 `squares`:

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> squares = (n**2 for n in numbers) 
```

如果我们把这个生成器传递给' tuple '构造函数，我们会得到一个元组:

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> squares = (n**2 for n in numbers) 
>>> tuple(squares) 
(1, 4, 9, 25, 49) `
```

如果我们对这个生成器用sum求和，我们将会得到0：

```python
>>> sum(squares) 
0
```

这是因为这个生成器现在是空的，我们已经消耗完了。如果我们再试着创建一个元组，我们会得到一个空的元组:

```python
>>> tuple(squares) 
() 
```

生成器是迭代器，**迭代器是单次使用的可迭代元素**。

#### 错误2: 部分消耗一个迭代器

同样，我们有一个生成器对象, `squares`:

```python
>>> numbers = [1, 2, 3, 5, 7] 
>>> squares = (n**2 for n in numbers) 
```

如果我们问“9”是否在这个“square”生成器中，我们会得到“True”:

```python
>>> 9 in squares 
True 
```

但是如果同样的问题我们再问一次，将会得到“False”:

```python
>>> 9 in squares 
False 
```

当我们询问‘9’是否在这个生成器中时，Python必须遍历这个生成器才能找到‘9’。

如果我们在找到“9”之后继续循环，我们只会得到最后两个数字，因为我们在这之前已经使用了前面的数字:

```
>>> numbers = [1, 2, 3, 5, 7] 
>>> squares = (n**2 for n in numbers) 
>>> 9 in squares 
True
>>> list(squares) 
[25, 49]
```

询问某个东西是否“包含”在迭代器中，会部分地消耗迭代器。因为如果不开始循环，就无法知道某个东西是否在迭代器中。

#### 错误3: 拆包也是迭代

当你在一个字典上进行循环时，会得到键：

```python
>>> counts = {'apples': 2, 'oranges': 1} 
>>> for key in counts: 
...     print(key) 
... 
apples oranges 
```

当你打开字典的时候，你也会得到键:

```python
>>> x, y = counts 
>>> x, y 
('apples', 'oranges') `
```

循环依赖于迭代器协议。可迭代拆包也依赖于迭代器协议。打开字典实际上与遍历字典是一样的。两者都使用迭代器协议，所以在这两种情况下得到了相同的结果。

### 15.概述

序列是可迭代的，但不是所有的可迭代元素都是序列。当有人说“可迭代”这个词时，你只能假设他们的意思是“可以迭代的东西”，而不要假设它可以循环两次、可以询问它的长度或者认定它已经被索引了。

迭代器是Python中最基本的可迭代元素的形式。如果你想在代码中创建一个惰性可迭代元素，请考虑使用迭代器，并考虑创建一个生成器函数或一个生成器表达式。

最后，请记住Python中的每种迭代类型都依赖于迭代器协议，因此理解迭代器协议是理解Python中循环的关键。