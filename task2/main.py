import os

print(f"Hello my name is {os.environ.get('last_name')} {os.environ.get('first_name')}  and I am {os.environ.get('age')}")
