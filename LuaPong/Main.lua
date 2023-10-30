-- # basics of lua # --

-- is a comment

[[
    Multi-
          line
              comments

]]

-- # defining variables # --

-- global variable --

hello = 'hello'

-- local variable --

local world = 'world'

-- # Functions # --

-- declare a function that days hello? --
-- def sayHello(text): <-- Python way --

function sayHello(text)
    print(text)
    end
-- have to finish function with 'end' --

sayHello('Hellow World!')

sayHellow(hello .. world) -- ( .. ) --> is concatenation of strings --

-- # conditional statements # --
-- if world == 'world': <-- Python way --

if world == 'world' then
    print('World')
else
    print('hello!')
end
-- again you have to finish conditionals with 'end'

-- # Loops # --

-- while loops count from 10 to 0 --
[[ Python way
    i = 10
    while i != 10:
        i -= 1
        print(i)
]]

-- Lua way for a while loop counting from 10 to 0 --

local i = 10
while i!= 0 do
    i = i-1
    print(i)
end

-- for loops count from 10 to 0 -- 
[[ Python way
    i = 11
    for j in reversed(range(i)):
        print(j)

]]

-- Lua way for loop counting from 10 to 0
for j = 10,1,-1 do      -- for (intialize var), (where to stop), (step) do --
    print(j)
end

-- repeat (do-while) loop
i = 10
repeat
    i = i-1
    print(i)
until i==0

-- # Tables # -- 

-- tables are similar to Python list --
-- one variable with many characteristics --

local person = {}
person.name = "ty" -- var.key = value
person.age = 87
person.height = 60

-- call the informat
print(person['name']) -- similar to Python Dictionary
print(person.name)

-- for loop to get all the information from the object

for key,value in pairs(person) do   -- 
    print(key,value)
end