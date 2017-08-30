#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

# Chapter 12

# ___________________________________________________________
#                                                      NOTES


# ___________________________________________________________
#                                             IMPLEMENTATION

class Node:

    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()

    def addChild(self, key, data=None):

        if not isinstance(key, Node):
            self.children[key] = Node(key, data)

        else:
            self.children[key.label] = key

class Trie:

    def __init__(self):
        self.head = Node()

    def ADD(self, word):
        current_node = self.head
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]

            else:
                word_finished = False
                break

        # For ever new letter, create a new child node
        if not word_finished:

            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1

        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.data = word

    def HAS_WORD(self, word):
        if word == '':
            return False

        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')

        # Start at the top
        current_node = self.head
        exists = True

        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]

            else:
                exists = False
                break

        # Still need to check if we just reached a word like 't'
        # that isn't actually a full word in our dictionary
        if exists:
            if current_node.data == None:
                exists = False

        return exists

    def START_WITH_PREFIX(self, prefix):
        """ Returns a list of all words in tree that start with prefix """

        words = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')

        # Determine end-of-prefix node
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words

        # Get words under prefix
        if top_node == self.head:
            queue = [node for key, node in top_node.children.iteritems()]
        else:
            queue = [top_node]

        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.data)

            queue = [node for key,node in current_node.children.iteritems()] + queue

        return words

    def GET_DATA(self, word):

        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))

        # Race to the bottom, get data
        current_node = self.head

        for letter in word:
            current_node = current_node[letter]

        return current_node.data

# ___________________________________________________________
#                                                       TEST

if __name__ == '__main__':

    trie = Trie()
    words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
    print "\nStore '%s' in trie\n" % words

    for word in words.split():
        trie.ADD(word)

    print "Is 'goodbye' in trie: ", trie.HAS_WORD('goodbye')

    print "All words with prefix '%s' are: %s" % ('g', trie.START_WITH_PREFIX('g'))
    print "All words with prefix '%s' are: %s\n" % ('to', trie.START_WITH_PREFIX('to'))
