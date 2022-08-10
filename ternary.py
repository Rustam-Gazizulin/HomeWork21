# greeting = 'Hello'
# name = 'Alex'
# if name:
#     greeting += f', {name}'
# print(greeting)
#
# greeting_ternary = f'Hello, {name}' if name else 'Hello!'
# print(greeting_ternary)


DEFAULT = 5
def_value = 0
new_def_value = def_value or DEFAULT
print(new_def_value)

DEFAULT = 3
if not def_value:
    def_value = DEFAULT
print(def_value)


a = [1, 3, '', 4, 6, 0, 5, 4]
res = [i if i else 99 for i in a]
print(res)

