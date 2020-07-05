u = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
l = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

message = "Bpgn wps p axiiat Aapbp pcs p exv pcs p rdl pcs p Gpqxs Gpqqxi."


print(message)
for a in range(0,26):
    
  o = ''
  for i in message:
      if i in u:
        #print("Upper case %s " % i)
        o += u[(u.index(i)+a)%len(u)]
      
      elif i in l:
        #print("Lower case %s " %i )
        o += l[(l.index(i)+a)%len(l)]
      else:
        o+= i
  print(o)
