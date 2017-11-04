import os

dict_pinyin = open('pinyin').read().lower().strip().split('\n')
dict_english = open('english').read().lower().strip().split('\n')


class Node(object):
    def __init__(self, data):
        self.data = data
        self.childrens = [None] * 26
        self.isValue = False
    
    def __repr__(self):
        return 'Node: '+str(self.data)

class WordsAndPinyinId(object):
    def __init__(self):
        self._pinyin_node = self.make_trie('pinyin')
        self._english_node = self.make_trie('english')

    @staticmethod
    def make_trie(language):
        if language == 'pinyin':
            word_list = dict_pinyin
        elif language == 'english':
            word_list = dict_english
        else:
            raise NotImplementedError('Not Implemented Lanuage!')

        root = Node(-1)
        node = root
        for word in word_list:
            node.isValue = True
            node = root
            for char in word:
                idx = ord(char)-ord('a')
                if not node.childrens[idx]:
                    node.childrens[idx] = Node(char)
                node = node.childrens[idx]
        node.isValue = True
        
        return root

    def match(self, passwd, language):
        if language == 'pinyin':
            node = self._pinyin_node
        elif language == 'english':
            node = self._english_node
        else:
            raise NotImplementedError('Not Implemented Lanuage!')

        passwd = passwd.lower()
        for i, char in enumerate(passwd):
            idx = ord(char)-ord('a')
            if idx < 0 or idx > 25:
                return False
            if not node.childrens[idx]:
                if i == 0 or not node.isValue:
                    return False
                return self.match(passwd[i:], language)
            else:
                node = node.childrens[idx]
                if node.isValue and self.match(passwd[i+1:], language):
                    return True
        return node.isValue

    def identify(self,pw):
        if self.match(pw, 'pinyin') or self.match(pw, 'english'):
            return True
        return False

# if __name__ == '__main__':
#     iden = WordsAndPinyinId()
#     print(iden.identify("nihao"))
