# Chapter 1 - const, inline，static, this

## 1.1 const

### (1) const 基础

如果const关键字不涉及到指针，我们很好理解，下面是涉及到指针的情况：

	int b = 500;
	const int* a = &b; [1]
	int const *a = &b; [2]
	int* const a = &b; [3]
	const int* const a = &b; [4]

参考《Effective c++》Item21上的做法，
如果 const 位于星号的左侧，则 const 就是用来修饰指针所指向的变量，即指针指向为常量；如果 const 位于星号的右侧，const 就是修饰指针本身，即指针本身是常量。

因此，[1]和[2]的情况相同，都是指针所指向的内容为常量（const放在变量声明符的位置无关），这种情况下不允许对内容进行更改操作，如不能*a = 3；[3]为指针本身是常量，而指针所指向的内容不是常量，这种情况下不能对指针本身进行更改操作，如a++是错误的；[4]为指针本身和指向的内容均为常量。

### (2) 作为参数

	void display(const double& r);
	void display(const double* r);

说明:

1. 在引用或者指针参数的时候使用 const 限制是有意义的，而对于值传递的参数使用 const 则没有意义
2. 保证引用的变量的值不被改变
3. const 在 double 前或者后面意思相同，只是不同的人的写法不同

### (3) const对象

声明为 const 的对象只能访问类中声明为 const 的成员函数，不能调用其它成员函数。

### (4) const成员函数

	类型说明符 函数名(参数表) const;
	void print(int i) const;

说明:

1. const 是函数类型的一个组成部分，因此在实现部分也要带 const 关键字
2. 常成员函数不能更新对象的数据成员，也不能调用该类中没有用 const 修饰的成员函数

### (5) 使用const的一些建议

1. 要大胆的使用 const，这将给你带来无尽的益处，但前提是你必须搞清楚原委
2. 要避免最一般的赋值操作错误，如将 const 变量赋值，具体可见思考题
3. 在参数中使用 const 应该使用引用或指针，而不是一般的对象实例，原因同上
4. const 在成员函数中的三种用法（参数、返回值、函数）要很好的使用
5. 不要轻易的将函数的返回值类型定为 const
6. 除了重载操作符外一般不要将返回值类型定为对某个对象的 const 引用

## 1.2 inline

### (1) 预处理宏

介绍内联函数之前，有必要介绍一下预处理宏。内联函数的功能和预处理宏的功能相似。相信大家都用过预处理宏，我们会经常定义一些宏，如：

	#define TABLE_COMP(x) ((x)>0 ? (x) : 0) 

就定义了一个宏。

为什么要使用宏呢？因为函数的调用必须要将程序执行的顺序转移到函数所存放在内存中的某个地址，将函数的程序内容执行完后，再返回到转去执行该函数前的地方。这种转移操作要求在转去执行前要保存现场并记忆执行的地址，转回后要恢复现场，并按原来保存地址继续执行。因此，函数调用要有一定的时间和空间方面的开销，于是将影响其效率。而宏只是在预处理的地方把代码展开，不需要额外的空间和时间方面的开销，所以调用一个宏比调用一个函数更有效率。 

但是宏也有很多的不尽人意的地方。

1. 宏不能访问对象的私有成员。
2. 宏的定义很容易产生二意性。

我们举个例子：

	#define TABLE_MULTI(x) (x*x) 

我们用一个数字去调用它，TABLE_MULTI(10)，这样看上去没有什么错误，结果返回100，是正确的，但是如果我们用TABLE_MULTI(10+10)去调用的话，我们期望的结果是400，而宏的调用结果是(10+10*10+10)，结果是120，这显然不是我们要得到的结果。避免这些错误的方法，**一定要给宏的参数都加上括号**。

	#define TABLE_MULTI(x) ((x)*(x)) 

这样可以确保不会出错，但是，即使使用了这种定义，这个宏依然有可能出错，例如使用TABLE_MULTI(a++)调用它，他们本意是希望得到(a+1)*(a+1)的结果，而实际上呢？我们可以看看宏的展开结果: (a++)*(a++)，如果a的值是４，我们得到的结果是5*6=30。而我们期望的结果是5*5=25,这又出现了问题。事实上，在一些C的库函数中也有这些问题。例如: Toupper(*pChar++)就会对pChar执行两次++操作，因为Toupper实际上也是一个宏。 

### (2) inline 函数 

我们可以看到宏有一些难以避免的问题，怎么解决呢？

下面就是用我要介绍的内联函数来解决这些问题，我们可以使用内联函数来取代宏的定义。而且事实上我们可以用内联函数完全取代预处理宏。

内联函数和宏的区别在于，宏是由预处理器对宏进行替代，而内联函数是通过编译器控制来实现的。而且内联函数是真正的函数，只是在需要用到的时候，内联函数像宏一样的展开，所以取消了函数的参数压栈，减少了调用的开销。你可以象调用函数一样来调用内联函数，而不必担心会产生于处理宏的一些问题。

我们可以用 inline 来定义内联函数，不过，**任何在类的声明部分定义的函数都会被自动的认为是内联函数**。

在函数声明或定义中函数返回类型前加上关键字 inline 即把min（）指定为内联。
	
	inline int min(int first, int secend) {/****/};

我们可以把它作为一般的函数一样调用。但是执行速度确比一般函数的执行速度要快。inline 函数对编译器而言必须是可见的，以便它能够在调用点内展开该函数。与非inline函数不同的是，inline函数必须在调用该函数的每个文本文件中定义。当然，对于同一程序的不同文件，如果C++ inline函数出现的话，其定义必须相同。

对于由两个文件compute.c和draw.c构成的程序来说，程序员不能定义这样的min()函数，它在compute.c中指一件事情，而在draw.c中指另外一件事情。如果两个定义不相同，程序将会有未定义的行为。

为保证不会发生这样的事情，建议把inline函数的定义放到头文件中。在每个调用该inline函数的文件中包含该头文件。这种方法保证对每个inline函数只有一个定义，且程序员无需复制代码，并且不可能在程序的生命期中引起无意的不匹配的事情。

### (3) inline 函数的编程风格

关键字inline 必须与函数定义体放在一起才能使函数成为内联，仅将 inline 放在函数声明前面不起任何作用。如下风格的函数Foo 不能成为内联函数：

	inline void Foo(int x, int y);   
	// inline 仅与函数声明放在一起   
	void Foo(int x, int y){}  

而如下风格的函数Foo 则成为内联函数：

	void Foo(int x, int y);   
	inline void Foo(int x, int y)   
	// inline 与函数定义体放在一起{} 

所以说，C++ inline函数是一种“用于实现的关键字”，而不是一种“用于声明的关键字”。一般地，用户可以阅读函数的声明，但是看不到函数的定义。尽管在大多数教科书中内联函数的声明、定义体前面都加了inline 关键字，但我认为inline 不应该出现在函数的声明中。这个细节虽然不会影响函数的功能，但是体现了高质量C++/C 程序设计风格的一个基本原则：声明与定义不可混为一谈，用户没有必要、也不应该知道函数是否需要内联。

定义在类声明之中的成员函数将自动地成为内联函数，例如：

	class A  
	{  
	public:
		void Foo(int x, int y) { }   
		// 自动地成为内联函数  
	} 

将成员函数的定义体放在类声明之中虽然能带来书写上的方便，但不是一种良好的编程风格，上例应该改成：

	// 头文件  
	class A  
	{  
	public:  
		void Foo(int x, int y);  
	}  
	// 定义文件  
	inline void A::Foo(int x, int y){}  

内联函数在C++类中，应用最广的，应该是用来定义存取函数。我们定义的类中一般会把数据成员定义成私有的或者保护的，这样，外界就不能直接读写我们类成员的数据了。对于私有或者保护成员的读写就必须使用成员接口函数来进行。如果我们把这些读写成员函数定义成内联函数的话，将会获得比较好的效率。

	Class sample {
	Private:
		int nTest;
	Public:
		int readtest(){ return nTest;}
		Void settest(int I) {nTest=I;}
	} 

当然，内联函数也有一定的局限性。就是函数中的执行代码不能太多了，如果，**内联函数的函数体过大，一般的编译器会放弃内联方式**，而采用普通的方式调用函数。这样，内联函数就和普通函数执行效率一样了。

## 1.3 static





## 1.4 this 指针

先要理解class的意思。class应该理解为一种类型，像int和char一样，是用户自定义的类型。（虽然比 int 和 char 这样 built-in 类型复杂的多，但首先要理解它们一样是类型)。用这个类型可以来声明一个变量，比如int x, myclass my等等。这样就像变量 x 具有 int 类型一样，变量 my 具有 myclass 类型。

理解了这个，就好解释 this 了，my 里的 this 就是指向 my 的指针。如果还有一个变量myclass mz，mz 的 this 就是指向 mz 的指针。这样就很容易理解this 的类型应该是 myclass *，而对其的解引用 *this 就应该是一个 myclass 类型的变量。

通常在class定义时要用到类型变量自身时，因为这时候还不知道变量名（为了通用也不可能固定实际的变量名），就用this这样的指针来使用变量自身。 

### (1) this指针的用处

一个对象的 this 指针并不是对象本身的一部分，不会影响sizeof(对象)的结果。this作用域是在类内部，当在类的非静态成员函数中访问类的非静态成员的时候，编译器会自动将对象本身的地址作为一个隐含参数传递给函数。也就是说，即使你没有写上 this 指针，编译器在编译的时候也是加上 this 的，它作为非静态成员函数的隐含形参，对各成员的访问均通过 this 进行。

例如，调用 date.SetMonth(9) <===> SetMonth(&date, 9)，this帮助完成了这一转换。

### (2) this指针的使用

一种情况就是，在类的非静态成员函数中返回类对象本身的时候，直接使用 return *this；另外一种情况是当参数与成员变量名相同时，如this->n = n （不能写成n = n）。 

### (3) this指针程序示例

this指针是存在与类的成员函数中,指向被调用函数所在的类实例的地址。根据以下程序来说明 this 指针：

	#include<iostream.h>
	class Point
	{ 
	  int x, y;
	public:
	  Point(int a, int b) { x=a; y=b;}
	  Void MovePoint( int a, int b){ x+=a; y+=b;}
	  Void print(){ cout<<"x="<<x<<"y="<<y<<endl;}
	};
	void main( )
	{
	   Point point1( 10,10);
	   point1.MovePoint(2,2);
	   point1.print( );
	}

当对象 point1 调用 MovePoint(2,2) 函数时，即将 point1 对象的地址传递给了 this 指针。

MovePoint 函数的原型应该是 void MovePoint( Point *this, int a, int b);第一个参数是指向该类对象的一个指针，我们在定义成员函数时没看见是因为这个参数在类中是隐含的。这样point1的地址传递给了 this，所以在 MovePoint 函数中便显式的写成：

	void MovePoint(int a, int b) { this->x +=a; this-> y+= b;}

即可以知道，point1调用该函数后，也就是point1的数据成员被调用并更新了值。即该函数过程可写成 point1.x+= a; point1. y + = b;

### (4) 关于this指针的一个精典回答

当你进入一个房子后，你可以看见桌子、椅子、地板等，但是房子你是看不到全貌了。对于一个类的实例来说，你可以看到它的成员函数、成员变量，但是实例本身呢？this 是一个指针，它时时刻刻指向你这个实例本身。

# Chapter 2 - pointers, refrence

## 2.1 refrence 引用

引用是C++中的概念，初学者容易把引用和指针混淆一起。以下程序中，n 是 m 的一个引用（reference），m 是被引用物（referent）。

	int m; 
	int &n = m;

n 相当于 m 的别名（绰号），对 n 的任何操作就是对m的操作。所以 n 既不是 m 的拷贝，也不是指向 m 的指针，其实 n 就是 m 它自己。 

**引用的规则：**

- 引用被创建的同时必须被初始化（指针则可以在任何时候被初始化）。 
- 不能有NULL引用，引用必须与合法的存储单元关联（指针则可以是NULL）。 
- 一旦引用被初始化，就不能改变引用的关系（指针则可以随时改变所指的对象）。 

以下示例程序中，k 被初始化为 i 的引用。语句 k = j 并不能将 k 修改成为 j 的引用，只是把 k 的值改变成为6。由于 k 是 i 的引用，所以 i 的值也变成了6。

	int i = 5; 
	int j = 6; 
	int &k = i; 
	k = j; // k和i的值都变成了6; 

**引用的主要功能是传递函数的参数和返回值**。

C++语言中，函数的参数和返回值的传递方式有三种：**值传递、指针传递和引用传递**。 

### (1) 以下是"值传递"的示例程序

由于Func1函数体内的x是外部变量n的一份拷贝，改变x的值不会影响n, 所以n的值仍然是0。

	void Func1(int x) 
	{ 
		x = x + 10; 
	} 
	... 
	int n = 0; 
	Func1(n); 
	cout << "n = " << n << endl; // n = 0 

### (2) 以下是"指针传递"的示例程序

由于Func2函数体内的x是指向外部变量n的指针，改变该指针的内容将导致n的值改变，所以n的值成为10。

	void Func2(int *x) 
	{ 
		(* x) = (* x) + 10; 
	} 
	... 
	int n = 0; 
	Func2(&n); 
	cout << "n = " << n << endl; // n = 10 

### (3) 以下是"引用传递"的示例程序

由于Func3函数体内的x是外部变量n的引用，x和n是同一个东西，改变x等于改变n，所以n的值成为10。

	void Func3(int &x) 
	{ 
		x = x + 10; 
	} 
	... 
	int n = 0; 
	Func3(n); 
	cout << "n = " << n << endl; // n = 10 

对比上述三个示例程序，**会发现"引用传递"的性质象"指针传递"，而书写方式象"值传递"**。 

实际上"引用"可以做的任何事情"指针"也都能够做，为什么还要"引用"这东西？ 
答案是"用适当的工具做恰如其分的工作"。 

指针能够毫无约束地操作内存中的任何东西，尽管指针功能强大，但是非常危险。 

如果的确只需要借用一下某个对象的"别名"，那么就用"引用"，而不要用"指针"，以免发生意外。

# Chapter 3 - char*, char[], string

## 3.1 char*, char[], string

在C中，并没有字符串这个数据类型，而是使用字符数组来保存字符串。C字符串实际上就是一个以null('\0')字符结尾的字符数组，null字符表示字符串的结束。需要注意的是：只有以null字符结尾的字符数组才是C字符串，否则只是一般的C字符数组。
    
C字符串定义时可以利用"="号进行初始化，但是以后不能利用"="对C字符串进行赋值。对C字符串的操作需要通过"string"文件中定义的字符串处理函数。例如：

```C++
//字符串的初始化
char a[11] = "huanying";
//字符串的赋值
strcpy(a,"nihao")
//获取字符串的长度，不包括'\0'在内
strlen(a);
printf("%s",a);
```

在C中也可以使用字符指针来访问一个字符串,通过字符指针指向存放字符串数组的首元素地址来进行访问.
char *a = "nihao";
printf("%s",a);

在C++中则把字符串封装成了一种数据类型string,可以直接声明变量并进行赋值等字符串操作。以下是C字符串和C++中string的区别：

	                             C字符串                 string对象
	所需的头文件名称       	<string>或<string.h>        	<string>或<string.h>
	为什么需要头文件       	为了使用字符串函数            为了使用string类
	如何声明                 char name[20];              string name;
	如何初始化               char name[20]="nihao";   	string name = "nihao";
	必须声明字符串长度么？		是                          否
	使用一个null字符么？     	是                          否
	怎样实现字符串赋值      	strcpy(name,"John");        name = "John";
	其他优点               	更快                        更易于使用，优选方案
	可以赋一个比现有字符更 	不能                        可以
	长的字符串么？  

### (1) C++常用字符串函数

```c++
char s1[]="I am a student";
char s2[20]="teacher";
char s3[]="student";
int result;
char s4[20],*p;
```

1. 串长度 int strlen(char *str)

   cout<<strlen(s1)<<endl; 输出14
   cout<<strlen(s2)<<endl; 输出7

2. 串拷贝 char *strcpy(char *str1,char *str2)

   strcpy(s4,s2);   //s4为"teacher"

3. 串连接 char *strcat(char *str1,char*str2)

   strcat(s2,s3); //s2为"teacherstudent"

4. 串比较 int strcmp(char *str1,char *str) //比较的是对应字符的ASCII码值，如果str1>str2,返回1

   result=strcmp(s2,s3);   //result>0
   result=strcmp(s2,s2);   //result=0
   result=strcmp(s3,s2);   //result<0

5. 串定位 char *strchr(char *str,char ch)

   p=strchr(s1,'s');    //找到返回字符在字串中的位置，否则返回-1
   strcpy(p,s2);      //s1为"I am a teacher"

6. 在一个串中查找是否存在和另一个串相等的子串

7. 截取子串形成一个新串

### (2) 字符串的输入

1. 方法一：使用输入操符来填充一个C字符串变量
   例如：
   char a[80];
   cin>>a;
   注：以这种方式来读取C字符串时，会忽略最初的空白字符(空格、制表符和换行符)，而且输入会在下一个空格或者换行符处停止。

2. 方法二：使用预定义函数getline获取整行输入(包括空格)
   getline函数有两个参数：第一个参数用于接收输入的C字符串变量；第二个参数用于规定getline最多能接收的字符个数。
   例如:
   char a[80];
   cin.getline(a,80);
   当遇到行结束的时候，输入才会停止。

### (3) C++ string类的输入

1. 方法一：和C字符串输入的方法一相同。
2. 方法二：使用getline函数。

例如：

```c++
string a;
getline(cin,a);
```

### (4) string对象和C字符串之间的转换

可以将C字符串存储在string类型的变量中，例如：
	

	char a[] = "nihao";
	string b;
	b=a;

但string对象不能自动的转换为C字符串，需要进行显式的类型转换，需要用到string类的成员函数c_str().
例如：

	strcpy(a,b.c_str());


### (5) 字符串到数字的转换

atoi函数获取一个C字符串参数，返回对应的int值。如果参数不与一个int值对应，atoi就会返回0。atoi函数在文件为cstdlib的库中。如果数字太大，不能转换成int类型的值，可以使用atol将字符串转换为long类型的值。
例如:

	atoi("1234");   //返回整数1234
	atoi("#123");   //返回0

# Chapter 4 - uint8\_t, uint16\_t, uint32\_t, uint64\_t

uint8\_t, uint16\_t, uint32\_t, uint64\_t  是什么数据类型?

那么_t的意思到底表示什么？它就是一个结构的标注，可以理解为type/typedef的缩写，表示它是通过typedef定义的，而不是其它数据类型。

uint8\_t，uint16\_t，uint32\_t 等都不是什么新的数据类型，它们只是使用typedef给类型起的别名，新瓶装老酒的把戏。不过，不要小看了typedef，它对于你代码的维护会有很好的作用。比如C中没有bool，于是在一个软件中，一些程序员使用int，一些程序员使用short，会比较混乱，最好就是用一个typedef来定义，如：

	typedef char bool;

一般来说，一个C的工程中一定要做一些这方面的工作，因为你会涉及到跨平台，不同的平台会有不同的字长，所以利用预编译和typedef可以让你最有效的维护你的代码。为了用户的方便，**C99标准的C语言**硬件为我们定义了这些类型，我们放心使用就可以了。

按照posix标准，一般整形对应的*_t类型为：

	1字节     uint8_t
	2字节     uint16_t
	4字节     uint32_t
	8字节     uint64_t

附：C99标准中inttypes.h的内容

```c++
00001 /*
00002    inttypes.h
00003 
00004    Contributors:
00005      Createdby Marek Michalkiewicz <marekm@linux.org.pl>
00006 
00007    THISSOFTWARE IS NOT COPYRIGHTED
00008 
00009    Thissource code is offered for use in the public domain.  You may
00010    use,modify or distribute it freely.
00011 
00012    Thiscode is distributed in the hope that it will be useful, but
00013    WITHOUTANY WARRANTY.  ALLWARRANTIES, EXPRESS OR IMPLIED ARE HEREBY
00014    DISCLAIMED.  This includes but is not limited towarranties of
00015    MERCHANTABILITYor FITNESS FOR A PARTICULAR PURPOSE.
00016  */
00017 
00018 #ifndef __INTTYPES_H_
00019 #define __INTTYPES_H_
00020 
00021 /* Use [u]intN_t if you need exactly N bits.
00022    XXX- doesn't handle the -mint8 option.  */
00023 
00024 typedefsigned char int8_t;
00025 typedefunsigned char uint8_t;
00026 
00027 typedefint int16_t;
00028 typedefunsigned int uint16_t;
00029 
00030 typedeflong int32_t;
00031 typedefunsigned long uint32_t;
00032 
00033 typedeflong long int64_t;
00034 typedefunsigned long long uint64_t;
00035 
00036 typedefint16_t intptr_t;
00037 typedefuint16_t uintptr_t;
00038 
00039 #endif
```

# Chapter 5 - new, delete

new和delete运算符用于动态分配和撤销内存的运算符

### (1) new用法

1. 开辟单变量地址空间

1) new int;  //开辟一个存放数组的存储空间,返回一个指向该存储空间的地址.int *a = new int 即为将一个int类型的地址赋值给整型指针a. 

2) int *a = new int(5) 作用同上,但是同时将整数赋值为5

2. 开辟数组空间

   一维: 

   	int *a = new int[100];  // 开辟一个大小为100的整型数组空间

   二维: 
   	

   	int **a = new int[5][6]

   三维及其以上:依此类推

一般用法: new 类型 [初值]

### (2) delete用法

1. int *a = new int;

   delete a;   //释放单个int的空间

2. int *a = new int[5];

   delete [] a; //释放int数组空间

要访问new所开辟的结构体空间,无法直接通过变量名进行,只能通过赋值的指针进行访问。

用new和delete可以动态开辟，撤销地址空间。在编程序时,若用完一个变量(一般是暂时存储的数组)，下次需要再用，但却又想省去重新初始化的功夫，可以在每次开始使用时开辟一个空间，在用完后撤销它。
