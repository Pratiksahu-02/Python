t1={"python","sql","data analsis","machine learning"}
t2={"sql","data analsis","cloud computing","devops"}

#find the skills that both teams have in common.
print(t1.intersection(t2))

#identify skills unique to each team.
print(t1.difference(t2))
print(t2.difference(t1))

#suggest a comprehensinve skill set required for the project by combining all skills. 
print(t1.union(t2))