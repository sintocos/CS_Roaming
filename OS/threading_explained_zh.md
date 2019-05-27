# Threading Explained

[英文版](<https://kishuagarwal.github.io/threads.html>)

通常编写的程序都是单线程的，单线程的意思就是处理器从程序的第一条指令开始，一行行往下执行程序，直到最终它到达执行完程序的最后一条指令，然后程序结束。当然程序中还有一些分支，但总体而言是这么一个模式。

但是有些情况下，你需要以某种方式同时做两件或多件工作，或者这些工作需要独立于其他工作。假设你正在构建一个具有两个按钮的桌面应用程序，`Start`和`Cancel`。按下`Start`将启动一些需要长时间运行的任务，按下`Cancel`将取消这些运行时间长的任务。

如果你尝试以普通方式（单线程方式）构建上述应用程序，你将看到单线程执行模式的最主要的缺点。当用户按下`Start`，需要长时间运行的任务将开始启动，由于整个应用程序是顺序运行，您的桌面应用程序就会被冻结，直到那个任务完成。这意味着，用户将无法通过按下`Cancel`按钮来取消任务。

这是其中的一种情况，而线程可以帮助你解决这个问题。但在了解线程是什么之前，还需要了解什么是进程。

一个进程是程序运行时的一个实例。如果你的程序指令只是放在硬盘的某些文件中，那么这并不构成一个进程。只有当程序实际启动运行时，操作系统才会为您的程序创建一个进程。

进程主要包括以下内容：

![images](https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Threading_explained-zh/1.png)

- 要执行的指令

- 程序中的全局变量和常量
- 用于管理函数调用的栈
- 用于动态分配内存的堆
- 打开的文件或者Socket的文件描述符
- 诸如用户ID,组ID等权限
- 程序执行的状态，比如程序计数器和寄存器

如果没有线程，进程就是操作系统可以安排在某个时刻运行的基本执行单元。当有多个进程时，操作系统给每个进程分配一段运行时间，并不断地从一个进程切换到另一个进程。为了使这种切换成为可能，操作系统会保存进程的当前状态，保存在一个称之为进程控制块的结构体中，这个进程控制块具有与上述列表基本相同的信息。之后操作系统重新调度该进程运行的时候，这个结构体可以确保进程恢复当前的状态，即恢复到它被停止运行的地方。

### 1. 线程

线程允许我们在一个进程里可以有多个并发执行流。使用线程，我们可以让操作系统执行多一个层次的调度。也就是说，在一个时刻可以执行所有线程中的某一个线程。

当您启动程序时，操作系统会为该程序创建一个包含上面所描述的信息的进程，并开始执行指令。这是执行的主要线程。现在你可以做的就是在同一个程序中创建一个新线程。这个线程会有以下内容：

![images](https://raw.githubusercontent.com/sintocos/Media/master/Markdown_images/Threading_explained-zh/2.png)

正如你所看到的，线程与进程共享大部分数据。你可以将进程视为一个程序资源分配的基本单位，而将线程视为程序执行的基本单位。进程拥有内存、文件描述符等资源，还有一些其他的东西，比如要执行的代码和执行的权限。你所创建的所有线程将与进程共享这些东西，但是进程会有一些额外的只属于它们自己的东西。

- 每个线程都有一个自己的线程堆栈。由于在一个程序中，每个线程都是一个自己所拥有的执行流程，因此每个线程都需要它自己的栈来跟踪调用的栈。
- 每个线程还需要存储它自己的状态。当该线程处于暂停时，所要存储的状态包括寄存器和程序计数器的内容。

如果您熟悉C语言中的`fork`函数，要注意线程与它并不一样。`fork`指令用于创建当前进程的子进程。在线程上可以执行的操作，你也可以在子进程上执行，但创建这些子进程并在它们之间进行上下文切换，与创建线程和在线程之间执行上下文切换相比，更加耗费资源。

原因很简单 -

- 在创建子进程时，子进程会创建父进程的完整副本，其中包括文件描述符、权限、要执行的代码等。子进程本身就和它的父进程一样。但是在创建线程时，由于每个线程共享进程的大部分数据，因此仅需要创建本地线程堆栈和线程状态，这种方式耗费资源非常少。
- 与线程上下文切换相比，执行进程上下文切换需要更多时间。因为与线程相比，进程必须保存更多信息。

### 2.多线程程序示例

前面谈了很多理论方面的东西。现在让我们看一下多线程程序的一个示例。

```c++
#include <pthread.h>
#include <stdio.h> 

int num_threads = 10;
int thread_num[10];

void* thread_function(void* arg) {
    int t= *(int *)(arg);
    printf("Hi from thread %d\n", t);
}

int main(void) {
    pthread_t threads[num_threads];
    for (int i = 0; i < num_threads; i++) {
        thread_num[i] = i;
        if (pthread_create(&threads[i], NULL, thread_function, &thread_num[i])) {
            printf("Error in creating thread %d\n", i);
        }
    }
    for (int i = 0; i < num_threads; i++) {
        if(pthread_join(threads[i], NULL)) {
            printf("Error in joining thread %d\n", i);
        }
        
    }
    return 0;
}
```

- 要使用线程，就必须导入`pthread.h`这个头文件。该文件包含所有与线程相关的函数的声明。
- 在`main`函数中，创建了一个`pthread_t`类型的数组，其中`pthread_t`是一个用来表示线程id的整数。
- 然后循环10次，并使用`pthread_create`函数创建10个线程。这个函数接受四个参数。第一个参数是内存地址，这个内存地址存储着正在被创建的线程的id。这里我们传递在`thread_num`的数组中相应位置的地址，这个位置对应着被创建的这个线程。第二个参数是如何创建线程的一些属性。我们将传递NULL进去，这样就会使用默认值。第三个参数是一个函数，将由正在被创建的线程执行的函数，在这里，我们传入`thread_function`。第四个参数是数据，这些数据传给将被线程执行的函数。在这里我们传递线程的数量作为参数。
- `pthread_create`函数将在运行成功时返回0，如果在创建线程时出现一些错误，则返回非零值。这就是为什么我把这个调用包装在if中，以捕获错误。
- 当一个线程被创建时，新线程将执行所给定的函数，而当前线程将继续执行下一条指令。所以，新线程将运行`thread_function`，与此同时，主线程继续运行循环，不断创建新线程。
- 在创建所有线程之后，主线程调用被创建的每个线程中的`pthread_join`函数。`pthread_join`函数用于将另外一个线程连接到当前线程。这是一个阻塞调用，所以在另一个线程没有运行完毕之前，当前线程将被阻塞。用这种方式来清理你在一个程序中创建的所有线程是一个非常好的习惯。
- `pthread_join`接受两个参数。第一个是要等待的线程的ID，第二个是内存地址，这个内存地址存储着该线程返回给其他线程的值。这里我们传递NULL，因为`thread_function`没有任何需要返回给主线程的值。

用下面的命令来运行上面的程序：

```
gcc thread.c -lpthread
```

其中`thread.c`是文件的名称，而`pthread`是一个库，里面包含所有函数的实际目标文件。你会得到类似以下的东西作为输出：

```
Hi from thread 0
Hi from thread 1
Hi from thread 5
Hi from thread 3
Hi from thread 6
Hi from thread 2
Hi from thread 4
Hi from thread 7
Hi from thread 8
Hi from thread 9
```

从上面的输出中可以明显看出，不同的线程以乱序的方式执行，你永远也无法预测它们执行的顺序。有时这会导致你的程序出现一些错误，这些错误难以找到。

### 3. 对共享对象的非独占访问

考虑下面这段代码,

```c++
#include <pthread.h>
#include <stdio.h>
int x = 0;
void* thread_function(void* arg) {
    for (int c = 0; c < 1000000; c++) {
        int i = x;
        i = i + 1;
        x = i;
    }
}
int main(void) {
    pthread_t thread;
    if (pthread_create(&thread, NULL, thread_function, NULL)) {
        printf("Error in creating thread \n");
    }
    for (int c = 0; c < 1000000; c++) {
        x = x + 1;
    }
    if(pthread_join(thread, NULL)) {
        printf("Error in joining thread\n");
    }
    printf("Final value of x is %d", x);
    return 0;
}
```

运行此程序时，每次运行时都有可能会看到不同的x值。在我的电脑上，这个程序执行5次得到了以下结果：

```
Final value of x is 1161394
Final value of x is 1100001
Final value of x is 1062798
Final value of x is 1205648 
Final value of x is 1533644
```

假设`x`变量的当前值是10。然后第二个线程执行指令`int i = x`，将10存储到 `i`里面。但是随后这个线程切换上下文切到第一个线程，而第一个线程执行指令`x = x + 1`，使得`x`的值增加到11。当第二个线程切回来时，它会将 `i`增加到11，并将11这个值存储在变量`x`中，替换`x`的旧值。

这种情况发生的原因是有两个线程对全局变量`x`进行非独占操作。读取`x`的值然后给`x`写入值，它并不是一个原子操作。因此，可能会发生这样的情况：一个线程在读取`x`的值之后，在该线程有机会保存`x`的值之前，某个其他的线程可能会修改`x`的值。

### 4. 对共享对象的独占访问：锁

要解决这个问题，我们必须使用锁。

```c++
#include <pthread.h>
#include <stdio.h>

int x = 0;
pthread_mutex_t x_mutex;

void* thread_function(void* arg) {
    for (int c = 0; c < 1000000; c++) {
        pthread_mutex_lock(&x_mutex);
        int i = x;
        i = i + 1;
        x = i;
        pthread_mutex_unlock(&x_mutex);
    }
}

int main(void) {
    pthread_t thread;

    pthread_mutex_init(&x_mutex, NULL);

    if (pthread_create(&thread, NULL, thread_function, NULL)) {
        printf("Error in creating thread \n");
    }
    for (int c=  0; c < 1000000; c++) {
        pthread_mutex_lock(&x_mutex);
        x = x + 1;
        pthread_mutex_unlock(&x_mutex);
    }
    if(pthread_join(thread, NULL)) {
        printf("Error in joining thread\n");
    }
    pthread_mutex_destroy(&x_mutex);
    printf("Final value of x is %d", x);
    return 0;
}
```

- 这里我们使用互斥锁进行锁定。互斥变量这么一种锁，它可以保护某些资源不会被同时访问和修改。使用互斥锁的方法是，一个线程在尝试访问某个共享变量时，它需要会在锁定或拥有这个变量对应的互斥变量，然后所有其他线程必须等待此线程解锁互斥变量，解锁之后其他线程才能对该共享变量执行操作。因此，互斥变量相当于该共享资源的守门人，并且一次只允许一个线程进门。
- 首先，我们使用`pthread_mutex_t`来定义一个互斥变量，然后在主函数中将互斥变量的地址传给`pthread_mutex_init`函数，这个函数将会初始化该互斥变量。`pthread_mutex_init`函数的第二个参数可以为互斥变量设置一些额外的属性，但这里我们不需要，所以只传入NULL。
- 主要的函数是`pthread_mutex_lock`和`pthread_mutex_unlock`。在我们访问`x`变量之前，我们首先获取互斥锁，在完成对`x`的处理后，再释放互斥锁，以便其他线程随后可以访问`x`。
- 在我们用完互斥锁之后，我们使用`pthread_mutex_destroy`函数来清理互斥锁，只要给这个函数传入互斥变量的地址就可以。

正确处理程序中的互斥体和锁可能是一项非常具有挑战性的任务。它需要一些经验，也需要对程序流程有着充分的理解。下面给出一个使用多线程的例子。

### 5. 使用多线程完成归并排序

```c++
#include <pthread.h>
#include <stdio.h>

typedef struct bound {
    int low;
    int high;
} bound;

int a[] = {5,6,1,2,3,7,4,8,9,0,11,10};
int size = 12;

void* merge_sort(void* arg) {
    bound limits = *((bound *)arg);
    int low = limits.low;
    int high = limits.high;

    // If the size is one, don't do anything
    if (low == high) {
        return;
    }
    // If the size of the array is 2 or more
    // Then break the range into two parts

    int mid = (low + high) / 2;

    // Create two threads to assign the task of 
    // sorting the two halfs of the array

    bound left = {.low=low, .high=mid};
    bound right = {.low=mid+1, .high=high};

    pthread_t left_thread, right_thread;
    
    if (pthread_create(&left_thread, NULL, merge_sort, &left)) {
        printf("Error in creating the thread at point %d %d\n", low, mid);
    }
    if (pthread_create(&right_thread, NULL, merge_sort, &right)) {
        printf("Error in creating the thread at point %d %d\n", mid+1, high);
    }
    
    // Wait for both the threads to complete
    pthread_join(left_thread, NULL);
    pthread_join(right_thread, NULL);

    // Now combine the two sorted sub-halfs into sorted array
    // Note: This can be done inplace also.
    
    //Create a temporary array to hold the sorted array
    int temp_size = high - low + 1;
    int temp[temp_size];

    int left_index = low;
    int right_index= mid+1;
    for (int i = 0; i < temp_size; i++) {
        if (left_index <= mid && right_index <= high) {
            if (a[left_index] < a[right_index]) {
                temp[i] = a[left_index];
                left_index++;
            } else {
                temp[i] = a[right_index];
                right_index++;
            }
        } else {
            if (left_index <= mid) {
                temp[i] = a[left_index++];
            } else {
                temp[i] = a[right_index++];
            }
        }
    }

    // Copy the temp array to the original array
    for (int i = 0; i < temp_size; i++) {
        a[low+i] = temp[i];
    } 
}

int main(void) {
    pthread_t mythread;
    bound initial = {.low=0, .high=size-1};

    // Call merge sort on the entire array
    merge_sort(&initial);

    // Print the sorted array
    for (int i = 0 ; i < size; i++) {
        printf("%d ", a[i]);
    }
    return 0;
}
```

