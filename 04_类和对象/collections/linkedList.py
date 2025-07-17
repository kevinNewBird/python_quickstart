class Node:
    def __init__(self, val, nxt):
        """
        :param val: 当前值
        :param nxt: 下一个节点对象
        """
        self.val = val
        self.next = nxt

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return 'Node({})'.format(self.__str__())


class LinkedList:

    def __init__(self, lst=None):
        self.__head = None
        self.__count = 0
        if lst is None or not lst:
            return

        for val in lst:
            self.add(val)

    def add(self, val):
        """
        头插法
        :param val: 值
        :return:
        """
        self.__head = Node(val, self.__head)
        self.__count += 1

    def remove(self, val):
        p = self.__head

        if p is None or not p:
            return

        # if head the val to remove
        if p.val == val:
            self.__head = p.next
            self.__count -= 1
            return

        while p is not None and p.next is not None and p.next.val != val:
            p = p.next

        # not found
        if p is None or p.next is None:
            return

        p.next = p.next.next
        self.__count -= 1

    def insert(self, idx, val):
        """
        如果没有找到插在头部
        :param idx:
        :param val:
        :return:
        """
        p = self.__head
        if self.is_empty() or idx == 0:
            self.__head = Node(val, self.__head)
            self.__count += 1
            return

        count = 1
        while p.next is not None:
            if idx == count:
                break
            # 保证p是前一个索引
            p = p.next
            count += 1
        p.next = Node(val, p.next)
        self.__count += 1

    def index(self, val):
        p = self.__head
        idx = 0
        while p is not None and p.val != val:
            idx += 1
            p = p.next
        return -1 if idx >= self.length() else idx

    def is_empty(self):
        return self.__head is None

    def length(self):
        return self.__count

    def __str__(self):
        p = self.__head
        s = '_> '
        while p is not None:
            s += str(p.val) + ' _> '
            p = p.next
        s += 'None'
        return s

    def __repr__(self):
        return 'LinkedList()'.format(self.__str__())


# ->5->4->3->2->1->None
ll = LinkedList([1, 2, 3, 4, 5])
print("linkedList result".ljust(25, " "), ":", ll)
print("linkedList is empty".ljust(25, " "), ":", ll.is_empty())
ll.remove(5)
print("remove linkedList result".ljust(25, " "), ":", ll)
ll.remove(1)
print("remove linkedList result".ljust(25, " "), ":", ll)
ll.remove(3)
print("remove linkedList result".ljust(25, " "), ":", ll)
ll.remove(6)
print("remove linkedList result".ljust(25, " "), ":", ll)
ll.insert(0, 6)
print("insert linkedList result".ljust(25, " "), ":", ll)
ll.insert(2, 3)
print("insert linkedList result".ljust(25, " "), ":", ll)
ll.insert(5, -1)
print("insert linkedList result".ljust(25, " "), ":", ll)
print("index linkedList result".ljust(25, " "), ":", ll.index(6))
print("index linkedList result".ljust(25, " "), ":", ll.index(3))
print("index linkedList result".ljust(25, " "), ":", ll.index(-1))
print("index linkedList result".ljust(25, " "), ":", ll.index(8))
