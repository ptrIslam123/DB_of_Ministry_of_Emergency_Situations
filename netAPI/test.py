

class Widget:

        def __wrapre(self, func, *args):
                def foo():
                        print("__begin")
                        res = func(*args)
                        print("__end")

                        return res

                return foo

        def eval(self, v1, v2):
                return self.__wrapre(self.sum, v1, v2)()

        
        def sum(self, v1, v2):
                return v1 + v2
        



def main():
        w = Widget()
        res = w.eval(10, 20)
        print("res = ", res)        

if __name__ == "__main__":
    main()