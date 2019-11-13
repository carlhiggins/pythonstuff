def lassttt():
    def lastone():
        def superall():
            def all():
                def name():
                    name = 'Alice'
                def age():
                    age = 12
                def intro():
                    print('Who goes there?')
                def inp():
                    name = input()
                def inp2():
                    age = input()
                def get_name(prompt):
                    def get_age():
                        myAge = input(prompt)
                        while myAge not in (12):
                            myAge = input(prompt)
                        return myAge
                    myName = input(prompt)
                    while myName not in ('Alice'):
                        myName = input(prompt)
                    return get_age
            intro()
            inp()
            print(get_name(prompt))
            return all
        
        all = superall()
        return all, superall
    
    all, superall = lastone()
    return lastone

lastone = lassttt()