using System;
					
public class Program
{
	public static void Main(string[] args)
	{  
		int sum=0,rev =0 ;
		Console.WriteLine("Enter the number:");
		int num =Convert.ToInt32(Console.ReadLine());
		int a = num;
		while (num>0)
		{
			rev = num % 10;
			sum = sum + rev;
			num = num / 10;
		}
		Console.WriteLine("The Sum of the digits of {0} is {1}", a, sum);
}
}
