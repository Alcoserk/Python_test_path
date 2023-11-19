def voted():
    voted = {}
    def check_voter(name):
        if voted.get(name):
            print("Выгони его")
        else:
            voted[name] = True
            print("Пусть голосует")


    def test():
        check_voter('Aleksandr')
        check_voter('Vlad')
        check_voter('Vlad')
    test()


if __name__ == '__main__':
    voted()