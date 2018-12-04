class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # int carry=0,i=num1.size()-1,j=num2.size()-1;
        # char ch1,ch2;
        # string answer;
        # while(i>-1||j>-1)
        # {   ch1=i>-1?num1[i--]:'0';
        #     ch2=j>-1?num2[j--]:'0';
        #     answer+=to_string((carry+ch1+ch2-96)%10);
        #     carry=(carry+ch1+ch2-96)/10;   }
        # if(carry) answer+="1";
        # reverse(answer.begin(),answer.end());
        # return answer;
        t1, t2 = 0, 0
        for i in num1:
            t1 *= 10
            t1 += ord(i) - 48

        for i in num2:
            t2 *= 10
            t2 += ord(i) - 48

        return str(t1 + t2)
