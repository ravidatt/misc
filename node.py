class Node:
    def __init__(self,data):
        self._data=data
        self._next=None

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def setNext(self,item):
        self._next=item

    def __str__(self):
        return "Data={}".format(self._data)


class LinkedList:
    def __init__(self):
        self.header=None

    def add(self,item):
        node=Node(item)
        node.setNext(self.header)
        self.header=node

    def show(self):
        while(self.header!=None):
            current=self.header
            print(current)
            self.header=current.getNext()

    def find(self,item):
        current=self.header
        isFound=False
        while(current!=None and isFound==False):
            if(current.getData()!=item):
              print(current)
              isFound=True
            current=current.getNext()
        return isFound

    def remove(self,item):
        prevrec=None
        current=self.header
        nextrec=None
        while current!=None:
            if current.getData()==item:
                if prevrec!=None :
                    prevrec.setNext(current.getNext())
                else:
                    self.header=current.getNext()
                current=current.getNext()
            else:
                nextrec = current.getNext()
                prevrec=current
                current=nextrec



link=LinkedList()
link.show()

link.add(30)
link.add(10)
link.add(20)
link.add(30)
link.add(40)
link.add(50)
link.add(60)

print("#####################")
link.remove(30)
link.remove(60)
link.remove(40)
link.remove(40)
link.remove(10)

link.show()
