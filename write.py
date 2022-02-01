def main():
    with open(file='users.txt', mode='w', encoding='utf-8') as f:
        f.write('Bob,79\n')
        f.write('Tom,59\n')
        print("withの中:", f.closed)
    print("withの外:", f.closed)


if __name__ == '__main__':
    main()
