## 编程问题的14种基本模式

### 1. 滑动窗口

滑动窗口模式是用于在给定数组或链表的特定窗口大小上执行所需的操作，比如寻找包含所有 1 的最长子数组。从第一个元素开始滑动窗口并逐个元素地向右滑，并根据你所求解的问题调整窗口的长度。在某些情况下窗口大小会保持恒定，在其它情况下窗口大小会增大或减小。

下面是一些你可以用来确定给定问题可能需要滑动窗口的方法：

- 问题的输入是一种线性数据结构，比如链表、数组或字符串
- 你被要求查找最长/最短的子字符串、子数组或所需的值

你可以使用滑动窗口模式处理的常见问题：

- 大小为 K 的子数组的最大和（简单）
- 带有 K 个不同字符的最长子字符串（中等）
- 寻找字符相同但排序不一样的字符串（困难）

### 2. 双指针或迭代器

双指针（Two Pointers）是这样一种模式：两个指针以一前一后的模式在数据结构中迭代，直到一个或两个指针达到某种特定条件。二指针通常在排序数组或链表中搜索配对时很有用；比如当你必须将一个数组的每个元素与其它元素做比较时。

双指针是很有用的，因为如果只有一个指针，你必须继续在数组中循环回来才能找到答案。这种使用单个迭代器进行来回在时间和空间复杂度上都很低效——这个概念被称为「渐进分析（asymptotic analysis）」。尽管使用 1 个指针进行暴力搜索或简单普通的解决方案也有效果，但这会沿 O(n²) 线得到一些东西。在很多情况中，二指针有助于你寻找有更好空间或运行时间复杂度的解决方案。

用于识别使用双指针的时机的方法：

- 可用于你要处理排序数组（或链接列表）并需要查找满足某些约束的一组元素的问题
- 数组中的元素集是配对、三元组甚至子数组

下面是一些满足双指针模式的问题：

- 求一个排序数组的平方（简单）
- 求总和为零的三元组（中等）
- 比较包含回退（backspace）的字符串（中等）

### 3. 快速和慢速指针或迭代器

快速和慢速指针方法也被称为 Hare & Tortoise 算法，该算法会使用两个在数组（或序列/链表）中以不同速度移动的指针。该方法在处理循环链表或数组时非常有用。

通过以不同的速度进行移动（比如在一个循环链表中），该算法证明这两个指针注定会相遇。只要这两个指针在同一个循环中，快速指针就会追赶上慢速指针。

如何判别使用快速和慢速模式的时机？

- 处理链表或数组中的循环的问题
- 当你需要知道特定元素的位置或链表的总长度时

何时应该优先选择这种方法，而不是上面提到的二指针方法？

- 有些情况不适合使用二指针方法，比如在不能反向移动的单链接链表中。使用快速和慢速模式的一个案例是当你想要确定一个链表是否为回文（palindrome）时。

下面是一些满足快速和慢速指针模式的问题：

- 链表循环（简单）
- 回文链表（中等）
- 环形数组中的循环（困难）

### 4. 合并区间

合并区间模式是一种处理重叠区间的有效技术。在很多涉及区间的问题中，你既需要找到重叠的区间，也需要在这些区间重叠时合并它们。该模式的工作方式为：

给定两个区间（a 和 b），这两个区间有 6 种不同的互相关联的方式：

理解并识别这六种情况有助于你求解范围广泛的问题，从插入区间到优化区间合并等。

那么如何确定何时该使用合并区间模式呢？

- 如果你被要求得到一个仅含互斥区间的列表
- 如果你听到了术语「重叠区间（overlapping intervals）」

合并区间模式的问题：

- 区间交叉（中等）
- 最大 CPU 负载（困难

### 5. 循环排序

这一模式描述了一种有趣的方法，处理的是涉及包含给定范围内数值的数组的问题。循环排序模式一次会在数组上迭代一个数值，如果所迭代的当前数值不在正确的索引处，就将其与其正确索引处的数值交换。你可以尝试替换其正确索引处的数值，但这会带来 O(n^2) 的复杂度，这不是最优的，因此要用循环排序模式。

如何识别这种模式？

- 涉及数值在给定范围内的排序数组的问题
- 如果问题要求你在一个排序/旋转的数组中找到缺失值/重复值/最小值

循环排序模式的问题：

- 找到缺失值（简单）
- 找到最小的缺失的正数值（中等）

### 6. 原地反转链表

在很多问题中，你可能会被要求反转一个链表中一组节点之间的链接。通常而言，你需要原地完成这一任务，即使用已有的节点对象且不占用额外的内存。这就是这个模式的用武之地。该模式会从一个指向链表头的变量（current）开始一次反转一个节点，然后一个变量（previous）将指向已经处理过的前一个节点。以锁步的方式，在移动到下一个节点之前将其指向前一个节点，可实现对当前节点的反转。另外，也将更新变量「previous」，使其总是指向已经处理过的前一个节点。

如何识别使用该模式的时机：

- 如果你被要求在不使用额外内存的前提下反转一个链表

原地反转链表模式的问题：

- 反转一个子列表（中等）
- 反转每个 K 个元素的子列表（中等）

### 7. 树的宽度优先搜索（Tree BFS）

该模式基于宽度优先搜索（BFS）技术，可遍历一个树并使用一个队列来跟踪一个层级的所有节点，之后再跳转到下一个层级。任何涉及到以逐层级方式遍历树的问题都可以使用这种方法有效解决。

Tree BFS 模式的工作方式是：将根节点推至队列，然后连续迭代知道队列为空。在每次迭代中，我们移除队列头部的节点并「访问」该节点。在移除了队列中的每个节点之后，我们还将其所有子节点插入到队列中。

如何识别 Tree BFS 模式：

- 如果你被要求以逐层级方式遍历（或按层级顺序遍历）一个树

Tree BFS 模式的问题：

- 二叉树层级顺序遍历（简单）
- 之字型遍历（Zigzag Traversal）（中等）

### 8. 树的深度优先搜索（Tree DFS）

Tree DFS 是基于深度优先搜索（DFS）技术来遍历树。

你可以使用递归（或该迭代方法的技术栈）来在遍历期间保持对所有之前的（父）节点的跟踪。

Tree DFS 模式的工作方式是从树的根部开始，如果这个节点不是一个叶节点，则需要做三件事：

1．决定现在是处理当前的节点（pre-order），或是在处理两个子节点之间（in-order），还是在处理两个子节点之后（post-order）

1. 为当前节点的两个子节点执行两次递归调用以处理它们

如何识别 Tree DFS 模式：

- 如果你被要求用 in-order、pre-order 或 post-order DFS 来遍历一个树
- 如果问题需要搜索其中节点更接近叶节点的东西

Tree DFS 模式的问题：

- 路径数量之和（中等）
- 一个和的所有路径（中等）

### 9. Two Heaps

在很多问题中，我们要将给定的一组元素分为两部分。为了求解这个问题，我们感兴趣的是了解一部分的最小元素以及另一部分的最大元素。这一模式是求解这类问题的一种有效方法。该模式要使用两个堆（heap）：一个用于寻找最小元素的 Min Heap 和一个用于寻找最大元素的 Max Heap。该模式的工作方式是：先将前一半的数值存储到 Max Heap，这是由于你要寻找前一半中的最大数值。然后再将另一半存储到 Min Heap，因为你要寻找第二半的最小数值。在任何时候，当前数值列表的中间值都可以根据这两个 heap 的顶部元素计算得到。

识别 Two Heaps 模式的方法：

- 在优先级队列、调度等场景中有用
- 如果问题说你需要找到一个集合的最小/最大/中间元素
- 有时候可用于具有二叉树数据结构的问题

Two Heaps 模式的问题：

- 查找一个数值流的中间值（中等）

### 10. 子集

很多编程面试问题都涉及到处理给定元素集合的排列和组合。子集（Subsets）模式描述了一种用于有效处理所有这些问题的宽度优先搜索（BFS）方法。

该模式看起来是这样：

给定一个集合 [1, 5, 3]

1． 从一个空集开始：[[]]
2．向所有已有子集添加第一个数 (1)，从而创造新的子集：[[], [1]]
3．向所有已有子集添加第二个数 (5)：[[], [1], [5], [1,5]]
4．向所有已有子集添加第三个数 (3)：[[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]]

如何识别子集模式：

- 你需要找到给定集合的组合或排列的问题

子集模式的问题：

- 带有重复项的子集（简单）
- 通过改变大小写的字符串排列（中等）

### 11. 经过修改的二叉搜索

只要给定了排序数组、链表或矩阵，并要求寻找一个特定元素，你可以使用的最佳算法就是二叉搜索。这一模式描述了一种用于处理所有涉及二叉搜索的问题的有效方法。

对于一个升序的集合，该模式看起来是这样的：

1．首先，找到起点和终点的中间位置。寻找中间位置的一种简单方法是：middle = (start + end) / 2。但这很有可能造成整数溢出，所以推荐你这样表示中间位置：middle = start + (end — start) / 2。
2．如果键值（key）等于中间索引处的值，那么返回这个中间位置。
3．如果键值不等于中间索引处的值：
4．检查 key < arr[middle] 是否成立。如果成立，将搜索约简到 end = middle — 1 5．检查 key > arr[middle] 是否成立。如果成立，将搜索约简到 end = middle + 1

下面给出了这种经过修改的二叉搜索模式的视觉表示：

经过修改的二叉搜索模式的问题：

- 与顺序无关的二叉搜索（简单）
- 在经过排序的无限数组中搜索（中等）

### 12. Top K

任何要求我们找到一个给定集合中前面的/最小的/最常出现的 K 的元素的问题都在这一模式的范围内。

跟踪 K 个元素的最佳的数据结构是 Heap。这一模式会使用 Heap 来求解多个一次性处理一个给定元素集中 K 个元素的问题。该模式是这样工作的：

1． 根据问题的不同，将 K 个元素插入到 min-heap 或 max-heap 中
2．迭代处理剩余的数，如果你找到一个比 heap 中数更大的数，那么就移除那个数并插入这个更大的数

这里无需排序算法，因为 heap 将为你跟踪这些元素。

如何识别前 K 个元素模式：

- 如果你被要求寻找一个给定集合中前面的/最小的/最常出现的 K 的元素
- 如果你被要求对一个数值进行排序以找到一个确定元素

前 K 个元素模式的问题：

- 前面的 K 个数（简单）
- 最常出现的 K 个数（中等）

### 13. K 路合并

K 路合并能帮助你求解涉及一组经过排序的数组的问题。

当你被给出了 K 个经过排序的数组时，你可以使用 Heap 来有效地执行所有数组的所有元素的排序遍历。你可以将每个数组的最小元素推送至 Min Heap 以获得整体最小值。在获得了整体最小值后，将来自同一个数组的下一个元素推送至 heap。然后，重复这一过程以得到所有元素的排序遍历结果。

该模式看起来像这样：

1．将每个数组的第一个元素插入 Min Heap
2．之后，从该 Heap 取出最小（顶部的）元素，将其加入到合并的列表。
3．在从 Heap 移除了最小的元素之后，将同一列表的下一个元素插入该 Heap
4．重复步骤 2 和 3，以排序的顺序填充合并的列表

如何识别 K 路合并模式：

- 具有排序数组、列表或矩阵的问题
- 如果问题要求你合并排序的列表，找到一个排序列表中的最小元素

K 路合并模式的问题：

- 合并 K 个排序的列表（中等）
- 找到和最大的 K 个配对（困难）



### 14. 拓扑排序

拓扑排序可用于寻找互相依赖的元素的线性顺序。比如，如果事件 B 依赖于事件 A，那么 A 在拓扑排序时位于 B 之前。

这个模式定义了一种简单方法来理解执行一组元素的拓扑排序的技术。

该模式看起来是这样的：

1．初始化。a）使用 HashMap 将图（graph）存储到邻接的列表中；b）为了查找所有源，使用 HashMap 记录 in-degree 的数量
2．构建图并找到所有顶点的 in-degree。a）根据输入构建图并填充 in-degree HashMap
3．寻找所有的源。a）所有 in-degree 为 0 的顶点都是源，并会被存入一个队列
4．排序。a）对于每个源，执行以下操作：i）将其加入到排序的列表；ii）根据图获取其所有子节点；iii）将每个子节点的 in-degree 减少 1；iv）如果一个子节点的 in-degree 变为 0，将其加入到源队列。b）重复 (a)，直到源队列为空。

如何识别拓扑排序模式：

- 处理无向有环图的问题
- 如果你被要求以排序顺序更新所有对象
- 如果你有一类遵循特定顺序的对象

拓扑排序模式的问题：

- 任务调度（中等）
- 一个树的最小高度



## 基本排序算法

可以参考： https://www.cnblogs.com/onepixel/articles/7674659.html

https://github.com/TheAlgorithms/Python

```python
list_original = [1, 3, 4, 5, 6, 3, 4, 5, 7, 0, 9, 33,8,10,2,11,17]
```



### 1. 冒泡排序

1.比较相邻的两个元素，如果第一个比第二个大，就交换。

2.比较每一对相邻元素，这样在最后的那个元素就应该是最大的元素

3.针对所有元素重复以上步骤，除了最后一个元素。

4.重复1-3步骤，直到排序完成

```python
def bubble_sort(input_list):
    length = len(input_list)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if input_list[j] > input_list[j + 1]:  # 如果前者比后者大，则交换
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

print('bubble_sort:',bubble_sort(list_original))
```



### 2. 选择排序

1.初始状态为R[1..n],有序区为空

2.第i趟排序(i=1,2,3,..,n-1)开始时，当前有序区和无序区分别为R[1,..,i-1]和R[i,..,n],该趟排序从当前的无序区中选出关键字最小的记录R[k],

将其与无序区中的第i个记录R交换，使得R[1,..,i]和R[i+1,..,n]分别变为记录个数增加一个的新有序区和记录个数减少一个的新无序区。

3.n-1趟结束时，数组有序化了

简单来说，就是在无序区域中不断选择最小的数，然后放到有序区域的最后面，有序区越来越大，无序区域越来越小，从而实现从小到大排序

```python
def selection_sort(input_list):
    length = len(input_list)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if input_list[j] < input_list[min_index]:  # 寻找无序区中最小的值
                min_index = j                          # 将最小的值进行索引
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list

print('selection_sort:',selection_sort(list_original))
```



### 3. 插入排序

1.从第一个元素开始，认为该元素已经排好了序

2.取出下一个元素，在已经排序的序列中从后往前扫描

3.如果该元素(已排序)大于新元素，将该元素移到下一位置

4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置

5.将新元素插入到该位置后

6.重复步骤2~5

插入排序在实现上通常采用in-place操作，即只需用到O(1)的额外空间，因而在从后往前扫描过程中，需要反复把已排序元素逐渐向后挪位，为最新元素提供插入空间

```python
def insertion_sort(input_list):
    length = len(input_list)
    for i in range(1,length-1):
        pre_index = i-1
        current = input_list[i]
        while pre_index >= 0 and input_list[pre_index] > current:
            input_list[pre_index+1] = input_list[pre_index]
            pre_index -= 1
        input_list[pre_index+1] = current
    return input_list

print('insertion_sort:',insertion_sort(list_original))
```



### 4. 希尔排序

亦称为递减增量排序算法。将整个待排序的序列分割成为若干子序列分别进行直接插入排序，具体算法描述为：

1.选择一个增量序列t1,t2,...,tk,

2.按增量序列个数k,对序列进行k趟排序

3.每趟排序，根据对应的增量ti,将待排序的学列分割成若干长度为m的子序列，分别对各子表进行直接插入排序。

增量为1时，将整个序列作为一个表来处理，表的长度即为整个序列的长度

```python
def shell_sort(input_list):
    length = len(input_list)
    gaps,gap = [],1
    while gap<length/3:
        gaps += [gap*3+1]
        gap *= 3
    for gap in gaps:
        i = gap
        while i < length:
            temp = input_list[i]
            j = i
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j -= gap
            input_list[j] = temp
            i += 1
    return input_list

print('shell_sort:',shell_sort(list_original))
```



### 5. 归并排序

建立在归并操作上的算法，采用了分治法(Divide and Conquer),将已经有序的子序列进行合并，得到完全有序的序列。

1.将长度为n的输入序列分成两个长度为n/2的子序列

2.对这两个子序列分别采用归并排序

3.将两个排序好的子序列合并成也给最终的有序序列

```python
def merge_sort(input_list):
    length = len(input_list)
    if length>1:
        middle = length//2
        left_half = merge_sort(input_list[:middle])
        right_half = merge_sort(input_list[middle:])
        i,j,k = 0,0,0
        left_length = len(left_half)
        right_length = len(right_half)
        while i<left_length and j<right_length:
            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i += 1
            else:
                input_list[k] = right_half[j]
                j += 1
            k += 1
        while i < left_length:
            input_list[k] = left_half[i]
            i += 1
            k += 1
        while j < right_length:
            input_list[k] = right_half[j]
            j += 1
            k += 1
    return input_list

print('merge_sort:',merge_sort(list_original))
```

或者将以上拆分为两个函数，更简单：

```python
def mergeSort(input_list):
    if len(input_list)<2:
        return input_list
    middle = len(input_list)//2
    left,right = input_list[:middle],input_list[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result=[]
    while left and right:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
```



### 6. 快速排序

快速排序的基本思想是通过一趟排序将待排记录分割成独立的两个部分，其中一部分记录的关键字比另一部分的关键字小，则可分别对这两部分记录继续进行排序

1.从序列中挑选一个元素，称为"基准"(pivot):

2.重新排序，所有元素比基准值小的放在基准的前面，所有元素比基准大的放在后面，相同的数可以放在任意一边。此操作称为分区(partition)操作

3.递归(recursive)地把小于基准值元素地子序列和大于基准值元素地子序列排序

```python
def quick_sort(input_list):
    length = len(input_list)
    if length <= 1:
        return input_list
    else:
        pivot = input_list[0]
        greater = [element for element in input_list[1:] if element>pivot]
        lesser = [element for element in input_list[1:] if element<=pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

print('quick_sort:',quick_sort(list_original))
```



### 7.  堆排序

堆排序是指利用堆这种数据结构进行排序地算法，堆积是一个类似于完全二叉树地结构，并同时满足堆积的性质，即子节点的键值或索引总是小于(或大于)其父节点

1.将初始待排关键字序列(R1,R2,...,Rn)构建成大顶堆，此堆为初始的无序区

2.将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,...,Rn-1)和新的有序区(Rn)，且满足R[1,2,...,n-1]<=R[n]

3.由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前的无序区(R1,R2,...,Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，

得到新的无序区(R1,R2,...,Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

```python
def heap_helper(input_list,index,heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and input_list[left_index] > input_list[largest]:
        largest = left_index
    if right_index < heap_size and input_list[right_index] > input_list[largest]:
    	largest = right_index
    if largest != index:
    	input_list[largest], input_list[index] = input_list[index], input_list[largest]
    	heap_helper(input_list, largest, heap_size)




def heap_sort(input_list):
    length = len(input_list)
    for i in range(length //2 -1,-1,-1):
        heap_helper(input_list,i,length)
    for i in range(length-1,0,-1):
        input_list[0],input_list[i] = input_list[i],input_list[0]
        heap_helper(input_list,0,i)
    return input_list

print('heap_sort:',heap_sort(list_original))
```



### 8. 计数排序



### 9. 桶排序





### 10. 基数排序





## 常用算法思想（添加实例）

### 1. 枚举



### 2. 递归&回溯



### 3. 分治



### 4. 动态规划





### 5. 贪心算法







## 常用数据结构

参考清华大学邓俊辉数据结构课程

### 1. 数组&字符串&二进制串



### 2. 链表



### 3. 队列&栈



### 4. 字典&Hash表



### 5.堆&优先队列

小顶堆 大顶堆

### 6. 树

DFS BFS 

### 7. 图

常见的图结构：邻接矩阵(简单，但浪费空间)， 邻接表(对任意一个顶点，使用字典存储与它相邻的顶点)

下面是Vertex类:

```python
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]
```
下面是Graph类：

```python
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
```

用上面的两个类构建一个图：

```python
g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
```

##### 广度优先搜索(BFS)

步骤：

（1）顶点v入队列。

（2）当队列非空时则继续执行，否则算法结束。

（3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。

（4）查找顶点v的第一个邻接顶点col。

（5）若v的邻接顶点col未被访问过的，则col入队列。

（6）继续查找顶点v的另一个新的邻接顶点col，转到步骤（5）。直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。

代码：

```python
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
 
def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')
```

##### 深度优先搜索(DFS)

步骤：

（1）访问初始顶点v并标记顶点v已访问。

（2）查找顶点v的第一个邻接顶点w。

（3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。

（4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。

（5）继续查找顶点w的下一个邻接顶点wi，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。
代码：

```python
from pythonds.graphs import Graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
 
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
 
    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

```

refer：https://blog.csdn.net/m0_37324740/article/details/80842499