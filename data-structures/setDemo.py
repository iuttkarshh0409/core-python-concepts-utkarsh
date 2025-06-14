lang1={"C","Java","Python"}
lang2={"Python","Rust","Go"}

lang1.add("JavaScript")
lang1.remove("C")
print("Final lang1 set "+str(lang1))
print("Final lang2 set "+str(lang2))

print("lang1 UNION lang2: "+str(lang1.union(lang2)))
print("lang1 INTERSECTION lang2: "+str(lang1.intersection(lang2)))
print("lang1-lang2: "+str(lang1.difference(lang2)))