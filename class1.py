class Software:
    def __init__(self, language):
        self.__language = language

    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self, value):
        self.__language = value

    # language = property(fget=get_lan, fset=set_lan)

obj = Software('python')
print(obj.language)
obj.language = 'java'
print(obj.language)

    