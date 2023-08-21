from asyncio import sleep, run

async def main(): 
    try: print(await sleep(2.5, result='Hello, Python!'))
    except: print('Goodbye, Python.')
    finally: print('Thank you, for using Python!')

if __name__ == '__main__': run(main())
