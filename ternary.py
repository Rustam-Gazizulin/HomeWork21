greeting = 'Hello'
name = 'Alex'
if name:
    greeting += f', {name}'
print(greeting)

greeting_ternary = f'Hello, {name}' if name else 'Hello!'
print(greeting_ternary)