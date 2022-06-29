name= "Akash Kumar."

a= name.capitalize()
print(a)

b= name.casefold()
print(b)

c= name.center(20)
print(c)

d= name.count("Kumar")
print(d)

e= name.encode()
print(e)

f= name.endswith(".")
print(f)

g= "A\tk\ta\ts\th"
print(g.expandtabs(3))

h= name.find("Kumar")
print(h)

i= "For only {price:.3f} dollers!"
print(i.format(price = 50))

j= name.format_map(name)
print(j)

k="Hello, Welcome My World"
print(k.index("Welcome"))

l= "Helloworld"
print(l.isalnum())

m= "Helloworld"
print(m.isalpha())

n= "123456789"
print(n.isdecimal())

print(n.isdigit())

o= "Demo"
print(o.isidentifier())

p= "demo"
print(p.islower())

print(n.isnumeric())

print(name.isprintable())

q= "   "
print(q.isspace())

print(name.istitle())

r= "EMRAN SIR IS A SUPERMAN"
print(r.isupper())

s= ("Akash","Munna","Delowar","Easin","Tanvin")
print("#".join(s))

t= "leo messi"
t2=t.ljust(10)
print(t,"is my favorite players.")

u= "HELLO MY FRIENDS"
print(u.lower())

v=t.lstrip()
print("Footballer",v,  "is my favorite players")

w= name.maketrans("s","p")
print(name.translate(w))

x= u.partition("MY")
print(x)

y= u.replace("FRIENDS","Love")
print(y)

z= name.rfind("Kumar")
print(z)

a2= u.rindex("MY")
print(a2)

b2= t.rjust(20)
print(b2,"is my favorite players.")

c2= "I could eat apple all day, apple are my favorite fruit"
c3= c2.rpartition("apple")
print(c3)

d2= "apple,mango,banana"
d3= d2.rsplit(",")
print(d3)

e2= t.rstrip()
print("Footballer",e2,  "is my favorite players")

f2= "Welcome Dipti"
f3= f2.split()
print(f3)

g2= "Meray pass tum ho\nMeer abru \nemotional  song"
g3= g2.splitlines()
print(g3)

h2= g2.startswith("Meray")
print(h2)

i2= "Hello My Name Is AKASH"
i3= i2.swapcase()
print(i3)

j2= "Hello my friends"
j3= j2.title()
print(j3)

k2= {20:30}
k3= "Hello Akash"
print(k3.translate(k2))

l2= f2.upper()
print(l2)

m2= "50"
m3= m2.zfill(20)
print(m3)

n2= t2.strip()
print("Footballer",n2,  "is my favorite players")