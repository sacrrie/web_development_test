t=['this','is','test']
a=' '.join(t)
def reverseWords(s):
        stuff=s.strip().split()
        i=len(stuff)-1
        temp=[]
        while i>=0:
            temp.append(stuff[i])
            i-=1
        answer=' '.join(temp)
        return answer
        #This is the fastest way
        #return " ".join(s.strip().split()[::-1])
        
print reverseWords(a)
print reverseWords("   a    b    ")