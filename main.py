def main(): 
    try: print('Hello, Python!'); raise(LookupError)
    except: print('Goodbye, Python.\nHello World'); return
    finally: print('Thank you, for using Python!')

if __name__ == '__main__': main()
