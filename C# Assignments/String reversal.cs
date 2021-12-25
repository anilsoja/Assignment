using System;
					
public class Program
{
	public static void Main(string[] args)
	{  
		int i;
		string reverse = "";
		Console.WriteLine("Enter the String:");
		string str = Console.ReadLine();
		int len = str.Length - 1;
		for(i=len; i>=0;i--){
			reverse =reverse + str[i];
		}
		Console.WriteLine("Reversed String is: {0}", reverse);
}
}
