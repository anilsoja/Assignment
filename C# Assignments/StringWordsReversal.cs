using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace A3
{
    class Program
    {
        static void Main(string[] args)
        {

            int count = 0;
            Console.WriteLine("enter the string");
            string str = Console.ReadLine();
            char[] array = str.ToCharArray();
            Console.WriteLine("string after reverse ");
            for (int i = array.Length - 1; i >= 0; i--)
            {
                if (array[i] != ' ')
                {
                    count++;
                }
                else if (array[i] == ' ')
                {
                    for (int j = i + 1; count > 0; j++, count--)
                    {
                        Console.Write(array[j]);
                    }
                    Console.Write("  ");
                }
            }
            for (int j = 0; j <= count; j++)
            {
                Console.Write(array[j]);
            }
            Console.ReadLine();

        }
    }
}
