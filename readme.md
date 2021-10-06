# Concurrency and Parallelism in python

High level concepts:
- **Concurrency** is the task of running and managing the multiple computations at the same time.
- **Parallelism** is the task of running multiple computations simultaneously.
- **Thread** of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically a part of the operating system
- **Syncronous** code execution is a sequence of instructions that runs in order, one after the other. When the thread waits for one instruction to finish to start the next one. For       example, writing to a file or reading from a disk, or calculating 2 to the power of 2389
- **Multithreading** (also called multitasking) is when a new thread is given a new task when the first thread is in waiting mode, multiple threads are used at once. This solving approach can cause race conditions.
- **Race Conditions**  A race condition is a situation on concurrent programming where two concurrent threads or processes compete for a resource and the resulting final state depends on who gets the resource first. A race condition is an undesirable situation that occurs when two or more process can access and change the shared data at the same time. It occurred because there were conflicting accesses to a resource.
- **Asynchronous** the same thread returns to run other part of the instructions instead of being blocked.
- **Multiprocessing** is when multiple sources are used each with his own thread, CPU core and memory.
- **Input and output, I/O** is the communication between an information processing system, such as a computer, and the outside world, possibly a human or another information processing system. Inputs are the signals or data received by the system and outputs are the signals or data sent from it.
- **Central Processing Unit (CPU)**, also called a central processor, main processor or just processor, is the electronic circuitry that executes instructions comprising a computer program.

***

Regarding execution speed, typically there are 2 types of bottlenecks when executing code: CPU bound, and I/O bound.

### **CPU bound**
The time to complete a task is determined by the speed of the processor
How its speed up: finding solutions to do more calculations in the same amount of time (for ex. whith multiprocessing or more powerfull CPU)

### **I/O bound**
The time it takes to complete a calculation is determined waiting for input or output operation, this time is determined by the speed of the memory I/O, hard drive, network, or some external resource.
How its speed up: overlapping time spent waiting for these slow external factors with extra calculations (CPU bound) processes. AsyncIO and threading are tools to solve these problems.

***

## AsyncIO VS threading VS Multiprocessing in Python
When some type of concurrency is needed in python, these are the 3 defacto libraries: AsyncIO, Threading and Multiprocessing.

## 1. threading
Efective when dealing with slow I/O bound operations. Each new process is spin up in a new thread speeding things up with the disadvantage of having to deal with race conditions, if the shared resources are not considered properly will result in random intermittent bugs that are hard to fix.

## 2. AsyncIO
Most useful when dealing with cost I/O bound operations has the advantage of being thread safe (since each process uses the same thread) and having complete control when the tasks return control to the main loop. That is uses cooperative multitasking so each task must announce when its ready to be switched out.

## 3. Multiprocessing
Spins multiple process each with his own cpu core, memory and thread. In python each process runs in its own Python interpreter and many processors are used. Has the disadvantage of requiring extra setup time and extra complexity to make some variable accessible by each process and share communication between them!

Extra: """Node.js is single threaded non blocking asynchronous framework, in javascript is achieved by something called the event loop, instead of waiting the main process to finish, it returns a callback (remember  like "call me back", the main process, when you have finished)"""

Sources:
*https://www.youtube.com/watch?v=0vFgKr5bjWI&t=65s
*https://realpython.com/python-concurrency/
*https://leimao.github.io/blog/Python-Concurrency-High-Level/
*https://en.wikipedia.org/wiki/Thread_(computing)
*https://www.geeksforgeeks.org/difference-between-concurrency-and-parallelism/
*https://stackoverflow.com/questions/34510/what-is-a-race-condition
*https://press.rebus.community/programmingfundamentals/chapter/input-and-output/
*https://en.wikipedia.org/wiki/Central_processing_unit
