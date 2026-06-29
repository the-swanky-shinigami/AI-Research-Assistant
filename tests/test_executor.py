from core.executor import Executor


def main():

    executor = Executor(timeout=10)

    result = executor.run("generated/hello.py")

    print(result)


if __name__ == "__main__":
    main()