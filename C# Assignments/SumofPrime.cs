using System;  
public class Sum_of_Prime
{  
    public static void Main() 
      {     
           long sum = 0;
            int flag = 0;
            int n = 2;
            while (flag < 500)
              {
                if (isPrime(n))
                {
                    sum += n;
                    flag++;
                }
                n++;
            }
           Console.WriteLine("Sum of Frist 500 Prime Nos: {0}" ,sum);
                    
    }
     public static bool isPrime(int n)
        {

            if (n == 1)
            return false;
            if (n == 2) 
            return true;

            for (int i = 2; i <= n/2; ++i)
            {
                if (n % i == 0) 
                return false;
            }

            return true;
        }
}
