""" Translating old JS Exercises to Python """

# return array of tripled values, assume always an array of integers
def tripler(array): 
    arr = []  
    for i in range(len(array)):
        arr.append(array[i]*3)
    return arr


print(tripler([1,2,3]))
print(tripler([-1,-2,-3]))
print(tripler([0.1,0.2,0.3]))

# return odd numbers, assume end is positive
def odd_range(end):
    arr = []
    for i in range(1, end+1, 2):
         arr.append(i)
    return arr

print(odd_range(40))
print(odd_range(1))
print(odd_range(39))

# build dictionary cat with name, color, and toys
def cat_builder(name, color, toys):
  return  {
    "name": name,
    "color": color,
    "toys": toys
  }

print(cat_builder('tom', 'grey', ['frying pan', 'dynamite']))


# Return different object's values with the same key
def value_pair(dict1, dict2, key):
    return [dict1[key], dict2[key]]

dict1 = {"name" : "Sam", "age":12}
dict2 = {"name" : "Sally", "age":14}
print(value_pair(dict1, dict2, "age"))


#Return T/F if key exists in dictionary
def  does_key_exist(dict, key):
    return key in dict.keys()

print(does_key_exist(dict1, "age"))
print(does_key_exist(dict2, "toys"))


#Return people over the age of 18
def adults(people):
    names = []
    for i in range(len(people)):
        person = people[i]
        if (person["age"] >= 18): names.append(person["name"])
    return names

people = [
    {"name": "Sara", "age": 12},
    {"name": "Ruth", "age": 42},
    {"name": "Ben", "age": 18}
]
print(adults(people))


# return True if number is prime, assume positive input
def is_prime(number):
    if (number < 2): return False
    if (number == 2): return True
    for i in range(2, int((number/2)+1)):
      if (number % i == 0):
        return False
    return True

print(is_prime(2) )# => true
print(is_prime(1693)) # => true
print(is_prime(15)) # => false
print(is_prime(303212)) # => false
  
#return the first n primes you encounter
def first_n_primes(n): 
    primes = []
    num = 2
    while (len(primes) < n):
      if (is_prime(num)):
        primes.append(num)
      num += 1
    return primes

print(first_n_primes(0)) # => []
print(first_n_primes(1)) # => [2]
print(first_n_primes(4)) # => [2, 3, 5, 7]

# return the sum of the first n primes
def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)
    for i in range(len(primes)):
        sum += primes[i]
    return sum

print(sum_of_n_primes(0)) # => 0
print(sum_of_n_primes(1)) # => 2
print(sum_of_n_primes(4)) # => 17


# return object of name to cumulative score
def count_scores(people):
    scoresObj = {}
    for i in range(len(people)):
        personObj = people[i]
        name = personObj["name"]
        score = personObj["score"]
        if (name in scoresObj): scoresObj[name] += score
        else: scoresObj[name] = score
    return scoresObj

peeps = [
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2}
]
print(count_scores(peeps)) # => { Pete: 4, Mike: 4, Dexter: 6 }

ppl = [ {"name": "Pete", "score": 10},
            {"name": "Mike", "score" : 10},
            {"name": "Pete", "score": -8},
            {"name": "Dexter", "score": 12}]
print(count_scores(ppl))  # => { Pete: 2, Mike: 10, Dexter: 12 }