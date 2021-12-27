using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StringReversal
{
    class Program
    {
        static void Main(string[] args)
        {

            int count = 0;
            Console.WriteLine("enter the string");
            string str = Console.ReadLine();
            char[] arr = str.ToCharArray();
            Console.WriteLine("string after reverse ");
            for (int i = arr.Length - 1; i >= 0; i--)
            {
                if (arr[i] != ' ')
                {
                    count++;
                }
                else if (arr[i] == ' ')
                {
                    for (int j = i + 1; count > 0; j++, count--)
                    {
                        Console.Write(arr[j]);
                    }
                    Console.Write("  ");
                }
            }
            for (int j = 0; j <= count; j++)
            {
                Console.Write(arr[j]);
            }
            Console.ReadLine();

        }
    }
}
