### 当前位置归零
```brainfuck
[-]
```
### 字符I/O
```brainfuck
,.
```
### 简单的循环
```brainfuck
,[.,] #从键盘读取一个字符并输出到屏幕上
```
这是一个连续从键盘读取字符并回显到屏幕上的循环。注意，这里假定0表示输入结束，事实上有些系统并非如此。以-1和“未改变”作为判断依据的程序代码分别是,+[-.,+]和,[->+>-<<]>[-<+>]>[[-]<<.[->>+<<],[->+>-<<]>[-<+>]>]。 
### 指针维护
```brainfuck
>,[.>,] #通过移动指针保存所有的输入，供后面的程序使用。 
```
### 加法
```brainfuck
[->+<] #破环性的加，左边的数归零
```
### 条件指令
```brainfuck
,----------[----------------------.,----------]
```
这个程序会把从键盘读来的小写字符转换成大写。按回车键退出程序。

首先，我们通过,读入第一个字符并把它减10（10 在大多数情况下为换行符 LF 的值）。如果用户按的是回车键，循环命令（[）就会直接跳转到程序的结尾：因为这时第一个字节已经被减到了零。如果输入的字符不是换行符（假设它是一个小写字符），程序进入循环。在这里我们再减去剩下的22，这样总共减掉32：这是ASCII码中小写字符和大写字符的差值。

下面我们把它输出到屏幕。然后接收下一个输入字符，并减去10。如果它是换行符，退出循环；否则，再回到循环的开始，减去22并输出……当循环退出时，因为后面已经没有其他的指令，程序也随之终止。 
### 加法器 add(summand, addend, *sum)
```brainfuck
>>[-]>[-]<<<        // clear cell #2 and #3
[->>+>+<<<]         // transfer cell #0 to #2 and #3
>
    >>[-<<<+>>>]<<  // transfer cell #3 to #0
    [->+>+<<]       // transfer cell #1 to #2 and #3
    >>[-<<+>>]<<    // transfer cell #3 to #1
<
```
该代码以 cell #3 作为临时变量，将保存在 cell #0 和 cell #1 中的两个整数相加，

结果保存在 cell #2；同时维持原来的两个存储单元数值不变，方便以后使用。

代码运行前，设定指针指向 cell #0，

第一步，先将 cell #2 和 cell #3 清空，确保不会有脏数据影响运算结果；

第二步，将 cell #0 的数值转移到 cell #2 和 cell #3，随后利用 cell #3 这个来恢复 cell #0 的值；

第三步，将 cell #1 的数值转移到 cell #2 和 cell #3，随后利用 cell #3 这个来恢复 cell #1 的值；

最后，指针归位（回到初始位置，即指向 cell #0），方便后续运算

### 乘法器 multiply(multiplicand, multiplier, *product)
```brainfuck
>>[-]>[-]>[-]<<<<       // clear cell #2 and #3 and #4
[->
    [->+>+<<]           // add cell #1 to #2
    >>
        [-<<+>>]        // move cell #3 back to #1
        >+<             // copy cell #0 to #4
    <<
<]
>>>>[-<<<<+>>>>]<<<<    // move cell #4 back to #0
```
跟上面的“加法器”类似，这个“乘法器”将保存在 cell #0 和 cell #1 的两个整数相乘，结果保存在 cell #2；同时维持原来的两个存储单元数值不变，方便以后使用。

更多代码解析请参见 https://github.com/moky/BrainFuck 
