def main(name: str) -> None:
    print(name.replace('.', '').replace(' ', '_').lower() + '.py')


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
