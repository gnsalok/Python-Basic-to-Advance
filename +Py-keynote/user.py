from library import Base

assert hasattr(Base, 'foo'),'You broke it...'
class Derived(Base):
    def bar(self):
        return self.foo



      