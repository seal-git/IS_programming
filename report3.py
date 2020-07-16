class Human:
    def __init__(self,name='Anonymous',wallet=1000):
        self.name = name
        self.wallet = wallet
    def hello(self):
        print("Hello! My name is ", self.name, ". I have ", self.wallet, 'JPY.')
    def give(self, p, money):
        """give money to other"""
        p.receive(money)
        self.wallet -= money
    def receive(self, money):
        """recieve money from other"""
        self.wallet += money

class Student(Human):
    def __init__(self,name='Anon. Student',wallet=500):
    ### write a method body ###
        super().__init__(name, wallet)
        self.subj = []
    def learn(self, subject):
    #### write a method body ###
        self.subj.append(subject)
    def hello(self):
    #print inherited attributes:
        super().hello()
    # print added attributes:
        print("I have learned:", self.subj, '.')
    def give(self, p, money):
        super().give(p, money)
    def receive(self, money):
        super().receive(money)
    def teach(self, st):
    ### write a method body ###
        if(len([i for i in self.subj if st.is_newsub(i)])>0):
            st.give(self, 10)
            st.learn([i for i in self.subj if st.is_newsub(i)][0])

    def is_newsub( self,sb ):
        """ check if subj is not learned """
        for s in self.subj:
            if sb == s:
                return False #Already learned
            # No mach occured
        return True
#
# Test code. Expected result:
# Hello! My name is  John . I have  490 JPY.
# I have learned: ['mathematics', 'history', 'biology', 'programming', 'statistics'] .
# Hello! My name is  Jack . I have  510 JPY.
# I have learned: ['programming', 'history', 'statistics', 'mathematics'] .
#
john = Student("John")
john.learn('mathematics')
john.learn('history')
john.learn('biology')

jack = Student("Jack")
jack.learn('programming')
jack.learn('history')
jack.learn('statistics')

john.teach(jack) #510 490

jack.teach(john) #500 500
jack.teach(john) #490 510
jack.teach(john) #490 510 (No new subjects for john)

for p in (john,jack):
    p.hello()