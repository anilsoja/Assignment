
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Array
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] Array_1 = new int[55];
            int[] Array_2 = new int[55];
           
            Console.WriteLine("enter the size of the  Array_1");
             int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("enter the elements of Array_1");
            for (int i = 0; i < n; i++)
            {
                Array_1[i] = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine("enter the size of the Array_2");
            int n1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("enter the elements of Array_2");
            for (int i = 0; i < n1; i++)
            {
                Array_2[i] = Convert.ToInt32(Console.ReadLine());
            }



             

            Console.WriteLine("\nMultiply corresponding elements of two arrays: ");

            for (int i = 0; i < n; i++)
            {
                
                Console.Write(Array_1[i] * Array_2[i] +" ");
            }
            Console.WriteLine("\n");
        }
    }
}
