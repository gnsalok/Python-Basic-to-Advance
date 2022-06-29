def main():
    print(f'First module name : {__name__}')

# it say this is driver program
if __name__ == "__main__":
    main()
    print("Run directly")
else:
    print("Run from import")