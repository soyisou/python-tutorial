import concurrent.futures


def printContent(content: str):
    for i in range(3):
        print(content, i)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        parameters_list = ['hello', 'world']
        futures = [executor.submit(printContent, param) for param in parameters_list]
        # 等待所有线程完成
        concurrent.futures.wait(futures)


if __name__ == '__main__':
    '''
    1. 方法一：直接调用
    hello
    hello
    hello
    world
    world
    world
    '''
    # printContent("hello")
    # printContent('world')
    main()
    print("All threads are done.")
