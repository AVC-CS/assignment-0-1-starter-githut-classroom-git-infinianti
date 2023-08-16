def main(): 
    try: print('Hello World, Welcome to Python!'); raise(LookupError)
    except: print('Goodbye World.')
    finally: print('Thank you, for using Python!')

if __name__ == '__main__': main()
