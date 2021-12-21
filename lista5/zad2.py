class Stack:
    '''Add item to the stack
    @param item: Item to add'''
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack += [item]

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return(str(self.stack))

def hanoi(n, start, end, middle):
    '''Solves the Hanoi tower problem
    @param n: number of disks
    @param start: start stick
    @param middle: auxiliary stick
    @param end: end stick'''
    start_stick = Stack()
    middle_stick = Stack()
    end_stick = Stack()
    disks = []
    for i in range (1, n+1):
        disks.append(f'disk{i}')
    disks.reverse()
    for i in range(0, len(disks)):
        start_stick.push(disks[i])
    print(start_stick, middle_stick, end_stick)

    def move_tower(n, start, end, middle):
        '''Solves the Hanoi tower problem for n disks
        @param n: number of disks
        @param start: start stick
        @param middle: auxiliary stick
        @param end: end stick'''
        if n >= 1:
            move_tower(n-1, start, middle, end)
            move_disk(start,end)
            move_tower(n-1,middle, end, start)

    def move_from_stack(n, start_stack, end_stack, middle_stack):
        '''Solves the Hanoi tower problem with stacks
        @param n: number of disks
        @param start: start stack
        @param middle: auxiliary stack
        @param end: end stack'''
        if n >= 1:
            move_from_stack(n-1, start_stack, middle_stack, end_stack)
            end_stack.push(start_stack.pop())
            move_from_stack(n-1, middle_stack, end_stack, start_stack)

    def move_disk(start, end):
        '''Print move
        @param start: start stick
        @param end: end stick'''
        print("moving disk from",start,"to",end)

    move_tower(n, start, end, middle)
    move_from_stack(n, start_stick, end_stick, middle_stick)
    print(start_stick, middle_stick, end_stick)

hanoi(3,"A","B","C")