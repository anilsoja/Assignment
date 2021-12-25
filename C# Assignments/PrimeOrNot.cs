using System;

class Program
{
    static void Main() {
        int flag =0, i;
      Console.WriteLine("Enter the number:");
       int num = Convert.ToInt32(Console.ReadLine());
        for(i=2;i<=num/2;i++){
                if(num % i == 0){
                  flag = 1;
                }
            }
            if(flag == 0){
                Console.WriteLine("The {0} is prime", num);
            }
            else{
                 Console.WriteLine("The {0} is not prime", num); 
            }
    }
    }
