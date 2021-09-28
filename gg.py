import sys
import re
vars={}
lines=open(sys.argv[1],"r").read().split("\n")
i=0
jumps={}
def sostT(text,vars):
     matches=re.findall(r"(?<=\$)(.*)(?=\$)",text)
     for match in matches:
          if match in vars.keys():
              text=text.replace("$"+match+"$",str(vars[match]))
     return text
try:
    while lines[i].strip()!="END":
        #print(lines[i])
        if lines[i][0]=="#":
            i+=1
            continue
        ag=lines[i].split(" ")
        if ag[0] == "INT":
            vars[ag[1]]=0
        elif ag[0]=="SET":
            vars[ag[1]]=ag[2]
        elif ag[0]=="DEC":
            vars[ag[1]]=int(vars[ag[1]])-1
        elif ag[0]=="INC":
            vars[ag[1]]=int(vars[ag[1]])+1
        elif ag[0]=="CP":
            vars[ag[1]]=vars[ag[2]]
        elif ag[0]=="JLE":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=vars[ag[3]]
            if vars[ag[2]]<=athr:
                i = jumps[ag[1]]
        elif ag[0]=="JME":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=vars[ag[3]]
            if vars[ag[2]]>=athr:
                i = jumps[ag[1]]
        elif ag[0]=="JL":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=vars[ag[3]]
            if vars[ag[2]]<athr:
                i = jumps[ag[1]]
        elif ag[0]=="JM":
            if str(ag[3]).isnumeric():
                athr=float(ag[3])
            else:
                athr=vars[ag[3]]
            if vars[ag[2]]>athr:
                i = jumps[ag[1]]
        elif ag[0][0]==":":
            jumps[ag[0][1:]]=i
        elif ag[0]=="OUT":
            print(sostT(" ".join(ag[1:]),vars).replace("\\n","\n"),end='')
        elif ag[0]=="IN":
            print(sostT(" ".join(ag[3:]),vars).replace("\\n","\n"),end='')
            vars[ag[2]]=int(input(""))
        i+=1
except Exception as e:
    print(vars)
    print(jumps)
    raise e
#print(lines)
