try:
    with open("file.txt", mode="r") as file:
        ...
except FileNotFoundError as e:
    print(f"File  {e} doesn't exist ")
except Exception as e:
    print(f"Unexpected Exception: {e}")
else:
    print("No Exceptions raised")
