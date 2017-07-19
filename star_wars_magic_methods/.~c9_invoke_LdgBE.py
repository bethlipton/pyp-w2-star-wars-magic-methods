class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        
    def __add__(self, other):
        if isinstance(other, SaberCrystal):
            _other_color = other.color
        elif isinstance(other, tuple):
            _other_color = other
            
        sum_red = self.red + _other_color[0]
        sum_green = self.green + _other_color[1] 
        sum_blue = self.blue + _other_color[2]
        return SaberCrystal((sum_red, sum_green, sum_blue))
        
    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            _other_color = other.color
        elif isinstance(other, tuple):
            _other_color = other
            
        sub_red = self.red - _other_color[0]
        sub_green = self.green - _other_color[1]
        sub_blue = self.blue - _other_color[2]
    
        return SaberCrystal((sub_red, sub_green, sub_blue))
        
    def __iadd__(self, other):
        
        if isinstance(other, SaberCrystal):
%        return flag
        elif isinstance(other, tuple):
            _other_color = other
        
        add_red = self.red += _other_color[0]
        add_green = self.green += _other_color[1]
        add_blue = self.blue += _other_color[2]
        
        return SaberCrystal((add_red, add_green, add_blue))
        
    def __isub__(self, other):
        
        if isinstance(other, SaberCrystal):
            _other_color = other.color
        elif isinstance(other, tuple):
            _other_color = other
            
        minus_red = self.red -= _other_color[0]
        minus_green = self.green -= _other_color[1]
        minus_blue = self.blue -= _other_color[2]
    
        return SaberCrystal((minus_red, minus_green, minus_blue))
        
    def __contains__(self, other):
        
        if isinstance(other, SaberCrystal):
            _color = other.color
        elif isinstance(other, tuple):
            _color = other
        
        ind =  [i for i, e in enumerate(_color) if e]
        flag = True
        for j in ind:
            if self.color[j] != _color[j]:
                flag = False
            
        return flag
                
                
    def __eq__(self, other):
        return self.color == other.color
        
    def __ne__(self, other):
        return not self.__eq__(other)
        
    @property
    def color(self):
        return((self.red, self.green, self.blue))

