#User function Template for python3

class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        if n<3:
            return -1
        res=-1
        for i in range(1,n-1):
            for j in range(1,m-1):
                current=mat[i][j]+sum(mat[i-1][j-1:j+2])+sum(mat[i+1][j-1:j+2])
                if current>res:
                    res=current
        return res
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends