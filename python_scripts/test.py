def _func():
  x = 300
  y = 400
  z = 500
  print("the function has run")
  return x * y * z



dict = {
"_function": _func,
"rand": "other value"
}

print(dict["_function"])

dict["_function"]()
