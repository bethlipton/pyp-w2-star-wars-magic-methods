
class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
    
    def __str__(self):
        return str(self.name)

    def __mul__(self, other):
        if isinstance(other, People):
            return "%s throws a thermal detonator at %s!" % (self.name, other.name)
        else:
            raise TypeError('oops')
    
    def __div__(self, other):
        if isinstance(other, People):
            return "%s swings a lightsaber at %s." % (self.name, other.name)
        else:
            raise TypeError('oops')
            
    def __call__(self):
        return "Help me %s, you're my only hope." % (self.name)

    def __neg__(self):
        self._dark_side = True
    
    def __pos__(self):
        self._dark_side = False
    
    def __invert__(self):
        self._dark_side = not self._dark_side
    
    def __lshift__(self, other):
        return "%s uses the force to pull %s towards them." % (self.name, other.name)
    
    def __rshift__(self, other):
        if isinstance(other, People):
            return "%s uses the force to push %s away from them." % (self.name, other.name)
        else:
            raise TypeError('oops')
            
    def __xor__(self, other):
        return "%s force chokes %s." % (self.name, other.name)
    
    def __eq__(self, other):
        if self.name == 'Han Solo' and other.name == 'Greedo':
            return 'Han Solo shoots Greedo.'
        elif self.name == 'Greedo' and other.name == 'Han Solo':
            return 'Han Solo shoots Greedo. BECAUSE HAN SHOOTS FIRST.'
        else:
            return '%s shoots %s.' % (self.name, other.name)
        
    @property
    def light_side(self):
        return not self._dark_side
    
    @property
    def dark_side(self):
        return self._dark_side
        
        