def key_to_value(**kwargs):
  for key, value in kwargs.items():
    print("{0} = {1}".format(key, value))


print(key_to_value({"hey": "3"}))
