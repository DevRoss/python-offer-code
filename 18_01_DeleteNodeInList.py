#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-18

"""由于垃圾windows把我的代码无缘无故给删了，所以现在直接使用MKYAN的代码，若有侵权，请告知"""


class ListNode:
    def __init__(self):
        self.value = None
        self.next_node = None


class Solution:
    def delete_node(self, head_node, del_node):
        """
        删除指定节点
        """
        if not (head_node and del_node):
            return False

        # 要删除的节点不是尾节点
        if del_node.next_node:
            del_next_node = del_node.next_node
            del_node.value = del_next_node.value
            del_node.next_node = del_next_node.next_node
            del_next_node.value = None
            del_next_node.next_node = None

        # 链表只要一个节点，删除头节点（也是尾节点）
        elif del_node == head_node:
            head_node = None
            del_node = None

        # 链表中有多个节点，删除尾节点
        else:
            node = head_node
            while node.next_node != del_node:
                node = node.next_node
            node.next_node = None
            del_node = None

        return head_node


if __name__ == '__main__':
    pass
